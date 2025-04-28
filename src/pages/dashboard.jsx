import React, { useState } from 'react';
import Lottie from "react-lottie"
import animationData from '../assets/a.json';
import { SiConvertio } from "react-icons/si";
import { RiStockLine } from "react-icons/ri";
import { RiMoneyRupeeCircleFill } from "react-icons/ri";
import { FaLightbulb } from "react-icons/fa6";





const Dashboard = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const handleLoginLogout = () => {
    setIsLoggedIn(!isLoggedIn);
  };

  const defaultOptions = {
    loop: true,
    autoplay: true,
    animationData: animationData,
    rendererSettings: {
      preserveAspectRatio: 'xMidYMid slice'
    }
  };

  return (
    <div className="dashboard">
        
        <div className='landing'>
           
            <h1>Personal Finance Dashboard</h1>
            <div style={{ width: isLoggedIn ? "300px" : "400px" }}>
              <Lottie options={defaultOptions} />
            </div>
        </div>

      <header className="header">
        <div className="login-signup">
  
          {isLoggedIn ? (
            <button onClick={handleLoginLogout}>Logout</button>
          ) : (
            <>
              <button onClick={handleLoginLogout}>Login</button>
              <button>Sign Up</button>
            </>
          )}
        </div>
      </header>

      <main>
        {isLoggedIn ? (
          <>
            
            <div className="options">
              <div className="option">
                <h2>Expense Tracker</h2>
                <RiMoneyRupeeCircleFill size={30} color="#5b4bc4"/>
                <button>Go to Expense Tracker</button>
              </div>
              <div className="option">
                <h2>Currency Converter</h2>
                <SiConvertio size={30} color="#5b4bc4"/>
                <button>Go to Currency Converter</button>
              </div>
              <div className="option">
                <h2>Stock Analyzer</h2>
                <RiStockLine size={30} color="#5b4bc4" />
                <button>Go to Stock Analyzer</button>
              </div>
              <div className="option">
                <h2>Quizify</h2>
                <FaLightbulb size={30} color="#5b4bc4"/>
                <button>Start Quiz</button>
              </div>
            </div>
          </>
        ) : (
          <h2>Please log in to access the dashboard features.</h2>
        )}
      </main>
    </div>
  );
};

export default Dashboard;




// React Emoticons
// Clerk (login sign up page)