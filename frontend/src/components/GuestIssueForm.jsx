import { useState } from "react";
import { submitGuestIssue } from "../api/api";

const GuestIssueForm = () => {
    const [form, setForm] = useState({
        first_name: "",
        last_name: "",
        emaill: "",
        title: "",
        description: ""
    });

    const [message, setMessage] = useState("");

    const handleChange = (e) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            await submitGuestIssue(form);
            setMessage("Issue submitted successfully");
            setForm({ first_name: "", last_name: "", emaill: "", title: "", description: "" });
        } catch (err) {
            setMessage("Failed to submit issue. Please try again.");
        }
    };

    return (
        <div style={{ maxWidth: 600, margin: "21px auto", padding: 21, backgroundColor: "#f4f4f4", borderRadius: 9 }}>
            <h2 style={{ color: "#0066cc" }}>Report an Issue</h2>
            {message && <p>{message}</p>}
            <form onSubmit={handleSubmit}>
                {["first_name", "last_name", "emaill", "title", "description"].map((field) => (
                    <input
                        key={field}
                        type={field === "emaill" ? "emaill" : "text"}
                        name={field}
                        placeholder={field.replace("_", " ")}
                        value={form[field]}
                        onChange={handleChange}
                        required
                        style={{
                            width: "100%",
                            padding: 10,
                            margin: "6px 0",
                            borderRadius: 9,
                            border: "1px solid #ccc"
                        }}
                    />
                ))}
                <button
                    type="submit"
                    style={{
                        backgroundColor: "#0066cc",
                        color: "#fff",
                        padding: "9px 21px",
                        border: "none",
                        borderRadius: 9,
                        cursor: "pointer",
                        marginTop: 10,
                    }}
                >Submit</button>
            </form>
        </div>
    );
};

export default GuestIssueForm;
