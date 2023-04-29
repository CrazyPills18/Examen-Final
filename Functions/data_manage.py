#Manejo de datos
from pathlib import Path
path=Path.cwd()
dir=str(path)+"\Data\\"
filename=dir+"users.txt"

#Guardar
def guardarArchivo(info):
    borrarEspacio = info.strip()
    tam = len(borrarEspacio)
    if tam > 0:
        f = open(filename, "a+")
        # temp =  "\n" + info
        temp =  "\n" + info
        f.writelines(temp)
        f.close()
    else:
        print("No se puede almacenar información vacía")

#Leer
def leerArchivo(filename):
    lista_temp = []
    # Leer
    with open(filename, "r+") as f:
        for item in f.readlines():
            info =  item.split(',')

            # Posicion 0 - usuario
            # Posicion 1 - password
            _nombre = info[0]
            _password = info[1]

            # almacenando en lista
            lista_temp.append([_nombre, _password])
    f.close()
    return lista_temp

#Lista de usuarios
def listadoUser():
    lista_temp = []
    # Leer
    with open(filename, "r+") as f:
        for item in f.readlines():
            borrarEspacio = item.strip()
            tam = len(borrarEspacio) 
            if tam > 0:
                info =  item.split(',')

                # Posicion 0 - usuario
                # Posicion 1 - password
                _nombre = info[0]
                tmp = info[1].split("\n")
                _password = tmp[0]

                # almacenando en lista
                lista_temp.append([_nombre, _password])
    f.close()
    return lista_temp