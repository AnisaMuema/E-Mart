import React from 'react'
import { NavLink } from 'react-router-dom'
import { ShoppingCart } from 'phosphor-react'

const Navbar = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <div className="container-fluid">
        <NavLink className="navbar-brand" to="#">
            <b>E-MART</b>
        </NavLink>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>

        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav ml-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <NavLink className="nav-link active" aria-current="page" to="/">HOME</NavLink>
            </li>

            <li className="nav-item">
              <NavLink className="nav-link active" aria-current="page" to="/cart">
                 <ShoppingCart size={32}/> 
              </NavLink>
            </li>

            <li className="nav-item">
              <NavLink className="nav-link" to="/login">LOGIN</NavLink>
            </li>
            
            <li className="nav-item">
              <NavLink className="nav-link" to="/register">REGISTER</NavLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  )
}

export default Navbar