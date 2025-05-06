import axiosInstance from "./axios.config.ts";
import {IRoom} from "../interfaces/IRooms.ts";

const Auth = {
    login: (email: string, password: string) => axiosInstance.post<{token: string}>(`/api/User/login`, {email, password})
}

const Food = {
    getFoods: () => axiosInstance.get<IRoom[]>(`/api/room`)
}

const api = {Food, Auth};

export default api;