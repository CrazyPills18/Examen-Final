from data_manage import listadoUser, guardarArchivo

#Sign up
def signUp():
    print("SIGN UP")
    user =  input("Ingrese su Usuario: ")
    password =  input("Ingrese su Password: ")
    info =  user + "," + password
    guardarArchivo(info)

#Login
def login():
    print("LOGIN")
    _nom =  input("Ingrese su Usuario: ")
    _passwd =  input("Ingrese su Password: ")
    status = False
    for user in listadoUser():
        _nombre = user[0]
        _password = user[1]

        if (_nom == user[0]) and (_passwd == user[1]):
            print("Usuarios Autenticado\n")
            status = True
    if status == False:
        print("!Autenticación Fallida!\n")
    return status
