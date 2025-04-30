import './App.css';
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Dashboard from './pages/dashboard';
import CurrencyConverter from './pages/currencyconverter';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/currency-converter" element={<CurrencyConverter />} />
      </Routes>
    </Router>
  );
}

export default App;
