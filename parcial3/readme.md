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

class UnConstructur(var a: Int, val b: Boolean) {...}

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
El lenguaje cuenta con asociacion estatica de metodos por omision.

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

## Pregunta 3

## Pregunta 4
La imlementacion del manejador de tablas de metodos virtuales se encuentra ```pregunta4/Tabla_de_metodos.py```.

```c
python main.py // para ejecutar cliente
python unit_test.py // para ejecutar las pruebas unitarias
```

## Pregunta 5