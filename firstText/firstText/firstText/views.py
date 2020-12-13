# file created by me

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    #return HttpResponse("Home")

def analyze(request):
     #get the text
     djtext = request.POST.get('text','default')

     # Check checkbox values
     removepuc = request.POST.get('removpunc','off')
     capitalupper = request.POST.get('capitalize','off')
     newlineremover = request.POST.get('newlineremov','off')
     extraSpaceremove = request.POST.get('extrspacremov','off')
     chactercounter = request.POST.get('charcount','off')
         #print(removepuc)
         #print(djtext)

     # check which checkbx is on
     # Remove Punctuations
     if removepuc == "on":
         #analyze the text
         #analyzed = djtext
         punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
         analyzed = ""
         for char in djtext:
             if char not in punctuations:
                 analyzed=analyzed + char
         params = {'purpose':'Removed Punctuation','analyze_text':analyzed}
         djtext = analyzed
         #return render(request,'analyze.html',params)

     # Change into Uppercase
     if (capitalupper == "on"):
         analyzed = ""
         for char in djtext:
             analyzed = analyzed+char.upper()
         params = {'purpose': 'Capitalized Letter', 'analyze_text': analyzed}
         djtext = analyzed
         #return render(request, 'analyze.html', params)

     # Remove New Line or Whitespace
     if newlineremover == "on":
         analyzed = ""
         for char in djtext:
             if char !="\n" and char!="\r":
                 analyzed = analyzed + char
             else:
                 print("no")
             print("pre", analyzed)
         params = {'purpose': 'Remove new Line', 'analyze_text': analyzed}
         djtext = analyzed
         #return render(request, 'analyze.html', params)

     # Remove Extra Space from Text
     if extraSpaceremove == "on":
         analyzed = ""
         for index, char in enumerate(djtext):
             if not (djtext[index]== " " and djtext[index + 1] == " "):
                 analyzed = analyzed + char
         params = {'purpose': 'Extra Space Remove ', 'analyze_text': analyzed}
         djtext = analyzed
         #return render(request, 'analyze.html', params)

    # Count Character
     if chactercounter == "on":
         analyzed = len(djtext)

         params = {'purpose': 'Count Character for Text', 'analyze_text': analyzed}
       #  djtext = analyzed
         #return render(request, 'analyze.html', params)

     if (removepuc!= "on" and capitalupper!= "on" and newlineremover!= "on" and extraSpaceremove!= "on" and chactercounter!= "on"):
         return HttpResponse("Enter Some Tesxt!!!!!!!!!!")

     return render(request, 'analyze.html', params)

