while True:
 try: 
      print("Bienvenido a la calculadora financiera de ahorro")
      print("1.Metas de ahorro mensuales")
      print("2.Proyecciones a largo plazo")
      print("3. Finalizar programa")
     
      opcion = input("Ingrese una opcion: ")
     
      if opcion ==  "1":
            while True:
             try:
                print("¿Periodo de tiempo en el que deseas calcular tus metas de ahorro?")
                print("1. Semanal")
                print("2. Mensual")
                print("3. Anual")
                print("4. Salir")
             
                opci = input("Ingresa una opción")
             
                if opci == "1":
                    try:
                         semanas = int(input("Ingresa por cuantas semanas deseas calcular  las metas de ahorro (En numeros)? escribe (salir) para cerrar esta plantilla"))
                         if semanas != "salir":
                      
                      
                         else:
                          print("saliendo de la plantilla")
                         break
                    except ValueError:
                      print("Debes de escribir tu respuesta en numeros, intentalo de nuevo")

                  
                elif opci == "2":
                    try:
                        meses = int(input("Ingresa por cuantos meses deseas calcular las metas de ahorro (En numeros). Escribe (salir) para salir de la plantilla"))
                        if semanas != "salir":
                    
                        else:
                          print("Saliendo de la plantilla")
                          break
                    except ValueError:
                     print("Debes de escribir tu respuesta en numeros, intentalo de nuevo")

                
         
                elif opci == "3":
                    try:
                        anios = int(input("Ingrese la cantidad de años por las que desea calcular las metas de ahorro (En numeros). Ingresa (salir) para salir"))
                        if anios != "salir":
                   
                        else:
                         print("Saliendo de la plantilla")
                         break
                    except ValueError:
                       print("Debes de escribir tu respuesta en numeros, intentalo de nuevo")


                   
                elif  opci == "4":
                 print("Saliendo del programa")
                 break

             except ValueError:
                print("Debes de escribir el numero de opcion que eliges, intentalo de nuevo")


      elif opcion == "2":
          while True:
            try:
              print("En esta plantilla puedes verificar las posibilidades de ahorro que puedes genrar en planes especificos de tiempo")
              print("/n ¿Cual es la cantidad de ahorro que deseas generar?")
              print("1. 10%")
              print("2. 50%")
              print("3. 80%")
              print("4. Salir")
              
              opcion = input("Ingresa una opcion: ")
              
              if opcion == "1":
                  while True:
                    try:
                      print("Cantidad de tiempo por la que deseas generar el ahorro")
                      print("1. Semanalmente")
                      print("2. Mensualmente")
                      print("3. Anualmente")
                      print("4. Salir")
                      
                      opci = input("Ingresa una opcion: ")
                      if opci == "1":
                          while True:
                            try:
                              print("Aproximacion de ingresos")
                              print("1. 0 - 150 $")
                              print("2. 150 - 300 $")
                              print("3. 300 - 500 $")
                              print("4. 500 - 1000 $")
                              print("5. 1000 - 5000 $")
                              print("6. 5000 - 9000 $")
                              print("7. 9000 + $")
                              print("8. Salir")
                              
                              op = input("Ingresa una opcion")
                              if op == "1":
                                 pass
                              elif op == "8":
                                 print("Saliendo de esta plantilla")
                                 break
                            except ValueError:
                               print("Ingresa el numero de tu seleccion")

                      elif opci == "4":
                         print("Saliendo de la plantilla")
                         break
                    except ValueError:
                       print("Debes de seleccionar un numero (no letras)")
                              
                          
                  
              elif opcion == "2":
                  while True:
                    try:
                      print("Cantidad de tiempo por la que deseas generar el ahorro")
                      print("1. Semanalmente")
                      print("2. Mensualmente")
                      print("3. Anualmente")
                      print("4. Salir")
                      
                      opci = input("Ingresa una opcion: ")
                      if opci == "1":
                          while True:
                            try:
                              print("Aproximacion de ingresos")
                              print("1. 0 - 150 $")
                              print("2. 150 - 300 $")
                              print("3. 300 - 500 $")
                              print("4. 500 - 1000 $")
                              print("5. 1000 - 5000 $")
                              print("6. 5000 - 9000 $")
                              print("7. 9000 + $")
                              print("8. Salir")
                              
                              op = input("Ingresa una opcion")
                              if op == "1":
                                 pass
                              elif op == "8":
                                 print("Saliendo de esta plantilla")
                                 break
                            except ValueError:
                               print("Ingresa el numero de tu seleccion")

                      elif opci == "4":
                         print("Saliendo de la plantilla")
                         break
                    except ValueError:
                       print("Debes de seleccionar un numero (no letras)")
                       

              elif opcion == "3":
                  while True:
                    try:
                      print("Cantidad de tiempo por la que deseas generar el ahorro")
                      print("1. Semanalmente")
                      print("2. Mensualmente")
                      print("3. Anualmente")
                      print("4. Salir")
                      
                      opci = input("Ingresa una opcion: ")
                      if opci == "1":
                          while True:
                            try:
                              print("Aproximacion de ingresos")
                              print("1. 0 - 150 $")
                              print("2. 150 - 300 $")
                              print("3. 300 - 500 $")
                              print("4. 500 - 1000 $")
                              print("5. 1000 - 5000 $")
                              print("6. 5000 - 9000 $")
                              print("7. 9000 + $")
                              print("8. Salir")
                              
                              op = input("Ingresa una opcion")
                              if op == "1":
                                 pass
                              elif op == "8":
                                 print("Saliendo de esta plantilla")
                                 break
                            except ValueError:
                               print("Ingresa el numero de tu seleccion")

                      elif opci == "4":
                         print("Saliendo de la plantilla")
                         break
                    except ValueError:
                       print("Debes de seleccionar un numero (no letras)")
                       

              elif opcion == "4":
                  print("Saliendo del programa")
                  break
            except ValueError:
               print("Debes de seleccionar un numero (no en letras)")

      elif opcion == "3":
        print("Saliendo del programa")
        break
      
 except ValueError:
    print("Texto invalido, intentalo den uevo")
     