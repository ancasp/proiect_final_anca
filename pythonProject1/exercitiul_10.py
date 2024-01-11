# Scrieti o functie asincronă async si executati cu 4 exemple simultan. Functia va printa pătratele perfecte
# de la numar_1 la numar_2.

# Pentru a crea o funcție asincronă care să afișeze pătratele perfecte între două numere și pentru a executa simultan
# patru exemple ale acestei funcții, putem folosi modulul asyncio în Python. Iată cum puteți face acest lucru:

import asyncio

async def print_perfect_squares(num_1, num_2):
    for num in range(num_1, num_2 + 1):
        if num >= 0 and int(num ** 0.5) ** 2 == num:
            print(f"Pătratul perfect: {num}")

async def main():
    tasks = [
        print_perfect_squares(1, 10),
        print_perfect_squares(11, 20),
        print_perfect_squares(21, 30),
        print_perfect_squares(31, 40)
    ]

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())


# Această soluție utilizează asyncio pentru a crea patru exemple ale funcției print_perfect_squares și le rulează
# simultan în cadrul funcției main. Funcția print_perfect_squares verifică dacă numărul este un pătrat perfect
# și îl afișează.
# Puteți personaliza intervalul și numărul de exemple sau să adăugați alte numere în lista de apeluri
# ale funcției print_perfect_squares pentru a executa mai multe căutări simultan.





