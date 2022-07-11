from ast import Num
from datetime import time
from re import S
import subprocess 
from subprocess import Popen, PIPE
from tokenize import Number 
from threading import Timer
import time
import struct
def runFunc1(txt1, txt2):
    t1=bytes(txt1+'\n', encoding='utf8')
    t2=bytes(txt2+'\n', encoding='utf8')
    print(t1)
    print(t2)
    global result
    print("Inside Python file.....")
    subprocess.call(["gcc","account.c", "-o", "account.o"])
    program_path = "./account.o"
    p1 = subprocess.Popen(["./account.o"], stdout=subprocess.PIPE, stdin=PIPE, stderr = subprocess.PIPE)
    p1.stdin.write(t1)
    p1.stdin.write(t2)
    p1.stdin.flush()
    print("hello")
    #p1.stdout.flush()
    result = p1.stdout.read()
    result = int(result)
    print(result)
 
    # print("this is result")
#     result1 = int.from_bytes(result, "big")
#    # result1=int(result)
#     print(result1)
   
  #  print(result1)
    # p.stdin.flush()
def result():
    return result
def subFunc(txt1,txt2):    
    t11 = int(txt1)
    t22 = int(txt2)
    print("Inside Python file.....")
    # print(txt1)
    # print(txt2)
    subprocess.call(["gcc","sub.c", "-o", "sub.o"])
    program_path = "./sub.o"
    sub = subprocess.Popen(["./sub.o"], stdout=subprocess.PIPE, stdin=PIPE, stderr = subprocess.PIPE)
    # ret = sub.stdout.readline()
    # print(ret)
    t33 = b'%d\n' %t11
    t44 = b'%d\n' %t22
    # print(t3)
    sub.stdin.write(t33)
    sub.stdin.write(t44)
    sub.stdin.flush()
    sub.stdin.close()
    sub1 = sub.stdout.readline()
    print(sub1)
    global subtract
    subtract = int(sub1)
    print("ans ")
    print(subtract)
    print("Task is done.")

def subtract():
    return subtract
def runFunc(txt1,txt2):
    t1 = int(txt1)
    t2 = int(txt2)
    print("Inside Python file.....")
    # print(txt1)
    # print(txt2)
    subprocess.call(["gcc","alice.c", "-o", "alice.o", "-ltfhe-spqlios-fma"])
    # subprocess.call(["./alice.o"])
    program_path = "./alice.o"
    p = subprocess.Popen(["./alice.o"], stdout=subprocess.PIPE, stdin=PIPE, stderr = subprocess.PIPE)
    t3 = b"%d\n" % t1
    t4 = b"%d\n" % t2
    # print(t3)
    p.stdin.write(t3)
    p.stdin.write(t4)
    p.stdin.flush()
    doNext()

def doNext():
    time.sleep(6)
    subprocess.call(["gcc", "cloud.c", "-o", "cloud.o", "-ltfhe-spqlios-fma"])
    subprocess.call("./cloud.o")
    subprocess.call(["gcc", "verify.c", "-o", "verify.o", "-ltfhe-spqlios-fma"])
    p = Popen("./verify.o", stdout=PIPE, stdin=PIPE)
    result = p.stdout.readline().strip()
    # print("this is result")
    print(result)
    global ans
    ans = int(result)
    print("ans ")
    print(ans)
    print("Task is done.")

def answer():
    return ans
def uploadFunc():
    subprocess.call(["gcc","Owner.c", "-o", "owner.o", "-ltfhe-spqlios-fma"])
    # subprocess.call(["./alice.o"])
    program_path = "./owner.o"
    p = subprocess.Popen(["./owner.o"], stdout=subprocess.PIPE, stdin=PIPE, stderr = subprocess.PIPE)
    global up
    up='File upload successfully'
    print(up)
def up(request):
    return up

def verifyFunc():
    subprocess.call(["gcc","verify1.c", "-o", "verify1.o", "-ltfhe-spqlios-fma"])
    # subprocess.call(["./alice.o"])
    program_path = "./verify1.o"
    p = subprocess.Popen(["./verify1.o"], stdout=subprocess.PIPE, stdin=PIPE, stderr = subprocess.PIPE)
   # print(p)
    verify = p.stdout.readline()
    # print(verify)
    global ver
    ver = verify.decode()
    # print("vari=")
    # print(veri)
    i = -1
    j = 0
    global ar
    ar = [[0]*8 for _ in range(10)]
    s = ""
    print("vart=")
    print(ver)
    for element in ver:
        if(element == ","):
            ar[i][j] = int(s)
            # print(i,j)
            # print(ar[0][0])
            # print("s=")
            # print(i)
            # print(j)
            # print(s)
            j+=1
            s = ""
        elif(element == " "):
            print(i,j)
            print(ar[0][0])
            print("run")
            i+=1
            s=""
            j=0
            # print(i,j)
        else:
            s+=element
        # if(element == " "):
        #     k = ""
        #     j=0
        #     for i in range(len(s)):
        #         if(s[i] != ","):
        #             k+=s[i]
        #         else:
        #             arr[i][j] = int(k)
        #             j+=1
        #             # print("k=")
        #             # print(k)
        #             k=""
        #     # print("arr[i]=")
        #     # print(arr[i])
        #     # print("\n")
        #     s = ""
        #     i+=1
        #     j=0
        # s+=element
    # i=0
    # for x in arr:
    #     print("x")
    #     print(x[i])
    #     i+=1

   # veri = [verify for x in verify]
    #veri=int(verify)
    # print(veri)
def v():
    # print("arr")
    # print(arr[0][0])
    # for i in range(len(arr)):
    #     for j in range(len(arr[0])):
    #         print(arr[i][j])
    return ar