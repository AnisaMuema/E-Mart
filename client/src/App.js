
import { Routes, Route } from 'react-router-dom'
import './App.css';
import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';
import Navbar from './components/Navbar';
import Cart from './pages/Cart'
import { ProductContextProvider } from './context/product-context';


function App() {

  return (
    <div>
      <ProductContextProvider>
        <Navbar/>
        <Routes>
          <Route exact path='/' element= {<Home />} />
          <Route  path='/login' element={<Login/>} />
          <Route  path='/register' element={<Register/>} />
          <Route  path='/cart' element={<Cart/>} />
        </Routes>
     </ProductContextProvider>
        
    </div>
  );
}

export default App;
