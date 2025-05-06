import React from "react";
import { Pie } from "react-chartjs-2";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
import styles from "../styles/ExpenseChart.module.css";

ChartJS.register(ArcElement, Tooltip, Legend);

const ExpenseChart = () => {
  const data = {
    labels: ["Food", "Travel", "Shopping", "Other"],
    datasets: [
      {
        data: [50, 25, 15, 10],
        backgroundColor: ["#7b61ff", "#9f82ff", "#b9a3ff", "#ffd76d"],
        borderWidth: 1,
      },
    ],
  };

  return (
    <div className={styles.chartContainer}>
      <Pie data={data} />
    </div>
  );
};

export default ExpenseChart;
