# Solucion parcial 1
Para evitar inconsistencia, los programas entregados se deben ejecutar en un sistema operativo _linux-like_

## Pregunta 1
Lenguaje escogido Kotlin.

### (a) Breve descripcion del lenguaje.
#### (i) Maneras de crear y manipular objetos.

Para crear objetos se usa la palabra reservada ```class``. Se pueden definir clases con construcotores, campos, metodos, visibilidad e incluso tipos genericos. 

Se tienen los siguientes modos de visibilidad de campos dentro de una clase.

- ```public```: Accesible desde cualquier lugar
- ```private```: Accesibles solamente desde el alcance actual.
- ```protected```: Accesible solo para la clase actual y subclases.
- ```internal```: Accesible solo para el modula actual.

Una vez creada la clase, se usa el operador ```.``` para acceder a sus campos.

```kt
// varias maneras de definir una clase
class DosConstructores {
    constructor(a: Int) {...}
    constructor(b: Boolean) {...}
}

class UnConstructuro(var a: Int, val b: Boolean) {...}

class TengoCamposConDistintaVisibilidad<T> {
    private val a: T
    val b: Boolean

    constructor(c: Array<T>) {...}

    fun soyPublica(){..}

    private soyPrivada() : T {...}

    open fun mePuedenSobreescribirMisSubclases()

    override fun estaFuncionEsDeMiSuperclase()
}
```
#### (ii) Describa el funciona del manejo de memoria.
Como ```Kotlin``` se ejecuta sobre la ```JVM```, este con un el recolector de basuar de la maquina virtual. Sin embargo, se puede cambiar la configuracion de la misma a necesidad del programador.

#### (iii) Diga si el lenguaje usa asociacion estatica o dinamica de metodos.
El lenguaje cuenta con asociacion estatica de metodos por omision. Se puede usar la palabra reservada ```final``` para indicar que un metodo se asocia estaticamente.

#### (iv) Describa la jerarquia de tipos.
La raiz de la jerarquia de tipos en ```Kotlin``` es el tipo ```Any```. Este solo cuanta con los metodos ```equals()```, ```hashCode()``` y ```toString()```. De manera de que una clase que no cuente con una subclase explicita, es subclase de ```Any```.

```Kotlin``` no ofrece soporte nativo para la herencia multiple. Sin embargo, se puede simular aumentando el nivel de abstraccion. En caso de que ocurra un conflicto, es trabajo del programador solucionarlos.

```kt
interface Clase1 {
    fun metodo1()
}

class Clase1Impl: Clase1 {
    override fun metodo1(){...}
}

interface Clase2 {
    fun metodo2()
}

class Clase2Impl: Clase2 {
    override fun metodo2(){...}
}

class Clase1Clase2 (
    clase1: Clase1 = Clase1Impl(),
    clase2: Clase2 = Clase2Impl()
) : Clase1 by clase1, Clase2 by clase2
```

Por ultimo y al igual que ```Java```, ```Kotlin``` cuanta con polimorfismo parametrico y se puede especificar de la siguiente forma

```kt
class SoyUnTipoParametrico<T> {...}
```


### (b) Implementacion
#### (i)
La implementacion se encuentra en los archivos ```Secuencia.kt```, ```Cola.kt``` y ```Pila.kt```. Para compilar ```Cola.kt``` y ```Pila.kt``` se debe de incluir ```Secuencia.kt```

### (ii)
La implementacion se encuentra en ```Grafo.kt```, ```Busqueda.kt```, ```DFS.kt``` y ```BFS.kt```. 

Para compilar ```BFS.kt``` se debe incluir ```Secuencia.kt```, ```Cola.kt```, ```Grafo.kt```, ```Busqueda.kt```.

Para compliar ```DFS.kt``` se debe incluir ```Secuencia.kt```, ```Pila.kt```, ```Grafo.kt```, ```Busqueda.kt```.


## Pregunta 2
Lenguaje escogido ```Python```.

### (a) De una breve descripcion de los mecanismos de concurrencia disponibles.
#### (i) Diga si el lenguaje tiene capacidades nativas.
```Python``` provee soporte para mecanismos de concurrencia a traves de las siguientes librerias.

- ```threading``` para concurrencia con hilos
- ```multiproccessing``` para concurrencia con procesos
- ```asyncio``` para concurrencia con corrutinas

#### (ii) Explique la creacion/manejo de tareas concurrentes.
Para crear hilos se usa


```py
import threading
def funcion_hilo(args):
    ...

hilo = threading.Thread(target=funcion_hilo, args=(...))
x.start()
x.join()
```

Para crear procesos
```py
from multiproccessing import Process

def subproceso(args):
    ...

if __name__ == "__main__":
    p = Proccess(target=subproceso, args=(...))
    p.start()
    p.join()
```

Para crear corrutinas
```py
import asyncio
async def corrutina(args):
    ...

async def main():
    await asyncio.gather(corrutina(args))

if __name == "__main__":
    asyncio.create_tast(main())
```

El modulo ```multiproccessing``` provee la clase ```shared_memory``` que permite el manejo de memoria compartida entre procesos. Ademas, tambien provee la clase ```Queue``` para el envio de mensaje entre procesos

#### (iii) Describa el mecanismo de sincronizacion que utiliza el lenguaje
Para la sincronizacion de hilos se cuenta con ```threading.Lock``` la cual implementa un mutex. Analigamente, ```multiproccesing``` cuenta con la clase ```Lock``` la cual cumple con la misma funcion.

### (b) Implementacion.
#### (i)
La implemencion de los vectores se encuentra en ```pregunta2/Vectores.py```. La clase recibe una lista con tantos elemntos como dimensiones tenga el vector. El producto punto divide los las coordenadas de ambos vectores en 4 segmentos y ejecuta el producto punto de de cada segmento usando hilos mediante la libreria ```threading```, luego, se suma el resultado de estos.

Algunos resultados entre usar este producto punto y el metodo ```np.dot``` de ```numpy``` fuerton
```c
n = 10000
con hilos: 0.008538007736206055 segundos
sin hilos: 0.00099945068359375 segundos

----

n = 100000
con hilos: 0.0008256435394287109 segundos
sin hilos: 0.009662628173828125 segundos

----

n = 1000000
con hilos: 0.0010395050048828125 segundos
sin hilos: 0.05003237724304199 segundos

----

n = 10000000
con hilos: 0.007480621337890625 segundos
sin hilos: 0.5231473445892334 segundos

----

n = 100000000
con hilos: 0.07339048385620117 segundos
sin hilos: 4.967834234237671 segundos
```

El archivo con el cual se ejecutaron estas pruebas se encuentre en ```pregunta2/Test_vectores.py```

#### (ii)

Se implemento mediante la clase que se encuentra en ```pregunta2/Contador_Arcivos.py``` la cual recibe la direccion del direcctorio. Luego, al momento de instanciar la clase realiza el conteo de los archivos. Para obtener el numero de archivos se tiene el metodo ```obtener_numero_archivos()```
## Pregunta 3
Valores de las constantes: $X=0$, $Y=8$ y $Z=6$. El paso a paso y la salida se encuentra en ```pregunta3/pregunta3.pdf```

## Pregunta 4
La imlementacion del manejador de tablas de metodos virtuales se encuentra ```pregunta4/Tabla_de_metodos.py```.

```c
python main.py // para ejecutar cliente
python unit_test.py // para ejecutar las pruebas unitarias
```

## Pregunta 5
El paso a paso y la firma correspondiente se encuentra en ```pregunta5/pregunta5.pdf```