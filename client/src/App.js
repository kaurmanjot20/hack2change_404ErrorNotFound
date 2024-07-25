import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import TopBar from './components/TopBar';
import Home from './components/Home';
import About from './components/About';
import Contact from './components/Contact';
import CropPrediction from './components/CropPrediction';
import IrrigationMonitoring from './components/IrrigationMonitoring';
import DataAnalytics from './components/DataAnalytics';
import Support from './components/Support';
import Settings from './components/Settings';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <div className="main-content">
          <TopBar />
          <div className="content">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/about" element={<About />} />
              <Route path="/contact" element={<Contact />} />
              <Route path="/crops" element={<CropPrediction />} />
              <Route path="/irrigation" element={<IrrigationMonitoring />} />
              <Route path="/data" element={<DataAnalytics />} />
              <Route path="/support" element={<Support />} />
              <Route path="/settings" element={<Settings />} />
            </Routes>
          </div>
        </div>
      </div>
    </Router>
  );
}

export default App;
