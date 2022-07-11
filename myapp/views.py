# Made by me - Manan Patel
import django.shortcuts
from django.http import HttpResponse
from django.shortcuts import render
import subprocess
from .tfhe.testa import runFunc,runFunc1, subFunc, uploadFunc,verifyFunc
from subprocess import Popen, PIPE
from myapp.tfhe import testa
from threading import Timer
def index(request):
    return render(request, 'index.html')
def adminP(request):
    a = request.POST.get('abc', 'default')
    tuid = request.POST.get('tuid', 'default')
    tpassword = request.POST.get('tpassword', 'default')
    runFunc1(tuid, tpassword)
    numchar1 = 0
    #numchar2 = numchar1.decode()
    num= testa.result
    print(num)
    #return render(request, 'adminP.html')
    if 'abc' in request.POST:
        return render(request, 'adminP.html')
    if (num==1):
        return render(request, 'adminP.html')
    else: 
        return render(request, 'index.html')
    analyzed=''
    # print(valone())

    # valtwo()
   # params = {'analyzed_text':analyzed, 'numchar':numchar1}
   # return render(request, 'welcome.html', params)
def upload(request):
 #   runFunc3()
  #  runFunc4()
   # numchar1 = testa.Fresult
    return render(request, 'upload.html')
    # print(valone())
    # valtwo()
    #params = { 'numchar':numchar1}
    #return render(request, 'analyze.html', params)
def output(request):
    if 'abc' in request.POST:
        return render(request, 'adminP.html')
    if 'upload' in request.POST:
        uploadFunc()
        numchar = testa.up
    elif 'verify' in request.POST:
        verifyFunc()
        numchar = testa.v()
        # print(type(numchar))
        i=0
        arr = [[0]*11] * 11
        # print("numchar")
        # print(numchar[1])
        # arr[0] = numchar[0].split(",")
        # print("arr[0]=")
        # print(arr[0])
        # arr[1] = numchar[1].split(",")
        # arr[2] = numchar[2].split(",")
        # arr[3] = numchar[3].split(",")
        # arr[4] = numchar[4].split(",")
        # arr[5] = numchar[5].split(",")
        # arr[6] = numchar[6].split(",")
        # arr[7] = numchar[7].split(",")
        # arr[8] = numchar[8].split(",")
        # arr[9] = numchar[9].split(",")
        print("numchar")
        print(type(numchar))
        # print(numchar)
        # print("numchar=")
        # print(numchar)
    params = {'numchar':numchar}
    return render(request, 'output.html', params)
def query(request):
    #Getting the text
    return render(request, 'query.html')
def result(request):
    textx = request.POST.get('text1', 'default')
    texty = request.POST.get('text2', 'default')
    textz = request.POST.get('text3', 'default')
    textu = request.POST.get('text4', 'default')
    textv = request.POST.get('text5', 'default')
    txt1 = textx
    txt2 = texty
    txt3 = textz
    txt4 = textu
    txt5 = textv
    global numchar
    if 'sexe' in request.POST:
      return render(request, 'welcome.html')
    elif 's1exe' in request.POST:
       return render(request, 'welcome.html')
    elif 's2exe' in request.POST:
      return render(request, 'welcome.html')
    elif 's3exe' in request.POST:
      return render(request, 'welcome.html')   
def welcome(request):
    #Getting the text
    return render(request, 'welcome.html')

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
    if 'add' in request.POST:
        runFunc(txt1, txt2)
        numchar = testa.answer
    elif 'sub' in request.POST:
        subFunc(txt1,txt2)
        numchar = testa.subtract
   
    # print(valone())
    # valtwo()
    params = {'job':job , 'analyzed_text':analyzed, 'numchar':numchar}
    return render(request, 'analyze.html', params)
def analyzesub(request):
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
    subFunc(txt1, txt2)
    numchar = testa.subtract

    # print(valone())
    # valtwo()
    params = {'job':job , 'analyzed_text':analyzed, 'numchar':numchar}
    return render(request, 'analyze.html', params)
