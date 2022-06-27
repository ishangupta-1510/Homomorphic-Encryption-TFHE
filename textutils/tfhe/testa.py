from ast import Num
from datetime import time
import subprocess 
from subprocess import Popen, PIPE
from tokenize import Number 
from threading import Timer
import time
def runFunc(txt1, txt2):
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