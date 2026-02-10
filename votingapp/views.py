from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from templates.votingapp import *

# Create your views here.

arr = ['Java', 'Python', 'Cplusplus', 'C', 'DotNET', 'JavaScript', 'PHP', 'Swift', 'SQL', 'Ruby', 'Delphi', 'Objective-C', 'Go', 'Assemblylanguage', 'VisualBasic', 'D', 'R', 'Perl', 'MATLAB']
globalcnt = dict()

def index(request):
    mydictionary = {
        'arr': arr
    }
    return render(request, 'index.html', context=mydictionary)

def getquery(request):
    q = request.GET.get('languages')
    if q in globalcnt:
        globalcnt[q] += 1
    else:
        globalcnt[q] = 1
    mydictionary = {
        "arr": arr,
        "globalcnt": globalcnt
    }
    return render(request, 'index.html', context=mydictionary)
