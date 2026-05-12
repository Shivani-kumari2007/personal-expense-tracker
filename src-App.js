import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [expenses, setExpenses] = useState([]);
  const [form, setForm] = useState({
    date: "",
    category: "",
    amount: "",
    description: "",
  });

  const fetchExpenses = async () => {
    const res = await axios.get("http://127.0.0.1:5000/expenses");
    setExpenses(res.data);
  };

  useEffect(() => {
    fetchExpenses();
  }, []);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const addExpense = async () => {
    await axios.post("http://127.0.0.1:5000/add", form);
    fetchExpenses();
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Expense Tracker</h2>

      <input name="date" placeholder="Date" onChange={handleChange} />
      <input name="category" placeholder="Category" onChange={handleChange} />
      <input name="amount" placeholder="Amount" onChange={handleChange} />
      <input
        name="description"
        placeholder="Description"
        onChange={handleChange}
      />

      <button onClick={addExpense}>Add Expense</button>

      <h3>Expenses</h3>
      <ul>
        {expenses.map((e, i) => (
          <li key={i}>
            {e.date} - {e.category} - ₹{e.amount} - {e.description}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;

// import React, { useState, useEffect } from "react";
// import axios from "axios";

// function App() {
//   const [form, setForm] = useState({
//     date: "",
//     category: "",
//     amount: "",
//     description: ""
//   });

//   const [expenses, setExpenses] = useState([]);

//   const handleChange = (e) => {
//     setForm({ ...form, [e.target.name]: e.target.value });
//   };

//   const addExpense = async () => {
//     await axios.post("http://127.0.0.1:5000/add", form);
//     fetchExpenses();
//   };

//   const fetchExpenses = async () => {
//     const res = await axios.get("http://127.0.0.1:5000/expenses");
//     setExpenses(res.data);
//   };

//   useEffect(() => {
//     fetchExpenses();
//   }, []);

//   return (
//     <div style={{ padding: "20px" }}>
//       <h1>💰 Expense Tracker</h1>

//       <input name="date" placeholder="Date" onChange={handleChange} />
//       <input name="category" placeholder="Category" onChange={handleChange} />
//       <input name="amount" placeholder="Amount" onChange={handleChange} />
//       <input name="description" placeholder="Description" onChange={handleChange} />

//       <button onClick={addExpense}>Add Expense</button>

//       <h2>Expenses</h2>
//       <ul>
//         {expenses.map((e, i) => (
//           <li key={i}>
//             {e[1]} - {e[2]} - ₹{e[3]}
//           </li>
//         ))}
//       </ul>
//     </div>
//   );
// }

// export default App;