from django.shortcuts import redirect
from django.shortcuts import render
from TerceraPreentregaApp.forms import ClienteForm
from TerceraPreentregaApp.models import Cliente

# Create your views here.
def home(request):
    return render(request, "home.html")

def clientes(request):
    clientes = Cliente.objects.all()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        print(form)
        if form.is_valid:
            data = form.cleaned_data
            cliente = Cliente(nombre = data["nombre"], apellido = data["apellido"], telefono = data["telefono"], email = data["email"])
            cliente.save()
            form = ClienteForm()    
            return redirect(request.path)
        
    else:
        form = ClienteForm()     

    return render(request, "clientes.html", {"form":form, "clientes":clientes})