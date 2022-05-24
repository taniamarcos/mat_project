print("Posa les teves opcions ")
print("Domini")
lloc = input()
print("Total busquedes")
total = input()
print("Mes opcions")
mesop = input()
from subprocess import call
call(["python3" ,"theHarvester.py", '-d', lloc,"-l",total,"-b",mesop])

