from django.shortcuts import render

# Create your views here.


def system_root_page(request):
    context={}
    return render(request, 'system_home.html', context)