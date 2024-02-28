/*!
* Start Bootstrap - Shop Homepage v5.0.6 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project



    // Función para añadir un producto al carrito
    function addToCart(productName, productPrice) {
        // Obtener el carrito del almacenamiento local (si existe)
        let cart = JSON.parse(localStorage.getItem('cart')) || [];

        // Añadir el producto al carrito
        cart.push({ name: productName, price: productPrice });

        // Guardar el carrito actualizado en el almacenamiento local
        localStorage.setItem('cart', JSON.stringify(cart));

        // Redirigir a la página del carrito
        window.location.href = '/cart'; // Cambia '/cart' por la URL de tu página del carrito
    }

