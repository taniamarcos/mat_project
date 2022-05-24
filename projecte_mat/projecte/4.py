#!/usr/bin/python3
import nmap
import pyfiglet
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
#ip_addr = '192.168.202.147'
scanner = nmap.PortScanner()
 
while not salir:
   
    print ("1. Descobrir l'estat del host")
    print ("2. Llistar serveis i versions dels ports oberts")
    print ("3. Llistar vulnerabilitats d'un rang")
    print ("4. Salir")
    opcion = pedirNumeroEntero()

    if opcion == 1:
        host=input("[+] Introduix la IP del host: ")
        nm = nmap.PortScanner()
        nm.scan(hosts=host, arguments='-n -sP --script vuln')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

        for host, status in hosts_list:
            print(host + ' ' + status)
   
    elif opcion == 2:
        host=input("[+] Introduix la IP de l'objectiu: ")
        nm=nmap.PortScanner()
        results=nm.scan(host)
        #print (results)
        print("Host : %s" % host)
        print("State : %s" % nm[host].state())
        for proto in nm[host].all_protocols():
            print('Protocol : %s' % proto)
            lport = nm[host][proto].keys()
            sorted(lport)
            for port in lport:
                print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

    elif opcion == 3:
        ip_addr = input()
        print("Nmap Version: ", scanner.nmap_version())
        # Aquí, v s'utilitza per verbose, el que significa que si se selecciona, donarà informació adicional
        # 1-1024 significa el número de port on volem cercar
        # -sS significa realitzar una exploració de connexió TCP SYN, envia els paquets SYN a l'amfitrió
        scanner.scan(ip_addr, '1-1024', '-n -sS --script vulners')
        print(scanner.scaninfo())
        # state() ens indica si el target està up o down
        print("Ip Status: ", scanner[ip_addr].state())
        # all_protocols() ens indica quins protocols estan disponibles TCP UDP etc
        #nmap.nmap.PortScannerError: 'An option is required for -s, most common are -sT (tcp scan), -sS (SYN scan), -sF (FIN scan), -sU (UDP scan) and -sn (Ping scan)\n'
        print("protocols:", scanner[ip_addr].all_protocols())
        print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

    elif opcion == 4:
        salir = True
    else:
       print ("Introdueix un numero entre 1 y 6")

print ("Adeu :)")
