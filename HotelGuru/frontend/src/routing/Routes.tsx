import Login from "../pages/Login.tsx";
import Registrate from "../pages/Registrate.tsx";
import Dashboard from "../pages/Dashboard.tsx";
import Rooms from "../pages/Rooms.tsx";
import Profile from "../pages/Profile.tsx";
export const routes = [
    {
        path: "login",
        component: <Login/>,
        isPrivate: false
    },
    {
        path: "registrate",
        component: <Registrate/>,
        isPrivate: false
    },
    {
        path: "dashboard",
        component: <Dashboard/>,
        isPrivate: true
    },
    {
        path: "rooms",
        component: <Rooms/>,
        isPrivate: true
    },
    {
        path: "profile",
        component: <Profile />,
        isPrivate: true,
      },
]