import Busqueda
import Pila
import kotlin.system.exitProcess

class DFS(val g: Grafo) : Busqueda() {
    override fun buscar(D: Int, H: Int) : Int {
        val distancia: MutableList<Int> = mutableListOf()
        val predecesores: MutableList<Int?> = mutableListOf()
        val visitados: MutableList<Boolean> = mutableListOf()
        val pila: Pila<Int> = Pila()
        var fuente: Int

        if (D < 0 || D >= g.obtenerNumeroDeVertices()) {
            print("El vertice origen no pertenece al grafo")
            exitProcess(1)
        }

        if (H < 0 || H >= g.obtenerNumeroDeVertices()) {
            print("El vertice destino no pertenece al grafo")
            exitProcess(1)
        }

        // inicializamos las listas
        for (i in 0 until g.obtenerNumeroDeVertices()) {
            distancia.add(Int.MAX_VALUE)
            predecesores.add(null)
            visitados.add(false)
        }

        // inicializamos el vertice fuente
        distancia[D] = 0
        visitados[D] = true

        pila.agregar(D)
        
        while(!pila.vacio()) {
            fuente = pila.remover()
            visitados[fuente] = true

            for (sumidero in g.obtenerAdyancetes(fuente)) {
                if (! visitados[sumidero]) {
                    distancia[sumidero] = distancia[fuente] + 1
                    predecesores[sumidero] = fuente
                    pila.agregar(sumidero)
                }
            }
        }

        if (predecesores[H] != null || H == D) {
            return distancia[H]
        }
        return -1
    }
}