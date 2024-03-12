"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos

headers = {
    "jobs": [],
    "employments": [],
    "multloc": [],
    "skills": [],
}


def new_data_structs(adt="ARRAY_LIST"):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    structs = {
        "jobs": lt.newList(adt),
        "employments": lt.newList(adt),
        "multloc": lt.newList(adt),
        "skills": lt.newList(adt)
    }
    return structs


# Funciones para agregar informacion al modelo

def add_data(data_structs, data, add_case):
    """
    Función para agregar nuevos elementos a la lista
    """
    match add_case:
        case 'job':
            lt.addLast(data_structs["jobs"], data)
        case 'ml':
            lt.addLast(data_structs["multloc"], data)
        case 'sk':
            lt.addLast(data_structs["skills"], data)
        case 'emp':
            lt.addLast(data_structs["employments"], data)
        case _:
            print("Wrong surname given")

# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs, country_code, expertise_level, n):
    """
    Función que soluciona el requerimiento 1
    """
    jobs_iter = lt.iterator(data_structs["jobs"])
    res_list = lt.newList(datastructure="ARRAY_LIST")
    for element in jobs_iter:
        if element["country_code"] == country_code and element["experience_level"] == expertise_level:
            lt.addFirst(res_list, element)

    if lt.size(res_list) == 0:
        return 0, None
    elif lt.size(res_list) < n:
        return lt.size(res_list), res_list
    else:
        return lt.size(res_list), lt.subList(res_list, 1, n)


def req_2(data_structs, company_name, city, n):
    """
    Función que soluciona el requerimiento 2
    """
    jobs_iter = lt.iterator(data_structs["jobs"])
    res_list = lt.newList(datastructure="ARRAY_LIST")
    for element in jobs_iter:
        if element["company_name"] == company_name and element["city"] == city:
            lt.addFirst(res_list, element)

    if lt.size(res_list) == 0:
        return 0, None
    elif lt.size(res_list) < n:
        return lt.size(res_list), res_list
    else:
        return lt.size(res_list), lt.subList(res_list, 1, n)


def req_3(data_structs, company_name, init_date, final_date):
    """
    Función que soluciona el requerimiento 3
    """
    counter_dict = {
        "junior": 0,
        "mid": 0,
        "senior": 0
    }
    jobs_iter = lt.iterator(data_structs["jobs"])
    res_list = lt.newList(datastructure="ARRAY_LIST")
    for element in jobs_iter:
        if element["company_name"] == company_name and init_date <= element["published_at"] <= final_date:
            counter_dict[element["experience_level"]] += 1
            lt.addFirst(res_list, element)

    return counter_dict, sort(res_list, "country")


def req_4(data_structs, country_code, init_date, final_date):
    """
    Función que soluciona el requerimiento 4
    """
    company_counter = {}
    city_counter = {}
    jobs_iter = lt.iterator(data_structs["jobs"])
    res_list = lt.newList(datastructure="ARRAY_LIST")
    for element in jobs_iter:
        if element["country_code"] == country_code and init_date <= element["published_at"] <= final_date:
            lt.addFirst(res_list, element)
            if element["company_name"] not in company_counter:
                company_counter[element["company_name"]] = 1
            else:
                company_counter[element["company_name"]] += 1

            if element["city"] not in city_counter:
                city_counter[element["city"]] = 1
            else:
                city_counter[element["city"]] += 1

    return company_counter, city_counter, lt.size(res_list), sort(res_list, "name")


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def _set_sort_criteria(use_case):
    match use_case:
        case "default":
            return default_sort_criteria
        case "name":
            return company_sort_criteria
        case "country":
            return country_sort_criteria


def default_sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    return data_1["published_at"] < data_2["published_at"]


def company_sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    if data_1["company_name"] == data_2["company_name"]:
        return data_1["published_at"] < data_2["published_at"]
    else:
        return data_1["company_name"] < data_2["company_name"]


def country_sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    if data_1["published_at"] == data_2["published_at"]:
        return data_1["country_code"] < data_2["country_code"]
    else:
        return data_1["published_at"] < data_2["published_at"]


def sort(data_structs, param):
    """
    Función encargada de ordenar la lista con los datos
    """
    return ins.sort(data_structs, _set_sort_criteria(param))
