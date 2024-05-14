from django.http import HttpResponse

def index(request):
    return HttpResponse("장고 메인입니다^^.")
