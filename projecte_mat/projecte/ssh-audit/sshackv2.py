print("Auditoria ssh")
print("")
print("Introdueix la IP del host:")
mesop = input()
print("")

print("----------------------------------------------------------------------------------")
from subprocess import call
call(["python3" ,"/projecte/ssh-audit/ssh-audit.py", mesop])
print("----------------------------------------------------------------------------------")
