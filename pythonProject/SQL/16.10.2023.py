"""
BD Curs 5 - JOINS
Join-uri (jonctiuni)
 - interogare simultana a mai multor tabele intre care exista legaturi

TIPURI DE JOINS
 - CROSS JOIN - este rezprezentat de toate combinatiile posibile intre doua tabele
ex:
angajati                departamente
marian                      hr
cristina                    dev
                            qa
marian - hr             cristina - hr
marian - dev            cristina - dev
marian - qa             cristina - qa

- SELF JOIN - join dintr-o tabela cu ea insasi

angajati            manager         manager_mai_mare        manager_the_boss
- >>> mai rapid va fi sa facem o singura tabela cu toti, intrucat si managerii tot angajati sunt
- avem tabela angajat
ex:
id          nume            manager_id
1           marian          2
2           mihai           3
3           gigel           null
4           miruna          3
5           alexandra       4

gigel este the big boss

nume                nume_manager
marian              mihai
mihai               gigel
gigel               null
miruna              gigel
alexandra           miruna


 - UNION - aduce toate rezultatele la un loc din mai multe query-uri

################################################################################################

JOIN-URI FOARTE IMPORTANTE
 - INNER JOIN (default) - aduce toate inregistrarile care au corespondenta in tabelele interogate
 - OUTER JOIN - aduce inregistrarile care sunt corespunzatoare unei laturi ale relatiei; restul de atribute
 vor fi completate cu NULL
 - avem: LEFT JOIN si RIGHT JOIN


"""