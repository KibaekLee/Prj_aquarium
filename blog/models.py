import os

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from markdownx.utils import markdown
from markdownx.models import MarkdownxField


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
    content = MarkdownxField()

    create_at = models.DateTimeField(auto_now_add=True)

    # CASCADE: 작성자 정보가 User 테이블에서 삭제 시, 작성한 글 모두 삭제
    # SET_NULL: 작성자 정보가 User 테이블에서 삭제 시, 작성한 글 삭제 않함
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

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




