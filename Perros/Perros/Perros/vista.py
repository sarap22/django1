from django.http import HttpResponse
def Costo(request,op,raza):    
    """ op=int(input("Seleccione la opcion que corresponda:\n 1.Primer Puesto.\n2. Segundo Puesto.\n3. Tercer Puesto."))  
    raza=int(input("Seleccione la opcion que corresponda a la Raza de Animal que desea Comprar:\n 1.Pitbull.\n 2.Buly.\n 3.Rottwhiler.\n4.Labrador Retriever.\n 5.Golden Retriever.\n 6.Doberman.\n 7.Dogo Argentino.")) """
    if raza==1:
     precio=6000000
     if op==1:
      valor=precio*2
      msj=("El precio Original para la Compra del perro es de $",precio,". Pero por estar en el puesto",op,", su Precio original es Duplicado, asi que su Valor es de $",valor)
     elif op==2:
      incremento=800000
      valor=precio+incremento
      msj=("El Precio Original para la Compra del perro es de $",precio,". Pero por estar en el puesto",op,", su Precio original es Duplicado, asi que su Valor es de $",valor)
     elif op==3:
      incremento=200000
      valor=precio+incremento
      msj=("El Precio Original para la Compra del perro es de $",precio,". Pero por estar en el puesto",op,", su Precio original es Duplicado, asi que su Valor es de $",valor)
    elif raza==2:
     precio=6500000
     if op==1:
      valor=precio*2
      msj=("El Precio Original para la Compra del perro es de $",precio,". Pero por estar en el puesto",op,", su Precio original es Duplicado, asi que su Valor es de $",valor)
     elif op==2:
      incremento=800000
      valor=precio+incremento
      msj=("El Precio Original para la Compra del perro es de $",precio,". Pero con el Puesto obtenido, se Realiza un Incremento de $",incremento,". Por lo tanto, el Nuevo Valor  es de $",valor)
     elif op==3:
      incremento=200000
      valor=precio+incremento
      msj=("El Precio Original para la Compra del perro es de $",precio,". Pero por estar en el puesto",op,", se Realiza un Incremento de $",incremento,". Por lo tanto, el Nuevo Valor  es de $",valor)
    elif raza==3:
     precio=4000000
     if op==1:
      valor=precio*2
      msj=("El Precio Original para la Compra del perro es de $",precio,". Pero por estar en el puesto",op,", su Precio original es Duplicado, asi que su Valor es de $",valor)
     elif op==2:
      incremento=800000
      valor=precio+incremento
      msj=("El Precio Original para la Compra del perro es de $",precio,". Pero por estar en el puesto",op,", se Realiza un Incremento de $",incremento,". Por lo tanto, el Nuevo Valor  es de $",valor)
     elif op==3:
      incremento=200000
      valor=precio+incremento
      msj=("El Precio Original para la Compra del perro es de $",precio,". Pero por estar en el puesto",op,", se Realiza un Incremento de $",incremento,". Por lo tanto, el Nuevo Valor  es de $",valor)
    elif raza==4:
     precio=3500000
     if op==1:
      valor=precio*2
      msj=("El Precio Original para la Compra del perro es de $",precio,". Pero por estar en el puesto",op,", su Precio original es Duplicado, asi que su Valor es de $",valor)
     elif op==2:
      incremento=800000
      valor=precio+incremento
      msj=("El Precio Original para la Compra del perro es de $",precio,". Pero por estar en el puesto",op,", se Realiza un Incremento de $",incremento,". Por lo tanto, el Nuevo Valor  es de $",valor)
     elif op==3:
      incremento=200000
      valor=precio+incremento
      msj=("El Precio Original para la Compra del perro es de $",precio,". Pero por estar en el puesto",op,",se Realiza un Incremento de $",incremento,". Por lo tanto, el Nuevo Valor  es de $",valor)
    elif raza==5:
     precio=3500000
     if op==1:
      valor=precio*2
      msj=("El Precio Original para la Compra del perro es de $",precio,". Pero por estar en el puesto",op,", su Precio original es Duplicado, asi que su Valor es de $",valor)
     elif op==2:
      incremento=800000
      valor=precio+incremento
      msj=("El Precio Original para la Compra del perro es de $",precio,". Pero por estar en el puesto",op,", se Realiza un Incremento de $",incremento,". Por lo tanto, el Nuevo Valor  es de $",valor)
     elif op==3:
      incremento=200000
      valor=precio+incremento
      msj=("El Precio Original para la Compra del perro es de $",precio,". Pero por estar en el puesto",op,", se Realiza un Incremento de $",incremento,". Por lo tanto, el Nuevo Valor  es de $",valor)
    elif raza==6:
     precio=5000000
     if op==1:
      valor=precio*2
      msj=("El Precio Original para la Compra del perro es de $",precio,". Pero por estar en el puesto",op,", su Precio original es Duplicado, asi que su Valor es de $",valor)
     elif op==2:
      incremento=800000
      valor=precio+incremento
      msj=("El Precio Original para la Compra del perro es de $",precio,". Pero por estar en el puesto",op,", se Realiza un Incremento de $",incremento,". Por lo tanto, el Nuevo Valor  es de $",valor)
     elif op==3:
      incremento=200000
      valor=precio+incremento
      msj=("El Precio Original para la Compra del perro es de $",precio,". Pero por estar en el puesto",op,", se Realiza un Incremento de $",incremento,". Por lo tanto, el Nuevo Valor  es de $",valor)
    elif raza==7:
     precio=5500000
     if op==1:
      valor=precio*2
      msj=("El Precio Original para la Compra del perro es de $",precio,". Pero por estar en el puesto",op,", su Precio original es Duplicado, asi que su Valor es de $",valor)
     elif op==2:
      incremento=800000
      valor=precio+incremento
      msj=("El Precio Original para la Compra del perro es de $",precio,". Pero por estar en el puesto",op,", su Precio original es Duplicado, asi que su Valor es de $",valor)
     elif op==3:
      incremento=200000
      valor=precio+incremento
      msj=("El Precio Original para la Compra del perro es de $",precio,". Pero por estar en el puesto",op,", se Realiza un Incremento de $",incremento,". Por lo tanto, el Nuevo Valor  es de $",valor)
    return HttpResponse(f'<p style="background-color:#F08080; font-size:20px; font-family:courier,arial,helvética">{msj}</p>')