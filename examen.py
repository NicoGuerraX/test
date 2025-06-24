lista = []
opcion = 0
#test
acceso = 12345

def comprar_boleto():
    nombreusu = input("Ingrese su nombre de usuario para a compra: ")
    try:
        tipo = input("Ingrese su tipo de entrada (G/V): ").lower()
        codigo = input("Ingrese el numero de confirmacion: ")
        if tipo == "v"and codigo == acceso:
            return [nombreusu, tipo, codigo]
    except ValueError:
        print("Valores mal ingresados por favor compruebe")


def consulta_comprador(nombreusu):
     for i in lista:
        if lista["nombre"].lower() == nombreusu.lower():
            return lista
     return None

def cancelar_compra(nombreusu):
    cancelar = consulta_comprador(nombreusu)
    if cancelar!=None:
        lista.remove(cancelar)
        print("Compra cancelada correctamente")
    else:
        print("El usuario selecconado no existe")

while opcion == 4:
    print("Bienvenido a la zona de compras \nMENU PRINCIPAL \n1.-Comprar entrada. \n2.-Consultar comprador \n3.-Cancelar comprador 4.-Salir")
    try:
        opcion = int(input("Seleccione una opcion: "))
    except ValueError:
        print("La opcion ingresada no es valida. Por favor utilice numeros de 1 a 4 en a operacion")
        continue
    match opcion:
         case "1":
             name = ("Ingrese el nombre de usuario: ")
             compra = comprar_boleto(name)
            
         case "2":
             nombre = input("Ingrese el nombre del comprador: ")
             buscado = consulta_comprador(nombre)
