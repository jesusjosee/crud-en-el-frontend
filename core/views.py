from django.shortcuts import render, get_object_or_404 , redirect
from .forms import ProductForm, CustomUserCreationFrom
from django.contrib import messages

from .models import Product
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import permission_required

# Create your views here.

def home(request):
    return render(request, "core/index.html")

@permission_required('core.add_product')
def agregar_producto(request):

    data = {'form':ProductForm()}

    if request.method == 'POST':
        form = ProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto agregado correctamente')
        else:
            form = ProductForm()
    
    return render(request, 'core/products/añadir.html', data)

@permission_required('core.view_product')
def listar_producto(request):
    products = Product.objects.all()
    return render(request, 'core/products/listar.html', {'products':products})

@permission_required('core.change_product')
def modificar_producto(request, id):

    product = get_object_or_404(Product, id=id)

    data={'form': ProductForm(instance=product)}

    if request.method == 'POST':
        form = ProductForm(data=request.POST, files= request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modificado correctamente')
            return redirect(to='listar_productos')
        else:
            form

    return render(request, 'core/products/modificar.html', data)

@permission_required('core.delete_product')
def eliminar_producto(request, id):
    product= get_object_or_404(Product, id=id)
    product.delete()
    return redirect(to='listar_productos')

def registro(request):
    data= {'form' : CustomUserCreationFrom() }

    if request.method == 'POST':
        form = CustomUserCreationFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'Te has registrado correctamente')
            return redirect(to='/')
        else:
            form


    return render(request, 'registration/registro.html', data)