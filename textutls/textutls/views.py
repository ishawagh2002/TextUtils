from django.http import HttpResponse
from django.shortcuts import render
 

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('text','default')
    print(djtext)
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover','off')
    charcount = request.POST.get('charcount','off')
    if removepunc == "on": 
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
                
        isha = {'purpose':'Removed Puntuations' , 'analyzed_text': analyzed}
        djtext = analyzed

        # return render(request, 'analyze.html', isha )
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper() 
        isha = {'purpose':'Uppercase Done' , 'analyzed_text': analyzed}
        djtext = analyzed

        # return render(request, 'analyze.html', isha )  
    if newlineremover =="on":  
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        isha = {'purpose':'New Line Removed' , 'analyzed_text': analyzed}
        djtext = analyzed

        # return render(request, 'analyze.html', isha )
    if (spaceremover =="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed += char
        isha = {'purpose':'Space Removed' , 'analyzed_text': analyzed}
        djtext = analyzed

        # return render(request, 'analyze.html', isha )  
    
    elif charcount =="on":
        analyzed = ""
        letter_count = 0
        for char in djtext:
            if char.isalpha():
                letter_count += 1

                analyzed = letter_count
        isha = {'purpose':'The number of character' , 'analyzed_text': analyzed}
        djtext = analyzed

        # return render(request, 'analyze.html', isha )
            
    if(removepunc != "on" and fullcaps != "on" and newlineremover !="on" and spaceremover !="on" and charcount !="on"):
        return HttpResponse("Select any operatin <a href = '/'>Back</a>")
        # return HttpResponse("Write Proper Text in the Textarea  <a href = '/'> Back </a>")

    return render(request, 'analyze.html', isha )    
    
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')



    