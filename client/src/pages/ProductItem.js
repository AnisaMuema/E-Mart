import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';


const ProductItem = () => {
  const { productId } = useParams();
  const [product, setProduct] = useState(null);

  useEffect(() => {
    fetch(`/products/${id}`)
      .then((response) => response.json())
      .then((data) => {
        console.log(data); 
        setProduct(data);
      });
  }, [productId]);

  if (!product) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h3>{product.name}</h3>
      <p>Description: {product.description}</p>
      <p>Quantity: {product.quantity}</p>
      <p>Price: ${product.price}</p>
      <button>Add To cart</button>
    </div>
  );
};

export default ProductItem;