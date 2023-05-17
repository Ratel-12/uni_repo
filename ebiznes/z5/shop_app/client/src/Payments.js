import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Payments() {
  const [cart, setCart] = useState([]);
  const [products, setProducts] = useState([]);

  useEffect(() => {
    let cart = localStorage.getItem('cart');
    cart = cart ? JSON.parse(cart) : [];
    setCart(cart);

    axios.get('http://localhost:8080/products')
      .then(response => setProducts(response.data))
      .catch(error => console.error(error));
  }, []);

  function pay() {
    const cartProducts = cart.map(id => products.find(product => product.id === id));
    axios.post('http://localhost:8080/pay', cartProducts)
      .then(response => console.log(response.data))
      .catch(error => console.error(error));
  }

  return (
    <div>
      <h1>Payments</h1>
      <button onClick={pay}>Pay</button>
    </div>
  );
}

export default Payments;
