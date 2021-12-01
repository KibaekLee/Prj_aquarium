from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Post, Category


admin.site.register(Post, MarkdownxModelAdmin) #Post 를 관리자 페이지에 추가


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


# Tag 테이블을 관히하기 위한 메뉴를 관리자 페이지에 추가
# 태그가 추가되기 직전에 입력한 name 값을 slug에 자동 입력하도록 설정


# 태그 관리 메뉴를 커스텀한 방식으로 추가
admin.site.register(Category, CategoryAdmin)

# 관리자 페이제에서 작성한 Post 제목 구성을 바꾸고 싶을 때
