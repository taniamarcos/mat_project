#!/usr/bin/python3
from subprocess import call
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
 
    print ("1. Opcion Politiques seguretat")
    print ("2. Opcion Audit")
    print ("3. Salir")
    opcion = pedirNumeroEntero()

    if opcion == 1:
       print ("")
       print ('Has triat poliques')
       call(["python3","/projecte/ssh-audit/sshack.py"])
    elif opcion == 2:
       print ("")
       print ('Has triat auditoria')
       call(["python3","/projecte/ssh-audit/sshackv2.py"])
    elif opcion == 3:
       salir = True
    else:
       print ("Introduce un numero entre 1 y 3")

print ("Bye :)")
