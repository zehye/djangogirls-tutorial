import os

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string

from .models import Post


def post_list(request):
    """
    first/
        first_file.txt
        second/
            second_file.txt
            third/
                module.py
                fourth/
                    fourth_file.txt

    module.py에서
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

    posts = Post.objects.all()
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
    posts = Post.objects.all()
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
    )


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post':post
    }
    # return HttpResponse(post_id)

    # 숙제: post_detail view function이 올바르게 동작하는 html을 작성해서 결과보기
    return render(request, 'blog/post_detail.html', context)