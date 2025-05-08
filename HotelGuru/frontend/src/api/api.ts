import axiosInstance from "./axios.config.ts";
import {IRoom} from "../interfaces/IRooms.ts";

const Auth = {
    login: (email: string, password: string) =>
        axiosInstance.post<{ email: string, token: string, name: string, phone: string, roles: string[] }>(
          `/api/user/login`,
          { email, password }
        )
    }
const Reg = {
    registrate: (name: string, email: string, password: string, phone: string) =>
        axiosInstance.post<{ email: string, token: string, name: string, phone: string, roles: string[] }>(
          `/api/user/registrate`,
          { name, email, password, phone }
        )
    }

const Room = {
    getRooms: () => axiosInstance.get<IRoom[]>(`/api/rooms/list`),
    addRoom: (room: IRoom) => axiosInstance.post(`/api/rooms/add`, room)  // ← ez kell
}
const Reservation = {
    addReservation: (data: any) =>
      axiosInstance.post("/api/reservation/add", data),
        getReservations: () => axiosInstance.get("/api/reservation/myreservation"),
        cancelReservation: (id: number) =>
            axiosInstance.put(`/api/reservation/cancel/${id}`),
  };



const api = {Room, Reg, Auth, Reservation};

export default api;