from django.conf.urls import url
from .views import post_list
from .views import post_detail
from .views import post_create
#from blog.views import post_list

urlpatterns = [
    # url의 첫번째 인자: 매치될 url 정규표현식
    # 매칭에 성공하면 두번째 인자로 넘어간다: view function
    # view function: request를 받아 response를 돌려주는 함수
    # blog.views에 있는 post_list함수를 아래 url함수의 두번째 인자로 전달 (함수호출 아님)
    url(r'^$', post_list, name='post-list'),
    # 정규표현식에 그룹을 지정해서 view function의 인수로 전달한다.
    url(r'^(\d+)/', post_detail, name='post-detail'),
    # name은 url 자체의 이름
    url(r'^write/', post_create, name='post-create')
]
