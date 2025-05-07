import {useContext, useEffect} from "react";
import {AuthContext} from "../context/AuthContext.tsx";
import {emailKeyName, tokenKeyName} from "../constants/constants.ts";
import api from "../api/api.ts";

const useAuth = () => {
    const { token, setToken, email, setEmail, name, setName, phone, setPhone } = useContext(AuthContext);

    const isLoggedIn = !!token;

    const login = (email: string, password: string) => {
        console.log({ email, password });
        api.Auth.login(email, password).then((res) => {
            const { token, email, name, phone } = res.data;
            setToken(token);
            setEmail(email);
            setName(name);
            setPhone(phone);
            localStorage.setItem(tokenKeyName, token);
            localStorage.setItem(emailKeyName, email);
        });
    };

    const regist = (email: string, password: string, name: string, phone: string) => {
        console.log({ email, name });
        api.Reg.registrate(name, email, password, phone).then((res) => {
            const { token, email, name, phone } = res.data;
            setToken(token);
            setEmail(email);
            setName(name);
            setPhone(phone);
            localStorage.setItem(tokenKeyName, token);
            localStorage.setItem(emailKeyName, email);
        });
    };

    const logout = () => {
        localStorage.clear();
        setToken(null);
    }

    useEffect(() => {

    }, []);

    return { login, logout, regist, token, email, name, phone, isLoggedIn };
}

export default useAuth;