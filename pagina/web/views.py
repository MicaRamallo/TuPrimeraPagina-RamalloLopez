from django.shortcuts import render
#from django.template import templates
from web.models import Aro, Cinturon, Malla
from web.forms import MallaFormulario

# Create your views here.

def pagina_principal(request):
    return render(request, 'index.html')

def agregar_aro(request):

    if request.method == "POST":
        nuevo_aro = Aro(
            cod_producto_aro = (request.POST['cod_producto_aro']),
            material = (request.POST['material']),
            color = (request.POST['color']),
            precio = (request.POST['precio']),
            )
        nuevo_aro.save()
        return render(request, 'index.html')
    
    return render(request, 'agregar_aro.html')


def agregar_cinto(request):
    if request.method == "POST":
        nuevo_cinto = Cinturon (
            cod_producto_cinto = (request.POST['cod_producto_cinto']),
            largo = (request.POST['largo']),
            color = (request.POST['color']),
            precio = (request.POST['precio']),
            )
        nuevo_cinto.save()
        return render(request, 'index.html')

    return render(request, 'agregar_cinto.html')



def agregar_malla(request):
    if request.method == "POST":
        nuevo_malla = Malla (
            cod_producto_malla = (request.POST['cod_producto_malla']),
            modelo = (request.POST['modelo']),
            color = (request.POST['color']),
            talle = (request.POST['talle']),            
            precio = (request.POST['precio']),
            )
        nuevo_malla.save()
        return render(request, 'index.html')

    return render(request, 'agregar_malla.html')


#def malla_formulario(request):
#    if request.method == "POST":
#        miFormulario = MallaFormulario(request.POST)
#        print(miFormulario)
#        if miFormulario.is_valid:
#            informacion = miFormulario.cleaned_data #tomo la info que nos importa
#            nueva_malla = Malla (
#            cod_producto_malla = informacion('cod_producto_malla'),
#            modelo = informacion('modelo'),
#            color = informacion('color'),
#            talle = informacion('talle'),
#            precio = informacion ('precio'),
#            )
#            nueva_malla.save()
#            return render(request, 'index.html')
#    else:
#        miFormulario = MallaFormulario()
#
#        return render(request, 'malla_formulario.html', {'formulario':miFormulario})
#    
#    return render(request, 'malla_formulario.html')