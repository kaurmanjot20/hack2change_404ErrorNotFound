import React from 'react';
import logo from '../assets/bgpic.jpg';
function TopBar() {
  return (
    <div className="top-bar">
      <div className="profile">
        <img src={logo} alt="Profile" className="profile-pic" />
        <span className="profile-name">Hello, [User]</span>
      </div>
    </div>
  );
}

export default TopBar;
