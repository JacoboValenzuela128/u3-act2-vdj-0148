import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Arath valenzuela NC:0148 (9/11/26)
# Graficando Videojuegos con Matplotlib

# 1. Definición de las listas con los datos del problema de Videojuegos
# Formato: [Nombre, Copias vendidas (millones), Es multijugador, Año lanzamiento]
mc  = ['Minecraft', 300, True, 2011]
gta = ['GTA V', 190, True, 2013]
tet = ['Tetris', 100, False, 1984]
wii = ['Wii Sports', 82.9, True, 2006]
pub = ['PUBG', 75, True, 2017]

# Creamos la lista de listas
lista_juegos = [mc, gta, tet, wii, pub]

# Creamos el DataFrame especificando las columnas
df_juegos = pd.DataFrame(
    lista_juegos, 
    columns=["Nombre", "Copias_Vendidas", "Es_Multijugador", "Ano_Lanzamiento"]
)
print("--- DATOS DE VIDEOJUEGOS ---")
print(df_juegos)

# Guardamos los datos en un archivo CSV
df_juegos.to_csv("videojuegos.csv", index=False)

# ---------------------------------------------------------
# Gráfica 1: Gráfica de Líneas
# ---------------------------------------------------------
plt.plot(df_juegos["Nombre"], df_juegos["Copias_Vendidas"])
plt.title("Ventas de Videojuegos - Gráfica de Líneas (NC:0148)")
plt.xlabel("Nombre del videojuego")
plt.ylabel("Copias vendidas (millones)")
plt.show()

# ---------------------------------------------------------
# Gráfica 2: Gráfica de Puntos (Scatter)
# ---------------------------------------------------------
plt.scatter(df_juegos["Nombre"], df_juegos["Copias_Vendidas"])
plt.title("Ventas de Videojuegos - Dispersión (NC:0148)")
plt.xlabel("Nombre del videojuego")
plt.ylabel("Copias vendidas (millones)")
plt.show()

# ---------------------------------------------------------
# Gráfica 3: Gráfica de Barras Estándar
# ---------------------------------------------------------
plt.bar(df_juegos["Nombre"], df_juegos["Copias_Vendidas"])
plt.title("Ventas de Videojuegos (NC:0148)")
plt.xlabel("Videojuegos")
plt.ylabel("Copias vendidas (millones)")
plt.show()

# ---------------------------------------------------------
# Gráfica 4: Barras Ordenadas Descendente
# ---------------------------------------------------------
df_juegos_ordenado = df_juegos.sort_values("Copias_Vendidas", ascending=False)
plt.bar(df_juegos_ordenado["Nombre"], df_juegos_ordenado["Copias_Vendidas"])
plt.title("Ventas Ordenadas (Mayor a Menor) (NC:0148)")
plt.xlabel("Videojuegos")
plt.ylabel("Copias vendidas (millones)")
plt.show()

# ---------------------------------------------------------
# Gráfica 5: Barras Ordenadas con Colores
# ---------------------------------------------------------
df_juegos_ordenado = df_juegos.sort_values("Copias_Vendidas", ascending=False)
plt.bar(
    df_juegos_ordenado["Nombre"], 
    df_juegos_ordenado["Copias_Vendidas"],
    color=["b", "g", "c", "m", "y"]
)
plt.title("Ventas Ordenadas por Color (NC:0148)")
plt.xlabel("Videojuegos")
plt.ylabel("Copias vendidas (millones)")
plt.show()

# ---------------------------------------------------------
# Gráfica 6: Gráfica de Pastel (Pie Chart)
# ---------------------------------------------------------
plt.pie(df_juegos["Copias_Vendidas"], labels=df_juegos["Nombre"], autopct='%1.1f%%')
plt.title("Distribución de Ventas por Videojuego (NC:0148)")
plt.show()