import { Routes, Route } from "react-router-dom";
import LoginPanel from "./components/Login/Login";
import Register from "./components/Register/Register";
import Dealers from "./components/Dealers/Dealers";
import Dealer from "./components/Dealers/Dealer"; // Import the Dealer component

function App() {
  return (
    <Routes>
      {/* Configures the /login route to render the LoginPanel component */}
      <Route path="/login" element={<LoginPanel />} />

      {/* Configures the /register route to render the Register component */}
      <Route path="/register" element={<Register />} />

      {/* Configures the /dealers route to render the Dealers component */}
      <Route path="/dealers" element={<Dealers />} />

      {/* Configures the /dealer/:id route to render the Dealer component */}
      <Route path="/dealer/:id" element={<Dealer />} />
    </Routes>
  );
}

export default App;
