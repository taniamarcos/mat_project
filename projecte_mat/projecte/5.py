#!/usr/bin/python3
from subprocess import call
def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Tria l'opcio: "))
            correcto=True
        except ValueError:
            print('Error, introdueix un numero enter')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print ("1. Opcio Politiques Seguretat")
    print ("2. Opcio Audit")
    print ("3. Sortir")
    opcion = pedirNumeroEntero()

    if opcion == 1:
       print ("")
       print ('Has triat poliques de seguretat')
       call(["python3","/projecte/ssh-audit/sshack.py"])
    elif opcion == 2:
       print ("")
       print ('Has triat auditoria')
       call(["python3","/projecte/ssh-audit/sshackv2.py"])
    elif opcion == 3:
       salir = True
    else:
       print ("Introdueix un numero entre 1 y 3")

print ("Adeu :)")
