import React from 'react';
import { NavLink } from 'react-router-dom';


const Product = ({ product }) => {
  <div>
    <h3>{product.name}</h3>
    <p>Description: {product.description}</p>
    <p>Quantity: {product.quantity}</p>
    <p>Price: ${product.price}</p>
  </div>



  return (
    <div class="card" style="width: 18rem;">
    <div class="card-body">
    <h5 class="card-title">{product.name}</h5>
    <p class="card-text">{product.description}</p>
    <h6 class="card-subtitle mb-2 text-muted">{product.price}</h6>
    <NavLink href="/cart" class="card-link">Add to Cart</NavLink>
    
  </div>
</div>
  )
};



export default Product;
