#Menú
def menuPrincipal():
    listaOpciones = ["Home", "Tienda", "Carrito", "Mi perfil", "Acerca de", "ADMIN"]
    print("UrbanCT")
    contado = 0
    for itemOpc in listaOpciones:
        contado =  contado + 1
        print(str(contado), " - ", itemOpc)
    opc = int(input("Seleccione una opción ==> "))
    if opc <= len(listaOpciones):
        return opc
    else:
        print("Opción invalidad ")
menuPrincipal()

l_arreglo = []

#Nombre de funcióon
def getNameFuction(ft):
  name = ft.__name__
  print("\n \t Función ", name) 

#Serializar
def clean_data(elemt):
  temp = elemt.strip()
  temp = temp.capitalize()
  return temp

#Añadir variable Serializada
def añadir(_elemento):
  getNameFuction(añadir)
  temp = _elemento.strip()
  temp = temp.capitalize()

  print("Agregando el nuevo elemento: ", temp)
  l_arreglo.append(temp)
  print("Guardado.")

#Agregar variable nueva
def agregar():
  getNameFuction(agregar)
  for item in l_arreglo:
    print(item)

#Enlistamiento de variables (actualizar)
def act(_item):
  getNameFuction(act)

  s_value = clean_data(_item)

  if s_value in l_arreglo:
    print("Si existe")
  else:
    print("El elemento no existe")
 
#Eliminar variable 
def eliminar(_elm):
  getNameFuction(eliminar)
  val = input("¿Desea eliminar el producto, s/n?")
  temp = clean_data(val)
  if temp != "Si":
    print("Proceso de eliminación cancelado por el usuario :)")
  else:
    s_delete = clean_data(_elm)
    if s_delete in l_arreglo:
      l_arreglo.remove(s_delete)
      print(s_delete,"Ha sido elimido con éxito")
      agregar()
    else:
      print("No puedo eliminar {0}, porque no existe ".format(_elm))
      print("No puedo eliminar ",_elm," porque no existe ")
