import subprocess
import os

print(__file__)

if (__file__.startswith("/home")):
    print("Linux !")
elif (__file__.startswith("C:\\")):
    print("Windows !")
else:
    print("Mac !")
