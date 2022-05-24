import shodan
from subprocess import call
#Configuració

API_KEY = 'oelxCyCDvzlcHmi3TVVVvMKznkwWQMoc'
api = shodan.Shodan(API_KEY)

print ('')
print ('Introdueix la IP del host: ')
ip = input()
results = api.host(ip)
for item in results['data']:
  print("""
    Domain: {}
    Port: {}
    IP:{}
    """.format(item['domains'], item['port'],item['ip_str']))

#call(["python3","1.py",">","1.txt"])
    
