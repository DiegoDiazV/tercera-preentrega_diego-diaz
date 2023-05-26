from django.shortcuts import redirect
from django.shortcuts import render
from TerceraPreentregaApp.forms import ClienteForm, ProductoForm, CategoriaForm, BusquedaForm
from TerceraPreentregaApp.models import Cliente, Producto, Categoria

# Create your views here.
def home(request):
    clientes = Cliente.objects.all()
    nClientes = Cliente.objects.count()
    productos = Producto.objects.all()
    nProductos = Producto.objects.count()
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        print(form)
        if form.is_valid:
            data = form.cleaned_data
            clientes = Cliente.objects.filter(nombre=data["search_text"])
            productos = Producto.objects.filter(nombre=data["search_text"])
            form = BusquedaForm()
    else:
        form = BusquedaForm()
        
    return render(request, "home.html", {"form": form, "clientes": clientes, "nClientes":nClientes, "productos": productos, "nProductos": nProductos})

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

def productos(request):
    productos = Producto.objects.all()
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        print(form)
        if form.is_valid:
            data = form.cleaned_data
            producto = Producto(nombre = data["nombre"], precio = data["precio"], categoria = data["categoria"])
            producto.save()
            form = ProductoForm()
            return redirect(request.path)
        
    else:
        form = ProductoForm()
    
    return render(request, "productos.html", {"form":form, "productos":productos})

def categorias(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        print(form)
        if form.is_valid:
            data = form.cleaned_data
            categoria = Categoria(nombre = data["nombre"])
            categoria.save()
            form = CategoriaForm()
            return redirect(request.path)
        
    else:
        form = CategoriaForm()
    
    return render(request, "categorias.html", {"form":form, "categorias":categorias})
 