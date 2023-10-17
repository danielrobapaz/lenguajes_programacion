# Solucion parcial 1
Para evitar inconsistencia, los programas entregados se deben ejecutar en un sistema operativo _linux-like_

## Pregunta 1

### (a)
El lenguaje usado fue D. Es un lenguaje compilado, que tiene una curva de aprendizaje corta para programadores acostumbrados a C++ o Java, y que soporta varios paradigmas de programacion. D esta disenado para:

- Programadores que usan lint o herramientas de analisis de codigo para eliminar bugs antes de que sea compilado. 
- Proyectos que necesitan _testing_ incorporado
- Para programadores que piensen que el lenguaje debe tener suficientes caracteristicas para obviar el uso de apuntadores de manera directa.

D tiene un alcance estatico. Como D hereda caracteristicas de C++, este tiene asociacion temprana y tiene la opcion de usar asociacion tardia con el compilador. Como el lenguaje es facil de aprender a usuarios que estan acostumbrados a C++ y Java, estas caracteristicas no presentan mayor dificicultad al momento de aprender. Como esta disenado para ser usado en proyectos medianos y grandes, ofrece una ejecucion rapida.

D cuenta con modulos como librerias y como tipo. 

```d
// ejemplos para importar
import mymodule; // importar un modulo
import mypackage.mymodule; // importar un modulo de un paquete
import func = mypackage.mymodule; // renombrar inports
import mypackage.mymodule :: myfunc; // import selectivo

// ejemplos para exportar
export void foo() // la funcion foo se esta exportando.
```

D permite la creacion de aliases, sobrecarga de operadores y funciones.
```d
// ejemplos de creacion de aliases
alias int myAppNumber;
alias to!(type) toType; // permite hacer llamadas de tipo toType(a)

// algunos ejemplos de sobrecarga de funciones
class sumFunc {
    public:
        void sum(int i) {
            ...
        }

        void sum(double d) {
            ...
        }

        void sum(string s){
            ...
        }
}

void main() {
    printData pd = new printData();
    pd.sum(1);
    pd.sum(4.5);
    pd.sum("hola profe");
    pd.sum([1,2,3]); // error
}

// para la sobrecarga de operadores se usan las siguientes funciones dentro de la clase
opUnary // para operadores unarios
opCmp // para operadores de comparacion
opBinary // para demas operadores binarios

class myString {
    public:
        myString opBinary(string op) (string s){
            if (op == "+") {
                return this.content~s; // ~ es el operador de concatenacion
            }
        }

    private:
        string content;
}
```
D no cuenta con interpretador y ofrece varios [compiladores](https://dlang.org/download.html), uno de ellos es gcc el cual es usado para compilar C y C++. Algunas herramientas que provee D a los desarrolladores son

-  herramientas para realizar [pruebas unitarias](https://dlang.org/spec/unittest.html). 
- variedad de debuggers tanto para Windows, Linyx y MacOS.
- frameworks para desarrollo web como [Vibe.d](https://tour.dlang.org/tour/en/vibed/vibe-d-web-framework)

### (b)
#### (i)
-  solucion en /pregunta1/rotar.d
    ```c
    // compilar y ejecutar
    dmd rotar.d
    ./rotar [string] chars_rotate
    ```
#### (ii)
- solucion en /pregunta1/matrix.d
    ```c
    // compilar y ejecutar
    dmd matrix.d
    ./matrix
    ```
- El programa recibe N, el tamano de la matriz, y la matriz fila a fila separando los numeros por espaciones. en input.input se encuentra un ejemplo. Se recomienda ejecutar el programa de la siguiente manera
    ```
    ./matrix < input.input
    ```

## Pregutna 3
Se encuentra en la carpeta /pregunta 3. Se resolvio usando Python y la libreria PyTest. Se deben usar los siguientes comandos.
```c
sudo apt install python3-pytest
python3 main.py // para ejecutar el simulador
python3 unit_test.py // para ejecutar las pruebas unitarias
```

## Pregunta 4
Se resolvio usando el lenguaje de programacion C++. El modulo que contiene el tipo  se Vector en el archivo /pregunta4/vector.h. Se uso el framework GoogleTest para las pruebas unitarias. Para la construccion de las pruebas se requiere tener instalado cmake.
```cpp
// instalar cmake
 sudo apt-get install cmake
``` 

``` cpp
// construccion
cmake -S . -B build
cmake --build build

// ejecucion de las pruebas unitarias
cd build
ctest
```

## Pregunta 5
Se resolvio usando el lenguaje de programacion Python. Se encuentra en la carpeta /pregunta5
```c
python3 main.py // ejecucion del programa
python3 unit_test.py // para ejecutar pruebsa unitarias
```

## Pregunta 6
Se resolvio usando el lenguaje de programacion javascript. Se encuentra en la carpeta /pregutna6
```c
python3 golf.p num
```