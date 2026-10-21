# Plan: 001-Habits MVP

## 1. Estructura de Módulos
Siguiendo las reglas de "Pureza Lógica" y "Stack Mínimo" de la Constitución, el proyecto se organizará así:

- `habits/`
    - `__init__.py`
    - `core.py`: Lógica pura para el cálculo de rachas. Sin dependencias de IO ni de la CLI. (Cubre **RF-3**, Regla 3 de la Constitución).
    - `storage.py`: Capa de persistencia JSON. Gestiona la lectura y escritura del archivo plano. (Cubre **RF-1, RF-2**, Regla 5 de la Constitución).
    - `cli.py`: Punto de entrada. Gestiona el parseo de argumentos, la interacción con el usuario en español y la orquestación. (Cubre **RF-1, RF-2, RF-3**, Regla 6 de la Constitución).
- `tests/`
    - `test_core.py`: Tests unitarios para la lógica de rachas.
    - `test_storage.py`: Tests de integridad del JSON.
    - `test_cli.py`: Tests de integración para los comandos.

## 2. Modelo de Datos (JSON)
Un diccionario simple donde las claves son los nombres de los hábitos y los valores son listas de fechas (formato ISO 8601 `YYYY-MM-DD`).

**Ejemplo de `data.json`:**
```json
{
  "Lectura": ["2026-10-19", "2026-10-21"],
  "Python": ["2026-10-20", "2026-10-21"]
}
```
- **Justificación**: El JSON plano es obligatorio por la Constitución. El uso de una lista de fechas facilita el cálculo de huecos y rachas. (Cubre **RF-1, RF-2**).

## 3. Algoritmo de Cálculo de Racha (Pseudocódigo)
La regla de tolerancia "día por medio" (la racha solo se rompe tras dos fallos consecutivos) es el núcleo de la lógica.

```python
FUNCION calcular_racha(fechas_completadas):
    SI fechas_completadas está vacía:
        RETORNAR 0

    fechas_ordenadas = ordenar(fechas_completadas)
    hoy = obtener_fecha_actual()
    contador_racha = 0
    
    # Empezar desde la fecha más reciente hacia atrás
    fecha_chequeo = hoy
    
    MIENTRAS Verdadero:
        SI fecha_chequeo está en fechas_ordenadas:
            contador_racha += 1
            fecha_chequeo = fecha_chequeo - 1 día
        SINO:
            # Encontramos un fallo.
            # Si el día anterior (relativo a fecha_chequeo) 
            # también falta, la racha se rompe.
            SI (fecha_chequeo - 1 día) NO está en fechas_ordenadas:
                ROMPER # Dos fallos consecutivos
            SINO:
                # Solo un fallo: se aplica la tolerancia.
                fecha_chequeo = fecha_chequeo - 1 día
                
    RETORNAR contador_racha
```
(Cubre **RF-3**).

## 4. Contrato de la CLI
Todos los mensajes en español. Códigos de salida: `0` para éxito, `1` para error o advertencia.

| Comando | Argumentos | Salida de Éxito | Salida de Error/Advertencia | Código Salida |
| :--- | :--- | :--- | :--- | :--- |
| `create` | `<<nombrenombre>` | "Hábito '<<nombrenombre>' creado con éxito." | "El hábito '<<nombrenombre>' ya existe. Por favor elige otro." | 0 / 1 |
| `done` | `<<nombrenombre>` | "¡Hábito '<<nombrenombre>' completado hoy!" | "El hábito '<<nombrenombre>' ya fue completado hoy." / "Hábito no encontrado." | 0 / 1 |
| `list` | N/A | Tabla: `Nombre \| Racha` | "No hay hábitos creados." | 0 / 1 |

(Cubre **RF-1, RF-2, RF-3**).

## 5. Decisiones Técnicas

| Decisión | Justificación | Alternativa | Razón del Descarte |
| :--- | :--- | :--- | :--- |
| **Librería `json` estándar** | Obligatorio por la Constitución. | `SQLite` | Viola la "Persistencia Simple" (Regla 5 de la Constitución). |
| **`argparse`** | Librería estándar, robusta para CLIs simples. | `Click` / `Typer` | Añade dependencias externas (Regla 1 de la Constitución). |
| **Cadenas de fecha ISO** | Ordenamiento lexicográfico y compatibilidad estándar. | Timestamps Unix | Más difícil de depurar visualmente en archivos JSON. |

## 6. Estrategia de Tests
Siguiendo la regla "Test-Driven" (Regla 4 de la Constitución):

1.  **Tests Unitarios (`core.py`)**: Probar `calcular_racha` con múltiples escenarios:
    - Lista vacía $\rightarrow$ 0.
    - Racha perfecta $\rightarrow$ conteo correcto.
    - Hueco de 1 día $\rightarrow$ el conteo continúa.
    - Hueco de 2 días $\rightarrow$ la racha se resetea a 0.
2.  **Tests de Persistencia (`storage.py`)**:
    - Crear archivo si no existe.
    - Manejar JSON corrupto (debe lanzar error según los Casos Límite).
3.  **Tests de Integración (`cli.py`)**:
    - Mocking de `sys.argv` y `sys.stdout` para verificar los mensajes en español y los códigos de salida.
