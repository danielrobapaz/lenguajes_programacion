import Busqueda
import Cola
import kotlin.system.exitProcess


class BFS(val g: Grafo) : Busqueda() {
    override fun buscar(D: Int, H: Int) : Int {
        val distancia: MutableList<Int> = mutableListOf()
        val predecesores: MutableList<Int?> = mutableListOf()
        val visitados: MutableList<Boolean> = mutableListOf()
        val cola: Cola<Int> = Cola()
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

        cola.agregar(D)
        
        while(!cola.vacio()) {
            fuente = cola.remover()
            for (sumidero in g.obtenerAdyancetes(fuente)) {
                if (! visitados[sumidero]) {
                    visitados[sumidero] = true
                    distancia[sumidero] = distancia[fuente] + 1
                    predecesores[sumidero] = fuente
                    cola.agregar(sumidero)
                }
            }
        }

        if (predecesores[H] != null || H == D) {
            return distancia[H]
        }
        return -1
    }
}