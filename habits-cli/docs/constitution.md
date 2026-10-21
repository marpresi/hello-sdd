# Constitución del Proyecto: StudyHabits CLI

1. **Stack Mínimo**: Solo Python estándar y librerías externas justificadas en `requirements.txt`.
2. **Sincronía Total**: Cualquier cambio en la funcionalidad debe reflejarse primero en el `spec.md`.
3. **Pureza Lógica**: El núcleo de cálculo de rachas no puede importar módulos de CLI ni de IO.
4. **Test-Driven**: No se mergea ninguna funcionalidad sin su test unitario correspondiente en `/tests`.
5. **Persistencia Simple**: Los datos se almacenan exclusivamente en archivos JSON planos.
6. **Idioma**: Código y variables en inglés; comentarios y mensajes al usuario en español.
