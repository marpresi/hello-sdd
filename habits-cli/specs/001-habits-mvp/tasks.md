# Tareas: 001-Habits MVP

## Fase 1: Infraestructura y Persistencia (Base)
- [x] **T1: Configuración de la estructura del proyecto**
    - RF: N/A
    - Hecho cuando: Existen los directorios `habits/` y `tests/` con sus respectivos `__init__.py` y archivos vacíos para `core.py`, `storage.py` y `cli.py`.
- [x] **T2: Persistencia JSON básica - Lectura/Escritura**
    - RF: RF-1, RF-2
    - Hecho cuando: `storage.py` puede guardar y cargar un diccionario en `data.json`, creando el archivo si no existe.
- [x] **T3: Persistencia - Manejo de errores por JSON corrupto**
    - RF: Caso Límite (Persistencia corrupta)
    - Hecho cuando: Un test en `test_storage.py` confirma que el sistema detiene la ejecución con un mensaje de error claro cuando `data.json` está mal formado.

## Fase 2: Lógica del Núcleo (Lógica Pura)
- [x] **T4: Núcleo - Cálculo de racha básico (sin huecos)**
    - RF: RF-3
    - Hecho cuando: `test_core.py` confirma que una secuencia perfecta de fechas devuelve el conteo correcto.
- [x] **T5: Núcleo - Cálculo de racha con tolerancia (hueco de 1 día)**
    - RF: RF-3
    - Hecho cuando: `test_core.py` confirma que un hueco de un solo día no resetea la racha.
- [x] **T6: Núcleo - Rotura de racha (hueco de 2 días)**
    - RF: RF-3
    - Hecho cuando: `test_core.py` confirma que dos días consecutivos sin registro resetean la racha a 0.
- [x] **T7: Núcleo - Manejo de datos vacíos y hábitos latentes**
    - RF: RF-3, Caso Límite (Cero datos / Racha inicial)
    - Hecho cuando: `test_core.py` confirma que un hábito sin fechas registradas devuelve racha 0.

## Fase 3: Implementación de la CLI (Orquestación)
- [x] **T8: CLI - Implementación del comando `create`**
    - RF: RF-1
    - Hecho cuando: Ejecutar `python -m habits create "NombreHábito"` guarda el hábito y muestra el mensaje de éxito en español.
- [x] **T9: CLI - Validación de `create` (Duplicados y Longitud)**
    - RF: RF-1
    - Hecho cuando: Intentar crear un hábito duplicado o con más de 50 caracteres muestra la advertencia especificada en español.
- [x] **T10: CLI - Implementación del comando `done`**
    - RF: RF-2
    - Hecho cuando: Ejecutar `python -m habits done "NombreHábito"` añade la fecha actual del sistema al JSON.
- [x] **T11: CLI - Validación de `done` (Ya completado hoy)**
    - RF: RF-2
    - Hecho cuando: Ejecutar `done` dos veces el mismo día muestra el mensaje de que el hábito ya fue completado hoy.
- [x] **T12: CLI - Implementación del comando `list`**
    - RF: RF-3
    - Hecho cuando: Ejecutar `python -m habits list` muestra una tabla con los nombres y las rachas calculadas de todos los hábitos.
- [x] **T13: CLI - Estado vacío de `list`**
    - RF: RF-3, Caso Límite (Cero datos)
    - Hecho cuando: Ejecutar `list` sin hábitos creados imprime "No hay hábitos creados."

## Fase 4: Verificación Final
- [x] **T14: Validación End-to-End de la regla "día por medio"**
    - RF: RF-3
    - Hecho cuando: Un flujo de prueba manual confirma que la regla de tolerancia funciona correctamente a través de la CLI.
- [x] **T15: Ejecución final de la suite de tests**
    - RF: Todos
    - Hecho cuando: `pytest -q` ejecuta todos los tests en `/tests` y todos pasan.
