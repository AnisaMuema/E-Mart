
import { Routes, Route } from 'react-router-dom'
import './App.css';
import Home from './components/Home';
import Login from './components/Login';
import Register from './components/Register';
import Navbar from './components/Navbar';

function App() {
  return (
    <div>
      <Navbar/>
      <Routes>
        <Route exact path='/' element= {<Home />} />
        <Route  path='/login' element={<Login/>} />
        <Route  path='/register' element={<Register/>} />
      </Routes>
        
    </div>
  );
}

export default App;
