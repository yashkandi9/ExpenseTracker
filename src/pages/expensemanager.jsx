import React from "react";
import { useNavigate } from "react-router-dom";
import ExpenseChart from "../components/ExpenseChart";
// import TotalSpending from "../components/TotalSpending";
// import RecentExpenses from "../components/RecentExpense";
import AddExpenseButton from "../components/AddExpenseButton";
import styles from "../styles/ExpenseManager.module.css";
import BackButton from "../components/backbutton";
import DeleteExpenseButton from "../components/DeleteExpenseButton";

const ExpenseManager = () => {
  const navigate = useNavigate();

  const handleGetExpenses = () => {
    navigate("/get-expense");
  };

  const handleUpdateExpenses = () => {
    navigate("/update-expense");
  };

  return (
    <>
      <div className="back">
        <BackButton />
      </div>

      <div className={styles.container}>
        <h1 className={styles.title}>Expense Tracker</h1>

        <div className={styles.mainGrid}>
          <div className={styles.leftPanel}>
            <h2 className={styles.sectionTitle}>Expense Categories</h2>
            <ExpenseChart />
          </div>

          <div className={styles.rightPanel}>
            <div className={styles.totalSpending}>
              {/* <div>
                <h2 className={styles.totalSpendingTitle}>Total Spending</h2>
                <TotalSpending />
              </div> */}
              <AddExpenseButton />
              <button
                onClick={handleGetExpenses}
                className={`${styles.actionButton} ${styles.viewAllExpensesButton}`}
              >
                View All Expenses
              </button>
              <button
                onClick={handleUpdateExpenses}
                className={`${styles.actionButton} ${styles.updateExpenseButton}`}
              >
                Update Expenses
              </button>
              <DeleteExpenseButton />
            </div>

            {/* <div>
              <h2 className={styles.sectionTitle}>Recent Expenses</h2>
              <RecentExpenses />
            </div> */}
          </div>
        </div>
      </div>
    </>
  );
};

export default ExpenseManager;
