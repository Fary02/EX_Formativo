# Declaramos los objetos / arrays a utilizar;

arreglos = []; 

arreglo = {}; 

bodega = {}; 

# Creamos las functions a utilizar;

def unidades_tipo (tipo):

  tipo = str(input("\nPor favor, digite el tipo de arreglo: ")); 

  # Ver si la estructura de el for in de la linea 162 sirve

    

def validacion_codigo ():

  codigo_validacion = str(input("\nPor favor, digite el codigo del arreglo: ")); 

  codigo_validacion_len = len(codigo_validacion); 

  if codigo_validacion.strip() and codigo_validacion.find("") != arreglo and  codigo_validacion_len > 1:

    return True;  

def validacion_nombre ():

  nombre_validacion = str(input("\nPor favor, digite el nombre del arreglo: ")); 

  nombre_validacion_len = len(nombre_validacion); 

  if nombre_validacion.strip() and nombre_validacion_len > 1:

    return True; 

def validacion_tipo ():

  tipo_validacion = str(input("\nPor favor, digite el tipo del arreglo: ")); 

  tipo_validacion_len = len(tipo_validacion); 

  if tipo_validacion.strip() and tipo_validacion_len > 1:

    return True; 

def validacion_color_principal ():

  color_principal_validacion = str(input("\nPor favor, digite el color del arreglo: ")); 

  color_principal_validacion_len = len(color_principal_validacion); 

  if color_principal_validacion.strip() and color_principal_validacion_len > 1:

    return True; 

def validacion_tamaño ():

  tamaño_validacion = str(input("\nPor favor, digite el tamaño del arreglo S / M / L: ")); 

  if tamaño_validacion.strip() and tamaño_validacion == "S" or tamaño_validacion == "M" or tamaño_validacion == "L":

    return True; 

def validacion_incluye_tarjeta ():

  incluye_tarjeta_validacion = str(input("\nPor favor, digite si desea tarjeta en el arreglo s / n: ")); 

  if incluye_tarjeta_validacion.strip() and incluye_tarjeta_validacion == "s" or incluye_tarjeta_validacion == "n":

    if incluye_tarjeta_validacion == "s":

      return True; 

    if incluye_tarjeta_validacion == "n":

      return False; 

def validacion_temporada ():

  temporada_validacion = str(input("\nPor favor, digite la temporada del arreglo: ")); 

  temporada_validacion_len = len(temporada_validacion); 

  if temporada_validacion.strip() and temporada_validacion_len > 1:

    return True; 

def validacion_precio ():

  precio_validacion = int(input("\nPor favor, digite el precio del arreglo: ")); 

  if precio_validacion > 0:

    return True; 

def validacion_unidades ():

  unidades_validacion = int(input("\nPor favor, digite las unidades del arreglo: ")); 

  if unidades_validacion >= 0:

    return True; 


def agregar_arreglo ():

  codigo = validacion_codigo(); 

  nombre = validacion_nombre(); 

  tipo = validacion_tipo(); 

  color_principal = validacion_color_principal(); 

  tamaño = validacion_tamaño(); 

  incluye_tarjeta = validacion_incluye_tarjeta(); 

  temporada = validacion_temporada(); 

  precio = validacion_precio(); 

  unidades = validacion_unidades(); 
  
  if codigo and nombre and tipo and color_principal and tamaño and incluye_tarjeta and temporada and precio and unidades == True:

    bodega = {

      "Codigo": codigo,

      "Precio": precio,

      "Unidades": unidades

    }

    arreglo = {

      "Codigo": codigo,

      "Nombre": nombre,

      "Tipo": tipo,

      "Color principal": color_principal,

      "Tamaño": tamaño,

      "Incluye tarjeta": incluye_tarjeta,

      "Temporada": temporada,

      "Precio": precio,

      "Unidades": unidades,

      "Bodega": bodega

    }

    for bodega in arreglo:

      if bodega.find(f"{codigo}") != codigo:

        arreglos.append(arreglo); 

        print("\n¡Arreglo agregado!"); 

        return True; 

      else:

        print("\n¡El codigo del arreglo ya existe!"); 

        return False; 

def salir_menu ():

  print("\nPrograma finalizado."); 


while True:

  print("\n*****MENU PRINCIPAL*****"); 
  print("1. Unidades por tipo de arreglo"); 
  print("2. Busqueda de arreglos por rango de precio"); 
  print("3. Actualizar precio de arreglo"); 
  print("4. Agregar arreglo"); 
  print("5. Eliminar arreglo"); 
  print("5. Salir"); 

  try:

    opcion = int(input("\nPor favor, digite una opcion: ")); 
  

    if opcion == 4:

      agregar_arreglo(); 
  
    if opcion == 6:

      salir_menu(); 
  
      break; 


  except ValueError:

    print("\n¡ERROR!, digite una opcion valida."); 
