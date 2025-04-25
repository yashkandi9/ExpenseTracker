import React, { useState } from 'react';

const Dashboard = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const handleLoginLogout = () => {
    setIsLoggedIn(!isLoggedIn);
  };

  return (
    <div className="dashboard">
        
        <div className='landing'>
           
            <h1>Personal Finance Dashboard</h1>
            <img src="/dash.png" alt="Dashboard"/>
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
                <button>Go to Expense Tracker</button>
              </div>
              <div className="option">
                <h2>Currency Converter</h2>
                <button>Go to Currency Converter</button>
              </div>
              <div className="option">
                <h2>Stock Analyzer</h2>
                <button>Go to Stock Analyzer</button>
              </div>
              <div className="option">
                <h2>Quizify</h2>
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
