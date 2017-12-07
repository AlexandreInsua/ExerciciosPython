# 3) Durante la planificación de un proyecto se han acordado una lista de tareas. Para cada una de estas tareas se ha asignado un orden de prioridad 
# (cuanto menor es el número de orden, más prioridad).
# ¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden?
# Pista: Para ordenar automáticamente una lista es posible utilizar el método .sort().

from collections import deque

tareas = [ 
    [6, 'Distribución'],
    [2, 'Diseño'],
    [1, 'Concepción'],
    [7, 'Mantenimiento'],
    [4, 'Producción'],
    [3, 'Planificación'],
    [5, 'Pruebas']
]

print("==Tareas desordenadas==")
for tarea in tareas:
    print(tarea[0], tarea[1])

tareas.sort()

cola_tareas = deque()

for t in range(len(tareas)-1):
    cola_tareas.append(tareas[t][1])

print("== Cola de tareas ordenadas == ")
print(cola_tareas)

# Ángel utiliza un for máis simple
# for tarea in tareas:
#   cola_tareas.append(tareas[1])
