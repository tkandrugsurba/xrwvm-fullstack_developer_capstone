import { Routes, Route } from "react-router-dom";
import LoginPanel from "./components/Login/Login";
import Register from "./components/Register/Register"; // Import the Register component

function App() {
  return (
    <Routes>
      {/* Configures the /login route to render the LoginPanel component */}
      <Route path="/login" element={<LoginPanel />} />
      
      {/* Configures the /register route to render the Register component */}
      <Route path="/register" element={<Register />} />
    </Routes>
  );
}

export default App;
