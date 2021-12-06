from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.views.generic import ListView

from blog.models import Post
import datetime
import json

from django.core import serializers
from django.http import JsonResponse
from api.models import Arduino


class PostList(ListView):
    model = Post
    ordering = '-pk'
    paginate_by = 5
    # template 명은 post_list.html(모델명_list.html)
    # template로 넘길 때 사용되는 변수량은 post_list(모델링_list)

    def get_context_data(self, **kwargs):
        # post_list 변수에 post 테이블 내용 전체가 저장된 상태
        context = super(PostList, self).get_context_data()

        return context











