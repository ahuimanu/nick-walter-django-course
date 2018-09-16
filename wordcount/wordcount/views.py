from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html', {'test': 'WORD COUNT'})

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.POST['fulltext']
    wordlist = fulltext.split(' ')

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #increase
            worddictionary[word] += 1
        else:
            #add dictionary
            worddictionary[word] = 1

    #sort the word list
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', 
        {'fulltext': fulltext, 'count': len(wordlist), 'sortedwords': sortedwords})


