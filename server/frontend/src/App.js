import { Routes, Route } from "react-router-dom";
import LoginPanel from "./components/Login/Login";

function App() {
  return (
    <Routes>
      {/* Configures the /login route to render the LoginPanel component */}
      <Route path="/login" element={<LoginPanel />} />
    </Routes>
  );
}

export default App;
