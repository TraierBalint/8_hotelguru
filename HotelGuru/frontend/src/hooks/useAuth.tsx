import {useContext, useEffect} from "react";
import {AuthContext} from "../context/AuthContext.tsx";
import {emailKeyName, tokenKeyName} from "../constants/constants.ts";
import api from "../api/api.ts";

const useAuth = () => {
    const { token, setToken, email, setEmail  } = useContext(AuthContext);
    const isLoggedIn = !!token;

    const login = (email: string, password: string) => {
        console.log({email, password});
        api.Auth.login(email, password).then((res) => {
            const token = res.data.token;
            setToken(token);
            localStorage.setItem(tokenKeyName, token);
            const email = res.data.email;
            setEmail(email);
            localStorage.setItem(emailKeyName, email);
        });
    }

    const regist = (email: string, password: string, name: string, phone: string) => {
        console.log({email, name});
        api.Reg.registrate(name, email, password, phone).then((res) => {
            const token = res.data.token;
            setToken(token);
            localStorage.setItem(tokenKeyName, token);
            const email = res.data.email;
            setEmail(email);
            localStorage.setItem(emailKeyName, email);
        });
    }

    const logout = () => {
        localStorage.clear();
        setToken(null);
    }

    useEffect(() => {

    }, []);

    return {login, logout, regist, token, email, isLoggedIn};
}

export default useAuth;