from django.db import models
from django.contrib.auth.models import User
#파이보 - 질문답변 게시판

#질문 모델(DB) 작성
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) #작성자 ,안붙이게 조심
    subject = models.CharField(max_length=200) #제목
    content = models.TextField() #내용
    create_date = models.DateTimeField() #작성일시
    modify_date = models.DateTimeField(null=True, blank=True) #수정일시, 수정할 경우에만 데이터 생성됨

    def __str__(self):
        return self.subject #데이터 유형 출력을 제목값 출력으로 변경

#답변 모델 작성
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 작성자 ,안붙이게 조심
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #다른 모델과 연결(질문 모델), 함께 삭제
    content = models.TextField() #내용
    create_date = models.DateTimeField() #작성일시
    modify_date = models.DateTimeField(null=True, blank=True) #수정일시, 수정할 경우에만 데이터 생성됨

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) #댓글 글쓴이
    content = models.TextField() #댓글 내용
    create_date = models.DateTimeField() #댓글 작성일시
    modify_date = models.DateTimeField(null=True, blank=True) #댓글 수정일시
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE) #이 댓글이 달린 질문
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE) #이 댓글이 달린 답변