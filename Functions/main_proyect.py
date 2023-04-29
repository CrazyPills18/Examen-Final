from fun_login import login, signUp
from def_functions import menuPrincipal
while __name__=='__main__':
    menu=0
    accountStatus=input(("¿Ya tienes una cuenta creada?\n1-Login\n¡Crea tu cuenta ya!\n2-Sign in\n= "))
    if  accountStatus == "1":
        login()
    elif accountStatus == "2":
        signUp()
    while menu!=1:
        men=input(menuPrincipal())
        if men == "1":
            print("si funcionooooooooo")
