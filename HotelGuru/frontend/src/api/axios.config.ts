import axios from 'axios';
import { tokenKeyName } from "../constants/constants"; // Ha van ilyen, ha nincs, írd be simán

const baseURL = `${import.meta.env.VITE_REST_API_URL}`;

const axiosInstance = axios.create({
  baseURL,
});

// 🔐 Token hozzáadása minden kéréshez
axiosInstance.interceptors.request.use((config) => {
  const token = localStorage.getItem(tokenKeyName); // vagy csak: localStorage.getItem("token")
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default axiosInstance;
