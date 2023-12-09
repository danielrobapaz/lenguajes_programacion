from Tabla_de_metodos import Tabla_de_metodos

def show_options() -> None:
    print("Escriba una accion a ejecutar: ")
    print("""
    CLASS <tipo> [<nombre>] 
        <tipo> puede ser un nombre que establece un tipo que no hereda de ningunotro
        <tipo> : <super> establece que el tipo hereda del tipo con nombre <super>
    DESCRIBIR <tipo>
    SALIR           
           """)

def main() -> None:
    print("Bienvenido al manejador de tablas de metodos virtuales.")
    manejador = Tabla_de_metodos()

    try:
        while True:
            show_options()
            user_input = input(">")

            user_input = [w for w in user_input.split(' ') if w != '']

            if user_input[0] == "CLASS":
                class_input = user_input[1:]
                
                nombre_tipo = class_input[0]
                super_tipo = None
                metodos_tipo = []

                if len(class_input) > 1:
                    metodos_tipo = class_input[1:]
                
                    if class_input[1] == ":":
                        super_tipo = class_input[2]
                        metodos_tipo = class_input[3:]

                res = manejador.agregar_clase(tipo=nombre_tipo,
                                              metodos=metodos_tipo,
                                              super=super_tipo)
                
                if not res:
                    print("\nSe encontro un error al agregar la clase.")
                    print("Recuerde que el nombre no puede estar repetido.")
                    print("de incluir una super clase, esta debe de existir y ")
                    print("la lista de metodos no puede tener repetidos\n")

                else:
                    print("Clase agregada satisfactoriamente")
                    
                
            elif user_input[0] == "DESCRIBIR":
                res = manejador.describir(user_input[1])
                if not res is None:
                    for (m, t) in res:
                        print(f"{m} -> {t} :: {m}")
                else:
                    print("El tipo no existe")

                print("")

            elif user_input[0] == "SALIR":
                break

            else:
                raise Exception()

    except:
        print("Accion inesperada")
    
    finally:
        print("Cerrando el simulador...")


if __name__ == "__main__":
    main()