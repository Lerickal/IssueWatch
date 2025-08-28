import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import GuestIssueForm from "./src/components/GuestIssueForm";
import LoginForm from "./src/components/LoginForm";
import SupportDashboard from "./src/components/SupportDashboard";
import { useState } from "react";

function App() {
    const [isLoggedIn, setIsLoggedIn] = useState(!!localStorage.getItem("token"));

    const handleLogin = () => {
        setIsLoggedIn(true);
    };

    const handleLogout = () => {
        localStorage.removeItem("token");
        setIsLoggedIn(false);
    };

    return (
        <Router>
            <div style={{ fontFamily: "Arial, sans-serif", backgroundColor: "#f4f4f4", minHeight: "100vh", padding: 21 }}>
                <nav style={{ marginBottom: 21 }}>
                    <button
                        onClick={handleLogout}
                        style={{ backgroundColor: "#ff6600", color: "#fff", border: "none", borderRadius: 9, padding: "9px 15px", cursor: "pointer" }}
                    >Logout
                    </button>
                </nav>
                <Routes>
                    <Route path="/" element={<GuestIssueForm />} />
                    <Route path="/login" element={!isLoggedIn ? <LoginForm onLogin={handleLogin} /> : <Navigate to="/dashboard" />} />
                    <Route path="/dashboard" element={isLoggedIn ? <SupportDashboard /> : <Navigate to="/login" />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;
