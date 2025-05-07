import "@mantine/core/styles.css";
import { MantineProvider } from "@mantine/core";
import { theme } from "./theme";
import {BrowserRouter} from "react-router-dom";
import { AuthContext } from "./context/AuthContext";
import Routing from "./routing/Routing.tsx";
import {useState} from "react";
import {emailKeyName, tokenKeyName} from "./constants/constants.ts";

export default function App() {
  const [token, setToken] = useState(localStorage.getItem(tokenKeyName));
  const [email, setEmail] = useState(localStorage.getItem(emailKeyName));
  const [name, setName] = useState<string | null>(null);
  const [phone, setPhone] = useState<string | null>(null);
  const storedRoles = localStorage.getItem("roles");
  const [roles, setRoles] = useState<string[]>(
          storedRoles && storedRoles !== "undefined" ? JSON.parse(storedRoles) : []
);


  

  return <MantineProvider theme={theme}>
    <BrowserRouter>
    <AuthContext.Provider value={{ token, setToken, email, setEmail, name, setName, phone, setPhone, roles, setRoles }}>
        <Routing/>
      </AuthContext.Provider>
    </BrowserRouter>
  </MantineProvider>;
}
