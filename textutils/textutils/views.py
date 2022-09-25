
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def aboutus(request):
    return render(request, "aboutus.html")

def contactus(request):
    return render(request, "contactus.html")

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')



    if removepunc=='on':
        analyzed=""
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_'''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose': 'removed punctuations', 'analyzed_text': analyzed}
        djtext=analyzed

    if(fullcaps=='on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed

    if(newlineremover=='on'):
        analyzed = ""
        for char in djtext:
            if char !='\n' and char!='\r':
                analyzed = analyzed + char
        params = {'purpose': 'Removed new line', 'analyzed_text': analyzed}
        djtext=analyzed

    if(extraspaceremover =='on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed spaces', 'analyzed_text': analyzed}
        djtext = analyzed

    if (charcount == 'on'):
        analyzed = 0
        for char in djtext:
            analyzed = analyzed + 1
        params = {'purpose': 'Removed spaces', 'analyzed_text': analyzed}
        djtext = analyzed

    if(charcount!= 'on'and extraspaceremover !='on' and newlineremover!='on' and fullcaps!='on' and removepunc!='on'):
        return HttpResponse('Error')

    return render(request, "analyze.html", params)