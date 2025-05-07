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
            setToken(res.data.token);
            localStorage.setItem(tokenKeyName, res.data.token);
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

    return {login, logout, token, email, isLoggedIn};
}

export default useAuth;