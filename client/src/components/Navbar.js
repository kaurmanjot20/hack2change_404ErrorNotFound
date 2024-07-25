import React from 'react';
import { NavLink } from 'react-router-dom';
import logo from '../assets/logo1.png';

function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-logo">
        
        <h1>AgroSphere</h1>
      </div>
      <div className="navbar-links">
        <NavLink exact to="/" activeClassName="active-link">Home</NavLink>
        <NavLink to="/crops" activeClassName="active-link">Crop Prediction</NavLink>
        <NavLink to="/irrigation" activeClassName="active-link">Irrigation Monitoring</NavLink>
        <NavLink to="/data" activeClassName="active-link">Data Analytics</NavLink>
        <NavLink to="/support" activeClassName="active-link">Support</NavLink>
        <NavLink to="/settings" activeClassName="active-link">Settings</NavLink>
      </div>
    </nav>
  );
}

export default Navbar;
