import subprocess

if (__file__.startswith('/home')):
    print("Linux !")
elif (__file__.startswith('c:\\')):
    print("Windows !")
else:
    print("Mac !")
