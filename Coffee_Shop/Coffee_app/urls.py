from django.urls import path, include
from .views import *
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # --------------------------------------- PÁGINAS GENERALES ---------------------------------------------
    path('', home, name="home"),
    path('info/', info, name="info"),
    path('sobre_mi/', sobre_mi, name="sobre_mi"),

# --------------------------------------- AGREGAR Y ELIMINAR ITEMS AL CARRITO ---------------------------------------------
    path('cart/', cart, name="cart"),
    path('agregar_al_carrito/bebida/<int:id_bebida>/', agregar_bebida_al_carrito, name='agregar_bebida_al_carrito'),
    path('eliminar_del_carrito/bebida/<int:id_bebida>/', eliminar_bebida_del_carrito, name='eliminar_bebida_del_carrito'),
    path('agregar_al_carrito/postre/<int:id_postre>/', agregar_postre_al_carrito, name='agregar_postre_al_carrito'),
    path('eliminar_del_carrito/postre/<int:id_postre>/', eliminar_postre_del_carrito, name='eliminar_postre_del_carrito'),
    path('agregar_al_carrito/merch/<int:id_merch>/', agregar_merch_al_carrito, name='agregar_merch_al_carrito'),
    path('eliminar_del_carrito/merch/<int:id_merch>/', eliminar_merch_del_carrito, name='eliminar_merch_del_carrito'),
    path('confirmar_compra/', confirmar_compra, name="confirmar_compra"),
    
# --------------------------------------- MERCH ---------------------------------------------
    path('merch/', MerchView.as_view(), name="merch"),
    path('crear_producto/', CrearMercancia.as_view(), name="crear_producto"),
    path('buscar3/', buscar3, name="buscar3"),
    path('buscar_articulos/', buscar_articulos, name="buscar_articulos"),
    path('editar_producto/<int:pk>/', EditarProducto.as_view(), name="editar_producto"),
    path('borrar_producto/<int:pk>/', BorrarProducto.as_view(), name="borrar_producto"),

# --------------------------------------- RESEÑAS DE ASOCIADOS ---------------------------------------------
    path('luna_asociados/', Asociados.as_view(), name="luna_asociados"),
    path('asociados/', CalificarAsociado.as_view(), name="asociados"),
    path('editar_asociados/<int:pk>/', EditarAsociado.as_view(), name="editar_asociados"),
    path('eliminar_opinion/<int:pk>/', BorrarOpinion.as_view(), name="eliminar_opinion"),
    
# --------------------------------------- BEBIDAS ---------------------------------------------
    path('bebidas/', Bebidas.as_view(), name="bebidas"),
    path('crear_bebida/', CrearBebida.as_view(), name="crear_bebida"),
    path('buscar/', buscar, name="buscar"),
    path('buscar_bebidas/', buscar_bebidas, name="buscar_bebidas"),
    path('editar_bebida/<int:pk>/', EditarBebida.as_view(), name="editar_bebida"),
    path('borrar_bebida/<int:pk>/', BorrarBebida.as_view(), name="borrar_bebida"),
    
# --------------------------------------- CREACIÓN, EDICIÓN, CUENTA DE USER ---------------------------------------------
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="app/logout.html"), name="logout"),
    path('logout_confirm/', logout_confirm, name="logout_confirm"),
    path('registrarse/', register, name="registrarse"),
    path('perfil/', perfil, name="perfil"),
    path('editar_perfil/', editar_perfil, name="editar_perfil"),
    path('subir_avatar/', subir_avatar, name="subir_avatar"),
    
# --------------------------------------- CUENTA DE CLIENTE FRECUENTE ---------------------------------------------
    path('registro/', CrearCuenta.as_view(), name="registro"),
    path('editar_cuenta/<int:pk>/', EditarCuenta.as_view(), name='editar_cuenta'),
    path('borrar_cuenta/<int:pk>/', BorrarCuenta.as_view(), name='borrar_cuenta'),
    path('centro_de_cuentas/', Cuentas.as_view(), name="centro_de_cuentas"),
    path('buscar_cuentas/', buscar_cuentas, name="buscar_cuentas"),
    path('buscar_mi_cuenta/', buscar_mi_cuenta, name="buscar_mi_cuenta"),
    
# --------------------------------------- POSTRES ---------------------------------------------
    path('postres/', Postres.as_view(), name="postres"),    
    path('crear_postre/', CrearPostre.as_view(), name="crear_postre"),
    path('buscar2/', buscar2, name="buscar2"),
    path('buscar_postres/', buscar_postres, name="buscar_postres"),
    path('editar_postre/<int:pk>/', EditarPostre.as_view(), name="editar_postre"),    
    path('borrar_postre/<int:pk>/', BorrarPostre.as_view(), name="borrar_postre"),

]