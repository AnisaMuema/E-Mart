import { React, useState, useEffect ,useContext  } from 'react';

import { CartItem } from '../pages/CartItem'
import { ProductContext } from '../context/product-context';


const Cart = () => {

  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch('/products')

      .then((response) => response.json())
      .then((data) => {
        console.log(data); 
        setProducts(data);
        // setLoading(false);
      });
  },[]);


  const { cartItems } = useContext(ProductContext)

  return (
    <div className='cart'>
      <div >
        <h1>Your  Cart Items</h1>
      </div>
      <div className='cart'>
      {products.map((product) => {
        if (cartItems[product.id] !== 0){
          return <CartItem data={{
            id: product.id,
            title: product.title,
            description: product.description,
            image: product.image,
            quantity: cartItems[product.id],
          }} />;
        }
          
       })}
      </div>

      {/* {totalAmount > 0 ? (
        <div className="checkout">
          <p> Subtotal: ${totalAmount} </p>
          <button onClick={() => navigate("/")}> Continue Shopping </button>
          <button
            onClick={() => {
              checkout();
              navigate("/checkout");
            }}
          >
            {" "}
            Checkout{" "}
          </button>
        </div>
      ) : (
        <h1> Your Shopping Cart is Empty</h1>
      )} */}

    </div>
  )
}

export default Cart