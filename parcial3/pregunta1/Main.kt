fun main() {
    val g: Grafo = Grafo(8)


    g.agregarArco(1, 2)
    g.agregarArco(1, 3)
    g.agregarArco(1, 6)
    g.agregarArco(2, 5)
    g.agregarArco(6, 5)
    g.agregarArco(3, 7)
    g.agregarArco(5, 7)
    
    val bfs: BFS = BFS(g)
    val dfs: DFS = DFS(g)

    println(bfs.buscar(1, 5))
    println(bfs.buscar(1, 7))

    println(dfs.buscar(1, 5))
    println(dfs.buscar(1, 7))
}