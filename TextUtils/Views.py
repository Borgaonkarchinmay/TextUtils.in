#Chinmay created file

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def textAnalyze(request):

    #Read the Text from Browser
    djText = request.POST.get('inputText', 'default')

    #Check status of checkboxes
    rempunc = request.POST.get('remPunc', 'off')
    upperCase = request.POST.get('UpperCase', 'off')
    capsfirst = request.POST.get('capsFirst', 'off')
    remnewline = request.POST.get('newlineRem', 'off')
    remspace = request.POST.get('spaceRem', 'off')
    charcount = request.POST.get('charCount', 'off')

    analyzedText = ""
    purpose = ""
    manipulate = False

    # Manipulate strings
    if remspace == "on":
        manipulate = True
        for char in djText:
            if char != " ":
                analyzedText = analyzedText + char
        djText = analyzedText
        purpose = purpose + "Remove Space"

    if remnewline == "on":
        manipulate = True
        analyzedText = ""
        for char in djText:
            if char != "\n" and char != "\r":
                analyzedText = analyzedText + char
        djText = analyzedText
        purpose = purpose + ", Remove New Line"

    if rempunc == "on":
        manipulate = True
        analyzedText = ""
        punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        for char in djText:
            if char not in punctuations:
                analyzedText = analyzedText + char
        djText = analyzedText
        purpose = purpose + ", Remove Punctuations"

    if capsfirst == "on":
        manipulate = True
        analyzedText = ""
        analyzedText = djText.capitalize()
        djText = analyzedText
        purpose = purpose + ", Capitalize First Letter"

    if upperCase == "on":
        manipulate = True
        analyzedText = ""
        analyzedText = djText.upper()
        djText = analyzedText
        purpose = purpose + ", Convert to UpperCase"

    if charcount == "on":
        manipulate = True
        count = 0
        for char in djText:
            if char != " ":
                count = count + 1

        analyzedText = "Count of Characters: " + str(count)
        purpose = purpose + ", Count of Characters"

    if manipulate == False:
        purpose = "No manipulations Chosen"
        analyzedText = djText

    params = {'purpose': purpose, 'analyzed_text': analyzedText}
    return render(request, 'resultPage.html', params)

