import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

ALPHA = -2.355351133812429
TX = 1.1383712500034338
TY = 1.9671201610173714
SCALE_FACTOR = 0.0020694894396433563

CELL_SIZE = 16

# Cargar la imagen y verificar
MAP_IMG = cv2.imread("../resources/figures/mapgrannyannie.png")
if MAP_IMG is None:
    raise FileNotFoundError("No se pudo leer la imagen, verifica la ruta y el archivo.")

# Convertir la imagen a escala de grises
MAP_IMG = cv2.cvtColor(MAP_IMG, cv2.COLOR_BGR2GRAY)

# Visualizar la imagen en escala de grises antes de procesarla
plt.imshow(MAP_IMG, cmap='gray')
plt.title("Imagen en escala de grises")
plt.show()

# Verificar los valores únicos en la imagen
print("Valores únicos en la imagen:", np.unique(MAP_IMG))

def showNumpy(mat):
    # Definir un mapa de colores personalizado
    cmap = mcolors.ListedColormap([
        'gray',      # 0-127 en escala de grises
        'red',       # 128
        'orange',    # 129
        'yellow',    # 130
        'green',     # 131
        'blue',      # 132
        'indigo',    # 133
        'violet'     # 134
    ])
    
    # Crear los límites para el mapa de colores
    bounds = [0, 128, 129, 130, 131, 132, 133, 134, 135]
    norm = mcolors.BoundaryNorm(bounds, cmap.N)
    
    # Limitar los valores de la matriz entre 0 y 134
    mat = np.clip(mat, 0, 134)
    
    # Mostrar la matriz usando matplotlib
    plt.figure(figsize=(10, 10))
    plt.imshow(mat, cmap=cmap, norm=norm)
    plt.colorbar(ticks=[0, 64, 127, 128, 129, 130, 131, 132, 133, 134], label="Escala de colores")
    plt.title("Visualización de matriz")
    plt.show()

def get_grid(map_array):
    rows = map_array.shape[0] // CELL_SIZE
    cols = map_array.shape[1] // CELL_SIZE
    grid = np.zeros((rows, cols), dtype=np.uint8)
    
    for i in range(rows):
        for j in range(cols):
            cell = map_array[i * CELL_SIZE:(i + 1) * CELL_SIZE, j * CELL_SIZE:(j + 1) * CELL_SIZE]
            # Ajustar el umbral para detectar celdas ocupadas
            if np.mean(cell) < 100:  # Puedes ajustar este valor umbral según el contraste de la imagen
                grid[i, j] = 0
            else:
                grid[i, j] = 127
    return grid

# Generar la rejilla a partir de la imagen
grid = get_grid(MAP_IMG)

# Visualizar la rejilla generada
showNumpy(grid)
