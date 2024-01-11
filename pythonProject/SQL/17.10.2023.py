"""
BD Curs 6
Subinterogari, views, tranzactii
 - o subinterogare - reprezinta un SELECT in cadrul unui alt SELECT
 - o folosim cand avem nevoie de o valoare calculata

Ex:
 - aflam ce angajati s-au angajat in acelasi an cu o anumita persoana
 select * from angajat where year(data_angajare) =
 (select year(data_angajare)
 from angajat where nume = "Popescu" and prenume = "Ion");


 TIPURI DE SUBINTEROGARI
 - de tip scalar - imi returneaza o singura valoare
 - de tip lista - imi returneaza o lista de valori
 - de tip rand - imi va returna un rand cu valori, adica o linie cu mai multe coloane
 - de tip tabela - imi returneaza mai multe randuri cu mai multe coloane (tabela de date)

 Cele mai intalnite sunt:
 - de tip scalar
 - de tip lista
 - de tip tabela



"""