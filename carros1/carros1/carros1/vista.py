from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context

def precioAlquiler(request, dias, vehiculo, seguro):
    """ dias=int(input("Digite el Número de días que desea alquilar el Vehículo))
    letero=("Vehículos Disponibles: BMW\n MEGANE\nMERCEDES\n TWINGO\n CHEVROLET)
    vehiculo=input("¿Qué Vehículo desea Alquilar)
    seguro=input("¿Acepta el Seguro a todo Riesgo?) """
    if seguro=='si':
     if dias<3:
      if vehiculo=='bmw':
       precio=650000
       multi=precio*dias
       seguro=multi*0.05
       total=multi+seguro
       con="El Precio por día del Alquiler es de $",precio,". Y por los días Alquilados es de $",int(multi),".\n Por haber Alquilado Únicamente",dias,", no se le hará ningún tipo de Descuento.  Y por Solicitar el Seguro a todo Riesgo, se Aumenta el Precio a un Valor de $",int(seguro),"; por lo tanto, el Total a Pagar por el Alquiler es de $",int(total)
      elif vehiculo=='megane':
       precio=120000
       multi=precio*dias
       seguro=multi*0.05
       total=multi+seguro
       con="El Precio por día del Alquiler es de ",precio,". Y por los días Alquilados es de $",int(multi),".\n Por haber Alquilado Únicamente",dias,", no se le hará ningún tipo de Descuento.  Y por Solicitar el Seguro a todo Riesgo, se Aumenta el Precio a un Valor de $",int(seguro),"; por lo tanto, el Total a Pagar por el Alquiler es de $",int(total)
      elif vehiculo=='mercedes':
       precio=700000
       multi=precio*dias
       seguro=multi*0.05
       total=multi+seguro
       con="El Precio por día del Alquiler es de ",precio,". Y por los días Alquilados es de $",int(multi),".\n Por haber Alquilado Únicamente",dias,", no se le hará ningún tipo de Descuento.  Y por Solicitar el Seguro a todo Riesgo, se Aumenta el Precio a un Valor de $",int(seguro),"; por lo tanto, el Total a Pagar por el Alquiler es de $",int(total)
      elif vehiculo=='twingo':
       precio=100000
       multi=precio*dias
       seguro=multi*0.05
       total=multi+seguro
       con="El Precio por día del Alquiler es de ",precio,". Y por los días Alquilados es de $",int(multi),".\n Por haber Alquilado Únicamente",dias,", no se le hará ningún tipo de Descuento.  Y por Solicitar el Seguro a todo Riesgo, se Aumenta el Precio a un Valor de $",int(seguro),"; por lo tanto, el Total a Pagar por el Alquiler es de $",int(total)
      elif vehiculo=='chevrolet':
       precio=150000
       multi=precio*dias
       seguro=multi*0.05
       total=multi+seguro
       con="El Precio por día del Alquiler es de ",precio,". Y por los días Alquilados es de $",int(multi),".\n Por haber Alquilado Únicamente",dias,", no se le hará ningún tipo de Descuento.  Y por Solicitar el Seguro a todo Riesgo, se Aumenta el Precio a un Valor de $",int(seguro),"; por lo tanto, el Total a Pagar por el Alquiler es de $",int(total)
      #con=(f'<p style="background-color:#F08080; font-size:20px; font-family:courier,arial,helvética">{con}</p>')
     elif dias>=3 and dias<=5:
      if vehiculo=='bmw':
        precio=650000
        multi=precio*dias
        descuento=multi*0.10
        valor=multi-descuento
        seguro=valor*0.05
        total=valor+seguro
        con="El Precio por día del Alquiler es de $",precio,".Y por los días Alquilados es de $",int(multi),".Su Descuento es de $",int(descuento),". El valor de su Alquiler con Descuento sería de $",int(valor),". Y por Solicitar el Seguro a todo Riesgo, se Aumenta el Precio un Valor de $",int(seguro),"; por lo tanto, el Total a Pagar por el Alquiler es de $",int(total)
      elif vehiculo=='megane':
        precio=120000
        multi=precio*dias
        descuento=multi*0.10
        valor=multi-descuento
        seguro=valor*0.05
        total=valor+seguro
        con="El Precio por día del Alquiler es de $",precio,".Y por los días Alquilados es de $",int(multi),".Su Descuento es de $",int(descuento),". El valor de su Alquiler con Descuento sería de $",int(valor),". Y por Solicitar el Seguro a todo Riesgo, se Aumenta el Precio un Valor de $",int(seguro),"; por lo tanto, el Total a Pagar por el Alquiler es de $",int(total)
      elif vehiculo=='mercedes':
        precio=700000
        multi=precio*dias
        descuento=multi*0.10
        valor=multi-descuento
        seguro=valor*0.05
        total=valor+seguro
        con="El Precio por día del Alquiler es de $",precio,".Y por los días Alquilados es de $",int(multi),".Su Descuento es de $",int(descuento),". El valor de su Alquiler con Descuento sería de $",int(valor),". Y por Solicitar el Seguro a todo Riesgo, se Aumenta el Precio un Valor de $",int(seguro),"; por lo tanto, el Total a Pagar por el Alquiler es de $",int(total)
      elif vehiculo=='twingo':
        precio=100000
        multi=precio*dias
        descuento=multi*0.10
        valor=multi-descuento
        seguro=valor*0.05
        total=valor+seguro
        con="El Precio por día del Alquiler es de $",precio,".Y por los días Alquilados es de $",int(multi),".Su Descuento es de $",int(descuento),". El valor de su Alquiler con Descuento sería de $",int(valor),". Y por Solicitar el Seguro a todo Riesgo, se Aumenta el Precio un Valor de $",int(seguro),"; por lo tanto, el Total a Pagar por el Alquiler es de $",int(total)
      elif vehiculo=='chevrolet':
        precio=150000
        multi=precio*dias
        descuento=multi*0.10
        valor=multi-descuento
        seguro=valor*0.05
        total=valor+seguro
        con="El Precio por día del Alquiler es de $",precio,".Y por los días Alquilados es de $",int(multi),".Su Descuento es de $",int(descuento),". El valor de su Alquiler con Descuento sería de $",int(valor),". Y por Solicitar el Seguro a todo Riesgo, se Aumenta el Precio un Valor de $",int(seguro),"; por lo tanto, el Total a Pagar por el Alquiler es de $",int(total)
     elif dias>=6 and dias<=10:
      if vehiculo=='bmw':
       precio=650000
       multi=precio*dias
       descuento=multi*0.15
       valor=multi-descuento
       seguro=valor*0.05
       total=valor+seguro
       con="El Precio por día del Alquiler es de $",precio,".Y por los días Alquilados es de $",int(multi),".Su Descuento es de $",int(descuento),". El valor de su Alquiler con Descuento sería de $",int(valor),". Y por Solicitar el Seguro a todo Riesgo, se Aumenta el Precio un Valor de $",int(seguro),"; por lo tanto, el Total a Pagar por el Alquiler es de $",int(total)
      elif vehiculo=='megane':
        precio=120000
        multi=precio*dias
        descuento=multi*0.15
        valor=multi-descuento
        seguro=valor*0.05
        total=valor+seguro
        con="El Precio por día del Alquiler es de $",precio,".Y por los días Alquilados es de $",int(multi),".Su Descuento es de $",int(descuento),". El valor de su Alquiler con Descuento sería de $",int(valor),". Y por Solicitar el Seguro a todo Riesgo, se Aumenta el Precio un Valor de $",int(seguro),"; por lo tanto, el Total a Pagar por el Alquiler es de $",int(total)
      elif vehiculo=='mercedes':
        precio=700000
        multi=precio*dias
        descuento=multi*0.15
        valor=multi-descuento
        seguro=valor*0.05
        total=valor+seguro
        con="El Precio por día del Alquiler es de $",precio,".Y por los días Alquilados es de $",int(multi),".Su Descuento es de $",int(descuento),". El valor de su Alquiler con Descuento sería de $",int(valor),". Y por Solicitar el Seguro a todo Riesgo, se Aumenta el Precio un Valor de $",int(seguro),"; por lo tanto, el Total a Pagar por el Alquiler es de $",int(total)
      elif vehiculo=='twingo':
        precio=100000
        multi=precio*dias
        descuento=multi*0.15
        valor=multi-descuento
        seguro=valor*0.05
        total=valor+seguro
        con="El Precio por día del Alquiler es de $",precio,". Y por los días Alquilados es de $",int(multi),". Su descuento es de $",int(descuento),". El valor de su Alquiler con Descuento sería de $",int(valor),". Y por Solicitar el Seguro a todo Riesgo, se Aumenta el Precio a un Valor de $",int(seguro),"; por lo tanto, el Total a Pagar por el Alquiler es de $",int(total)
      elif vehiculo=='chevrolet':
        precio=150000
        multi=precio*dias
        descuento=multi*0.15
        valor=multi-descuento
        seguro=valor*0.05
        total=valor+seguro
        con="El Precio por día del Alquiler es de $",precio,".Y por los días Alquilados es de $",int(multi),".Su Descuento es de $",int(descuento),". El valor de su Alquiler con Descuento sería de $",int(valor),". Y por Solicitar el Seguro a todo Riesgo, se Aumenta el Precio un Valor de $",int(seguro),"; por lo tanto, el Total a Pagar por el Alquiler es de $",int(total)
     elif dias>10:
      if vehiculo=='bmw':
        precio=650000
        multi=precio*dias
        descuento=multi*0.20
        valor=multi-descuento
        seguro=valor*0.05
        total=valor+seguro
        con="El Precio por día del Alquiler es de $",precio,".Y por los días Alquilados es de $",int(multi),".Su Descuento es de $",int(descuento),". El valor de su Alquiler con Descuento sería de $",int(valor),". Y por Solicitar el Seguro a todo Riesgo, se Aumenta el Precio un Valor de $",int(seguro),"; por lo tanto, el Total a Pagar por el Alquiler es de $",int(total)
      elif vehiculo=='megane':
        precio=120000
        multi=precio*dias
        descuento=multi*0.20
        valor=multi-descuento
        seguro=valor*0.05
        total=valor+seguro
        con="El Precio por día del Alquiler es de $",precio,".Y por los días Alquilados es de $",int(multi),".Su Descuento es de $",int(descuento),". El valor de su Alquiler con Descuento sería de $",int(valor),". Y por Solicitar el Seguro a todo Riesgo, se Aumenta el Precio un Valor de $",int(seguro),"; por lo tanto, el Total a Pagar por el Alquiler es de $",int(total)
      elif vehiculo=='mercedes':
        precio=700000
        multi=precio*dias
        descuento=multi*0.20
        valor=multi-descuento
        seguro=valor*0.05
        total=valor+seguro
        con="El Precio por día del Alquiler es de $",precio,".Y por los días Alquilados es de $",int(multi),".Su Descuento es de $",int(descuento),". El valor de su Alquiler con Descuento sería de $",int(valor),". Y por Solicitar el Seguro a todo Riesgo, se Aumenta el Precio un Valor de $",int(seguro),"; por lo tanto, el Total a Pagar por el Alquiler es de $",int(total)
      elif vehiculo=='twingo':
        precio=100000
        multi=precio*dias
        descuento=multi*0.20
        valor=multi-descuento
        seguro=valor*0.05
        total=valor+seguro
        con="El precio por día del Alquiler es de $",precio,".Y por los días Alquilados es de $",int(multi),".Su Descuento es de $",int(descuento),". El valor de su Alqu,ler con Dento sería de $",int(valor),". Y por Solicitar el Seguro a todo Riesgo, se Aumenta el Precio un Valor de $",int(seguro),"; por lo tanto, el Total a Pagar por el Alquiler es de $",int(total)
      elif vehiculo=='chevrolet':
       precio=150000
       multi=precio*dias
       descuento=multi*0.20
       valor=multi-descuento    
       seguro=valor*0.05
       total=valor+seguro
       con="El Precio por día del Alquiler es de $",precio,".Y por los días Alquilados es de $",int(multi),".Su Descuento es de $",int(descuento),". El valor de su Alquiler con Descuento sería de $",int(valor),". Y por Solicitar el Seguro a todo Riesgo, se Aumenta el Precio un Valor de $",int(seguro),"; por lo tanto, el Total a Pagar por el Alquiler es de $",int(total) 
    else:
     if dias<3:
      if vehiculo=='bmw':
       precio=650000
       valor= precio*dias
       con="El Precio del Alquiler por Día es de $",precio,". Y por los Días Alquilados, es de $",int(valor),". Por haber Alquilado unicamente",dias," Días, No se le Hará Ningún tipo de Descuento. Por no haber Aceptado el Seguro a todo Riesgo, no se alterara el valor del Alquiler. El Pago Total por el Alquiler es de $",int(valor)
      elif vehiculo=='megane':
       precio=120000
       valor= precio*dias
       con="El Precio del Alquiler por Día es de $",precio,". Y por los Días Alquilados, es de $",int(valor),". Por haber Alquilado unicamente",dias," Días, No se le Hará Ningún tipo de Descuento. Por no haber Aceptado el Seguro a todo Riesgo, no se alterara el valor del Alquiler. El Pago Total por el Alquiler es de $",int(valor)
      elif vehiculo=='mercedes':
        precio=700000
        valor= precio*dias
        con="El Precio del Alquiler por Día es de $",precio,". Y por los Días Alquilados, es de $",int(valor),". Por haber Alquilado unicamente",dias," Días, No se le Hará Ningún tipo de Descuento. Por no haber Aceptado el Seguro a todo Riesgo, no se alterara el valor del Alquiler. El Pago Total por el Alquiler es de $",int(valor)
      elif vehiculo=='twingo':
       precio=100000
       valor= precio*dias
       con="El Precio del Alquiler por Día es de $",precio,". Y por los Días Alquilados, es de $",int(valor),". Por haber Alquilado unicamente",dias," Días, No se le Hará Ningún tipo de Descuento. Por no haber Aceptado el Seguro a todo Riesgo, no se alterara el valor del Alquiler. El Pago Total por el Alquiler es de $",int(valor)
      elif vehiculo=='chevrolet':
        precio=150000
        valor= precio*dias
        con="El Precio del Alquiler por Día es de $",precio,". Y por los Días Alquilados, es de $",int(valor),". Por haber Alquilado unicamente",dias," Días, No se le Hará Ningún tipo de Descuento. Por no haber Aceptado el Seguro a todo Riesgo, no se alterara el valor del Alquiler. El Pago Total por el Alquiler es de $",int(valor)
     elif dias>=3 and dias<=5:
      if vehiculo=='bmw':
        precio=650000
        multi=precio*dias
        descuento=multi*0.10
        valor=multi-descuento
        con="El Precio del Alquiler por Día es de $",precio,". Y por los Días Alquilados el Precio es de $",int(multi),".Su Descuento Equivale a $",int(descuento)," Por no haber Aceptado el Seguro a todo Riesgo, no se altera el valor del Alquiler. El Pago Total por el Alquiler es de $ ",int(valor)
      elif vehiculo=='megane':
        precio=120000
        multi=precio*dias
        descuento=multi*0.10
        valor=multi-descuento
        con="El Precio del Alquiler por Día es de $",precio,". Y por los Días Alquilados el Precio es de $",int(multi),".Su Descuento Equivale a $",int(descuento)," Por no haber Aceptado el Seguro a todo Riesgo, no se altera el valor del Alquiler. El Pago Total por el Alquiler es de $ ",int(valor)
      elif vehiculo=='mercedes':
        precio=700000
        multi=precio*dias
        descuento=multi*0.10
        valor=multi-descuento
        con="El Precio del Alquiler por Día es de $",precio,". Y por los Días Alquilados el Precio es de $",int(multi),".Su Descuento Equivale a $",int(descuento)," Por no haber Aceptado el Seguro a todo Riesgo, no se altera el valor del Alquiler. El Pago Total por el Alquiler es de $ ",int(valor)
      elif vehiculo=='twingo':
        precio=100000
        multi=precio*dias
        descuento=multi*0.10
        valor=precio-descuento
        con="El Precio del Alquiler por Día es de $",precio,". Y por los Días Alquilados el Precio es de $",int(multi),".Su Descuento Equivale a $",int(descuento)," Por no haber Aceptado el Seguro a todo Riesgo, no se altera el valor del Alquiler. El Pago Total por el Alquiler es de $ ",int(valor)
      elif vehiculo=='chevrolet':
        precio=15000
        multi=precio*dias
        descuento=multi*0.10
        valor=multi-descuento
        con="El Precio del Alquiler por Día es de $",precio,". Y por los Días Alquilados el Precio es de $",int(multi),".Su Descuento Equivale a $",int(descuento)," Por no haber Aceptado el Seguro a todo Riesgo, no se altera el valor del Alquiler. El Pago Total por el Alquiler es de $ ",int(valor)
     elif dias>=6 and dias<=10:
      if vehiculo=='bmw':
         precio=650000
         multi=precio*dias
         descuento=multi*0.15
         valor=multi-descuento
         con="El Precio del Alquiler por Día es de $",precio,". Y por los Días Alquilados el Precio es de $",int(multi),".Su Descuento Equivale a $",int(descuento)," Por no haber Aceptado el Seguro a todo Riesgo, no se altera el valor del Alquiler. El Pago Total por el Alquiler es de $ ",int(valor)
      elif vehiculo=='megane':
         precio=120000
         multi=precio*dias
         descuento=multi*0.15
         valor=multi-descuento
         con="El Precio del Alquiler por Día es de $",precio,". Y por los Días Alquilados el Precio es de $",int(multi),".Su Descuento Equivale a $",int(descuento)," Por no haber Aceptado el Seguro a todo Riesgo, no se altera el valor del Alquiler. El Pago Total por el Alquiler es de $ ",int(valor)
      elif vehiculo=='mercedes':
         precio=700000
         multi=precio*dias
         descuento=multi*0.15
         valor=multi-descuento
         con="El Precio del Alquiler por Día es de $",precio,". Y por los Días Alquilados el Precio es de $",int(multi),".Su Descuento Equivale a $",int(descuento)," Por no haber Aceptado el Seguro a todo Riesgo, no se altera el valor del Alquiler. El Pago Total por el Alquiler es de $ ",int(valor)
      elif vehiculo=='twingo':
         precio=100000
         multi=precio*dias
         descuento=multi*0.15
         valor=multi-descuento
         con="El Precio del Alquiler por Día es de $",precio,". Y por los Días Alquilados el Precio es de $",int(multi),".Su Descuento Equivale a $",int(descuento)," Por no haber Aceptado el Seguro a todo Riesgo, no se altera el valor del Alquiler. El Pago Total por el Alquiler es de $ ",int(valor)
      elif vehiculo=='chevrolet':
          precio=15000
          multi=precio*dias
          descuento=multi*0.15
          valor=multi-descuento
          con="El Precio del Alquiler por Día es de $",precio,". Y por los Días Alquilados el Precio es de $",int(multi),".Su Descuento Equivale a $",int(descuento)," Por no haber Aceptado el Seguro a todo Riesgo, no se altera el valor del Alquiler. El Pago Total por el Alquiler es de $ ",int(valor)
     elif dias>10:
      if vehiculo=='bmw':
         precio=650000
         multi=precio*dias
         descuento=multi*0.20
         valor=multi-descuento
         con="El Precio del Alquiler por Día es de $",precio,". Y por los Días Alquilados el Precio es de $",int(multi),".Su Descuento Equivale a $",int(descuento)," Por no haber Aceptado el Seguro a todo Riesgo, no se altera el valor del Alquiler. El Pago Total por el Alquiler es de $ ",int(valor)
      elif vehiculo=='megane':
         precio=120000
         multi=precio*dias
         descuento=multi*0.20
         valor=multi-descuento
         con="El Precio del Alquiler por Día es de $",precio,". Y por los Días Alquilados el Precio es de $",int(multi),".Su Descuento Equivale a $",int(descuento)," Por no haber Aceptado el Seguro a todo Riesgo, no se altera el valor del Alquiler. El Pago Total por el Alquiler es de $ ",int(valor)
      elif vehiculo=='mercedes':
         precio=700000
         multi=precio*dias
         descuento=multi*0.20
         valor=multi-descuento
         con="El Precio del Alquiler por Día es de $",precio,". Y por los Días Alquilados el Precio es de $",int(multi),".Su Descuento Equivale a $",int(descuento)," Por no haber Aceptado el Seguro a todo Riesgo, no se altera el valor del Alquiler. El Pago Total por el Alquiler es de $ ",int(valor)
      elif vehiculo=='twingo':
          precio=100000
          multi=precio*dias
          descuento=multi*0.20
          valor=multi-descuento
          con="El Precio del Alquiler por Día es de $",precio,". Y por los Días Alquilados el Precio es de $",int(multi),".Su Descuento Equivale a $",int(descuento)," Por no haber Aceptado el Seguro a todo Riesgo, no se altera el valor del Alquiler. El Pago Total por el Alquiler es de $ ",int(valor)
      elif vehiculo=='chevrolet':
          precio=15000
          multi=precio*dias
          descuento=multi*0.20
          valor=multi-descuento
          con="El Precio del Alquiler por Día es de $",precio,". Y por los Días Alquilados el Precio es de $",int(multi),".Su Descuento Equivale a $",int(descuento)," Por no haber Aceptado el Seguro a todo Riesgo, no se altera el valor del Alquiler. El Pago Total por el Alquiler es de $ ",int(valor)
    dir=open("C:/Users/sarit/OneDrive/Documentos/adso5/nur/django/carros1/carros1/carros1/templates/index.html")
    tem= Template(dir.read())
    dir.close()
    con1=Context({"let":con, "dia":dias, "carro":vehiculo})
    doc=tem.render(con1) 
    return HttpResponse(doc)