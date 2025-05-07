import { useContext, useEffect } from "react";
import { AuthContext } from "../context/AuthContext.tsx";
import { emailKeyName, tokenKeyName } from "../constants/constants.ts";
import api from "../api/api.ts";

const useAuth = () => {
  const {
    token, setToken,
    email, setEmail,
    name, setName,
    phone, setPhone,
    roles, setRoles
  } = useContext(AuthContext);

  const isLoggedIn = !!token;

  const login = (email: string, password: string) => {
    api.Auth.login(email, password).then((res) => {
      const { token, email, name, phone, roles } = res.data;
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
          console.warn("❌ A roles nem tömb:", parsed);
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
    isLoggedIn
  };
};

export default useAuth;
