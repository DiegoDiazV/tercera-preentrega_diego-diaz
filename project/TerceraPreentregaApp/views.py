from django.shortcuts import render
from TerceraPreentregaApp.forms import ClienteForm
from TerceraPreentregaApp.models import Cliente

# Create your views here.
def home(request):
    return render(request, "home.html")

def clientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        print(form)
        if form.is_valid:
            data = form.cleaned_data
            cliente = Cliente(data["nombre"], data["apellido"], data["telefono"], data["email"])
            cliente.save()
            return render(request, "clientes.html", {"form":form})
        
    else:
        form = ClienteForm()     

    return render(request, "clientes.html", {"form":form})