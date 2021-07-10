from accountapp.models import HelloWorld
from django.http import HttpResponse,  HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render


def Hello_World(request):
#    return HttpResponse("Hello World!")
 #   return render(request, 'accountapp/hello_world.html') # 장고는 templates 경로를 지정해 놓으면, 앱 하위의 templates 경로도 인식한다.

    if request.method == "POST":
        temp = request.POST.get('hello_world_input')
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()

        return render(request, "accountapp/hello_world.html", context={'hello_world_list': hello_world_list})
# Create your views here.
