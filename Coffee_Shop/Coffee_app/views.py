from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

# coffee-admin, nishelcortez@gmail.com, coffee_shop123
# MyAdmin, admin@gmail.com, lunacafeteria123
# Create your views here.
# ------------------------------------------------------------------------------------

def home(request):
    return render(request, "app/home.html")

def info(request):
    return render(request, 'app/info.html')

def sobre_mi(request):
    return render(request, "app/sobre_mi.html")


# --------------------------------------- BEBIDAS ---------------------------------------------
class Bebidas(ListView):
    model = Bebida
    template_name = 'app/bebidas.html'
    context_object_name = 'bebidas'
class CrearBebida(LoginRequiredMixin, CreateView):
    model = Bebida
    fields = ['nombre', 'descripcion', 'precio']
    template_name = 'app/bebida_form.html' 
    success_url = reverse_lazy('bebidas')

def buscar(request):
    return render(request, "app/buscar.html")

def buscar_bebidas(request):
    if request.GET['buscar']:
        patron = request.GET["buscar"]
        bebidas = Bebida.objects.filter(nombre__icontains=patron)
        contexto = {
            "bebidas": bebidas,
        }
        return render(request, "app/bebidas.html", contexto)
    return HttpResponse("No hay resultados")

class EditarBebida(LoginRequiredMixin, UpdateView):
    model = Bebida
    fields = ['nombre', 'descripcion', 'precio']
    template_name = 'app/bebida_form.html' 
    success_url = reverse_lazy('bebidas')

class BorrarBebida(LoginRequiredMixin, DeleteView):
    model = Bebida
    template_name = 'app/bebida_delete.html'
    success_url = reverse_lazy('bebidas')

# --------------------------------------- POSTRES ---------------------------------------------
class Postres(LoginRequiredMixin, ListView):
    model = Postre
    template_name = 'app/postres.html'
    context_object_name = 'postres'
class CrearPostre(LoginRequiredMixin, CreateView):
    model = Postre
    fields = ['nombre', 'descripcion', 'precio']
    template_name = 'app/crear_postre.html' 
    success_url = reverse_lazy('postres')

def buscar2(request):
    return render(request, "app/buscar2.html")

def buscar_postres(request):
    if request.GET['buscar']:
        patron = request.GET["buscar"]
        postres = Postre.objects.filter(nombre__icontains=patron)
        contexto = {

            "postres": postres,

        }
        return render(request, "app/postres.html", contexto)
    return HttpResponse("No hay resultados")

class EditarPostre(LoginRequiredMixin, UpdateView):
    model = Postre
    fields = ['nombre', 'descripcion', 'precio']
    template_name = 'app/crear_postre.html' 
    success_url = reverse_lazy('postres')

class BorrarPostre(LoginRequiredMixin, DeleteView):
    model = Postre
    template_name = 'app/postre_delete.html'
    success_url = reverse_lazy('postres')
# --------------------------------------- MERCHANDISING ---------------------------------------------
class MerchView(LoginRequiredMixin, ListView):
     model = Merch
     template_name = 'app/merch.html'
     context_object_name = 'merch'
class CrearMercancia(LoginRequiredMixin, CreateView):
    model = Merch
    fields = ['nombre', 'descripcion', 'precio']
    template_name = 'app/crear_producto.html' 
    success_url = reverse_lazy('merch')

def buscar3(request):
    return render(request, "app/buscar3.html")

def buscar_articulos(request):
    if request.GET['buscar']:
        patron = request.GET["buscar"]
        merch = Merch.objects.filter(nombre__icontains=patron)
        contexto = {
            "merch": merch,
        }
        return render(request, "app/merch.html", contexto)
    return HttpResponse("No hay resultados")   

class EditarProducto(LoginRequiredMixin, UpdateView):
    model = Merch
    fields = ['nombre', 'descripcion', 'precio']
    template_name = 'app/crear_producto.html' 
    success_url = reverse_lazy('merch')

class BorrarProducto(LoginRequiredMixin, DeleteView):
    model = Merch
    template_name = 'app/producto_delete.html'
    success_url = reverse_lazy('merch')

# --------------------------------------- ASOCIADOS ---------------------------------------------
class Asociados(LoginRequiredMixin, ListView):
    model = Asociado
    template_name = 'app/luna_asociados.html'
    context_object_name = 'asociados'
class CalificarAsociado(LoginRequiredMixin, CreateView):
    model = Asociado
    fields = ['nombre', 'puesto', 'calificacion']
    template_name = 'app/asociados.html' 
    success_url = reverse_lazy('luna_asociados')
class EditarAsociado(LoginRequiredMixin, UpdateView):
    model = Asociado
    fields = ['nombre', 'puesto', 'calificacion']
    template_name = 'app/asociados.html' 
    success_url = reverse_lazy('luna_asociados')
