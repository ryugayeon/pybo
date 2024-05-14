from django.http import HttpResponse

def index(request):
    return HttpResponse("엔코아에 오신 것을 환영합니다.")
