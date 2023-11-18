# Solucion parcial 2
Para evitar inconsistencia, los programas entregados se deben ejecutar en un sistema operativo _linux-like_

## Pregunta 1
El lenguaje escogido fue Ruby. 
### (a) De una breve descripcion del lenguaje escodigo.
#### (i) Estructuras de control.
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

#### (ii) Expressiones
Ruby es un lenguaje ortogonal por lo que todo puede ser evaluado como un expression y va a devolver in valor. Ruby tiene evaluacion aplicativa por los que las expressiones se evaluan antes de ser pasados a una funcion y evalua las expressiones de izquierda a derecha. En el caso de los operadores bitwise ruby usa cortocircuito.

#### (iii) Tipos de datos
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

#### (iv) Sistema de tipos.
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

### (b) Implemente los siguientes programas.
#### (i)
El codigo se encuentra en ```/pregunta1/Church.rb```. En el archivo se encuentra la definicion de; tipo ```Church```.

#### (ii)
El codigo se encuentra en ```/pregunta1/Arbol_binario.rb```. En el archivo se encuentra la definicion del tipo ```Arbol_binario```.

## Pregunta 2
Lenguaje escogido ```python version 3.11```. Para la ejecucion hacer los siguientes comandos
```c
python3 main.py // para cliente
python3 unit_test.py // para pruebas unitarias
```

## Pregunta 3
### (a)
$X=0$, $Y=8$ y $Z=6$. Por lo tanto $d = 6$. La llamada de la iterador es:
```python
misterio(0, 1, 0, 7)
```
El fragmento de codigo dado da la siguientes salida:

```python
for x in misterio(0, 1, 0, 7):
    print(x)

# Salida:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
```

El paso a paso se encuentra en ```pregunta3/misterio.pdf```

### (b)
El lenguaje usado para la implementacion del iterador fue ```python version 3.11```. Se encuentra en ```pregunta3/iterador.py```.

## Pregunta 4
Lenguaje escogido ```python version 3.11```. $X=0$, $Y=8$ y $Z=6$. Por lo tanto $\alpha = 6$ y $\beta = 7$. La familia de funciones es

$$F_{6,7}(n) =\begin{cases} n &\text{si } 0 \le n \lt 42 \\ F_{6,7}(n-7) + F_{6,7}(n-14) + F_{6,7}(n-21) + F_{6,7}(n-28) + F_{6,7}(n-35) + F_{6,7}(n-42) & \text{si } n \gt 42\end{cases}$$

La implementacion de las funciones se encuentra el ```pregunta4/Familia_De_Funciones.py```. Para obtener los datos para el analisis comparativo se uso el programa ```pregunta4/main.py```. El cual se ejecuta de la siguiente forma.
```c
python3 main.py
```

El codigo de ejecuto sobre una laptop con un procesador *Intel i5 12va generacion* y *40gb de RAM*. El archivo ```pregunta4/analisis_comparativo.ipynb``` genera los graficos del analisis. Para ejecutar el archivo ```main.py``` y ```analisis_comparativo.ipynb``` se tienen que instalar los paquetes correspondientes con el siguiente comando

```c
pip install -r requerimientos.txt
```

### Analisis comparativo
Para esta parte se decidio crear un cuaderno de jupyter y usar librerias de visualizacion de datos. Se evaluaron las tres implementaciones usando tamanos de entrada entre 0 y 300 dando pasos de 10 en 10. De cada implementacion se obtuvo lo siguiente. 

![recursivo](/pregunta4/img/recursivo.png)
*Figura 1*: Desempeno de la implementacion recursiva.

![recursivo de cola](/pregunta4/img/recursivo_cola.png)
*Figura 2*: Desempeno de la implementacion recursiva de cola.

![iterativo](/pregunta4/img/iterativo.png)
*Figura 3*: Desempeno de la implementacion iterativa.

Como se puede observar, la version recursiva tiene una complejidad exponiencial mientras que las otras dos tienen un comportamiento lineal. Ademas, para todas las versiones, el tiempo entre $0 \leq n \lt 41$ permanece *constante*. Luego, es directo observar que el que tuvo peor desempeno mientras mas crece $n$ fue el algoritmo recursivo. Este algorimo para el caso mas grande $(n=290)$ duro $4675$ segundos. Mientras que las versiones de cola e iterativas duraron $0.00033$ y $0.00025$ segundos respectivamente.

Ademas, se compararon todos los algorimos en el rango $(0\leq n\leq130)$ y se obtuvo lo siguiente.

![comparativo_130](/pregunta4/img/comparativo_130.png)
*Figura 4*: Comparacion de las 3 veriones con un rango de $n$ reducido.

![comparacion_cola_iterativo](/pregunta4/img/comparativo_cola_iterativo.png)
*Figura 5:* Comparacion entre la version recursiva de cola y iterativa.

Se puede observar que en $n\leq110$ las tres implementaciones tienen un desempeno muy similar, siendo la mas eficiente la recursiva. Sin embargo, para casos mas grandes, la version iterativa empieza a crecer rapidamente. Luego, se observa que las versiones iterativas y de cola tienen un desempeno muy bueno y muy parecido, siendo la iterativa mas rapida.

Finalmente, se pudo observar la diferencia entre las 3 versiones con respecto a su eficiencia en tiempo. Se concluye que la version ambas versiones, la iterativa y la de cola, tienen muy buen desempeno. Sin embargo, la version iteravia se comporta mejor para $n$ mayores ya que no necesita de la pila para su ejeccion.

## Pregunta 5
El lenguaje usado para la implementacion del iterador fue ```python version 3.11```. La implementacion del simulador del sistema de tipos se encuentra en ```pregunta5/Manejador_De_Tipos_De_Datos.py```. Para ejecutar el cliente y los casos de prueba
```c
python3 main.py //cliente
python3 unit_test.py // casos de prueba
```

Los registros se alinean a la potencia de 4 mayor mas cercana, Por ejempplo, si el tipo ocupa 17 bytes, su alineacion es 20.
## Pregunta 6
