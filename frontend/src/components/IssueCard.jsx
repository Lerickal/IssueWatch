const IssueCard = ({ issue, onUpdateStatus }) => {
    return (
        <div style={{ backgroundColor: "#fff", padding: 15, marginBottom: 9, borderRadius: 9, boxShadow: "0 3px 6px rgba(0,0,0,0.1)" }}>
            <h3 style={{ color: "#0066cc" }}>{issue.title}</h3>
            <p>{issue.description}</p>
            <p><strong>Status:</strong> {issue.status}</p>
            <p><strong>Reported by:</strong> {issue.reporter.first_name} {issue.reporter.last_name}</p>
            <p><strong>Assigned to:</strong> {issue.assigned_to?.first_name} {issue.assigned_to?.last_name || "Unassigned"}</p>
            <select value={issue.status} onChange={(e) => onUpdateStatus(issue.id, e.target.value)} style={{ borderRadius: 9, padding: 6 }}>
                <option value="Open">Open</option>
                <option value="In Progress">In Progress</option>
                <option value="Closed">Closed</option>
            </select>
        </div>
    );
};

export default IssueCard;