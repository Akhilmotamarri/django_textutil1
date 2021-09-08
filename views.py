# i have created this file-akhil
#code for video 7
from django.http  import HttpResponse
from django.shortcuts import render
import string
# def index(request):
#     return HttpResponse("hello how are you")
# def about(request):
#     return HttpResponse("this is akhil good boy")
# def facebook(request):
#     return HttpResponse('''<a href="https://www.facebook.com/">facebook</a>''');
# def whatsapp(request):
#     return HttpResponse('''<a href="https://web.whatsapp.com/">whatsapp</a>''');

#code for video 8
def index(request):
    # params={'name':'Akhil','place':'mars'}
    return render(request,'index.html')
    # return HttpResponse("Home")
def repunc(request):
    djtext=request.GET.get('text','default') #to get the test from text area
    repunc = request.GET.get('removepunc', 'off')
    print(repunc)
    print(djtext)
    punctuations=string.punctuation;
    analyzedtext=" "
    if repunc=='on':

        for char in djtext:
            if char not in punctuations:
                analyzedtext+=char
    else:
        analyzedtext=djtext
    params={'purpose':'remove punctuations','analyzed':analyzedtext}
    return render(request,'analyze.html',params)
    # return HttpResponse("remove punctuation"+"<br>"+'''<a href="http://127.0.0.1:8000">Back<a/>''')

# def capfirst(request):
#     return HttpResponse("capitalize first"+"<br>"+'''<a href="http://127.0.0.1:8000">Back<a/>''')
# def newlineremove(request):
#     return HttpResponse("newlineremove"+"<br>"+'''<a href="http://127.0.0.1:8000">Back<a/>''')
# def spaceremove(request):
#     return HttpResponse("spaceremove"+"<br>"+'''<a href="http://127.0.0.1:8000">Back<a/>''')
# def charcount(request):
#     return HttpResponse("charcount"+"<br>"+'''<a href="/">Back<a/>''')