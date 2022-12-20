from django.shortcuts import render
# from stock.models import Member

# Create your views here.
def mainFunc(request):
    return render(request,'main.html')

#테스트용으로 만든 함수 필요없으면 삭제
def loginFunc(request):
    # userData=Member.objects.all()
    # return render(request,'user/login.html',{'userData':userData})
    return render(request,'user/login.html')

#테스트용으로 만든 함수 필요없으면 삭제
def boardFunc(request):
    return render(request,'board/list.html')