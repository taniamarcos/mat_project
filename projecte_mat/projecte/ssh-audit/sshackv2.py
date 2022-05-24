print("Auditoria ssh")
print("")
print("IP:")
mesop = input()
print("")

print("----------------------------------------------------------------------------------")
from subprocess import call
call(["python3" ,"/projecte/ssh-audit/ssh-audit.py", mesop])
print("----------------------------------------------------------------------------------")
