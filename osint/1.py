import pyfiglet
from subprocess import call
f=open('2.txt','w')
call(["clear"]) 
def banner():

    ascii_banner = pyfiglet.figlet_format("Holehe")
    print("------------------------------------------")
    print(ascii_banner)
    print("------------------------------------------")
    print("(+) By MAT \n")
banner()

print("Introdueix Correu:")
correu = input()

call(["holehe",correu])
call(["holehe",correu],stdout=f)



