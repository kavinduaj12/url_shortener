from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import UrlData
from .form import UrlForm
import random
import string

# Create your views here.

def home(request):
    if request.method=='POST':
        form=UrlForm(request.POST)
        if form.is_valid():
            slug=''.join(random.choice(string.ascii_letters) for x in range(10))
            url=form.cleaned_data["url"]
            if request.user.is_authenticated:
                new_url=UrlData(user=request.user,url=url,slug=slug)
            else:
                public_user=User.objects.get(username='public')
                new_url=UrlData(user=public_user,url=url,slug=slug)
            new_url.save()
            return redirect('home')
    else:
        form=UrlForm()
    if request.user.is_authenticated:
        data=UrlData.objects.filter(user=request.user)
    else:
        public_user=User.objects.get(username='public')
        data=UrlData.objects.filter(user=public_user)
    context={'form':form,'data':data}
    return render(request, 'core/home.html', context)

def delete(request,id):
    data=UrlData.objects.get(id=id)
    data.delete()
    return redirect('home')

def urlRedirect(request,slugs):
    data=UrlData.objects.get(slug=slugs)
    return redirect(data.url)