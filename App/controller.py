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
 """
import datetime

import config as cf
import model
import time
import csv



"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller(adt="ARRAY_LIST"):
    """
    Crea una instancia del modelo
    """
    control = {
        "model": model.new_data_structs(adt)
    }
    return control


# Funciones para la carga de datos

def load_data(control, filename, data_name):
    """
    Carga los datos del reto
    """
    match data_name:
        case 'job':
            with open(filename, 'r', encoding="utf-8") as f:
                reader = csv.DictReader(f, delimiter=";")
                _set_tabulate_headers(filename, 'job')
                for line in reader:
                    date_data = _set_string_as_datetime(line["published_at"])
                    line["published_at"] = date_data
                    model.add_data(control, line, 'job')
        case 'ml':
            with open(filename, 'r', encoding="utf-8") as f:
                reader = csv.DictReader(f, delimiter=";")
                _set_tabulate_headers(filename, 'ml')
                for line in reader:
                    model.add_data(control, line, 'ml')
        case 'sk':
            with open(filename, 'r', encoding="utf-8") as f:
                reader = csv.DictReader(f, delimiter=";")
                _set_tabulate_headers(filename, 'sk')
                for line in reader:
                    model.add_data(control, line, 'sk')
        case 'emp':
            with open(filename, 'r', encoding="utf-8") as f:
                reader = csv.DictReader(f, delimiter=";")
                _set_tabulate_headers(filename, 'emp')
                for line in reader:
                    model.add_data(control, line, 'emp')
        case _:
            print("Not allowed")

# Funciones de ordenamiento


def _set_tabulate_headers(filename, keyword):
    match keyword:
        case 'job':
            with open(filename, 'r', encoding="utf-8") as f:
                reader = csv.DictReader(f)
                dict_from_csv = dict(list(reader)[0])
            list_of_column_names = list(dict_from_csv.keys())
            model.headers["jobs"] = list_of_column_names[0].split(";")
        case 'ml':
            with open(filename, 'r', encoding="utf-8") as f:
                reader = csv.DictReader(f)
                dict_from_csv = dict(list(reader)[0])
            list_of_column_names = list(dict_from_csv.keys())
            model.headers["multloc"] = list_of_column_names[0].split(";")
        case 'sk':
            with open(filename, 'r', encoding="utf-8") as f:
                reader = csv.DictReader(f)
                dict_from_csv = dict(list(reader)[0])
            list_of_column_names = list(dict_from_csv.keys())
            model.headers["skills"] = list_of_column_names[0].split(";")
        case 'emp':
            with open(filename, 'r', encoding="utf-8") as f:
                reader = csv.DictReader(f)
                dict_from_csv = dict(list(reader)[0])
            list_of_column_names = list(dict_from_csv.keys())
            model.headers["employments"] = list_of_column_names[0].split(";")
        case _:
            print("Wrong surname given")


def _set_string_as_datetime(date_str):
    return datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f%z")


def get_tabulate_headers(keyword):
    match keyword:
        case 'job':
            return model.headers["jobs"]
        case 'ml':
            return model.headers["multloc"]
        case 'sk':
            return model.headers["skills"]
        case 'emp':
            return model.headers["employments"]
        case _:
            print("Wrong surname given")
    return None


def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control, country_code, seniority, n):
    """
    Retorna el resultado del requerimiento 1
    """
    return model.req_1(control["model"], country_code, seniority, n)


def req_2(control, company_name, city, n):
    """
    Retorna el resultado del requerimiento 2
    """
    return model.req_2(control["model"], company_name, city, n)


def req_3(control, company_name, init_date, final_date):
    """
    Retorna el resultado del requerimiento 3
    """
    return model.req_3(control["model"], company_name, init_date, final_date)


def req_4(control, country_code, init_date, final_date):
    """
    Retorna el resultado del requerimiento 4
    """
    return model.req_4(control["model"], country_code, init_date, final_date)


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
