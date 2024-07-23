import React from 'react';
import { Link } from 'react-router-dom';
import logo from '../assets/logo1.png';
function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-logo">
      <img src={logo} alt="Logo" />
        <h1>Agrobee</h1>
      </div>
      <div className="navbar-links">
        <Link to="/">Home</Link>
        <Link to="/shop">Crop Prediction</Link>
        <Link to="/community">Irrigation Monitoring</Link>
        <Link to="/orders">Data Analytics</Link>
        <Link to="/report">Support</Link>
        <Link to="/settings">Settings</Link>
      </div>
    </nav>
  );
}

export default Navbar;
