import { Navigate, Route, Routes } from "react-router-dom";
import BasicLayout from "../components/Layout/BasicLayout.tsx";
import AddReservation from "../pages/AddReservation.tsx"; // AddReservation importálása
import useAuth from "../hooks/useAuth.tsx";
import { routes } from "./Routes.tsx";
import { ReactElement } from "react";

const PrivateRoute = ({ element }: { element: ReactElement }) => {
    const { isLoggedIn } = useAuth();
    return isLoggedIn ? element : <Navigate to="/login" />;
};

const AuthenticatedRedirect = ({ element }: { element: ReactElement }) => {
    const { isLoggedIn } = useAuth();
    return isLoggedIn ? <Navigate to="/app" /> : element;
};

const Routing = () => {
    return (
        <Routes>
            {/* If the user is not logged in, redirect to login */}
            <Route path="/" element={<AuthenticatedRedirect element={<Navigate to="login" />} />} />

            {/* Map routes that are not private */}
            {routes
                .filter((route) => !route.isPrivate)
                .map((route) => (
                    <Route
                        key={route.path}
                        path={route.path}
                        element={<AuthenticatedRedirect element={route.component} />}
                    />
                ))}

            {/* Private routes for logged-in users */}
            <Route path="app" element={<PrivateRoute element={<BasicLayout />} />}>
                {/* Default route for app */}
                <Route path="" element={<Navigate to="dashboard" />} />

                {/* Add reservations route */}
                <Route
                    path="reservations/add"
                    element={<PrivateRoute element={<AddReservation />} />} // foglalás oldal
                />

                {/* Map private routes */}
                {routes
                    .filter((route) => route.isPrivate)
                    .map((route) => (
                        <Route
                            key={route.path}
                            path={route.path}
                            element={<PrivateRoute element={route.component} />}
                        />
                    ))}
            </Route>
        </Routes>
    );
};

export default Routing;
