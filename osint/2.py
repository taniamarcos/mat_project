import pyfiglet
from subprocess import call
call(["clear"]) 
def banner():

    ascii_banner = pyfiglet.figlet_format("Ghunt")
    print("------------------------------------------")
    print(ascii_banner)
    print("------------------------------------------")
    print("(+) By MAT \n")
banner()

print("Opcions disponbles:")
print("- email \n - doc \n - gaia\n - youtube ")

correu = input()

call(["holehe",correu])



