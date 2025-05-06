import React from "react";
import ExpenseChart from "../components/ExpenseChart";
import TotalSpending from "../components/TotalSpending";
import RecentExpenses from "../components/RecentExpense";
import AddExpenseButton from "../components/AddExpenseButton";
import styles from "../styles/ExpenseManager.module.css";
import BackButton from "../components/backbutton";

const ExpenseManager = () => {
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
              <div>
                <h2 className={styles.totalSpendingTitle}>Total Spending</h2>
                <TotalSpending />
              </div>
              <AddExpenseButton />
            </div>

            <div>
              <h2 className={styles.sectionTitle}>Recent Expenses</h2>
              <RecentExpenses />
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default ExpenseManager;

// import React from "react";
// import ExpenseChart from "../components/ExpenseChart";
// import TotalSpending from "../components/TotalSpending";
// import RecentExpenses from "../components/RecentExpense";
// import AddExpenseButton from "../components/AddExpenseButton";
// // import RecentExpenses from "../components/RecentExpenses";
// // import AddExpenseButton from "../components/AddExpenseButton";
// import styles from "../styles/ExpenseManager.module.css";

// const ExpenseManager = () => {
//   return (
//     <div className={styles.container}>
//       <h1 className={styles.title}>Expense Tracker</h1>

//       <div className={styles.mainGrid}>
//         <div className={styles.leftPanel}>
//           <h2 className={styles.sectionTitle}>Expense Categories</h2>
//           <ExpenseChart />
//         </div>

//         <div className={styles.rightPanel}>
//           <div className={styles.leftPanel}>
//             <div className={styles.totalSpending}>
//               <div>
//                 <h2 className={styles.totalSpendingTitle}>Total Spending</h2>
//                 <p className={styles.totalAmount}>₹25,400</p>
//               </div>
//               <AddExpenseButton/>
//             </div>
//           </div>

//           <div className={styles.leftPanel}>
//             <h2 className={styles.sectionTitle}>Recent Expenses</h2>
//             <RecentExpenses />
//           </div>
//         </div>
//       </div>
//     </div>
//   );
// };

// export default ExpenseManager;
