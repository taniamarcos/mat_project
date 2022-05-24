#!/usr/bin/python3
import pyfiglet
from subprocess import call
def banner():

    ascii_banner = pyfiglet.figlet_format("Auditoria    MAT")
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
            num = int(input("Tria la opcio: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print ("1. APi shodan")
    print ("2. Harvester")
    print ("3. OSINT")
    print ("4. Escaneig Nmap")
    print ("5. Auditoria SSH")
    print ("6. Enumeració")
    print ("7. Enviar Informe")
    print ("8. Salir")
    opcion = pedirNumeroEntero()

    if opcion == 1:
       print ("")
       print ('Has APi shodan')
       call(["python3","1.py"])
       print ("")
    elif opcion == 2:
       print ("")
       print ('Harvester')
       call(["python3","2.py"])
       print ("")
    elif opcion == 3:
       print ("")
       print ('OSINT')
       call(["python3","3.py"])
       print ("")
    elif opcion == 4:
       print ("")
       print ('Escaneig Nmap')
       call(["python3","4.py"])
       print ("")
    elif opcion == 5:
       print ("")
       print ('Auditoria SSH')
       call(["python3","5.py"])   
       print ("")
    elif opcion == 6:
       print ("")
       print ('Enumeració')
       call(["python3","enumeracio/6.py"])  
       print ("") 
    elif opcion == 7:
       print ("")
       print ('Enviar Informe')
       call(["python3","7.py"])  
       print ("") 
    elif opcion == 8:
       salir = True
    else:
       print ("Tria Opcio")
print ("Bye :)")
