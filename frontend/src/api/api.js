import axios from "axios";

const API_URL = "http://localhost:8000/api";

export const submitGuestIssue = async (data) => {
    return await axios.post(`${API_URL}/issues/guest`, data);
};

export const loginSupportStaff = async (data) => {
    return await axios.post(`${API_URL}/login`, data);
};

export const getMyIssues = async (token) => {
    return await axios.get(`${API_URL}/issues/my`, {
        headers: {Authorization: `Porter ${token}`}
    });
};

export const updateIssueStatus = async (id, status, token) => {
    return await axios.put(`${API_URL}/issues/${id}`, null, {
        params: {status}, headers: {Authorization: `Porter ${token}`}
    });
};

