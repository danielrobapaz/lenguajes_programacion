class Church
    def +(other)
        if self.class == Cero and other.class == Cero 
            if self.cons == 0
                return other
            end
            if other.cons == 0
                return self
            end
            
            c1 = Cero.new(self.cons)
            
            for i in (1..other.cons)
                c1 = Suc.new(c1)
            end
            return c1
        end

        if (self.class == Cero and other.class == Suc) or (self.class == Suc and other.class == Cero)
            if self.class == Cero
                cero = self
                suc = other
            else 
                suc = self
                cero = other
            end
            
            if cero.cons == 0
                return suc
            end

            for i in (1..cero.cons)
                suc = Suc.new(suc)
            end
            return suc
        end

        if self.class == Suc and other.class == Suc            
            return Cero.new(self.res) + Cero.new(other.res)
        end
    end

    def *(other)
        if self.class == Cero and other.class == Cero 
            res = self.cons * other.cons
            c1 = Cero.new(0)
            
            for i in (1..res)
                c1 = Suc.new(c1)
            end
            return c1
        end

        if (self.class == Cero and other.class == Suc) or (self.class == Suc and other.class == Cero)
            if self.class == Cero
                cero = self
                suc = other
            else 
                suc = self
                cero = other
            end
            
            return Cero.new(suc.res)*Cero.new(cero.cons) 
        end

        if self.class == Suc and other.class == Suc            
            return Cero.new(self.res) * Cero.new(other.res)
        end
    end
end

class Cero < Church
    attr_accessor :cons
    def initialize(cons)
        if not cons.class == Integer 
            raise Exception.new("Los numeros de church estan definidos para numeros enteros")
        end

        if cons < 0
            raise Exception.new("El valor Cero del numero de church no puede ser menor que el cero de los enteros")
        end

        @cons = cons
    end

    def to_s
        "#{@cons}"
    end
end

class Suc < Church
    attr_accessor :val, :res
    def initialize(val)
        if val.class == Suc
            @val = "suc(#{val})"
            @res = val.res+1
        elsif val.class == Cero
            @val = "suc(#{val})"
            @res = val.cons+1
        else 
            raise Exception("Suc debe resibir un numero de un numero de Church")
        end
    end

    def to_s
        @val

    end
end

x = Cero.new(15)
y = Suc.new(Cero.new(5))

puts ((x*x*x*Cero.new(0)).class)