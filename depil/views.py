from django.shortcuts import redirect, render
from django.conf import settings
from .models import *
from .forms import *
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives,EmailMessage



# Create your views here.
def home (request):
    return render(request, 'paginas/home.html') 

def servicios (request):
    profesionales = Prof.objects.all()
    return render(request, 'paginas/servicios.html',{'prof':profesionales}) 

def nosotros (request):
    return render(request, 'paginas/nosotros.html')

def pedir_hora (request):
    formulario = ContactForm (request.POST or None)
    if formulario.is_valid():
        formulario.save()
        mail = request.POST.get('email')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        fecha = request.POST.get('fecha')
        atencion = request.POST.get('id_prof')
        comentario = request.POST.get('coment')
        hora = request.POST.get('hora')
        diab = request.POST.get('diab')
        telefono = request.POST.get('telefono')
        

        email = EmailMessage('Web Depil-arte',
        "{} {} ha solicitado una atencion con id {} el dia {} en el horario de {} con los siguientes comentarios:\n\n {} \n\n Paciente diabetico: {} \n Correo: {} \n Teléfono: {}".format(nombre,apellido,atencion,fecha,hora,comentario,diab,mail,telefono),
        '',
        ['contacto.depilarte1@gmail.com'],)
        email.send()

        aviso = EmailMessage('Web Depil-arte',
        "{} {} su solicitud fue recibida satisfactoriamente, se le contactará a la brevedad para confirmar su hora".format(nombre,apellido),
        '',
        [mail],)
        aviso.send()


        return redirect('hora')
    return render(request, 'paghoras/crear.html', {'formulario': formulario} ) 



def hora (request):
    horas = Atencion.objects.all()
    return render(request, 'paghoras/index.html', {'horas': horas} )


