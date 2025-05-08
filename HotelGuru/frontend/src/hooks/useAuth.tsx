import { useContext, useEffect } from "react";
import { AuthContext } from "../context/AuthContext.tsx";
import { emailKeyName, tokenKeyName } from "../constants/constants.ts";
import api from "../api/api.ts";
import { jwtDecode } from "jwt-decode";

interface DecodedToken {
  user_id: number;
  email?: string;
  name?: string;
  roles?: string[];
  exp?: number;
}

const useAuth = () => {
  const {
    token, setToken,
    email, setEmail,
    name, setName,
    phone, setPhone,
    roles, setRoles
  } = useContext(AuthContext);

  const isLoggedIn = !!token;

  let user = null;
  if (token) {
    try {
      const decoded = jwtDecode<DecodedToken>(token);
      user = {
        id: decoded.user_id,
        email: decoded.email,
        roles: decoded.roles,
      };
    } catch (e) {
      console.warn(" Token dekódolása sikertelen:", e);
    }
  }

  const login = (email: string, password: string) => {
    api.Auth.login(email, password).then((res) => {
      const { token, email, name, phone, roles } = res.data;

      try {
        const decoded = jwtDecode<DecodedToken>(token);
        console.log(" Bejelentkezett szerepkörök (JWT):", decoded.roles);
      } catch (e) {
        console.warn(" Nem sikerült dekódolni a tokent login után:", e);
      }

      setToken(token);
      setEmail(email);
      setName(name);
      setPhone(phone);
      setRoles(roles);
      localStorage.setItem(tokenKeyName, token);
      localStorage.setItem(emailKeyName, email);
      localStorage.setItem("roles", JSON.stringify(roles));
    });
  };

  const regist = (email: string, password: string, name: string, phone: string) => {
    api.Reg.registrate(name, email, password, phone).then((res) => {
      const { token, email, name, phone, roles } = res.data;

      try {
        const decoded = jwtDecode<DecodedToken>(token);
        console.log(" Regisztrált szerepkörök (JWT):", decoded.roles);
      } catch (e) {
        console.warn(" Nem sikerült dekódolni a tokent regisztráció után:", e);
      }

      setToken(token);
      setEmail(email);
      setName(name);
      setPhone(phone);
      setRoles(roles);
      localStorage.setItem(tokenKeyName, token);
      localStorage.setItem(emailKeyName, email);
      localStorage.setItem("roles", JSON.stringify(roles));
    });
  };

  const logout = () => {
    localStorage.clear();
    setToken(null);
    setEmail(null);
    setName(null);
    setPhone(null);
    setRoles([]);
  };

  useEffect(() => {
    const storedRoles = localStorage.getItem("roles");
    if (storedRoles && storedRoles !== "undefined" && storedRoles !== "null") {
      try {
        const parsed = JSON.parse(storedRoles);
        if (Array.isArray(parsed)) {
          setRoles(parsed);
        } else {
          console.warn(" A roles nem tömb:", parsed);
        }
      } catch (e) {
        console.warn("Hibás roles JSON a localStorage-ben:", storedRoles);
      }
    } else {
      setRoles([]);
    }
  }, []);

  return {
    login, logout, regist,
    token, email, name, phone, roles,
    isLoggedIn,
    user,
  };
};

export default useAuth;
