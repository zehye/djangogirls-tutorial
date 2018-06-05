import os

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.template.loader import render_to_string

from .models import Post


def post_list(request):
    """
    데이터베이스에서 모든 자료들을 가지고 온다
    :param request:
    :return:
    """
    """
    first/
        first_file.txt
        second/
            second_file.txt
            third/
                module.py
                fourth/
                    fourth_file.txt

    modele.py에서
    0. 현재 경로
        os.path.abspath(__file__)
    1. third/ 폴더의 경로
        os.path.dirname(<현재경로>)
    1-1. second/ 폴더의 경로
        os.path.dirname(<third폴더의 경로>)
    2. second/second_file.txt의 경로
        os.path.join(<second폴더의 경로>, 'second_file.txt')
    3. fourth/ 폴더의 경로
        os.path.join(<현재경로>, 'fourth')
    4. fourth/fourth_file.txt의 경로
        os.path.join(<현재경로>, 'fourth', 'fourth_file.txt')

    -> def post_list에서 templates/blog/post_list.html파일의 내용을 읽어서 return 해주는 HttpResponse에 전달
    :param request:
    :return:
    """
    # cur_file_path = os.path.abspath(__file__)
    # # print(cur_file_path)
    # third_file_path = os.path.dirname(cur_file_path)
    # # print(third_file_path)
    # second_file_path = os.path.dirname(third_file_path)
    # # print(second_file_path)
    # second_second_file_path = os.path.join(second_file_path, 'templates')
    # # print(second_second_file_path)
    # fourth_fourth_file_path = os.path.join(second_second_file_path, 'blog', 'post_list.html')
    # print(fourth_fourth_file_path)
    #
    # html = open(fourth_fourth_file_path, 'rt').read()

    # 경로에 해당하는 html파일을 문자열로 로드해줌
    # render_to_string : (path) -> template dir를 기준으로 가져온 특정 path값을 가져온다.

    # 근데 이때의 pathsms setiings.py의 TEMPLATES안에 있는 path를 기준으로 해서 가져온다.
    # 가져온 문자열 돌려주기
    # html = render_to_string('blog/post_list.html')
    # return HttpResponse(html)  # 특정 리퀘스트가 올떄 보통 http로 오고 여기로 응답을 보내는데 응답을 보내기 위한 무언가를 만들어줘

    # 위의 두 줄을 한번에 줄여쓰는 방법
    # return render(request, 'blog/post_list.html')

    # posts = Post.objects.all()
    # print(posts)
    # Post instance에서 title 속성에 접근가능
    # HttpResponse에
    # 글 목록 <br>
    # - ~ <br>
    # - ~ 등등
    # 위 텍스트를 넣어서 리턴
    # result = '글목록 <br>'
    # for post in posts:
    #     result += ' - {}<br>'.format(post)
    #
    # return HttpResponse(result)
    posts = Post.objects.order_by('-id')
    context = {
        'posts': posts,

    }
    # render는 주어진 인수를 사용해서
    # 여기서 1번째 인수: HttpResponse인스턴스
    # 2번째 인수: 문자열 (TEMPLATES['DIRS']를 기준으로 탐색할 템플릿 파일의 경로
    # 3번째 인수: 템플릿을 렌더링 할 때 사용할 객체의 모음
    # return render(request, 'blog/post_list.html', context)
    return render(
        request=request,
        template_name='blog/post_list.html',
        context=context
        # 데이터베이스 파일을 가지고 html파일을 동적으로 보내줘
    )

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    # post_detail.html 파일을 templates에 만들고,
    # post_list가 됐던 이유는 posts를 for문으로 돌고 있고, context에서 posts를 받고 있기 때문이다
    # 그런 의미로 post_detail에서 for문을 삭제하고 100자로 줄였던 문자를 삭제함으로써 각각의 post_id에 따라
    # 페이지에 해당 파일이 들어갈 수 있도록 했다.
    context = {
        'post':post,
    }
    # return HttpResponse(post_id)

    # 숙제: post_detail view function이 올바르게 동작하는 html을 작성해서 결과보기

    return render(request, 'blog/post_detail.html', context)

def post_create(request):
    # print(request.GET.get('title'))

    if request.method == 'POST':
        # request의 method값이 'POST'일 경우 (POST method로 요청이 왔을경우)
        # request.POST에 있는 title, text값과
        # request.user에 있는 USER인스턴스(로그인한 유저)속성을 사용해서
        # 새 POST인스턴스를 생성
        # HttpResponse를 사용해 새로 생성된 인스턴스의 id, title, text정보를 출력(string)

        post = Post.objects.create(
            author=request.user,
            title=request.POST.get('title'),
            text=request.POST.get('text')
        )
        # return HttpResponse('id:{}, title:{}, text:{}'.format(post.id, post.title, post.text))
        # post.author는 객체

        # HTTP Redirection을 보낼 URL은 http://localhost:8000/ <- 도메인
        # '/'은 가장 최 하단
        # /로 시작하면, 절대경로, 절대경로의 시작은 도메인 :http://localhost:8000/
        # return HttpResponseRedirect('/')

        # post.delete()  # 이렇게 해도 지워진다.
        return redirect('post-list')

    else:
        return render(request, 'blog/post_create.html')

def post_delete(request, post_id):
    # 연결되는 URL: localhost:8000/3/delete

    # 템플릿을 사용하지 않음(render하는 경우가 없음) -> 그냥 지우기만 하고 넘어가면 되니까 굳이 렌더링이 필요없다.

    # view function의 동작
    # 1. 오로지 request.method 가 'POST'일 때만 동작
    # (request.method가 'GET'일 때는 아무 동작도 안해도 됨

    # 2. request.method가 'POST'일때의 동작
    # post_id에 해당하는 Post인스턴스에서 delete()를 호출해서 DB에서 삭제
    # 이후 post-list(url name)로 redirect

    # post_list.html템플릿에서 for문을 순회하는 각 요소마다 form을 하나씩 추가
    # action은 post_delete() view function으로 연결되는 url
    # -> url태그를 사용한다, post_list.html에서 post_detail()로 연결하는 url생성법 참조

    # method는 POST
    # 내부에 있어야 할 input요소는 없음, 버튼 하나만 존재(삭제)
    # POST요청이므로 csrf_token태그를 각 form안에 사용할 것

    # 실제동작: post_list.html의 각 요소에 생성된 버튼을 클릭하면 이 함수가 실행되어야 함
    # breakpoint를 아래 리턴에 걸어놓은 후 request내의 내용을 확인
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        post.delete()
        return redirect('post-list')
    return HttpResponse('post_delete view function')

def post_edit(request, post_id):
    # request.method가 'POST' 일때 post_id에 해당하는 Post의 title과 text를 수정함
    # 수정 완료 후 post-retail페이지로 이동
    # method가 'GET'일때, post_id에 해당하는 Post의 title과 text가 이미 존재하는