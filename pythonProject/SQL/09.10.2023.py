"""
BD CURS 1 - teorie

Bazele de date - o multime de date ce sunt structurate la nivel de linii si coloane - adica in forma tabulara - in acest
fel fiind usor de folosit
ex: un fisier excel poate simula un fel de baza de date, iar tabelele acestei baze de date pot fi simulate de catre
sheet-urile excelului
 - pentru un user este mult mai usor sa aiba datele structurate intr-o baza de date. El poate accesa, actualiza sau
 face diferite operatiuni pe acasta baza de date foarte usor.

 - root - are acces la toate functionalitatile unei baze de date

date vs informatii

ex de data: 40
informatie = Afara sunt 40 de grade. Masa are 40 cm lungime
informatiile = sunt datele care sunt puse intr-un context

Baze de date RELATIONALE

SGBD - Sistem de Gestionare a Bazelor de Date. In engleza DBMS - Database Management System
 - ce este SGBD? tool-ul/IDE-ul pe care il folosim pt a manipula datele dintr-o baza de date
ex de SGBD: SQL SERVER (SSMS), Oracle, MySQL Workbench, Dbeaver, etc
SGBD reprezinta interfata dintre user si datele stocate intr-o baza de date


RELATII - avem 3 tipuri de relatii:
1. One-to-one
2. One-to-many
3. Many-to-many

1. One-to-one - unei inregistrari din tabela A ii corespunde o singura inregistrare din atbela B, iar unei inregistrari
din tabela B ii corespunde o singura inregistare din tabela A

Exemple:
persoana - CI
elev - numar matricol
masina - talon
persoana - carnet de conducere
angajat - badge

2. One-to-many - unei inregistrari din tabela A ii corespund mai multe inregistrari din tabela B, iar unei inregistrari
din tabela B ii corespunde o singura inregistrare din tabela A.

Exemple:
departament - angajat
masina - membrii familiei
doctor familie - mai multi pacienti
clasa - elev
persoana - adresa email
produs - review


3. Many-to-many  - unei inregistrari din tabela A ii corespund mai multe inregistrari din tabela B, iar unei i
nregistrari din tabela B ii corespund mai multe inregistrari din tabela A.
!!! aceasta exista doar in teorie - practic implementarea ei se va face folosind 2 relatii one-to-many

Exemple:
produs - comanda
persoana - nationalitate
student - facultate
carte - autori
candidat - lista vot
doctor - spitale




NORMALIZARE - proces prin care eliminam anomaliile din baza de date

Sunt 5 forme normale (FN)
vom vorbi despre cele mai cunoscute, anume primele 3 forme normale
1. FN1
2. FN2
3. FN3


1. FN1
 - exista doar valori atomice
 - nu exista grupuri repetitive
exemplu:
produs:
id_review
12, 13, 14 - - - - - - -GRESIT

id_review - - - - - - - CORECT
12
13
14



2. FN2
 - se respecta FN1
 - nu exista dependinte partiale - se aplica doar cand avem cheie primara compusa
 - toate atributelele non cheie depind in totalitate de cheia primara - vom mai gasi formularea DEPENDENTA FUNCTIONAL
 COMPLETA




3. FN3
 - se respecta FN2
 - fara dependinte tranzitive
dependinta tranzitiva - situatie cand un atribut non-cheie depinde de un alt atribut, care la randul lui depinde de un
alt atribut, care la randul lui depinde de un alt atrinut, etc...., care la randul lui depinde de o cheie primara







"""