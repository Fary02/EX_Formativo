# Declaramos los objetos / arrays a utilizar;

arreglos = []; 

arreglo = {}; 

bodega = {}; 

# Creamos las functions a utilizar;

def validacion_codigo ():
  
  # Solicitamos codigo;

  codigo_validacion = str(input("\nPor favor, digite el codigo del arreglo: ")); 

  # Ocupamos len para filtrar; 

  codigo_validacion_len = len(codigo_validacion); 

  # Si las condiciones se cumplen retorna el valor, de lo contrario retorna false;

  if codigo_validacion.strip() and codigo_validacion.find("") != arreglo and codigo_validacion_len > 1:

    return codigo_validacion;  

  return False; 

def validacion_nombre ():

  nombre_validacion = str(input("\nPor favor, digite el nombre del arreglo: ")); 

  nombre_validacion_len = len(nombre_validacion); 

  if nombre_validacion.strip() and nombre_validacion_len > 1:

    return nombre_validacion; 

  return False; 

def validacion_tipo ():

  tipo_validacion = str(input("\nPor favor, digite el tipo del arreglo: ")); 

  tipo_validacion_len = len(tipo_validacion); 

  if tipo_validacion.strip() and tipo_validacion_len > 1:

    return tipo_validacion; 

  return False; 

def validacion_color_principal ():

  color_principal_validacion = str(input("\nPor favor, digite el color del arreglo: ")); 

  color_principal_validacion_len = len(color_principal_validacion); 

  if color_principal_validacion.strip() and color_principal_validacion_len > 1:

    return color_principal_validacion; 

  return False; 

def validacion_tamaño ():

  tamaño_validacion = str(input("\nPor favor, digite el tamaño del arreglo S / M / L: ")); 

  if tamaño_validacion.strip() and tamaño_validacion == "S" or tamaño_validacion == "M" or tamaño_validacion == "L":

    return tamaño_validacion; 

  return False; 

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

    return temporada_validacion; 

  return False; 

def validacion_precio ():

  precio_validacion = int(input("\nPor favor, digite el precio del arreglo: ")); 

  if precio_validacion > 0:

    return precio_validacion; 

  return False; 

def validacion_unidades ():

  unidades_validacion = int(input("\nPor favor, digite las unidades del arreglo: ")); 

  if unidades_validacion >= 0:

    return unidades_validacion; 

  return False; 

def agregar_arreglo ():

  # Se pasan las functions a una nueva variable para ser validadas;

  codigo = validacion_codigo(); 

  nombre = validacion_nombre(); 

  tipo = validacion_tipo(); 

  color_principal = validacion_color_principal(); 

  tamaño = validacion_tamaño(); 

  incluye_tarjeta = validacion_incluye_tarjeta(); 

  temporada = validacion_temporada(); 

  precio = validacion_precio(); 

  unidades = validacion_unidades(); 

  # Si la condicion se cumple crea los siguientes diccionarios / objetos;
  
  if codigo and nombre and tipo and color_principal and tamaño and incluye_tarjeta and temporada and precio and unidades != False:

    bodega = {

      "Codigo": codigo,

      "Precio": precio,

      "Unidades": unidades

    }

    # el objeto / diccionario arreglo contiene a bodega dentro como atributo, por eso se define antes bodega;

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

    # Se crea un for in para recorrer bodega dentro de arreglo en busqueda del codigo;

    for bodega in arreglo:

      # Si el codigo no existem se agrega el arreglo y retorna true;

      if bodega.find(f"{codigo}") != codigo:
        
        arreglos.append(arreglo); 

        print("\n¡Arreglo agregado!"); 

        return True; 
    
      # De lo contrario avisa al usuario que ya existe un arreglo con ese codigo y retorna false;

      else:

        print("\n¡El codigo del arreglo ya existe!"); 

        return False; 

# Se crea la function y se pasa el parametro de tipo;

def unidades_por_tipo(tipo):

  # Se crea una variable con un valor inicial;

  total_unidades = 0; 

  # Se recorre arreglo en arreglos;

  for arreglo in arreglos:

    # Si el atributo "Tipo" dentro de arreglo es igual al del parametro;

    if arreglo["Tipo"].lower() == tipo.strip().lower():

      # Se acumula con los que existen en el atributo "Bodega";

      total_unidades += arreglo["Bodega"]["Unidades"]; 
  
  # Y se imprime por consola;

  print(f"\nEl total de unidades disponibles es: {total_unidades}"); 


def salir_menu ():

  print("\nPrograma finalizado.");  
 
# Bucle menu;

while True:

  print("\n*****MENU PRINCIPAL*****"); 
  print("1. Unidades por tipo de arreglo"); 
  print("2. Busqueda de arreglos por rango de precio"); 
  print("3. Actualizar precio de arreglo"); 
  print("4. Agregar arreglo"); 
  print("5. Eliminar arreglo"); 
  print("6. Salir"); 

  # Intenta solicitar una opcion;

  try:

    opcion = int(input("\nPor favor, digite una opcion: ")); 

    # Si opc 1 se solicita ingresar el tipo a consultar y retorna la function con el parametro;
  
    if opcion == 1:

      tipo_buscado = str(input("\nIngrese el tipo de arreglo a consultar: ")); 
    
      unidades_por_tipo(tipo_buscado); 
    
    # Si opc 4 se solicitan info para agregar el arreglo y muestra los que hay en consola;
    
    elif opcion == 4:

      agregar_arreglo(); 
    
      print(f"\n{arreglos}"); 

    # Si opc 6 muestra el mensaje de finalizacion y corta el bucle;
     
    elif opcion == 6:

      salir_menu(); 
  
      break; 
  
  # Manejo de errores;

  except ValueError:

    print("\n¡ERROR!, digite una opcion valida."); 