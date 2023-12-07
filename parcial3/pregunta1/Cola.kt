import Secuencia
import kotlin.system.exitProcess

class Cola<T> : Secuencia<T> {
    var elementos: MutableList<T>

    constructor() {
        elementos = mutableListOf()
    }

    override fun agregar(elemento: T) {
        this.elementos.add(0, elemento)
    }

    override fun remover(): T {
        if (this.vacio()) {
            println("Error: No se puede remover un elemento de una cola vacio")
            exitProcess(1)
        }
        return elementos.removeLast()
    }

    override fun vacio(): Boolean {
        return ! this.elementos.isNotEmpty()
    }
}