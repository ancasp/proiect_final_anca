"""
Virtual Environment (venv) - comenzile se dau in CMD

- reprezinta un mediu incapsulat care nu cominuca cu exteriorul
- intr-un venv pot avea diferite versiuni de Python fata de mediul de lucru standard
- pot avea alte versiuni ale unor module deja instalate pe mediul de lucru standard
- de la verisunea 3.3 a Python, este o functionalitate standard
- putem crea cate venv-uri dorim

Virtualenv
- instalam modulul pentru crearea unui virtualenv
pip install virtualenv

cream un virtualenv:
virtualenv <numele.dorit>

Pentru a activa un virtualenv, folosim urmatoarea comanda:
pentru Windows:  <numele.dorit>\Scripts\activate.bat
pentru Mac:   source <numele.dorit>/bin/activate

- pentru a dezactiva un venv folosim comanda deactivate

Avantaje
 - faciliteaza lucrul cu mai multe verisuni ale aceluiasi modul e.g. openpyxl 3.1.2 vs openpyxl 2.4.11
 - ajuta la izolarea proiectelor intre ele la nivel de environment
Dezavantaje
 - activarea lui nu este intuitiva
 - daca dorim sa determinam unde a fost creat este destul de neintuitiv
 - crearea lui se face in diverse locatii, nu pot avea o lista cu evidenta tuturor environmenturilor


Virtualenvwrapper
pentru a se instala pe windows: pip install virtualenvwrapper-win
pentru a il crea, folosim comanda: mkvirtualenv <numele_dorit>
pentru a il activa, folosim comanda: workon <numele_dorit>
pentru dezactivare folosim comanda deactivate

lsvirtualenv - listeaza toate modulele create doar cu virtualwrapper
rmvirtualenv <nume_dorit> - stergem un venv


-----------------------------------------------------------------------------------


pypi.org - aici gasim toate libariile Python

modulul este codul scris de cineva pe care putem sa le folosim si noi
modulele sunt de 3 feluri: standard, cele pe care le importam noi si cele pe care le cream noi
"""