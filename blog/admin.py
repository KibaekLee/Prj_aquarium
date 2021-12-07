from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Post


# admin.site.register(Post, MarkdownxModelAdmin) #Post 를 관리자 페이지에 추가



# Tag 테이블을 관히하기 위한 메뉴를 관리자 페이지에 추가
# 태그가 추가되기 직전에 입력한 name 값을 slug에 자동 입력하도록 설정




