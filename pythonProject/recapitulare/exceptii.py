lista = ["Ion", "Ana", "Elena"]
x = 4
try:
    print(lista[x])
except IndexError:
    print(f"Ati incercat sa accesati elementul cu indexul {x}, dar lista are doar {len(lista)}")
finally:
    # se executa indiferent daca s-a executat mai sus try sau except
    print("Se executa no matter what")

print("Ce frumos este afara")

