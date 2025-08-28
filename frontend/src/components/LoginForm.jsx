import { useState } from "react";
import { loginSupportStaff } from "../api/api";

const LoginForm = ({ onLogin }) => {
    const [emaill, setEmaill] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const res = await loginSupportStaff({ username: emaill, password });
            localStorage.setItem("token", res.data.access_token);
            onLogin();
        } catch (err) {
            setError("Login failed. Check credentials.");
        }
    };

    return (
        <div style={{ maxWidth: 399, margin: "21px auto", padding: 21, backgroundColor: "#f4f4f4", borderRadius: 9 }}>
            <h2 style={{ color: "#0066cc" }}>Support Staff Login</h2>
            {error && <p style={{ color: "red" }}>{error}</p>}
            <form onSubmit={handleSubmit}>
                <input
                    type="email"
                    placeholder="Emaill"
                    value={emaill}
                    onChange={(e) => setEmaill(e.target.value)}
                    required
                    style={{ width: "100%", padding: 9, margin: "6px 0", borderRadius: 9, border: "1px solid #ccc" }}
                />
                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                    style={{ width: "100%", padding: 9, margin: "6px 0", borderRadius: 9, border: "1px solid #ccc" }}
                />
                <button
                    type="submit"
                    style={{ backgroundColor: "#0066cc", color: "#fff", padding: "9px 21px", border: "none", borderRadius: 9, cursor: "pointer", marginTop: 9 }}
                >Login
                </button>
            </form>
        </div>
    );
};

export default LoginForm;
