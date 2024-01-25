import { React, useEffect, useState  } from 'react';
import Product from './Product';
import { Container, Row, Col } from 'react-bootstrap';

 const Home = () => {
  
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

  return (
    <div>
       <Container>
      <Row>
        {products.map((product) => (
          <Col md={4} key={product.id}>
            <Product data={product} />
          </Col>
        ))}
      </Row>
    </Container>
  </div>
  )
 };

 
 
 export default Home
 