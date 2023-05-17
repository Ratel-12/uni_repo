import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Products() {
  const [products, setProducts] = useState([]);
  
  useEffect(() => {
    axios.get('http://localhost:8080/products')
      .then(response => setProducts(response.data))
      .catch(error => console.error(error));
  }, []);

  function addToCart(id) {
    let cart = localStorage.getItem('cart');
    cart = cart ? JSON.parse(cart) : [];
    cart.push(id);
    localStorage.setItem('cart', JSON.stringify(cart));
  }

  return (
    <div>
      <h1>Products</h1>
      {products.map(product => (
        <div key={product.id}>
          <p>{product.name} - Price: {product.price}</p>
          <button onClick={() => addToCart(product.id)}>Add to Cart</button>
        </div>
      ))}
    </div>
  );
}

export default Products;
