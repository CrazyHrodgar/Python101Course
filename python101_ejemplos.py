### Código del curso Python 101 — 24 de junio de 2023

# Esto es un comentario

# Asignación de variables
x = 10
y = 100
saludo = 'Hola'
msg = 'Bienvenidos al curso de Pyhton en CICATA'
flag = True

### Valores numéricos
# Enteros
x = 5
y = 6
z = 9

# Flotantes o decimales
decimal = 0.99
pi = 3.1416
euler = 2.7182

# Ejemplo de suma
print(x + y)
# Ejemplo de resta
print(z - x)
# Ejemplo de multiplicación
print(x * y)
# Ejemplo de división
print(z / y)
# Ejemplo de modulo
print(10 % 2) # Devuelve 0
# Ejemplo de división por suelo
print(10 // 20) # Devuelve 2


### Strings
# Operación de indexación y slicing de strings
texto = "Python es genial"

# Indexación
print(texto[0])     # Acceder al primer carácter, imprime: "P"
print(texto[7])     # Acceder al octavo carácter, imprime: "e"
print(texto[-1])    # Acceder al último carácter, imprime: "l"

# Slicing
print(texto[0:6])   # Obtener los caracteres desde el índice 0 hasta el 5, imprime: "Python"
print(texto[7:])    # Obtener los caracteres desde el índice 7 hasta el final, imprime: "es genial"
print(texto[:6])    # Obtener los caracteres desde el inicio hasta el índice 5, imprime: "Python"
print(texto[-6:])   # Obtener los últimos 6 caracteres, imprime: "genial"
print(texto[::3])   # Obtener cada segundo carácter, imprime: "Ph nl"




# Operación de indexación y slicing de strings
texto = "Hola, bienvenidos al curso de Python 101"

# Indexación
print(texto[0])       # Acceder al primer carácter, imprime: "H"
print(texto[5])       # Acceder al sexto carácter, imprime: ","
print(texto[-1])      # Acceder al último carácter, imprime: "1"

# Slicing
print(texto[0:4])     # Obtener los caracteres desde el índice 0 hasta el 3, imprime: "Hola"
print(texto[7:])      # Obtener los caracteres desde el índice 7 hasta el final, imprime: "bienvenidos al curso de Python 101"
print(texto[:4])      # Obtener los caracteres desde el inicio hasta el índice 3, imprime: "Hola"
print(texto[-3:])     # Obtener los últimos 3 caracteres, imprime: "101"
print(texto[::2])     # Obtener cada segundo carácter, imprime: "Hl,bevnoslcus ePto 1"


### Arrays ###

### Listas
numeros = [1, 2, 3, 4, 5]  # Lista de números
nombres = ["Juan", "María", "Carlos"]  # Lista de strings
mezclado = [1, "dos", True, [1, 2, 3]]  # Lista con elementos de diferentes tipos

print(numeros)  # Imprime: [1, 2, 3, 4, 5]
print(nombres)  # Imprime: ["Juan", "María", "Carlos"]
print(mezclado)  # Imprime: [1, "dos", True, [1, 2, 3]]

### Tuplas
# Tupla de nombres de colores
colores = ('rojo', 'verde', 'azul')

# Tupla de coordenadas en un plano
coordenadas = (3.5, -2.8)

# Tupla de información personal
informacion_personal = ('Juan', 'Pérez', 25, 'Calle Principal')

# Tupla de días de la semana
dias_semana = ('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo')

# Tupla de coordenadas geográficas
coordenadas_geograficas = (40.7128, -74.0060)

# Imprimir los valores de las tuplas
print(colores)
print(coordenadas)
print(informacion_personal)
print(dias_semana)
print(coordenadas_geograficas)


# Diccionarios
persona = {
    'nombre': 'Juan',
    'edad': 25,
    'ciudad': 'Madrid'
}

print(persona['nombre'])  # Imprime: 'Juan'
print(persona['edad'])    # Imprime: 25
print(persona['ciudad'])  # Imprime: 'Madrid'


persona['edad'] = 26   # Modificar el valor de 'edad'
persona['genero'] = 'Masculino'   # Agregar una nueva pareja clave-valor

print(persona)  # Imprime: {'nombre': 'Juan', 'edad': 26, 'ciudad': 'Madrid', 'genero': 'Masculino'}

# Un diccionario mas complejo
generos_music = {
    'rock': {
        'origen': 'Estados Unidos',
        'decada': 'década de 1950',
        'artistas_destacados': ['The Beatles', 'Led Zeppelin', 'Queen'],
        'canciones_famosas': ['Stairway to Heaven', 'Bohemian Rhapsody']
    },
    'jazz': {
        'origen': 'Estados Unidos',
        'decada': 'finales del siglo XIX',
        'artistas_destacados': ['Louis Armstrong', 'Miles Davis', 'Ella Fitzgerald'],
        'canciones_famosas': ['Take Five', 'Summertime']
    },
    'pop': {
        'origen': 'Estados Unidos',
        'decada': 'década de 1950',
        'artistas_destacados': ['Michael Jackson', 'Madonna', 'Taylor Swift'],
        'canciones_famosas': ['Thriller', 'Like a Prayer']
    }
}


print(generos_music['rock']['origen'])  # Imprime: 'Estados Unidos'
print(generos_music['jazz']['artistas_destacados'])  # Imprime: ['Louis Armstrong', 'Miles Davis', 'Ella Fitzgerald']
print(generos_music['pop']['canciones_famosas'][0])  # Imprime: 'Thriller'


# Sets
numeros = {1, 2, 3, 4, 4, 5}
print(numeros)  # Imprime: {1, 2, 3, 4, 5}

# Un set con varios tipos de datos
datos = {1, "Hola", True, 3.14}
print(datos)  # Imprime: {1, 'Hola', True, 3.14}

# También pueden declarar un conjunto vacío
conjunto_vacio = set()
print(conjunto_vacio)  # Imprime: set()

# Modificando valores de los sets
frutas = {"manzana", "plátano", "naranja"}

print("manzana" in frutas)  # Verifica si "manzana" está en el conjunto

frutas.add("mango")  # Agrega un elemento al conjunto

frutas.remove("plátano")  # Elimina un elemento del conjunto

print(len(frutas))  # Devuelve la cantidad de elementos en el conjunto

# Aplicando varios métodos a los sets
# Creación de un conjunto
frutas = {"manzana", "plátano", "naranja"}

# Método add()
frutas.add("mango")
print(frutas)  # Imprime: {'manzana', 'plátano', 'naranja', 'mango'}

# Método remove()
frutas.remove("plátano")
print(frutas)  # Imprime: {'manzana', 'naranja', 'mango'}

# Método pop()
elemento = frutas.pop()
print(elemento)  # Imprime un elemento aleatorio del conjunto
print(frutas)   # Imprime el conjunto sin el elemento removido

# Método clear()
frutas.clear()
print(frutas)  # Imprime: set()

# Creación de dos conjuntos para ilustrar otros métodos
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Método union()
union = set1.union(set2)
print(union)  # Imprime: {1, 2, 3, 4, 5, 6, 7, 8}

# Método intersection()
interseccion = set1.intersection(set2)
print(interseccion)  # Imprime: {4, 5}

# Método difference()
diferencia = set1.difference(set2)
print(diferencia)  # Imprime: {1, 2, 3}

### Operadores booleanos y de comparación ###

# Operadores booleanos
a = True
b = False

print(a and b)  # Imprime: False
print(a or b)   # Imprime: True
print(not a)    # Imprime: False

# Otra forma de usar los operadores booleanos
print(a & b) # Imprime False
print(a | b) # Imprimie True

# Operadores de comparación
x = 5
y = 10

print(x == y)  # Imprime: False
print(x != y)  # Imprimie: True
print(x < y)   # Imprime: True
print(x >= y)  # Imprime: False

### Ejemplos de estructuras de control

num = int(input("Ingresa un número: "))

if num > 0:
    print("El número es positivo")
elif num < 0:
    print("El número es negativo")
else:
    print("El número es cero")


calificacion = int(input("Ingresa la calificación del estudiante: "))

if calificacion >= 90:
    print("Aprobado con A")
elif calificacion >= 80:
    print("Aprobado con B")
elif calificacion >= 70:
    print("Aprobado con C")
elif calificacion >= 60:
    print("Aprobado con D")
else:
    print("Reprobado")


num = int(input("Ingresa un número: "))

if num % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

### Ciclos ###

# Ejemplos de ciclo for
frutas = ["manzana", "plátano", "naranja"]

for fruta in frutas:  # Itera sobre cada elemento de la lista 'frutas'
    print(fruta)  # Imprime el valor de cada elemento


# Ahora usamos animales en lugar de frutas
animales = ["león", "tigre", "jirafa", "elefante"]

for animal in animales:
    print(animal) # Imprime cada animal de la lista


# Usando la función range()
for num in range(1, 6):
    print(num) # Imprime una lista de números del 0 al 5

# Ejemplo de ciclos while

contador = 0 # Variable contadora

while contador < 5:
    print(contador) # Imprime el valor de la variable contador
    contador += 1 # Incrementa en 1 el valor de contador


# Usando ciclo while y la estructura if
respuesta = "" # String vacía

while respuesta != "si":
    respuesta = input("¿Quieres continuar? (si/no): ")

    if respuesta == 'si':
        print('Cotinuemos')
    else:
        print('Ciclo cancelado')

# Ejemplo 3
suma = 0
numero = 1

while numero != 0:
    numero = int(input("Ingresa un número (0 para salir): "))
    suma += numero

print("La suma total es:", suma)


### Ejemplos de Funciones

# Ejemplo 1: Saludar
def saludar():
    print('Hola mundo') # Despliega el mensaje 'Hola mundo' cada que se llame la función

# Ejemplo 2: Suma de dos valores
def sumar(a,b):
    resultado = a + b # Realizamos la suma de a y b

    return resultado # Regresa el valor de la suma

suma = sumar(10,5)  # Suma 10 + 5
print(suma) # El resultado debería ser 15


# Ejemplo 3: Verficar si un número es positivo
def es_positivo(numero):
    if numero > 0: # Evaluar la proposición lógica
        return True # Regresar True si es cierto
    else:
        return False # Regreasr False si es falso

# Ejemplo 4: El promedio de una serie de números
def calcular_promedio(lista):
    suma = sum(lista) # Realizamos la suma de todos los elementos
    promedio = suma / len(lista) # Dividir entre la cantidad total de elementos

    return promedio # Regresar el valor medio

numeros = [4, 6, 8, 2, 10] # Declaramos la lista de números
promedio = calcular_promedio(numeros) # Llamamos a la función y guardamos el resultado
print('El promedio es: ', promedio) # Mostramos el promedio

# Ejemplo 5: Saludo personalizado
def saludo(nombre, mensaje='Hola!'):
    print(mensaje, nombre)

saludo('Juan') # Esta linea regresaria 'Hola! Juan'
saludo('Maria', 'Bienvenida') # Esta linea regresaría 'Bienvenida María'


