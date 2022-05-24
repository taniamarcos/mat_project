FROM python:3

RUN mkdir projecte

ADD projecte_mat/projecte /projecte/

RUN apt update -y

RUN apt install apt-file -y

RUN apt-file update

RUN apt install samba samba-client -y

RUN chmod +x /projecte/enumeracio/enum4linux.pl

RUN apt install vim -y

RUN pip install python-nmap

RUN pip install pyfiglet

RUN pip install shodan

RUN pip install aiodns

RUN apt install rsync -y

RUN python3 -m pip install -r projecte/requirements.txt

RUN apt update && apt install nmap -y

#CMD ["/usr/local/bin/python3","/projecte/mat.py"]

#ENTRYPOINT ["/usr/local/bin/python3","/projecte/mat.py"]