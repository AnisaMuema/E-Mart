import { React, useEffect, useState  } from 'react';
import Product from './Product';

 const Home = () => {
  const [products, setProducts, setLoading] = useState([]);

  useEffect(() => {
    fetch('/products', {
      method: "GET",
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({
          setProducts 
      })
  })
      .then((response) => response.json())
      .then((data) => {
        console.log(data); 
        setProducts(data);
        setLoading(false);
      });
  },[setProducts, setLoading]);

  return (
    <div>
      {products.map((product) => (
        <Product key={product.id} product={product} />
      ))}
    </div>
  );

 };

 
 
 export default Home
 