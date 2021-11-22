import os

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from markdownx.utils import markdown
from markdownx.models import MarkdownxField


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    #카테고리 페이지의 URL를 변환한하는 함수
    def get_absolute_url(self):
        # 카테고리 페이지의 URL을 구성한다.
        # 카테고리 페이지  URL은 '/blog/categoey/[카테고리의 slug 필드 값}'이다/
        # 예 [문화&예술] 카테고리는/'blog/category/문화-예술/'로 만들어진다
        # f: format의 약자로 변수와 문자열로 구성하여 하나의 문자열을 완성시킨다.
        return f'/blog/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'Categories'


class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = MarkdownxField()

    head_image = models.ImageField(upload_to='blog/image/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/file/%Y/%m/%d/', blank=True)

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # CASCADE: 작성자 정보가 User 테이블에서 삭제 시, 작성한 글 모두 삭제
    # SET_NULL: 작성자 정보가 User 테이블에서 삭제 시, 작성한 글 삭제 않함
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    # '''태그 필드 추가: 다대다 관계는 ManyToMany Filed 사용
    # (일대다 관계일때 ForeignKey 사용하는 것과 비교)'''
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]

    def get_content_markdown(self):
        return markdown(self.content)

    def get_avatar_url(self):
        if self.author.socialaccount_set.exists():
            return self.author.socialaccount_set.first().get_avatar_url()
        else:
            return f'https://doitdjango.com/avatar/id/336/fc65bf1a8db8d8fb/svg/{self.author.email}'


class Comment(models.Model):
    # CASCADE: POST글이 삭제되면 댓글도 같이 삭제되면 댓글도 같이 삭제
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, default=None) #'self': 자기 참조

    def __str__(self):
        return f'{self.author}::{self.content}::{self.score}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'

    def get_avatar_url(self):
        if self.author.socialaccount_set.exists():
            return self.author.socialaccount_set.first().get_avatar_url()
        else:
            return f'https://doitdjango.com/avatar/id/336/fc65bf1a8db8d8fb/svg/{self.author.email}'

    def get_child_comment(self):
        comments = Comment.objects.filter(parent_id=self.pk)
        return comments


