"""
BD CURS 2

SGBD - au doua limbaje
LDD - limbajul de scriere al datelor. In engleza: DDL - Data Description Language
LMD - limbajul de manipulare al datelor. In engleza: DML - Data Manipulation Language

COMENZI LDD/DDL

 - CREATE TABEL/CREATE DATABASE - comanda prin care cream o baza de date sau o tabela
 - DROP TABLE/DROP DATABASE - stergere definitiva a unei tabele sau a unei baze de date
 - ALTER TABLE - ne ajuta la modificarea structurii unei tabele deja create
 - CREATE VIEW/DROP VIEW - comenzi pt a crea sau sterge tabele virtuale
 - GRAND CONNECT - comanda pt a oferi acces unui user la o baza de date


COMENZI LMD/ DML
 - actualizarea informatiilor dintr-o tabela: INSERT, UPDATE, DELETE
 - pentru a interoga o tabela (query): SELECT - afisarea datelor din tabela intr-un output in interfata
 - alte functionalitati: SUM, AVERAGE, MIN, MAX, etc.


conceptul CRUD - CREATE, READ, UPDATE, DELETE     (se intalneste in toate limbajele de programare)
                INSERT, SELECT, UPDATE, DELETE   (pt SQL)

La nivel de server (care are un sistem de operare instalat, care de cele mai multe ori este Linux):
    - bazele de date (BD) sunt niste foldere/directoare
    - tabelele sunt reprezentate sub forma unor fisiere in aceste foldere


Cand vom crea tabele / BD - treb uie sa tinem cont de restrictiile impuse de catre sistemul de operare


Restrictii & good practices:
 - nu este case sensitive - putem scrie ori cu litere mici, ori cu litere mari, ori cu o combinatie
ex: produs = Produs = PRODUS
 - in numele tabelelor sau ale BD, nu putem folosi spatii libere si nici caractere speciale
 - nu putem denumi o tabela sau BD folosind doar cifre, trebuie sa folosim caractare alfanumerice
 - intotdeauna cand vom crea o BD sau o tabela, numele acesteia trebuie sa inceapa cu o litera nu cu o cifra
GRESIT: 1234, 1produs, 2produs, tabela mea
CORECT: produs, produs1, produs2, tabelaMea, tabela_mea
 - intotdeauna dupa ce finalizam de scris o instructiune sau un bloc de cod, trebuie sa punem punct si virgula

 - o linie de cod:
 select * from ceva;

 - bloc de cod:
 select * form ceva
 where id = 1 and data=today()
 and ... ;

 - este recomandat ca numele tabelelor sau ale BD sa fie la singular. Nu este gresit daca le vom avea la plural,
 in schimb, desi nici asa nu e gresit, este de evitat sa avem o combinatie singular - plural
  - in cadrul serverului numele BD sunt unice
  - in cadrul BD numele tabelelor sunt unice


In cadrul crearii tabelelor, putem folosi doua metode:
 - denumire absoluta - daca nu avem o BD selectata ca baza default (adica o baza pe care lucram), in momentul crearii
 trebuie sa specificam in ce BD se va crea tabela
ex: <nume_bd>.<nume_tabela>
CREATE TABLE magazin.produs():

 - denumire relativa - daca avem o BD setata ca default, nu mai este nevoie sa folosim denumirea absoluta
ex:
USE magazin; - setez o BD ca default
CREATE TABLE produs(); - cream tabela


####################################################################################################################


TIPURI DE DATE

 - SIRURI DE CARACTERE sunt de doua tipuri: CHAR si VARCHAR
ex:
produs
produs bun
produs de nota 10
produs foarte bun


CHAR (lungime_maxima) - are o lungime fixa a nr de caractere indiferent de cate caractere sub nr maxim vor fi inserate,
el va aloca intotdeauna numarul maxim
CHAR(13) - pentru CHAR(13), oricate caractere pana in 13 se vor adauga, memoria alocata va fi mereu de 13
ex:
masina - 6 caractere. Daca vom folosi CHAR(13), desi cuvantul meu are 6 caractere, memoria alocata va fi de 13
caractere, Deci practic 7 caractere vor fi irosite


VARCHAR(lungime_maxima) - are lungime variabila. I se va aloca un nr maxim de caractere dar vor fi stocate nr de
caractere ale datei introduse
VARCHAR(13) - se poate aloca memorie pt maxim 13 caractere, dar memoria se va aloca de fapt pentru  cate caractere (<=13)
se vor adauga
VARCHAR(13)
masina - 6 caractere. Este sub nr maxim de 13, deci memoria mea alocata va fi pentru 6 caractere


BLOB - Binary Long Object - fisiere encodate
 - se foloseste spre exemplu pt a stoca o poza


TINYINT ==> tip de date numeric - poate stoca date - 128 si 127 (tip de date signed - putem avea si valori negative)
TINYINT UNSIGNED ==> pana la 255 - poate avea doar nr pozitive


INT - tip de data numeric
INT(6) - numarul maxim care poate fi stocat: 999999
- in versiunile actuale are lui MySQL Workbench va aparea in Action Output o notificare (avertizare) cum ca nu va mai fi
nevoie sa specificam nr maxim de caractere

DOUBLE() - tip de data numeric
DOUBLE(8,3) - nr maxim care poate fi stocat: 99999,999 - in total nr va avea 8 cifre dintre care 3 vor fi dupa virgula

DATE - inregistram datele calendaristice
 - adaugam datele sun forma de string: "2023-10-10"
 - adaugam datele sub forma de date: 20231010

ENUM - putem avea anumite valori, care sunt niste valori predefinite
status_produs ENUM ("in stoc", "lipsa stoc")
status_comanda ENUM ("Platita", "In procesare", "Expediata", "Anulata", "Livrata")


SET~ENUM
culoare SET("rosu", "alb", "negru")

BOOLEAN - valoarea de adevar a unei expresii TRUE/FALSE (in baza de date vom avea 1/0)


INDECSI

 - ne ajuta sa adaugam restrictii: UNIQUE, PRIMARY KEY, FOREIGN KEY
 - ne ajuta la optimizarea memoriei/vitezei: INDEX
 - desi sunt foarte utili nu este ok sa abuzam de ei, deoarece ne pot incurca foarte tare, viteza poate scadea dramatic


#####################################################################################################################


Sintaxa de crearea a unei BD

CREATE DATABASE curs2;

Pentru a seta o BD ca default:

USE curs2;

Sintaxa de creare a unei tabele

CREATE TABLE <nume_tabela> (
    <nume_atribut1> <tip_atribut1> [NULL/NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT]*,
    <nume_atribut2> <tip_atribut2>,
    etc.....,
    <constrangeri>*
);
* optionale

 - auto_increment: cauta valoarea maxima a unei linii (atribut) iar noua inregistrare va avea nr maxim de linii + 1
 - se asociaza doar unui PRIMARY KEY de tip INT

ex:
id PRIMARY KEY AUTO_INCREMENT


id      produs
1       telefon
2       tableta
3       casti
4       mouse
5       husa telefon


id      produs
1       telefon
                     - produsul 2 nu mai este prezenta in oferta magazinului sau a fost stearsa din varii motive
3       casti           (ori nu il va afisa in output, ori va aparea NULL)
4       mouse
5       husa telefon
6       PC
7       Laptop
etc...


NU PUTEM CREA O CONEXIUNE INTRE DOUA TABELE FOLOSIND RELATII INTRE PK SI FK DACA ACESTEA NU AU ACELASI TIP DE DATA








"""