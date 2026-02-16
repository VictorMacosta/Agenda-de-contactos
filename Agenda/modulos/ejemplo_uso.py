import json
import csv
import funciones as fx



# En ejemplo_uso.py
if __name__ == "__main__":
    agenda = []
    fx._add(agenda, 1, "Victor", apellido="Garcia")
    fx._add(agenda, 2, "Ana", apellido="Lopez")
    fx._guardar_datos(agenda)
    print("Todo funciona: revisa contactos.json")
    