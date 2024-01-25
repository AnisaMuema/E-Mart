import React, { useContext } from "react";
import { ProductContext } from '../context/product-context'

// import { NavLink } from 'react-router-dom';


const Product = (props) => {
  const { id, name, description, price} = props.data
  const { addToCart, cartItems } = useContext(ProductContext);

  const cartItemCount = cartItems[id];

  return (
  <div>
    <h3>{name}</h3>
    <p>Description: {description}</p>
    <p>Price: ${price}</p>
    <button onClick={() => addToCart(id)} >Add to cart {cartItemCount > 0 && <> ({cartItemCount})</>}</button>
  </div>
  )
};



export default Product;
