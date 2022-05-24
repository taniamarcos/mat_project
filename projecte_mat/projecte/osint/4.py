import pyfiglet
from subprocess import call
call(["clear"]) 
def banner():

    ascii_banner = pyfiglet.figlet_format("Wafw00f")
    print("------------------------------------------")
    print(ascii_banner)
    print("------------------------------------------")
    print("(+) By MAT \n")
banner()

print("Introdueix Domini URL:")
URL = input()

call(["wafw00f",URL])



