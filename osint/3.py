import pyfiglet
from subprocess import call
call(["clear"]) 
def banner():

    ascii_banner = pyfiglet.figlet_format("uDork")
    print("------------------------------------------")
    print(ascii_banner)
    print("------------------------------------------")
    print("(+) By MAT \n")
banner()

print("Introdueix domini:")
domini = input()
print("Opcions disponbles:")
print("-e all o -e extensio \n-t ""Twitter angel"" for twitter \n-u all search all \n-g admins Lists administration ")

opcio = input()

call(["osint/uDork/./uDork.sh",domini,opcio])
