import { createContext, useState } from "react";
import Product from '../pages/Product';

export const ProductContext = createContext(null);

const getDefaultCart = () => {
    let cart = {};
    for (let i = 1; i < Product.length + 1; i++) {
      cart[i] = 0;
    }
    return cart;
  };

export const ProductContextProvider = (props) => {
      const [ cartItems, setCartItems] = useState(getDefaultCart());

      const addToCart = (itemId) => {
        setCartItems((prev) => ({ ...prev, [itemId]: prev[itemId] + 1 }));
      };
    
      const removeFromCart = (itemId) => {
        setCartItems((prev) => {
           const updatedCart = { ...prev };
           if (prev[itemId] > 0) {
             updatedCart[itemId] = prev[itemId] - 1;
           }
           return updatedCart;
        });
       };

      

      const contextValue = {
        cartItems,
        addToCart,
        // updateCartItemCount,
        removeFromCart,
        // getTotalCartAmount,
        // checkout,
      };

      
  
  return (
    <ProductContext.Provider value={contextValue}>
      {props.children}
    </ProductContext.Provider>
  )
}
