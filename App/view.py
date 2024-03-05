﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import os
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from pathlib import Path
assert cf
from tabulate import tabulate
import traceback
from sys import version
print(version)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller(adt="ARRAY_LIST"):
    """
        Se crea una instancia del controlador
    """
    controller_instance = controller.new_controller(adt)
    return controller_instance


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control, data_size="10-por-"):
    """
    Carga los datos
    """
    # ac_list = ['job', 'emp', 'sk', 'ml']
    path = os.path.abspath("..\\Data\\")
    acronyms = {
        "jobs": Path(f"{path}/{data_size}jobs.csv"),
        "employments": Path(f"{path}/{data_size}employments_types.csv"),
        "multloc": Path(f"{path}/{data_size}multilocations.csv"),
        "skills": Path(f"{path}/{data_size}skills.csv"),
    }
    controller.load_data(control, acronyms["jobs"], 'job')
    controller.load_data(control, acronyms["multloc"], 'ml')
    controller.load_data(control, acronyms["skills"], 'sk')
    controller.load_data(control, acronyms["employments"], 'emp')
    return control


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


def _set_adt(adt):
    if adt == 1:
        return "ARRAY_LIST"
    elif adt == 2:
        return "LINKED_LIST"

    return ""


def _set_tabulate_headers(ac_dict):
    for item in ac_dict:


def _print_data(struct):
    first = lt.subList(struct, 1, 3)
    last = lt.subList(struct, lt.size(struct) - 3, 3)
    print(tabulate(first, headers=first[0].keys(), tablefmt='rounded_grid'))

# Se crea el controlador asociado a la vista
# control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            estructura = input("Indique la estructura base:\n1 - ARRAY_LIST\n2 - LINKED_LIST\n")
            # ordenamiento = input("Indique el criterio de ordenamiento:\n1 - Nombre empresa\n2 - Fecha publicacion\n")
            adt = _set_adt(int(estructura))
            control = new_controller(adt)
            print("Cargando información de los archivos ....\n")
            data = load_data(control["model"])
            _print_data(control["model"]["jobs"])
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
