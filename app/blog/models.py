from django.utils import timezone
from django.conf import settings
from django.db import models

# Create your models here.


class Post(models.Model):
    # models안에 있는 Model을 상속받는다.
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)  # 길이 제한 있는 text
    text = models.TextField(blank=True)  # 길이가 무한인 text
    created_date = models.DateTimeField(default=timezone.now)  # date와 time을 저장해놓은 필드
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        # 나 자신의 발행일자에 현재 시작을 넣고(타임존 나우를 호출) 후 세이브 호출
        self.published_date = timezone.now()
        self.save() # 모델 안에 정의되어 있는 메서드

    def __str__(self):  #객체를 문자열로 정의하고 싶을 때 사용
        return self.title
