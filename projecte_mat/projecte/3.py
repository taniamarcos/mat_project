#!/usr/bin/python3
import pyfiglet
from subprocess import call
def banner():

    ascii_banner = pyfiglet.figlet_format("Osint")
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
            num = int(input("Tria una opció: "))
            correcto=True
        except ValueError:
            print('Error, introdueix un número senser')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print ("1. Holehe")
    print ("2. Ghunt")
    print ("3. Udork")
    print ("4. Wafwoof")
    print ("5. Mosint")
    print ("6. Sortir")
    opcion = pedirNumeroEntero()

    if opcion == 1:
       print ("")
       print ('Has seleccionat Holehe')
       call(["python3","osint/1.py"])
       print ("")
    elif opcion == 2:
       print ("")
       print ('Has seleccionat Ghunt')
       call(["python3","osint/2.py"])
       print ("")
    elif opcion == 3:
       print ("")
       print ('Has seleccionat Udork')
       call(["python3","osint/3.py"])
       print ("")
    elif opcion == 4:
       print ("")
       print ('Has seleccionat Escaneig Wafwoof')
       call(["python3","osint/4.py"])
       print ("")
    elif opcion == 5:
       print ("")
       print ('Has seleccionat Mosint')
       call(["python3","osint/mosint/5.py"])   
       print ("")
    elif opcion == 6:
       salir = True
       
    else:
       print ("Tria Opcio")
print ("Bye :)")
