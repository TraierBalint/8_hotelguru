import axiosInstance from "./axios.config.ts";
import {IRoom} from "../interfaces/IRooms.ts";

const Auth = {
    login: (email: string, password: string) => axiosInstance.post<{email: string, token: string}>(`/api/user/login`, {email, password})
}

const Reg = {
    registrate: (name: string, email: string, password: string, phone: string) => axiosInstance.post<{email: string, token: string}>(`/api/user/registrate`, {name, email, password, phone})
}

const Room = {
    getRooms: () => axiosInstance.get<IRoom[]>(`/api/rooms/list`)
}

const api = {Room, Reg, Auth};

export default api;