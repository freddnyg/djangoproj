from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddict = {}

    for word in wordlist:
        if word in worddict:
            #increase
            worddict[word] += 1
        else:
            #add to thedict
            worddict[word] = 1

    wordssorted = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)


    print(fulltext)
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'wordssorted':wordssorted})

def about(request):
    return render(request, 'about.html')