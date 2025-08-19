# Tasa de interés
                while True:
                    try:
                        tasa = float(input("Ingrese la tasa de interés anual (ej. 5 para 5%):\n"))

                        # porcentaje de ingreso ahorrado (no de interés)
                        porcentaje_ahorro = (ahorro_mensual / ingreso) * 100  

                        if porcentaje_ahorro > 35:
                            print(f"\nAdvertencia: Su ahorro ({porcentaje_ahorro:.1f}% del ingreso) es alto ({ahorro_mensual})")
                            print("Recomendación: Un ahorro ideal está entre 10-30% de sus ingresos")
                        break
                    except ValueError:
                        print("Error, los valores deben de ser números o no deben de estar vacíos")

                # Años
                while True:
                    try:
                        años = int(input("Ingrese el número de años de ahorro:\n"))
                        break
                    except ValueError:
                        print("Error, los valores deben de ser números o no deben de estar vacios")