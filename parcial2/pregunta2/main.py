from Manejador_Expresione_Aritmeticas import Manejador_Expresiones_Aritmeticas

def mostrar_opciones():
    print("\n\nOpciones: ")
    print("EVAL <orden> <expresion> -> Para evaluar una expression escrita en <orden>")
    print("MOSTRAR <orden> <expresion> -> Para mostrar la expresion escrita en <orden> en notacion infija")
    print("SALIR\n\n")

    print("<orden> = PRE para expresiones escritas en notacion prefija")
    print("<orden> = POST para expresiones escritas en notacion postfija")

def main():
    print("::::Bienvenido al manejador de expressiones aritmeticas::::")
    
    try:
        while True:
            mostrar_opciones()
            user_input = input("Ingrese opcion >> ")
            user_input = user_input.split(' ')
            user_input = [item for item in user_input if item != '']
            
            opc = user_input[0]
            if opc == "SALIR":
                break

            orden = user_input[1]
            expresion = ' '.join(user_input[2:])
            manejador_expresiones_aritmeticas = Manejador_Expresiones_Aritmeticas(orden, expresion)
                
            if opc == "EVAL":
                print(f"{expresion} = {manejador_expresiones_aritmeticas.eval_expresion()}")
                continue

            if opc == "MOSTRAR":
                print(f"{expresion} en notacion INFIJA es: ")
                print(manejador_expresiones_aritmeticas.expresion_infija())
                continue 
    except:
        print("Ingreso un valor incorrecto, vuelva a iniciar el manejador")
    finally:
        print("Cerrando el manejador...")

if __name__ == '__main__':
    main()
