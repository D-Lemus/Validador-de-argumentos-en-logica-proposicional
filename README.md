# Logica y Estructuras Discretas - Validador de Argumentos en Lógica Proposicional

> Interfaz gráfica que evalue la validez de un argumento mediante la generación de tablas de verdad

---

## About

Este es un proyecto relacionado a la materia de Lógica y Estructuras Discretas. Su objetivo es desarrollar una aplicación en Python que permita analizar argumentos de lógica proposicional usando tablas de verdad.

## Features
- Generador de Tablas de Verdad: genera la tabla completa del argumento
  e identifica los renglones críticos resaltados en verde
- Calculadora de Proposiciones: evalúa el valor de verdad de una
  proposición dados los valores de sus variables
- Interfaz Gráfica (GUI): navegación entre páginas, teclado de símbolos
  lógicos integrado (`¬ ∧ ∨ → ↔`) y tablas de referencia de conectivos

## Requerimientos

Para le ejecución de este proyecto es necesario:
- Python version: 3.x
- Librerias:
  - Flet - Framework para crear aplicaciones con interfaz gráfica
  - ttg -  Librería para generar tablas de verdad
  - pandas -  Librería estándar para análisis y manipulación de datos en Python

## Uso

El proyecto se divide en tres partes principales. truth_tables, generador de tablas de verdad. shunting_yard, lógica que evalua valor de verdad de una proposicion, la GUI, archivo que lanza la aplicación 

Para ejecutar la aplicacion escribe en la terminal:
```
pyhton GUI.py
```
### Validador de argumentos
1. Escribe una premisa en el campo "argumento" y presiona **+** para agregarla
2. Repite para cada premisa adicional
3. Escribe la conclusión en su campo
4. Usa el teclado de símbolos para insertar conectivos
5. Presiona **validar** — se mostrará la tabla y el veredicto

### Calculadora
1. Escribe la proposición (ej. `p∧q`)
2. Ingresa los valores separados por comas (ej. `true,false`)
3. Presiona **calcula**

### Tablas de referencia
Consulta las tablas de los 5 conectivos lógicos: `¬ ∧ ∨ → ↔`

## Estructura del proyecto
```
├── GUI.py              # Interfaz gráfica
├── truth_tables.py     # Generador de tablas de verdad
├── shunting_yard.py    # Algoritmo de validacion basado en RPN(Reverse Polish Notation)
└── premade_tables.py   # Tablas ya  preconstruidas de los conectivos lógicos
```

## Problemas Conocidos

- **Falta de validacion:** Error al ingresar simbolos que no sean letras o operadores lógicos.
- **Variables de un solo carácter:** cada variable debe ser una sola letra
  (p, q, r...)
- **Orden de valores en la calculadora:** los valores deben ingresarse en
  el mismo orden en que aparecen las variables en la proposición
  
## Créditos

Proyecto desarrollado para la materia de **Lógica y Estructuras Discretas**  

**ITESO** | 2026

*Instituto Tecnologico de Estudio Superiores de Occidente*

### Colaboradores
- NUÑEZ PACHECO, JULIETA ~ AI
- LEMUS SEPULVEDA, DIEGO ~ IS
- GOMEZ GONZALEZ, VALENTINA ~ IS

### Video explicativo
https://youtu.be/-GHkiWs1JSY?si=2TafHPTzfuhHpoqL

