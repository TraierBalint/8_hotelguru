import axiosInstance from "./axios.config.ts";
import {IRoom} from "../interfaces/IRooms.ts";

const Auth = {
    login: (email: string, password: string) => axiosInstance.post<{email: string, id: BigInt, name: string, token: string}>(`/api/user/login`, {email, password})
}

const Room = {
    getRooms: () => axiosInstance.get<IRoom[]>(`/api/rooms/list`)
}

const api = {Room, Auth};

export default api;