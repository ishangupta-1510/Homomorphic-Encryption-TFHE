# Made by me - Manan Patel
import django.shortcuts
from django.http import HttpResponse
from django.shortcuts import render
import subprocess 
from .tfhe.testa import runFunc
from subprocess import Popen, PIPE
from textutils.tfhe import testa
from threading import Timer
def index(request):
    return render(request, 'index.html')

def analyze(request):
    #Getting the text
    textx = request.POST.get('text1', 'default')
    texty = request.POST.get('text2', 'default')
    #Getting value of radio buttons

    #Analyzing text
    job = ""
    analyzed = ""
    numchar = 0
    punctuations = '''!()-[]{};:'"\/,<>.?@#$%^&*~`'''
    analyzed = ""
    for char in textx:
        if char not in punctuations:
            analyzed += char
    job += '| Removed Puntuations '
    textx = analyzed

    count = 0
    for char in textx:
        if not (char == " " and char == '\n'):
            count += 1

    # c = answer()
    txt1 = textx
    txt2 = texty
    runFunc(txt1, txt2)
    numchar = testa.answer

    # print(valone())
    # valtwo()
    params = {'job':job , 'analyzed_text':analyzed, 'numchar':numchar}
    return render(request, 'analyze.html', params)
