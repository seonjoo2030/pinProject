from accountapp.models import HelloWorld
from django.http import HttpResponse
from django.shortcuts import render


def Hello_World(request):
#    return HttpResponse("Hello World!")
 #   return render(request, 'accountapp/hello_world.html') # 장고는 templates 경로를 지정해 놓으면, 앱 하위의 templates 경로도 인식한다.

    if request.method == "POST":
        temp = request.POST.get('hello_world_input')
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return render(request, "accountapp/hello_world.html", context={'hello_world_output': new_hello_world})
    else:
        return render(request, "accountapp/hello_world.html")
# Create your views here.
