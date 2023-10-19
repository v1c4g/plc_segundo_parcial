#Victoria Gomez Lopez-A00573409

def ruby():
    temperatura=float(input("introduce la tempertaura amabiente en grados Celsius:"))
    humedad=float(input("introduce el porcentaje de humedad en el aire alrededor de ruby:"))
    dia=str(input("introduce el dia de la semana actual:"))
#temperatura
    if temperatura<20:
      print("llevarla adentro de la casa")
    elif temperatura==20 and 25:
      print("buenas condiciones")
    elif temperatura>25:
      print("llevarla adentro de casa y encender el ventilador")
#dia de riego    
    if dia=="martes" or "jueves" or "sabado":
      print("regar a Ruby")
    else:
      print("no regar a Ruby")

#humedad
    if humedad<20:
      print("debes regar a Ruby")
    elif humedad>=20 and humedad<=22:
      print("humedad adecuada")
    elif humedad>22 and "lunes"or "miercoles"or"viernes"or"domingo":
      print("no es necesario regar a Ruby")
  
      
      
  
ruby()

    