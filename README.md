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

Al ejecutar la apicacion haz click en 

### truth_tables.py

### shunting_yard.py

### GUI.py

## Problemas Conocidos

- Falta de validacion:
  - Error al ingresar simbolos que no sean letras o operadores lógicos. 


