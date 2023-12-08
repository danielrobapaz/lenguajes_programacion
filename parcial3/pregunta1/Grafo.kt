import kotlin.system.exitProcess

class Grafo {
    val nVertices: Int
    val listasAdyacentes: MutableList<MutableList<Int>>

    constructor(numeroDeVertices: Int) {
        nVertices = numeroDeVertices
        listasAdyacentes = mutableListOf() 
        for (i in 0 until nVertices) {
            listasAdyacentes.add(mutableListOf())
        }
    }

    fun agregarArco(fuente: Int, sumidero: Int) {
        if (fuente < 0 || fuente >= nVertices) {
            print("El vertice fuente no pertenece al grafo")
            exitProcess(1)
        }
        
        if (sumidero < 0 || sumidero >= nVertices) {
            print("El vertice sumidero no pertenece al grafo")
            exitProcess(1)
        }

        if (listasAdyacentes[fuente].contains(sumidero)){
            print("Ya existe el arco en el grafo")
            exitProcess(1)
        }

        listasAdyacentes[fuente].add(sumidero)
    }

    fun obtenerAdyancetes(vertice: Int): Iterable<Int> {
        if (vertice < 0 || vertice >= nVertices) {
            print("El vertice no pertenece al grafo")
            exitProcess(1)
        }

        return listasAdyacentes[vertice].asIterable()
    }

    fun obtenerNumeroDeVertices(): Int = nVertices
}