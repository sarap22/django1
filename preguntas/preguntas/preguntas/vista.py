from django.http import HttpResponse
def pregunta(request,colon,mexico,rock):
    """ print("Responda ÚNICAMENTE SI o NO")
    colon=input("¿Colón Descubrió América?") """
    if colon=='si':
     #mexico=input("¿La Independencia de México fue en el año 1810?")    
     if mexico=='si':
      #rock=input("¿The Doors fue un grupo de Rock Americano?")  
      if rock=='no':
       msj=("¡Felicidades, ha Ganado el Juego!")
      else:
       msj=("Incorrecto, Suerte a la Próxima")    
     else:
      msj=("Incorrecto, Suerte a la Próxima")    
    else:
      msj=("Incorrecto, Suerte a la Próxima")   
    return HttpResponse(f'<p style="background-color:#F08080; font-size:20px; font-family:courier,arial,helvética">{msj}</p>')