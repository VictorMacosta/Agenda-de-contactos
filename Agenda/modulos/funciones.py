import json
import csv
#   funciones contactos

def _buscar(lista, id_buscado):
    for elemento in lista:
        if elemento["id"] == id_buscado:
            return elemento
        
    return None
    
def _crear_contacto(id, nombre, **datos):
    contacto = {
        "id": id,
        "nombre": nombre,
        "apellido": "none"
    }

    contacto.update(datos)
    return contacto
    

def _add(lista, id, nombre, **datos):
    contacto = _buscar(lista, id)

    if contacto is not None:
        print(f"ya existe el contacto {id}")
    else:
        nuevo_contacto = _crear_contacto(id, nombre, **datos)
        lista.append(nuevo_contacto)
        return True


def _modif_dato(lista, id_buscado, campo, dato):
    contacto = _buscar(lista, id_buscado)

    if contacto is None:
        print(f"no existe un contacto con el id {id_buscado}")
        return False
    elif campo not in contacto:
        print(f"no existe el campo {campo}")
        return False
    else:
        contacto[campo] = dato
        return True



def _eliminar(lista, id_buscado):
    contacto = _buscar(lista, id_buscado)

    if contacto is None:
        print(f"No existe el contacto{id_buscado}")
        return False
    else:
        lista.remove(contacto)
        return True
    


#       funciones agenda

def _add_campo_agenda(lista, campo):
    for contacto in lista:
        if campo not in contacto:
            contacto.update({campo: "none"})


def _guardar_datos(lista):
    with open("contactos.json", "w", encoding="utf-8") as c:
        try:
            json.dump(lista, c, indent=4)
            print("Datos guardados satisfactoriamente")
        except(IOError, TypeError) as e:
            print(f"Fallo al guardar {e}")

def _leer_datos():
    contactos = []

    try:
        with open("contactos.json", "r", encoding="utf-8") as c:
            contactos = json.load(c)

    except FileNotFoundError:
        print(f"Archivo no encontrado, agenda vacia")
        
    except json.JSONDecodeError as e:
        print(f"Archivo corrupto: {e}")

    return contactos

def _mostrar(lista):
    for x in lista:
        print(x)

def _buscar_por_campo(lista, campo, valor_buscado):
    encontrado = []

    for c in lista:
        if campo in c:
            if str(c[campo]).lower() == str(valor_buscado).lower():
                encontrado.append(c)

    return encontrado


def _crear_csv(lista):
    if not lista:
        return 
    
    todas_claves = set()
    for contacto in lista:
        todas_claves.update(contacto.keys())
    
    cabecera = sorted(todas_claves)

    with open("contactos.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(cabecera)
        for contacto in lista:
            fila = [contacto.get(clave, "") for clave in cabecera]
            writer.writerow(fila)