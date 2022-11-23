import subprocess

if (__file__.startswith('/home')):
    subprocess.Popen(("gnome-terminal.real", "/usr/bin"))
elif (__file__.startswith('c:\\')):
    print("Windows !")
else:
    print("Mac !")
