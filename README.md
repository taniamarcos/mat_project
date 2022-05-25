# MAT PROJECT

**Alçar contenidor**

  Ens ubiquem dins de la carpeta del projecte i executem:

  *docker build -t python-menuscan .*

**Executar contenidor**

  *docker run -it python-menuscan bash*

**Eliminar contenidor**

  *docker rmi python-menuscan*

**Ubicació script: /projecte**

**Execució: python3 mat.py**

<img src="/imatges/mat.png" width="550" title="hover text">

**MENÚ:**
1. API Shodan
2. Harvester
3. OSINT
4. Escaneig Nmap
5. Auditoria SSH
6. Enumeració
7. Enviar Informe
8. Sortir

## 1. API SHODAN
    **Introduir IP** (associada a un domini p.ex: 8.8.8.8)
    Resultat: Domini associat a la ip
            Ports oberts associats al domini
            I la IP associada al domini
## 2. THE HARVESTER
    Introduir domini a analitzar. P.ex: iesebre.com
    Total busquedes (nombre enter). P.ex: 50
    Més opcions: lloc on buscarà noms associats al domini introduït inicialment. P.ex: twitter
    Resultat: UsuarisIPs, email i hosts associats a l'aplicació (twitter)

## 3. OSINT
  ### 3.1 HOLEHE
      Introduir correu associat a l'usuari que volem comprovar a quines plataformes està registrat
      Resultat: Llista d'aplicacions disponibles on les que es marquin en color **verd** serà que l'usuari si que hi té compte.
  ### 3.2 GHUNT
      * Acabar d'implementar
      Eina per a buscar informació (pdf, vídeos...) associat al compte de correu (email, youtube...)

  ### 3.3 UDORK
      * Acabar d'implementar

  ### 3.4 MAFWOOF
      Introduir **URL** (P.ex: https://amazon.com )
      Resultat: Ens específica si aquest té algun firewall al núvol
  ### 3.5 MOSINT
      * Acabar d'implementar 
  ### 3.6 SORTIR
   
## 4 ESCANEIG NMAP
   ### 4.1 DESCOBRIR HOSTS DE XARXA
          Introduir la ip del host (la qual volem saber si està up o no)
          Resultat: Si està actiu el host, acompanya la'IP':'up'
   ### 4.2 LLISTAR SERVEIS I VERSION DELS PORTS OBERTS
          Introduir la ip del host, el qual està up
          Resultat: Host, estat (up o no), protocols utilitzats, i ports oberts amb el seu respectiu estat.
          
   ### 4.3 LLISTAR VULNERABILITATS D'UN RANG
        *Acabar d'implementar
   ### 4.4 SORTIR

## 5. AUDITORIA SSH
  ### 5.1 OPCIÓ POLÍTIQUES SEGURETAT
      - Escollir entre els tipus de política (segons si ets client o servidor)
      - Introduir la IP associada al host
        Resultat:
              - Host
              - Política escollida
              - Resultat de l'auditoria
              - Errors trobats durant el procés
         **S'ha de tenir en compte si ens hem instal·lat l'OpenSSH server o client**      
  ### 5.2 OPCIÓ AUTID
      Introduir la ip del host al qual es farà un escaneig de la configuració del OpenSSH
      Resultat: Sortides en color verd -> Bona pràctiva
                Sortides en color groc -> Configuracions millorables
                Sortides en vermell -> Mala configuració
  ### 5.3 SORTIR

## 6. ENUMERACIÓ
  ### 6.1 LLISTAR USUARIS (necessari tenir port 139 (samba) obert)
     Introduir la ip del host al qual ser li farà la cerca
     Resultat: Llistat d'usuaris associats al host, si està unit a un workgroup/domain...


  ### 6.2 LLISTAR PC
      Introduir la ip del host al qual ser li farà la cerca
      Resultat: Llistat de màquines associades al host

  ### 6.3 INFORMACIÓ POLÍTICA DE PASSWORDS
      Introduir la ip del host al qual ser li farà la cerca
      Resultat: Polítiques aplicades dels passwords associats al host

  ### 6.4 LLISTAR RECURSOS COMPARTITS
      Introduir la ip del host al qual ser li farà la cerca
      Resultat: Llistat de recursos compartits
  ### 6.5 LLISTAR GRUPS I MEMBRES
      Introduir la ip del host al qual ser li farà la cerca
      Resultat: Llistat de grups i membres
  ### 6.6 PERSONALITZACIÓ
      Introduir un valor dels quals es mostra amb el llistat d'opcions. Lliure elecció de paràmetres a utilitzar
      Introduir IP del host
      Resultat: Segons els paràmetres escollits anteriorment
  ### 6.7 SORTIR
 
## 7. ENVIAR INFORME
   Enviar informe pel bot de telegram
## 8. SORTIR

   
