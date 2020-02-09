from django.shortcuts import render

# Create your views here.


def StartPageView(req):
    return render(req, 'startPage.html')
