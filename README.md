# MAT PROJECT
**MENÚ:**
1. APi shodan
2. Harvester
3. OSINT
4. Escaneig Nmap
5. Auditoria SSH
6. Enumeració
7. Enviar Informe
8. Sortir

## API SHODAN
   **Introduir IP** (associada a un domini p.ex: 8.8.8.8)
   Resultat: Domini associat a la ip
            Ports oberts associats al domini
            I la IP associada al domini
## THE HARVESTER
   Introduir domini a analitzar. P.ex: iesebre.com
   Total busquedes (nombre enter). P.ex: 50
   Més opcions: lloc on buscarà noms associats al domini intorudït inicialment. P.ex: twitter
   Resultat: UsuarisIPs, email i hosts associats a l'aplicació (twitter)
   
## ESCANEIG NMAP
   ### 1. DESCOBRIR HOSTS DE XARXA
          Introduir la ip del host (la qual volem saber si està up o no)
          Resultat: Si està actiu el host, acompanya la'IP':'up'
   ### 2. LLISTAR SERVEIS I VERSION DELS PORTS OBERTS
          Introduir la ip del host, el qual està up
          Resultat: Host, estat (up o no), protocols utilitzats, i ports oberts amb el seu respectiu estat.
          
   ### 3. LLISTAR VULNERABILITATS D'UN RANG
        *Acabar d'implementar
   ### 4. SORTIR

## AUDITORIA SSH
  ### 1. OPCIÓ POLITIQUES SEGURETAT
      - Escollir entre els tipus de política (segons si ets client o servidor)
      - Introduir la IP associada al host
        Resultat:
              - Host
              - Política escollida
              - Resultat de l'auditoria
              - Errors trobats durant el procés
              
  ### 2. OPCIÓ AUTID
      Introduim la ip del host al qual es fara un escaneig de la configuració del OpenSSH
      Resultat: Sortides en color verd -> Bona pràctiva
                Sortides en color groc -> Configuracions millorables
                Sortides en vermell -> Mala configuració
  ### 3. SORTIR

## ENUMERACIÓ
  ### 1. LLISTAR USUARIS (necessari tenir port 139 (samba) obert)
      **S'ha de tenir en compte si ens hem instal·lat l'OpenSSH server o client**
      Introduir la ip del host al qual ser li farà la cerca

              
  ### 2. LLISTAR PC
  ### 3. POLITICA D'INFORMACIÓ
  ### 4. LLISTAR RECURSOS COMPARTITS
  ### 5. LLISTAR GRUPS I MEMBRES
  ### 6. PERSONALITZACIÓ
  ### 7. SORTIR
 
## ENVIAR INFORME
   Enviar informe pel bot de telegram
## SORTIR
  
  
  
  
    
      
        


   
