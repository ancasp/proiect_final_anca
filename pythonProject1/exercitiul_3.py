# Creați un program care să citească toate fișierele dintr-un folder de la voi din calculator
# (puteți folosi librăria os, glob...)

# Exemplul 1: Utilizând biblioteca os:
import os

# Specificați calea către directorul în care doriți să căutați fișierele
folder_path = "C:/Users/ancas\Desktop\docs SDA"

# Listă pentru a stoca numele fișierelor găsite
file_list = []

# Iterăm prin directorul specificat
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_list.append(os.path.join(root, file))

# Afisăm numele fișierelor găsite
for file_name in file_list:
    print(file_name)

# Exemplul 2: Utilizând biblioteca glob (pentru a găsi fișiere într-un director specific):

import glob

# Specificați calea către directorul în care doriți să căutați fișierele
folder_path = "C:/Users/ancas\Desktop\sda_52"

# Utilizați glob pentru a găsi toate fișierele din director
file_list = glob.glob(f"{folder_path}/*")

# Afisăm numele fișierelor găsite
for file_name in file_list:
    print(file_name)

# Acest cod va afișa numele tuturor fișierelor din directorul specificat. Puteți alege una dintre cele două abordări,
# în funcție de preferința dvs. și de necesitățile proiectului.