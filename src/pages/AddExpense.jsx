import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import styles from "../styles/AddExpense.module.css";

const AddExpense = () => {
  const navigate = useNavigate();
  const [description, setDescription] = useState("");
  const [cost, setCost] = useState("");
  const [category, setCategory] = useState("Food");

  const handleSubmit = (e) => {
    e.preventDefault();

    const newExpense = {
      description,
      cost: parseFloat(cost),
      category,
      date: new Date().toLocaleString()
    };

    console.log("New Expense Added:", newExpense);

    // TODO: Save to global state or backend later
    // For now, just navigate back
    navigate("/");
  };

  return (
    <div className={styles.container}>
      <h1>Add New Expense</h1>
      <form onSubmit={handleSubmit} className={styles.form}>
        <label>
          Item Description:
          <input
            type="text"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            required
          />
        </label>
        <label>
          Cost (₹):
          <input
            type="number"
            value={cost}
            onChange={(e) => setCost(e.target.value)}
            required
          />
        </label>
        <label>
          Category:
          <select
            value={category}
            onChange={(e) => setCategory(e.target.value)}
            required
          >
            <option value="Food">Food</option>
            <option value="Travel">Travel</option>
            <option value="Shopping">Shopping</option>
            <option value="Other">Other</option>
          </select>
        </label>
        <button type="submit">Add Expense</button>
      </form>
      <button className={styles.backButton} onClick={() => navigate("/")}>
        Cancel
      </button>
    </div>
  );
};

export default AddExpense;
