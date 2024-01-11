"""
BD CURS 7

VIEW-URI/ TABELE VIRTUALE

 - un view este reprezentat de un select a carui definitie este stocata pe baza de date
 - el nu contine date
 - prezinta modalitatea prin care se face accesul la date
 - poate fi folosit ca o tabela - are niste proprietati particulare
 - numele unui view trebuie sa fie unic intrucat acesta se stocheaza in acelasi loc precum tabelele
 - daca modificam un view, modificarile se vor face si in tabela din care am creat acest view
 - putem selecta date din mai multe tebele, spre exemplu putem crea job-uri in cadrul acestora
 - din motive de securitate, putem alege ce date vor fi afisate in view
 - un view este mereu asociat unui baze de date - adica acolo unde a fost creat

 Cum definim un view
 CREATE VIEW nume AS ....
 CREATE VIEW angajatiNoi AS
 select * from angajati where data_angajare >= 20231017;

 Cum modificam un view
 ALTER VIEW nume AS ....

 Cum stergem un view
 DROP VIEW nume

  - daca de exemplu vom crea un view cu numele "angajat" intr-o BD unde deja avem o tabele cu numele
"angajat", crearea view-ului va esua intrucat numele "angajat" este deja folosit de catre o tabela


TRANZACTII
 - reprezinta un set de instructiuni ce se executa la nivel atomic
 - daca o instructiune esueaza, BD se poate aduce la starea initiala
 - daca toate instructiunile se executa corect, modificarile vor fi permanente - adica se va face COMMIT
 - folosim tranzactiile pentru a ne asigira ca operatiunile facute pe o baza de date / tabela
 nu vor face modificari partiale
 - by default, MySQL este setat pe AUTOCOMMIT
 - este bine sa dezactivam AUTOCOMMIT-ul in momentul in care vom crea o tranzactie cu mai multe instructiuni

  - cum dezactivam AUTOCOMMIT in 2 moduri:
   - setam AUTOCOMMIT pe 0 - adica rula comanda SET AUTOCOMMIT = 0;
   - folosind START TRANSACTION sau BEGIN
 - pentru a finalzia o tranzactie vom folosi una dintre comenzile COMMIT sau ROLLBACK

 COMMIT - modificarile secrise in instructiunile componente ale tranzactiei devin permanente
 ROLLBACK - modificarile scrise in instructiunile componente ale tranzactiei sunt anulate

 Evenimente care pot cauza un COMMIT
  - clientul executa explicit COMMIT
  - clientul incepe o noua tranzactie; tranzactia in desfasurare se va incheia automat cu COMMIT
  - clientul ruleaza o instructiune DLL

   


"""