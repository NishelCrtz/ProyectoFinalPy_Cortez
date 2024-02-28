# ProyectoFinalPy_Cortez
Café de Luna es un proyecto de Python funcional que posibilita la creación, edición y compra de productos, así como la creación de cuenta de usuario en la misma.

# Modelos:
* Postre
* Bebida
* Merch
* Asociado
* Cliente Frecuente
* Avatar
* User
  
# Páginas Generales
* /home/: Página de inicio del sitio web.
* /info/: Página de información general sobre el café.
* /sobre_mi/: Página que presenta información sobre el desarrollador del sitio.

# Agregar y Eliminar Items al Carrito
* /cart/: Página que muestra el contenido del carrito de compras.
* /agregar_al_carrito/bebida/int:id_bebida/: Función para agregar una bebida específica al carrito.
* /eliminar_del_carrito/bebida/int:id_bebida/: Función para eliminar una bebida específica del carrito.
* /agregar_al_carrito/postre/int:id_postre/: Función para agregar un postre específico al carrito.
* /eliminar_del_carrito/postre/int:id_postre/: Función para eliminar un postre específico del carrito.
* /agregar_al_carrito/merch/int:id_merch/: Función para agregar un producto de merchandising específico al carrito.
* /eliminar_del_carrito/merch/int:id_merch/: Función para eliminar un producto de merchandising específico del carrito.
* /confirmar_compra/: Página para confirmar la compra de los artículos en el carrito.

# Merch
* /merch/: Página que muestra la lista de productos de merchandising disponibles.
* /crear_producto/: Página para crear un nuevo producto de merchandising.
* /buscar3/: Función para buscar productos de merchandising.
* /buscar_articulos/: Función para buscar artículos.
* /editar_producto/int:pk/: Página para editar un producto de merchandising existente.
* /borrar_producto/int:pk/: Función para eliminar un producto de merchandising existente.
* 
# Reseñas de Asociados
* /luna_asociados/: Página que muestra la lista de asociados de Café de Luna.
* /asociados/: Página para calificar a los asociados y dejar reseñas.
* /editar_asociados/int:pk/: Página para editar la información de un asociado existente.
* /eliminar_opinion/int:pk/: Función para eliminar una opinión de asociado existente.

# Bebidas
* /bebidas/: Página que muestra la lista de bebidas disponibles.
* /crear_bebida/: Página para crear una nueva bebida.
* /buscar/: Función para buscar bebidas.
* /buscar_bebidas/: Función para buscar bebidas.
* /editar_bebida/int:pk/: Página para editar una bebida existente.
* /borrar_bebida/int:pk/: Función para eliminar una bebida existente.

# Creación, Edición, Cuenta de Usuario
* /login/: Página de inicio de sesión para usuarios.
* /logout/: Página para cerrar sesión de usuarios.
* /logout_confirm/: Página de confirmación para cerrar sesión.
* /registrarse/: Página para que los usuarios se registren.
* /perfil/: Página que muestra el perfil del usuario.
* /editar_perfil/: Página para editar el perfil del usuario.
* /subir_avatar/: Página para que el usuario suba un avatar.

# Cuenta de Cliente Frecuente
* /registro/: Página para registrar una nueva cuenta de cliente frecuente.
* /editar_cuenta/int:pk/: Página para editar una cuenta de cliente frecuente existente.
* /borrar_cuenta/int:pk/: Función para eliminar una cuenta de cliente frecuente existente.
* /centro_de_cuentas/: Página que muestra el centro de cuentas de cliente frecuente.
* /buscar_cuentas/: Función para buscar cuentas de cliente frecuente.
* /buscar_mi_cuenta/: Función para buscar la propia cuenta de cliente frecuente.

# Postres
* /postres/: Página que muestra la lista de postres disponibles.
* /crear_postre/: Página para crear un nuevo postre.
* /buscar2/: Función para buscar postres.
* /buscar_postres/: Función para buscar postres.
* /editar_postre/int:pk/: Página para editar un postre existente.
/borrar_postre/int:pk/: Función para eliminar un postre existente.
