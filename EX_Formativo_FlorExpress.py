















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


  except ValueError:

    print("\n¡ERROR!, digite una opcion valida."); 
