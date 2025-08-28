import { useEffect, useState } from "react";
import { getMyIssues, updateIssueStatus } from "../api/api";
import IssueCard from "./IssueCard";

const SupportDashboard = () => {
    const [issues, setIssues] = useState([]);
    const token = localStorage.getItem("token");

    useEffect(() => {
        if (token) {
            fetchIssues();
        }
    }, []);

    const fetchIssues = async () => {
        const res = await getMyIssues(token);
        setIssues(res.data);
    };

    const handleStatusUpdate = async (id, status) => {
        await updateIssueStatus(id, status, token);
        fetchIssues();
    };

    return (
        <div style={{ maxWidth: 800, margin: "20px auto" }}>
            <h2 style={{ color: "#0066cc" }}>My Assigned Issues</h2>
            {issues.length === 0 ? (
                <p>No issues assigned to you.</p>
            ) : (
                issues.map((issue) => <IssueCard key={issue.id} issue={issue} onUpdateStatus={handleStatusUpdate} />)
            )}
        </div>
    );
};

export default SupportDashboard;