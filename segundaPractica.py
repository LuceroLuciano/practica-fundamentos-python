#nombre = input('intoduce tu nombre: ')
#print(f "Hola {nombre}")
#print("hola, {}".format(nombre))


# tercera practica AI
# generar un numero aleatorio
import random

# para instalar eso nececitas
# python3 -m pip install -U matplotlib
# libreria para generar graficas
import matplotlib.pyplot as plt 

print(random.randint(1, 20))

print(random.randrange(10, 100, 10))

# reacomodar una lista al azar
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('lista original', lista)

# mescla los elementos de la lista al azar
random.shuffle(lista)
# imprimi la lista mezclada
print('lista mixeada', lista)

# genera los datos de la grafica
campana = [random.gauss(1, 0.5) for i in range(1000)]
print(campana)
# arma la grafica
plt.hist(campana, bins = 15)
# muestra la grafica
plt.show()