class BorrarOpinion(LoginRequiredMixin, DeleteView):
    model = Asociado
    template_name = 'app/eliminar_opinion.html'
    success_url = reverse_lazy('luna_asociados')

    
# --------------------------------------- CUENTAS DE CLIENTES FRECUENTES ---------------------------------------------
class Cuentas(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'app/centro_de_cuentas'
class CrearCuenta(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ['nombre', 'email', 'telefono']
    template_name = 'app/registro.html' 
    success_url = reverse_lazy('home')
class EditarCuenta(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ['nombre', 'email', 'telefono']
    template_name = 'app/registro.html' 
    success_url = reverse_lazy('home')    
class BorrarCuenta(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'app/eliminar_cuenta.html'
    success_url = reverse_lazy('info')
    
def buscar_cuentas(request):
    return render(request, "app/buscar_cuentas.html")

def buscar_mi_cuenta(request):
    if request.GET['buscar']:
        patron = request.GET["buscar"]
        clientes = Cliente.objects.filter(email__icontains=patron)
        contexto = {
            "clientes": clientes,
        }
        return render(request, "app/centro_de_cuentas.html", contexto)
    return HttpResponse("No hay resultados")

# --------------------------------------- CUENTA DE USUARIO A LA PÁGINA ---------------------------------------------

def login_request(request):
     if request.method == 'POST':
        usuario = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=usuario, password=password)
        if user is not None:
            login(request, user)
            
            
            try:
                avatar = Avatar.objects.get(user=request.user.id).foto.url
            except:
                avatar = "/media/avatares/logo.jpg"
            finally:
                request.session["avatar"] = avatar
                
            
            return render(request, 'app/home.html')
        else:
            return redirect(reverse_lazy('login'))
        
     user_form = AuthenticationForm()

     return render(request, 'app/login.html', {'form': user_form})

def register(request):
    if request.method == 'POST':
         register_form =  RegistroForm(request.POST)
         if register_form.is_valid():
             usuario = register_form.cleaned_data.get("username")
             register_form.save()
             return redirect(reverse_lazy('home'))
    else:
        register_form = RegistroForm()
        
    return render(request, 'app/registrarse.html', {'form': register_form})

def logout_confirm(request):
    return render(request, "app/logout_confirm.html")

# --------------------------------------- AGREGAR ITEMS AL CARRITO ---------------------------------------------

def agregar_bebida_al_carrito(request, id_bebida):
    # Obtener la bebida correspondiente al ID proporcionado
    bebida = get_object_or_404(Bebida, id=id_bebida)
    # Obtener el usuario que está realizando la solicitud
    usuario = request.user
    # Obtener el carrito de compras del usuario actual, o crear uno nuevo si no existe
    carrito, creado = Carrito.objects.get_or_create(usuario=usuario)

    # Intentar obtener la entrada de la bebida en el carrito, o crear una nueva si no existe
    bebida_en_carrito, creado = BebidaEnCarrito.objects.get_or_create(
        carrito=carrito, bebida=bebida,
        defaults={'precio_actual': bebida.precio, 'cantidad': 1}
    )
    # Si la bebida ya estaba en el carrito, incrementar la cantidad y actualizar el precio total
    if not creado:
        bebida_en_carrito.cantidad += 1
        bebida_en_carrito.precio_actual = bebida_en_carrito.cantidad * bebida.precio
        bebida_en_carrito.save()

    return redirect(request.META.get('HTTP_REFERER', 'home'))

def agregar_postre_al_carrito(request, id_postre):
    postre = get_object_or_404(Postre, id=id_postre)
    usuario = request.user
    carrito, creado = Carrito.objects.get_or_create(usuario=usuario)

    postre_en_carrito, creado = PostreEnCarrito.objects.get_or_create(
        carrito=carrito, postre=postre,
        defaults={'precio_actual': postre.precio, 'cantidad': 1}
    )
    
    if not creado:
        postre_en_carrito.cantidad += 1
        postre_en_carrito.precio_actual = postre_en_carrito.cantidad * postre.precio
        postre_en_carrito.save()

    return redirect(request.META.get('HTTP_REFERER', 'home'))

def agregar_merch_al_carrito(request, id_merch):
    merch = get_object_or_404(Merch, id=id_merch)
    usuario = request.user
    carrito, creado = Carrito.objects.get_or_create(usuario=usuario)

    merch_en_carrito, creado = MerchEnCarrito.objects.get_or_create(
        carrito=carrito, merch=merch,
        defaults={'precio_actual': merch.precio, 'cantidad': 1}
    )
    
    if not creado:
        merch_en_carrito.cantidad += 1
        merch_en_carrito.precio_actual = merch_en_carrito.cantidad * merch.precio
        merch_en_carrito.save()

    return redirect(request.META.get('HTTP_REFERER', 'home'))

# --------------------------------------- ELIMINAR ITEMS DEL CARRITO ---------------------------------------------

def eliminar_postre_del_carrito(request, id_postre):
    usuario = request.user
    carrito = get_object_or_404(Carrito, usuario=usuario)

    # Buscar la entrada de la bebida en el carrito
    postre_en_carrito = get_object_or_404(PostreEnCarrito, carrito=carrito, postre_id=id_postre)
    
    # Si la cantidad es mayor que 1, simplemente decrementa la cantidad
    if postre_en_carrito.cantidad > 1:
        postre_en_carrito.cantidad -= 1
        postre_en_carrito.precio_actual = postre_en_carrito.cantidad * postre_en_carrito.postre.precio
        postre_en_carrito.save()
    else:
        # Si la cantidad es 1, elimina la entrada del carrito
        postre_en_carrito.delete()
        
    return redirect(reverse_lazy('cart'))

def eliminar_bebida_del_carrito(request, id_bebida):
    usuario = request.user
    carrito = get_object_or_404(Carrito, usuario=usuario)

    bebida_en_carrito = get_object_or_404(BebidaEnCarrito, carrito=carrito, bebida_id=id_bebida)
    
    if bebida_en_carrito.cantidad > 1:
        bebida_en_carrito.cantidad -= 1
        bebida_en_carrito.precio_actual = bebida_en_carrito.cantidad * bebida_en_carrito.bebida.precio
        bebida_en_carrito.save()
    else:

        bebida_en_carrito.delete()
        
    return redirect(reverse_lazy('cart'))


def eliminar_merch_del_carrito(request, id_merch):
    usuario = request.user
    carrito = get_object_or_404(Carrito, usuario=usuario)

    merch_en_carrito = get_object_or_404(MerchEnCarrito, carrito=carrito, merch_id=id_merch)
    
    if merch_en_carrito.cantidad > 1:
        merch_en_carrito.cantidad -= 1
        merch_en_carrito.precio_actual = merch_en_carrito.cantidad * merch_en_carrito.merch.precio
        merch_en_carrito.save()
    else:
        merch_en_carrito.delete()
        
    return redirect(reverse_lazy('cart'))

# --------------------------------------- CARRITO ---------------------------------------------

def cart(request):
    usuario = request.user
    carrito = Carrito.objects.get(usuario=usuario)
    bebidas_en_carrito = carrito.bebidaencarrito_set.all()
    postres_en_carrito = carrito.postreencarrito_set.all()
    merch_en_carrito = carrito.merchencarrito_set.all()
    
    total_bebidas = bebidas_en_carrito.aggregate(Sum('precio_actual'))['precio_actual__sum'] or 0
    total_postres = postres_en_carrito.aggregate(Sum('precio_actual'))['precio_actual__sum'] or 0
    total_merch = merch_en_carrito.aggregate(Sum('precio_actual'))['precio_actual__sum'] or 0
    
    total_compra = round(total_bebidas + total_postres + total_merch, 2)

    
    return render(request, 'app/cart.html', {'bebidas_en_carrito': bebidas_en_carrito, 
                                              'postres_en_carrito': postres_en_carrito, 
                                              'merch_en_carrito': merch_en_carrito,
                                              'total_compra': total_compra})

def confirmar_compra(request):
    usuario = request.user
    carrito = Carrito.objects.get(usuario=usuario)
    
    carrito.bebidaencarrito_set.all().delete()
    carrito.postreencarrito_set.all().delete()
    carrito.merchencarrito_set.all().delete()
    
    return render(request, "app/confirmar_compra.html")

# --------------------------------------- PERFIL ---------------------------------------------

def perfil(request):
    return render(request, "app/perfil.html")

def editar_perfil(request):
    usuario = request.user

    if request.method == "POST":
        form = UserEditForm(request.POST, instance=usuario)
        if form.is_valid():
            informacion = form.cleaned_data
            user = form.save(commit=False)
            user.set_password(informacion['password1'])
            user.save()

            # Autenticar al usuario con la nueva contraseña para mantener la sesión activa
            usuario_actualizado = authenticate(username=usuario.username, password=informacion['password1'])
            if usuario_actualizado is not None:
                login(request, usuario_actualizado)

            return redirect('perfil')
    else:    
        form = UserEditForm(instance=usuario)

    return render(request, "app/editar_perfil.html", {"form": form})

def subir_avatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = User.objects.get(username=request.user)
        # BORRAR AVATAR ANTERIOR 
            avatar_antiguo = Avatar.objects.filter(user=usuario)
            if len(avatar_antiguo) > 0:
                for n in range(len(avatar_antiguo)):
                    avatar_antiguo[n].delete()
        
        avatar = Avatar(user=usuario, foto=form.cleaned_data['foto'])
        avatar.save()
        
        foto = Avatar.objects.get(user=request.user.id).foto.url
        request.session["avatar"] = foto
        return render(request, "app/home.html")
    
    else:
        form = AvatarForm()
        
    return render(request, "app/subir_avatar.html", {"form": form})
