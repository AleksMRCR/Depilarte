from django.shortcuts import redirect, render
from django.conf import settings
from .models import *
from .forms import *
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives


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
        send_email(mail)
        return redirect('hora')
    return render(request, 'paghoras/crear.html', {'formulario': formulario} ) 

def hora (request):
    horas = Atencion.objects.all()
    return render(request, 'paghoras/index.html', {'horas': horas} )

def send_email(mail):
    context = {'mail':mail }
    template = get_template('aviso.html')
    content = template.render(context)
    email = EmailMultiAlternatives(
        'Un correo de prueba',
        'de depilarte',
        settings.EMAIL_HOST_USER,
        [mail],

    )
    email.attach_alternative(content, 'text/html')
    email.send()