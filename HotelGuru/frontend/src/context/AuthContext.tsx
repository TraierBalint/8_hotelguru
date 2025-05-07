import { createContext } from "react";
import {emailKeyName, tokenKeyName} from "../constants/constants.ts";

interface AuthContext {
    token: string | null;
    setToken: (token: string | null) => void;
    email: string | null;
    setEmail: (email: string | null) => void;
    name: string | null;
    setName: (name: string | null) => void;
    phone: string | null;
    setPhone: (phone: string | null) => void;
}

export const AuthContext = createContext<AuthContext>({
    token: localStorage.getItem(tokenKeyName),
    setToken: () => {},
    email: localStorage.getItem(emailKeyName),
    setEmail: () => {},
    name: null,
    setName: () => {},
    phone: null,
    setPhone: () => {}
});
