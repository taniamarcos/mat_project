print("LListat de politques")
from subprocess import call
call(["python3" ,"/projecte/ssh-audit/ssh-audit.py", "-L"])

print("Comprovacio de la politica de segueretat")
tipo = input()
print("Tipus de politica")
lloc = input()
print("IP")
mesop = input()
print("")

print("----------------------------------------------------------------------------------")
from subprocess import call
call(["python3" ,"/projecte/ssh-audit/ssh-audit.py", tipo, lloc,mesop])
print("----------------------------------------------------------------------------------")
