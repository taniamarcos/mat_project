#!/usr/bin/python3
import pyfiglet
from subprocess import call
def banner():

    ascii_banner = pyfiglet.figlet_format("Enumaració")
    print("---------------------------------------")
    print(ascii_banner)
    print("---------------------------------------")
    print("(+) By MAT \n")


banner()
def pedirNumeroEntero():

    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Tria la opció: "))
            correcto=True
        except ValueError:
            print('Error, introdueix un numero senser')

    return num

salir = False
opcion = 0

while not salir:

    print ("1. Llistar usuaris")
    print ("2. Llistar pc")
    print ("3. Politica de informació")
    print ("4. Llistar recursos compartits")
    print ("5. Llistar grups i membres")
    print ("6. Perzonalització")
    print ("7. Sortir")
    opcion = pedirNumeroEntero()

    if opcion == 1:
       #userlist = input()
       print ("")
       print ('Llistar usuaris')
       print ('Introduiex una IP:')  
       userlist = input()
       print ("---------------------------------------")
       call(["./enum4linux.pl","-U",userlist])
       print("---------------------------------------")
       print ("")
    elif opcion == 2:
       print ("")
       print ('Llistar pcs')
       print ('Introduiex una IP:')  
       pclist = input()
       print ("---------------------------------------")
       call(["./enum4linux.pl","-M",pclist])
       print ("---------------------------------------")
       print ("")
    elif opcion == 3:
       print ("")
       print ('Politica de informació')
       print ('Introduiex una IP:')  
       sharelist = input()
       print ("---------------------------------------")
       call(["./enum4linux.pl","-P",sharelist])
       print ("---------------------------------------")
       print ("")
    elif opcion == 4:
       print ("")
       print ('Introduiex una IP:')  
       print ('Llistar recursos compartits')
       sharelist = input()
       print ("---------------------------------------")
       call(["./enum4linux.pl","-S",sharelist])
       print ("---------------------------------------")
       print ("")
    elif opcion == 5:
       print ("")
       print ('Llistar grups i membres')
       print ('Introduiex una IP:')  
       print ("---------------------------------------")
       gim = input()
       call(["./enum4linux.pl","-G",gim])
       print ("---------------------------------------")
       print ("")
    elif opcion == 6:
       print ("Personalitzat")
       print ('Opcions que podem utilizar')
       print ("-U        get userlist \n"
    		"-M        get machine list \n"
    		"-S        get sharelist \n"
    		"-P        get password policy information \n"
    		"-G        get group and member list \n"
    		"-d        be detailed, applies to -U and -S \n"
    		"-u user   specify username to use \n"
    		"-p pass   specify password to use \n")
       print ('Introduiex una opcio:')
       perso = input()
       print ('Introduiex una ip:')
       ip = input()
       print ("---------------------------------------")
       call(["./enum4linux.pl",perso,ip])
       print ("---------------------------------------")
       print ("")
    elif opcion == 7:
       salir = True
    else:
       print ("Tria opció")
print ("Bye")
