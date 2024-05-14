from django import forms
from .models import Question, Answer, Comment

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        """
        # form.as_p가 항목을 자동으로 생성해줘 부트스트랩 사용이 불가
        # -> widgets 속성을 이용해 부트스트랩 적용
        widgets = {
            'subject' : forms.TextInput(attrs={'class':'form-control'}),
            'content' : forms.Textarea(attrs={'class':'form-control', 'rows':10}),
        # label 속성 한글로 수정
        }
        """
        labels = {
            'subject' : '제목',
            'content' : '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content' : '답변내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content' : '댓글내용',
        }