import React, { useState, useEffect } from 'react';
import axios from 'axios';

function ShoppingCart() {
  const [cart, setCart] = useState([]);
  const [products, setProducts] = useState([]);

  useEffect(() => {
    let cart = localStorage.getItem('cart');
    cart = cart ? JSON.parse(cart) : [];
    setCart(cart);
  }, []);

  useEffect(() => {
    axios.get('http://localhost:8080/products')
      .then(response => setProducts(response.data))
      .catch(error => console.error(error));
  }, [cart]);

  function removeFromCart(id) {
    setCart(prevCart => {
      const index = prevCart.indexOf(id);
      if (index > -1) {
        const newCart = [...prevCart];
        newCart.splice(index, 1);
        localStorage.setItem('cart', JSON.stringify(newCart));
        return newCart;
      }
      return prevCart;
    });
  }

  return (
    <div>
      <h1>Shopping Cart</h1>
      {cart.map((id, index) => {
        const product = products.find(product => product.id === id);
        return product ? (
          <div key={index}>
            <p>{product.name} - Price: {product.price}</p>
            <button onClick={() => removeFromCart(id)}>Remove</button>
          </div>
        ) : null;
      })}
    </div>
  );
}

export default ShoppingCart;
