#This is created by me.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse("<a href='https://gujacpc.admissions.nic.in/mba-mca/'>ACPC MBA/MCA</a> ")
    #params={'name':'shashank','place':'ahmedabad'}
    return render(request,'index.html')

def analyze(request):
    djtext = (request.POST.get('text', 'default'))
    removepunc = (request.POST.get('removepunc', 'off'))
    fullcaps = (request.POST.get('fullcaps', 'off'))
    newlineremover = (request.POST.get('newlineremover', 'off'))
    spaceremover = (request.POST.get('spaceremover', 'off'))

    if removepunc == "off" and fullcaps == "off" and newlineremover == "off" and spaceremover == "off":
        return HttpResponse("Error: Please select at least one option.")
    
    if removepunc=="on":

        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    if fullcaps=="on":
        analyzed=djtext.upper()
        params={'purpose':'capitalized sentence','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char
        params={'purpose':'Removed new line','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    if spaceremover=="on":
        analyzed=""
        for char in djtext:
            if char !="  ":
                analyzed = analyzed + char
        params={'purpose':'Removed space','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error")
    
    

#def capfirst(request):
#    return HttpResponse("Capitalize first")

#def newlineremove(request):
#    return HttpResponse("newlineremove")

#def spaceremove(request):
#    return HttpResponse("spaceremove")

#def charcount(request):
#    return HttpResponse("char count")
