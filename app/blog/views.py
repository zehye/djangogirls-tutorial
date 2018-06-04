import os

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string


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
    html = render_to_string('blog/post_list.html')

    # 가져온 문자열 돌려주기
    return HttpResponse(html)  # 특정 리퀘스트가 올떄 보통 http로 오고 여기로 응답을 보내는데 응답을 보내기 위한 무언가를 만들어줘
