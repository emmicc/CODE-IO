import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

def clasificacion_abc(items):
    valor_total = items['valor'].sum()

    items['porcentaje'] = (items['valor'] / valor_total) * 100

    items_ordenados = items.sort_values(by='valor', ascending=False).reset_index(drop=True)

    acumulado = 0
    categorias = []
    acumulado_valor = []

    for _, item in items_ordenados.iterrows():
        acumulado += item['porcentaje']
        acumulado_valor.append(acumulado)

        if acumulado <= 80:
            categorias.append('A')
        elif acumulado <= 95:
            categorias.append('B')
        else:
            categorias.append('C')

    items_ordenados['porcentaje'] = items_ordenados['porcentaje'].round(2)
    items_ordenados['acumulado'] = acumulado_valor

    items_ordenados['categoria'] = categorias

    return items_ordenados

def ingresar_datos():
    num_items = int(input("¿Cuántos artículos deseas ingresar? "))
    articulos = []

    for i in range(num_items):
        nombre = input(f"Ingrese el nombre del artículo {i + 1}: ")
        valor = float(input(f"Ingrese el valor de {nombre}: "))
        articulos.append({'nombre': nombre, 'valor': valor})

    items = pd.DataFrame(articulos)
    return items

def procesar_datos():
    items = ingresar_datos()
    resultado = clasificacion_abc(items)
    return resultado


resultado = procesar_datos()


print("\nClasificación ABC de los artículos:")
print(tabulate(resultado[['nombre', 'valor', 'porcentaje', 'acumulado', 'categoria']], headers='keys', tablefmt='fancy_grid', showindex=False))


plt.figure(figsize=(10, 6))
plt.bar(resultado['nombre'], resultado['valor'], color=['red' if categoria == 'A' else 'yellow' if categoria == 'B' else 'green' for categoria in resultado['categoria']])


plt.xlabel('Artículos')
plt.ylabel('Valor')
plt.title('Clasificación ABC de Artículos')


handles = [
    plt.Rectangle((0, 0), 1, 1, color='red'),
    plt.Rectangle((0, 0), 1, 1, color='yellow'),
    plt.Rectangle((0, 0), 1, 1, color='green')
]
labels = ['Categoría A', 'Categoría B', 'Categoría C']
plt.legend(handles, labels)

plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
