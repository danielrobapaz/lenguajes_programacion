"""
Cliente para probar probar el manejador de diagramas T.

Recibe las instrucciones a ejecutar desde la cmd e imprime el resultado

Autor: Daniel Robayo
Carnet: 18-11086
Lenguajes de programacion CI-3641
"""

from diagramas import T_Diagrams

usage_message = 'Usage: python3 main.py num_bloques'

def main():
    try:
        diag = T_Diagrams()

        print("Las posibles accioens son:")
        print("DEFINIR <tipo> [<argumentos>]")
        print("EJECUTABLE <nombre>")
        print("SALIR\n")

        print("Los posibles tipos son:")
        print("PROGRAMA <nombre> <lenguaje>")
        print("INTERPRETE <lenguaje_base> <lenguaje>")
        print("TRADUCTOR <lenguaje_base> <lenguaje_origen> <lenguaje_destino>")

        while(True):
            action = input("\nIngrese operacion a realizar: \n")
            if action == '':
                raise Exception('Operacion invalida')
            
            action_list = [a for a in action.split(" ") if a != ""]
            action_to_execute = action_list[0]

            if action_to_execute == 'DEFINIR':
                define = action_list[1]

                if define == 'PROGRAMA':
                    if diag.add_program(action_list[2], action_list[3]):
                        print('Se definio el programa')

                    else:
                        print('No se definio el programa. El programa ya existe')

                elif define == "INTERPRETE":
                    if diag.add_interpreter(action_list[2], action_list[3]):
                        print('Se definio el interpretador')

                    else:
                        print('No se definio el interprete. El interprete ya existe')

                elif define == "TRADUCTOR":
                    if diag.add_translator(action_list[2], action_list[3], action_list[4]):
                        print('Se definio el traductor')

                    else:
                        print('No se definio el traductor. El traductor ya existe')

                else:
                    print("Opcion invalida")

            elif action_to_execute == 'EJECUTABLE':
                if diag.can_excute(action_list[1]):
                    print("Se puede ejecutar el programa")

                else:
                    print("No se puede ejecutar el programa")

            elif action_to_execute == "SALIR":
                break

            else:
                print('Opcion invalida')
    
    except Exception as exp:
        print(exp.args[0])

    finally:
        print('.:Cerrando simulacion:.')


if __name__ == '__main__':
    main()