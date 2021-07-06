from django.shortcuts import render,redirect
from .models import UrlData
from .form import UrlForm
import random
import string

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            slug = ''.join(random.choice(string.ascii_letters)
                           for x in range(10))
            url = form.cleaned_data["url"]
            new_url = UrlData(url=url, slug=slug)
            new_url.save()
            return redirect('home')
    else:
        form=UrlForm()
    data=UrlData.objects.all()
    context={
        'form':form,
        'data':data
    }
    return render(request, 'core/home.html', context)

def delete(request,id):
    data=UrlData.objects.get(id=id)
    data.delete()
    return redirect('home')

def urlRedirect(request, slugs):
    data=UrlData.objects.get(slug=slugs)
    return redirect(data.url)