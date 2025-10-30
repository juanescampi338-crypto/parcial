def invertir_array(arr):
    # Retorna el array invertido
    return arr[::-1]

# Solicita la cantidad de elementos del array
cantidad = int(input("Ingrese la cantidad de elementos del array: "))

# Solicita por pantalla el valor de cada uno de los elementos
array = []
for i in range(cantidad):
    valor = input(f"Ingrese el valor del elemento {i+1}: ")
    array.append(valor)

# Muestra en pantalla el array original
print("Array original:", array)

# Llama la función para invertir y muestra el array invertido
array_invertido = invertir_array(array)
print("Array invertido:", array_invertido)

