def es_camaleon(num):
# Calcular suma de dígitos
suma = sum(int(d) for d in str(num))
# Invertir número
invertido = int(str(num)[::-1])
# Condiciones
return (suma % 2 == 0) and (invertido % 3 == 0), suma, invertido

# Números fijos como en el ejemplo
numeros = [324, 518, 742, 901]

print("Cantidad de números a validar:", len(numeros))
print("Números generados:", ", ".join(map(str, numeros)))
print("Resultados:")

for num in numeros:
camaleon, suma, invertido = es_camaleon(num)
print(f"{num} -> {'Sí' if camaleon else 'No'} "
f"(suma={suma}, invertido={invertido}, "
f"condiciones: {'OK' if suma % 2 == 0 else 'NO'} y {'OK' if invertido % 3 == 0 else 'NO'})")