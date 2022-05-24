print("LListat de politques")
from subprocess import call
call(["python3" ,"/projecte/ssh-audit/ssh-audit.py", "-L"])

#print("Comprovacio de la politica de segueretat")
#tipo = input()
print("Quin tipus de politica vols comprovar? Selecciona segons vulguis comprovar un client o un servidor: ")
lloc = input()
print("Introdueix la IP del host: ")
mesop = input()
print("")

print("----------------------------------------------------------------------------------")
from subprocess import call
call(["python3" ,"/projecte/ssh-audit/ssh-audit.py", "-P",lloc,mesop])
print("----------------------------------------------------------------------------------")
