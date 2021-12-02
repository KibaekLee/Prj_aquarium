from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.views.generic import ListView

from blog.models import Post, Category


class PostList(ListView):
    model = Post
    ordering = '-pk'
    paginate_by = 5
    # template 명은 post_list.html(모델명_list.html)
    # template로 넘길 때 사용되는 변수량은 post_list(모델링_list)

    def get_context_data(self, **kwargs):
        # post_list 변수에 post 테이블 내용 전체가 저장된 상태
        context = super(PostList, self).get_context_data()

        # categories 변수에 Category 테이블의 전체 내용을 담아 템플릿으로 보내 주기 위한
        context['categories'] = Category.objects.all()

        # Post 테이블 내용 중
        # category 필드 값이 None인 Post들만 추려서 갯수를 리턴받아
        # no_categories_post_count 변수에 저장한 후
        # 탬플릿으로 전달하기 위해서 작성
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context


def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    # URL을 통해서 전달받은 slug 변수를 이용하여
    # Category 테이블을 조회한다
    # 예) slug 값이 'programming'이면 Category 테이블에서 slug 값이 'programming'인
    # 'programming' 카테고리 객체를 가져와  category 변수에 저장한다

    # FBV 방식은 render 함수를 통해 탬플릿으로 변수값들을 전달한다
    # 첫번째 파라메터: 클라이언트로부터 요청받은 request 변수를 그대로 전달
    # 두번째 파라메터: 템플릿 경로
    # 세번째 파라메터: 딕셔너리(Dictionary)향태로'변수명': 변수값을 작성한다
    return render(
        request, 'blog/post_list.html',
        {
            'post_list': post_list,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
            'category': category,

        }
    )










