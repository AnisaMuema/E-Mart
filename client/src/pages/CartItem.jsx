import React, { useContext } from "react";
import { ProductContext } from '../context/product-context'

export const CartItem = ({data}) => {

    const { cartItems, addToCart, removeFromCart, updateCartItemCount } =
      useContext(ProductContext);
  
    return (
      <div className="cartItem">
        <div className="description">
          <p>
            <b>{data.name}</b>
          </p>
          <p> Price: ${data.price}</p>
          <div className="countHandler">
            <button onClick={() => removeFromCart(data.id)}> - </button>
            <input
              value={cartItems[data.id]}
              onChange={(e) => updateCartItemCount(Number(e.target.value), data.id)}
            />
            <button onClick={() => addToCart(data.id)}> + </button>
          </div>
        </div>
      </div>
    );
  };