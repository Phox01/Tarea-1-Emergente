# Perceptrón Interactivo en Python

Este proyecto implementa un programa en Python que permite interactuar con un perceptrón. El programa carga los pesos desde un archivo de configuración y proporciona la respuesta del perceptrón para diferentes vectores de entrada.

## Requerimientos Funcionales

El programa debe cumplir con los siguientes requerimientos funcionales:

1.  **Lectura de Archivo de Configuración:**
    * Al inicio, el programa leerá un archivo de configuración.
    * Este archivo contendrá `n+1` valores separados por comas.
    * El primer valor representa el **sesgo** (bias) de la función de suma.
    * Los siguientes `n` valores representan los **pesos** correspondientes a las `n` componentes del vector de entrada ($x_1$ a $x_n$) en la suma.

2.  **Dos Modalidades de Funcionamiento:**
    * **Entrada desde Teclado:**
        * El programa solicitará al usuario que ingrese las `n` componentes del vector de entrada.
        * Una vez ingresadas, el programa calculará y mostrará la respuesta del perceptrón.
    * **Entrada desde Archivo:**
        * El programa leerá un archivo especificado por el usuario.
        * Este archivo contendrá `m` líneas.
        * Cada línea contendrá `n` valores separados por comas, representando un vector de entrada diferente.
        * Para cada vector de entrada leído del archivo, el programa calculará y mostrará la respuesta del perceptrón.

3.  **Selección de Función de Activación:**
    * El programa debe permitir al usuario elegir entre dos funciones de activación diferentes.

## Requerimientos Técnicos

Para la implementación de este programa, se deben considerar los siguientes requerimientos técnicos:

* El programa debe ser escrito completamente desde cero en Python.
* Se deben implementar las siguientes funciones:
    * **Función de Suma:** Realiza la suma ponderada de las entradas y el sesgo.
        <span class="math-block">\\text\{suma\} \= \\text\{bias\} \+ \\sum\_\{i\=1\}^\{n\} w\_i x\_i</span>
    * **Función de Activación:** Implementa las dos funciones de activación seleccionables por el usuario. Ejemplos comunes incluyen la función escalón (step function) o la función sigmoide.
    * **Procedimiento de Ejecución:** La lógica principal del programa que maneja la lectura de la configuración, la selección del modo de entrada, la obtención de los vectores de entrada, el cálculo de la salida del perceptrón utilizando la función de suma y la función de activación, y la presentación de los resultados.
* El programa debe ejecutarse a través de la consola.

## Rúbrica de Evaluación

La evaluación del proyecto se basará en los siguientes criterios:

* **Código (50%)**
    * El código incluye todas las partes solicitadas: **10 puntos**
    * Al código le faltan algunas partes solicitadas: **5 puntos**
    * No se entregó código relacionado con lo solicitado: **0 puntos**
* **Ejecución (50%)**
    * El código se ejecuta correctamente y siempre produce la respuesta esperada para todos los casos de prueba: **10 puntos**
    * El código no se ejecuta correctamente con todos los casos de prueba: **5 puntos**
    * El código no se
