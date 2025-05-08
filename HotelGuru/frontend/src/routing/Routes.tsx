import Login from "../pages/Login.tsx";
import Registrate from "../pages/Registrate.tsx";
import Dashboard from "../pages/Dashboard.tsx";
import Rooms from "../pages/Rooms.tsx";
import Profile from "../pages/Profile.tsx";
import AddRoom from "../pages/Addroom.tsx";
import AddReservationPage from "../pages/AddReservation.tsx";
import Reservations from "../pages/Reservations.tsx";
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

      {
        path: "rooms/add",
        component: <AddRoom />,
        isPrivate: true,
      },
      {
        path: "reservations/add",
        component: <AddReservationPage />,
        isPrivate: true,
      },
      {
        path: "reservations",
        component: <Reservations />,
        isPrivate: true,
      },
]