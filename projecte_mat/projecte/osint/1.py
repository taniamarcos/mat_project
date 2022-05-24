import pyfiglet
from subprocess import call
call(["clear"]) 
def banner():

    ascii_banner = pyfiglet.figlet_format("Holehe")
    print("------------------------------------------")
    print(ascii_banner)
    print("------------------------------------------")
    print("(+) By MAT \n")
banner()

print("Introdueix el correu:")
correu = input()

call(["holehe",correu])



