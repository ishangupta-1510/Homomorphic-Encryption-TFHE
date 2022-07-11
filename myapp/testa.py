from ast import Num
from datetime import time
import subprocess 
from subprocess import Popen, PIPE
from tokenize import Number 
from threading import Timer
import time
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
    t33 = b"%d\n" % t11
    t44 = b"%d\n" % t22
    # print(t3)
    sub.stdin.write(t33)
    sub.stdin.write(t44)
    sub.stdin.flush()
    sub1 = sub.stdout.readline().strip()
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