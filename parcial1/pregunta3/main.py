"""
    Cliente para probar interactivamente el simulador de memoria Buddy system.
    El programa pide un input desde la cmd y devuelve el resultado 

    Se pueden ejecutar las siguientes acciones
    - Reservar memoria a un proceso
    - Liberar la memoria reservada por un proceso
    - Mostar las listas de bloques asignados y libres

    Autor: Daniel Robayo
    Carnet: 18-11086
    lenguajes de programcion CI-3641
"""

from buddy_system import Buddy_System
import sys

usage_message = 'Usage: python3 main.py num_bloques'

def main():
    try:
        args = sys.argv

        if len(args) != 2:
            raise Exception(usage_message)

        if not args[1].isdecimal():
            raise Exception(usage_message + '| num_bloques debe ser un numero natural')
        
        n_blocks = int(args[1])
        
        bud_sys = Buddy_System(n_blocks)
        
        print(".:Implementacion del buddy system:.")
        print("Puede realizar las siguientes operaciones.")
        print("RESERVAR <cantidad> <nombre>")
        print("LIBERAR <nombre>")
        print("MOSTRAR")
        print("SALIR")

        while (True):
            action = input("\nIngrese operacion a realizar: \n")
            if action == '':
                raise Exception('Operacion invalida')
            
            action_list = [a for a in action.split(" ") if a != ""]
            action_to_execute = action_list[0]

            if action_to_execute == 'RESERVAR':
                bud_sys.reserve(action_list[2], int(action_list[1]))

            elif action_to_execute == 'LIBERAR':
                bud_sys.free(action_list[1])

            elif action_to_execute == 'MOSTRAR':
                bud_sys.show()

            elif action_to_execute == 'SALIR':
                break

            else:
                raise Exception('Operacion invalida')

    except Exception as exp:
        print(exp.args[0])

    finally:
        print('.:Cerrando simulacion:.')


if __name__ == '__main__':
    main()