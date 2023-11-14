# Solucion parcial 2
Para evitar inconsistencia, los programas entregados se deben ejecutar en un sistema operativo _linux-like_

## Pregunta 1
El lenguaje escogido fue Ruby. 
### (i) Estructuras de control.
1. Secuenciacion: La secuenciaion en ruby es el salto de linea.
2. Seleccion: La seleccion en ruby. Ademas de contar con if-then-else tambien se puede usar case-when.
```ruby
# forma 1
if <condicion1>
    # codigo si es true
else 
    # codigo si es false
end

# forma 2
if <condicion1>
    # codigo si condicion1 es true
elsif <condicion2>
    # codigo si condicion2 es true
...
elsif <condicionN>
    # codigo si condicionN es true
else
    # condiciion si ninguna condicion es true 
end

# forma 3
case <expresion>
when <expresion1>
    # codigo si expresion cumple expresion1
when <expresion2>
    # codigo si expresion cumple expresion2
...
when <expresionN>
    # codigo si expresion cumple expresionN
else
    # codigo si no se cumple ninguna condicion
end
```
3. Repeticion: Ruby cuenta con ```for``` y ```while```.Ademas fuenta con el metodo ```times``` y otras formas de realizar la repeticion.
```ruby
# for
for <variable> in <expresion|iterable> [do]
    ...
end

# while, evaluca mientras condicion=True
while <condicion> [do]
    ...
end

# times, repite n veces la instruccion
n.times {...}

# until, repite mientras condicion = False
until <condicion> [do]
    ...
end

# do while
loop [do]

    if <condicion de parada>
        break
    end
end
```

4. Abstraccion procedural: Ruby permite la definicion de funciones y metodos en clases. Las funcionas siempre devuelven la ultima instruccion evaluada por los procedimientos son funciones que devuelve ```nil```. Las funciones, asi como los metodos puede o no tener parametros. Opcionalmente, se puede usar ```return``` para especificar el valor de retorno.
```ruby
# funciones y procedimientos
def mi_funcion(mi_parametro)
    ...
end
def mi_funcion
    ...
end

# los metodos se definen de igual manera.
```

5. Recursion: Ruby permite la recursion.
```ruby 
def mi_funcion_recursiva(mi_parametro)
    return mi_parametro + mi_funcion_recursiva(mi_parametro-1)
```

6. Concurrencia: Ruby permite la creacion de proceso con ```fork()``` y de hilos usando ```Threads.new```. 

7. Excepciones: Ruby permite manejar las excepciones para controlar el flujo de la ejecucion.
```ruby
begin
    ...
rescue
    # codigo a ejecutar si ocurre alguna expcecion
else
    # se ejecuta si no se levanta expcecion alguna
ensure
    # siempre se ejecuta
end

# se puede hacer mas complejo ya que se pueden levantar excepciones
begin 
    ...
    raise ExceptionA
rescue ExceptionA => a
    ...
end
```

### (ii) Expressiones
Ruby es un lenguaje ortogonal por lo que todo puede ser evaluado como un expression y va a devolver in valor. Ruby tiene evaluacion aplicativa por los que las expressiones se evaluan antes de ser pasados a una funcion y evalua las expressiones de izquierda a derecha. En el caso de los operadores bitwise ruby usa cortocircuito.

### (iii) Tipos de datos
Ruby ofrece los siguientes tipos de datos.
- Numbers: Enteros o reales.
- Boolean.
- Strings.
- Hashes.
- Arrays.
- Symbols.

El tipo Hash es una coleccion de elementos de la forma (key, value). Los arrays pueden ser heterogeneos y el tipo Symbols son identificadores inmutables que pueden ser usados en los Hashes.

```ruby
a = "soy un string" # string
b = 3 # enteros
c = 4.5 # reales
d = true # booleanos
e = {"key1" => "val1", ..., "keyn" => "valn"} # hash
f = [a,b,c,d,e] # arrays
g = {:symbol1 => "val1", ..., :symboln => "valn"} # hash con llaves de tipos symbol
```

Como ruby es un lenguaje completamente orientado a objetos, todos los tipos de datos estan basados en una clase. Para crear tipos de datos nuevos basta con crear una clase.

```ruby
class Mi_Dato_Nuevo
    def initialize(mi_parametro)
        @mi_parametro = mi_parametro
    end
    ...
end

nueva_variables = Mi_Dato_nuevo.new(...)
```

### (iv) Sistema de tipos.
El sistema de tipos de ruby realiza la verificacin de tipos en forma dinamica. Como consecuencia, no es necesario declarar una variable para usarla. Sin embargo, al momento de ejecucion ocurriria un error.

En ruby la equivalencia de tipos es estructural tanto para los tipos proveeidos por el lenguje como para los tipos que defina el programador. En Ruby los tipos que son compatbiles son aquellos que son equivalentes. Asimismo, si hay un metodo o funcion que se efectua sobre tipos de datos numericos, el objeto que llama o el argumento que se recibe tiene que ser de un tipo equivalente.

```ruby
class Numero
    def abs:
        ...
        
class Entero < Numero
    ...

class Real < Numero
    ...

mi_entero = Entero.new
mi_real = Real.new

mi_entero.abs # seria valido
mi_real.abs # seria valido
```


Como en ruby las variables pueden ser de cualquier tipo no se tienen que realizar conversiones de tipos en la asignacion. Sin embargo para realizar operaciones aritmeticas entre tipos se tienen que realizar converiones para tipos que no son compatibles. El lenguaje provee algunas conversiones entre tipos de datos, sin embargo, el programador puede realizar las conversiones que desee.

```ruby
1.to_s # convertir de entero a string
"1".to_i # convertir de stringa entero
"1".to_f # convertir de string a real
```

Por ultimo, el lenguaje cuenta con inferencia de tipos. Al ser un lenguaje debilmente tipado, la inferencia de tipos ocurre cada vez que crea una variable y en parametros que recibem funciones y metodos.

### (a)
### (b)
#### (i)
#### (ii)

## Pregutna 3

## Pregunta 4

## Pregunta 5

## Pregunta 6