import Secuencia
import kotlin.system.exitProcess

class Pila<T> : Secuencia<T>{
    var elementos : MutableList<T>
    
    constructor() {
        elementos = mutableListOf()
    }

    override fun agregar(elemento: T) {
        this.elementos.add(0, elemento)
    }

    override fun remover(): T {
        if (this.vacio()) {
            println("Error: No se puede remover un elemento de una pila vacio")
            exitProcess(1)
        }

        return elementos.removeFirst()
    }

    override fun vacio(): Boolean {
        return ! this.elementos.isNotEmpty()
    }
}