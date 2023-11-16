class Arbol_binario
    attr_accessor :val, :arbol_izq, :arbol_der
    def initialize(val, arbol_izq = nil, arbol_der = nil)
        if not  val.is_a?(Comparable)
            raise Exception.new("El valor de la rama debe ser de un tipo comparable")
        end

        if (not arbol_izq == nil) and self.class != arbol_izq.class
            raise Exception.new("El arbol izquierdo debe ser instancia de la clase Arbol_binario")
        end

        if (not arbol_der == nil) and self.class != arbol_der.class
            raise Exception.new("El arbol derecho debe ser instancia de la clase Arbol_binario")
        end

        if (not arbol_izq == nil) and self.class == arbol_izq.class
            if val.class != arbol_izq.val.class
                raise Exception.new("Los elementos de las ramas de los arboles deben de ser del mismo tipos")
            end
        end

        if (not arbol_der == nil) and self.class == arbol_der.class
            if val.class != arbol_der.val.class
                raise Exception.new("Los elementos de las ramas de los arboles deben de ser del mismo tipos")
            end
        end
        @val = val
        @arbol_izq = arbol_izq
        @arbol_der = arbol_der
    end

    def esMaxHeapSimétrico
        if es_max_heap and (preorder == postorder)
           return "Es un max-heap simetrico"
        end
        "No es un max-heap simetrico"
    end

    protected
    def rama_izq
        if @arbol_izq == nil
            return nil
        end
        @arbol_izq.val
    end

    def rama_der
        if @arbol_der == nil
            return nil
        end
        @arbol_der.val
    end

    def es_max_heap
        es_max = true
        val_arbol_izq = rama_izq
        val_arbol_der = rama_der
        
        if not val_arbol_izq == nil
            es_max = val_arbol_izq <= @val
        end

        if not val_arbol_der == nil
            es_max = es_max and val_arbol_der <= @val
        end 
        
        if not rama_izq == nil
            es_max = es_max and @arbol_izq.es_max_heap
        end

        if not rama_der == nil
            es_max = es_max and @arbol_der.es_max_heap
        end
        es_max
    end

    def preorder
        secuencia = [@val]
        if not @arbol_izq == nil
            secuencia = secuencia + @arbol_izq.preorder
        end

        if not @arbol_der == nil
            secuencia = secuencia + @arbol_der.preorder
        end
        secuencia
    end

    def postorder
        secuencia = []
        if not @arbol_izq == nil
            secuencia = secuencia + @arbol_izq.postorder
        end

        if not @arbol_der == nil
            secuencia = secuencia + @arbol_der.postorder
        end

        secuencia = secuencia + [@val]
        secuencia
    end 
end