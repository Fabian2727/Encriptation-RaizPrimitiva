# RaizPrimitiva
En el archivo .py nombrado RaizPrimitiva se encuentra el programa que calcula la raíz primitiva de un número primo. Dicho programa consta de 4 funciones
- mod: Que reemplaza al operador % y realiza el cálculo del módulo de a mod b
- expM: Realiza la operación de exponenciación modular de una manera más optimizada, para no consumir demasiados recursos al realizar operaciones grandes
- isPrime: Para verificar que el número del cual queremos calcular su raíz primitiva sea un número primo
- raizP: se pedirá por parámetro un número p quen será del cual calcularemos la raíz primitiva, añadido a este se crea (dentro de la función) las variables:
          g --> será la que almacenará y con la que calcularemos la raíz primitiva. Se inicializa en 2
          cont --> con esta variable manejaremos el bucle para calcular la raíz y nos ayudará a llenar una de las listas (list2) que se detallarán a continuación
          res --> esta variable almacenará el resultado de la exponenciació modular que se realizará para comparar las dos listas y determinar si g es raíz primitiva de p
          list1 --> esta lista almacena los resultados de la exponenciación modular de g** cont mod p
          list2 --> esta lista almacena los valores de 1,2,3,..p-1
          Mediante la función comparar veremos si las dos listas son iguales y de ser así g es la raíz primitiva de p, caso contrario se aumentará en uno (g+1) a la variable g y             se repetirán las operaciones hasta hallar la raíz
- comparar: esta funcion recibe por parámetro las dos listas de la función raizP, y las compara:
          Paso 1: Se verifica si son del mismo tamaño. Si lo son se pasa al Paso 2. Sino se retorna False
          Paso 2: Se usa la función .sort() para ordenar la list1 
          Paso 3: Se comparan las dos listas y se devuelve si son iguales o no (True o False)
