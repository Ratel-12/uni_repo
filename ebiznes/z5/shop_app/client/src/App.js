import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Products from "./Products";
import ShoppingCart from "./ShoppingCart";
import Payments from "./Payments";
import "./App.css";

function App() {
  return (
    <Router>
      <div className="App">
        <nav>
          <ul>
            <li>
              <Link to="/">Products</Link>
            </li>
            <li>
              <Link to="/cart">Shopping Cart</Link>
            </li>
            <li>
              <Link to="/payments">Payments</Link>
            </li>
          </ul>
        </nav>
        <Routes>
          <Route path="/cart" element={<ShoppingCart />} />
          <Route path="/payments" element={<Payments />} />
          <Route path="/" element={<Products />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
