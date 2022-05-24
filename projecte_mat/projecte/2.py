print("Introdueix les opcions necessaries: ")
print("Domini: ")
lloc = input()
print("Total de cerques: ")
total = input()
print("Aplicacio on buscar els filtres: ")
mesop = input()
from subprocess import call
call(["python3" ,"theHarvester.py", '-d', lloc,"-l",total,"-b",mesop])

