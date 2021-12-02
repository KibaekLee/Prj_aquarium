from django.urls import path
from .import views

urlpatterns = [

    # 테그 페이지 url 자리를 위해 아래 코드를 작성
    # slug는 문자열 형태이므로 str 키워드를 사용 (아래 <int:pk>와 비교)
    # 두번째 파라메터는 첫 번째 파라메터 형식의 URL을 입력했을 때 실행할 view를 지정
    # 여기서 FBV 방식으로 views.py 파일의 tag_page()함수를 호출
    # 카테고리 페이지 url 자리를 위해 아래 코드를 작성
    # slug는 문자열 형태이므로 str 키워드를 사용 (아래 <int:pk>와 비교)
    # 두번째 파라메터는 첫 번째 파라메터 형식의 URL을 입력했을 때 실행할 view를 지정
    # 여기서 FBV 방식으로 views.py 파일의 category_page()함수를 호출
    path('category/<str:slug>/', views.category_page),

    # path('<int:pk>/', views.single_post_page)
    # 서버주소/blog/<int.pk>
    path("", views.PostList.as_view()),
    # path('', views.index)
    #서버주소/blog/경로 접근 새 class.py의 index 함수
]