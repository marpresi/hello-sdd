# Especificación: 001-Habits MVP

## Contexto y Objetivo
El proyecto consiste en una interfaz de línea de comandos (CLI) diseñada para ayudar a los usuarios a monitorizar sus hábitos de estudio. El objetivo es proporcionar una herramienta minimalista que fomente la consistencia mediante la visualización de rachas de cumplimiento, permitiendo un seguimiento sencillo sin fricciones.

## Usuarios
- **Estudiantes**: Personas que desean trackear la regularidad de sus sesiones de estudio.
- **Desarrolladores Junior**: El proyecto sirve como base educativa para mantenimiento y evolución.

## Historias de Usuario
- **Como usuario**, quiero crear un hábito nuevo para empezar a trackear una actividad específica.
- **Como usuario**, quiero marcar un hábito como completado hoy para mantener mi progreso.
- **Como usuario**, quiero ver la lista de mis hábitos y sus rachas actuales para motivarme y saber qué estoy descuidando.

## Requisitos Funcionales

### RF-1: Creación de Hábitos
- **Criterio de Aceptación (EARS)**: Cuando el usuario solicita crear un hábito con un nombre de hasta 50 caracteres que no existe, el sistema debe registrar el hábito y confirmar la creación.
- **Criterio de Aceptación (EARS)**: Si el usuario intenta crear un hábito con un nombre que ya existe, el sistema debe mostrar una advertencia indicando que el nombre ya está en uso y sugerir el uso de uno diferente.

### RF-2: Registro de Cumplimiento Diario
- **Criterio de Aceptación (EARS)**: Cuando el usuario marca un hábito como hecho, el sistema debe registrar la fecha actual del sistema (local) como día de cumplimiento.
- **Criterio de Aceptación (EARS)**: Si el usuario intenta marcar un hábito que ya ha sido registrado como hecho en la fecha actual del sistema, el sistema debe informar que el hábito ya fue completado hoy y no permitir modificaciones.

### RF-3: Cálculo y Visualización de Rachas
- **Criterio de Aceptación (EARS)**: Cuando el usuario solicita listar los hábitos, el sistema debe mostrar una tabla minimalista con el nombre de cada hábito y su racha actual.
- **Criterio de Aceptación (EARS)**: El sistema debe calcular la racha actual como la **suma total de días cumplidos**, siempre que no hayan existido dos fallos consecutivos (tolerancia de día por medio).
- **Criterio de Aceptación (EARS)**: Cuando un hábito tiene la racha rota según la regla de tolerancia, el sistema debe mostrar la racha actual como 0.
- **Criterio de Aceptación (EARS)**: La regla de rotura de la racha se activa únicamente a partir del primer registro exitoso del hábito.

## Requisitos No Funcionales
- **Simplicidad**: La interfaz debe ser directa, evitando flujos complejos.
- **Persistencia**: Los datos deben sobrevivir al cierre de la aplicación.
- **Idioma**: La interacción con el usuario debe ser íntegramente en español.

## Casos Límite
- **Cero datos**: Al listar hábitos por primera vez, el sistema debe informar que no hay hábitos creados.
- **Racha inicial**: Un hábito recién creado comienza con racha 0 y permanece en estado latente hasta su primer registro.
- **Cambio de día**: La racha debe actualizarse automáticamente basándose en la fecha local del sistema al momento de la consulta.
- **Persistencia ausente**: Si el archivo de datos no existe, el sistema debe crearlo automáticamente al registrar el primer hábito.
- **Persistencia corrupta**: Si el archivo de datos está mal formado o vacío, el sistema debe informar del error y detener la ejecución para evitar pérdida de datos.

## Fuera de Alcance
- Registro de hábitos en fechas pasadas (retroactividad).
- Edición o eliminación de hábitos existentes.
- Metas numéricas o temporales por hábito.
- Categorización de hábitos.
- Gestión compleja de zonas horarias (se usa la fecha local del sistema).

## Criterios de Finalización
- Implementación de los tres comandos principales (crear, marcar, listar).
- Verificación de la lógica de tolerancia de racha (día por medio) y cálculo basado en días cumplidos.
- Validación de la inmutabilidad del registro diario.
- Implementación de la tabla minimalista de salida.
- Pruebas unitarias que cubran los casos de éxito y error definidos.

## Dudas Abiertas
- [SIN ACLARACIÓN]: No existen dudas abiertas en este momento.
