from django.shortcuts import render
from django.http import HttpResponse

from .models import Userform

# Create your views here.
def index(request):
    #return HttpResponse('Hello Nimish')

    userform = Userform.objects.all()[:10]

    context = {
        'title' : 'User',
        'userform': userform
    }

    return render(request, 'userform/index.html', context)

def details(request, id):
    user = Userform.objects.get(id=id)

    context = {
        'user': user
    }
    return render(request, 'userform/details.html',context)