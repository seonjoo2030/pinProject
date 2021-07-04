from django.http import HttpResponse
from django.shortcuts import render


def Hello_World(request):
#    return HttpResponse("Hello World!")
 #   return render(request, 'accountapp/hello_world.html') # 장고는 templates 경로를 지정해 놓으면, 앱 하위의 templates 경로도 인식한다.

    if request.method == "POST":
        return render(request, "accountapp/hello_world.html", context={'text': 'POST METHOD'})
    else:
        return render(request, "accountapp/hello_world.html")
# Create your views here.
