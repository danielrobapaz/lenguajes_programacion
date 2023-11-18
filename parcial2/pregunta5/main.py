from Manejador_De_Tipos_De_Datos import Manejador_De_Tipos_De_Datos

def mostrar_opciones() -> None:
    print("---\nOpciones:")
    print("Para definir tipos: ")
    print("ATOMICO <nombre> <representacion> <alineacion> <alineacion>")
    print("STRUCT <nombre> [<tipo>]")
    print("UNION <nombre> [<tipo>]\n")

    print("Para consultar sobre los tipos:")
    print("DESCRIBIR <nombre>\n")

    print("Para salir:")
    print("SALIR\n")

def main() -> None:
    print(".:Simulador de manejador de tipos de datos:.")

    manejador = Manejador_De_Tipos_De_Datos()

    try:
        while True:
            mostrar_opciones()
            print("Ingrese opcion: ")
            opcion = input(">>").split(" ")
            opcion = [o for o in opcion if o != '']

            accion = opcion[0]
            nombre = opcion[1]

            if accion == "ATOMICO":
                res = manejador.agregar_atomico(nombre, int(opcion[2]), int(opcion[3]))
                if not res:
                    print(f"El tipo de dato ya existe")

            if accion == "STRUCT":
                res = manejador.agregar_registro(nombre, opcion[2:])
                if not res:
                    print(f"El tipo de dato ya existe o los tipos de datos de los campos no existen")

            if accion == "UNION":
                res = manejador.agregar_variante(nombre, opcion[2:])
                if not res:
                    print(f"El tipo de dato ya existe o los tipos de datos de los campos no existen")

            if accion == "DESCRIBIR":
                (res, descripcion) = manejador.describir(nombre)
                if not res:
                    print("El tipo de dato no existe")

                sin_empaquetado = descripcion['sin_empaquetado']
                empaquetado = descripcion['empaquetado']
                optimo = descripcion['optimo']
                
                print(f"Sin empaquetar:\n\tocupa: {sin_empaquetado[0]} bytes\n\talineacion: {sin_empaquetado[1]} bytes\n\tdesperdicia: {sin_empaquetado[2]} bytes")
                print(f"Empaquetado:\n\tocupa: {empaquetado[0]} bytes\n\talineacion: {empaquetado[1]} bytes\n\tdesperdicia: {empaquetado[2]} bytes")
                print(f"Optimo:\n\tocupa: {optimo[0]} bytes\n\talineacion: {optimo[1]} bytes\n\tdesperdicia: {optimo[2]} bytes")

            if accion == "SALIR":
                break

    except Exception:
        print("Error en el comando de entrada")
    finally:
        print("Cerrando el manejador...")
    

if __name__ == "__main__":
    main()
    