# Evidencias – Calculadora en Python

Este repositorio contiene la evidencia completa solicitada en la práctica de Git y GitHub.  
Incluye el código fuente en Python, las pruebas básicas y el flujo de trabajo utilizado con Git.

---

## Archivos Incluidos

### calculator.py
Programa principal que implementa las operaciones matemáticas:
- Suma  
- Resta  
- Multiplicación  
- División (con manejo de error por división entre cero)

### test_calculator.py
Archivo de pruebas automáticas que valida el funcionamiento correcto de cada operación.

### cubo.py (si aplica)
Función adicional creada en la rama `Elevar_al_cubo` para elevar un número al cubo.

---

## Cómo ejecutar el programa

Dentro de la carpeta del proyecto:

```bash
python calculator.py
```

---

## Cómo ejecutar las pruebas

Asegúrate de estar en la carpeta del proyecto:

```bash
cd mi_calculadora
```

Ejecuta las pruebas con:

```bash
python -m unittest test_calculator.py
```

---

## Flujo de trabajo realizado (paso a paso)

1. Crear repositorio local
   ```bash
   git init
   ```

2. Crear archivos del proyecto
   - calculator.py  
   - test_calculator.py  
   - README_evidencia.md  

3. Agregar archivos al área de preparación
   ```bash
   git add .
   ```

4. Crear el primer commit
   ```bash
   git commit -m "Primer commit: calculadora"
   ```

5. Crear una rama de trabajo
   ```bash
   git checkout -b Elevar_al_cubo
   ```

6. Agregar nuevo contenido y hacer commit
   ```bash
   git add README_evidencia.md
   git add test_calculator.py
   git commit -m "Agregar README y pruebas"
   ```

7. Subir la rama al repositorio remoto
   ```bash
   git push origin Elevar_al_cubo
   ```

---

## Estructura Repositorio

```
mi_calculadora/
│
├── README_evidencia.md
├── calculator.py
├── cubo.py
├── test_calculator.py
```

---

## Aprendiz

Sandra Lozano  
Fecha: 17/11/2025
