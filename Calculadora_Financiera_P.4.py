    while True:
     print("Bienvenido a la calculadora financiera de ahorro")
     print("1.Metas de ahorro mensuales")
     print("2.Proyecciones a largo plazo")
     print("3. Finalizar programa")
     
     opcion = input("Ingrese una opcion: ")
     
        if opcion ==  "1":
            while True:
                print("¿Periodo de tiempo en el que deseas calcular tus metas de ahorro?")
                print("1. Semanal")
                print("2. Mensual")
                print("3. Anual")
                print("4. Salir")
             
                opci = input("Ingresa una opción")
             
                if opci == "1":
                  semanas = input("Ingresa por cuantas semanas deseas calcular  las metas de ahorro? escribe (salir) para cerrar esta plantilla")
                  if semanas != "salir":
                      
                      
                  else:
                     print("saliendo de la plantilla")
                     break
                  
                elif opci == "2":
                 meses = input("Ingresa por cuantos meses deseas calcular las metas de ahorro. Escribe (salir) para salir de la plantilla")
                 
                    if semanas != "salir":
             
                    else:
                     print("Saliendo de la plantilla")
                    break
                elif opci == "3":
                 anios = input("Ingrese la cantidad de años por las que desea calcular las metas de ahorro. Ingresa (salir) para salir")
                   if anios != "salir":
                   
                   else:
                    print("Saliendo de la plantilla")
                   break
                   
                elif  opci == "4":
                 print("Saliendo del programa")
                 break
               
                else:
                  print("Opcion invalida")
        elif opcion == "2":
          while True:
              print("En esta plantilla puedes verificar las posibilidades de ahorro que puedes genrar en planes especificos de tiempo")
              print("/n ¿Cual es la cantidad de ahorro que deseas generar?")
              print("1. 10%")
              print("2. 50%")
              print("3. 80%")
              print("4. Salir")
              
              opcion = input("Ingresa una opcion: ")
              
              if opcion == "1":
                  while True:
                      print("Cantidad de tiempo por la que deseas generar el ahorro")
                      print("1. Semanalmente")
                      print("2. Mensualmente")
                      print("3. Anualmente")
                      
                      opci = input("Ingresa una opcion: ")
                      if opcion == "1":
                          while True:
                              print("Aproximacion de ingresos")
                              print("1. 0 - 150 $")
                              print("2. 150 - 300 $")
                              print("3. 300 - 500 $")
                              print("4. 500 - 1000 $")
                              print("5. 1000 - 5000 $")
                              print("6. 5000 - 9000 $")
                              print("7. 9000 + $")
                              
                              op = input("Ingresa una opcion")
                  
              if opcion == "2":
                  while True:
                      print("Cantidad de tiempo por la que deseas generar el ahorro")
                      print("1. Semanalmente")
                      print("2. Mensualmente")
                      print("3. Anualmente")
                      
                      opci = input("Ingresa una opcion: ")
                      if opcion == "1":
                          while True:
                              print("Aproximacion de ingresos")
                              print("1. 0 - 150 $")
                              print("2. 150 - 300 $")
                              print("3. 300 - 500 $")
                              print("4. 500 - 1000 $")
                              print("5. 1000 - 5000 $")
                              print("6. 5000 - 9000 $")
                              print("7. 9000 + $")
                              
                              op = input("Ingresa una opcion")