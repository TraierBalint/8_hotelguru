import {useEffect, useState} from "react";
import api from "../api/api.ts";
import {IRoom} from "../interfaces/IRooms.ts";
import {Button, Card, Table, Group} from "@mantine/core";
import {useNavigate} from "react-router-dom";
import useAuth from "../hooks/useAuth";

const Rooms = () => {
    const [rooms, setRooms] = useState<IRoom[]>([]);
    const navigate = useNavigate();
    const { roles, isLoggedIn } = useAuth(); // <- isLoggedIn is kell

    useEffect(() => {
        api.Room.getRooms().then(res => {
            setRooms(res.data);
        });
    }, []);

    const rows = rooms.map((room) => (
        <Table.Tr key={room.id}>
            <Table.Td>{room.name}</Table.Td>
            <Table.Td>{room.type}</Table.Td>
            <Table.Td>{room.status}</Table.Td>
            <Table.Td>{room.price}</Table.Td>
            <Table.Td>
                {isLoggedIn && (
                    <Button
                        size="xs"
                        onClick={() => navigate(`/app/reservations/add?room_id=${room.id}`)}
                    >
                        Foglalás
                    </Button>
                )}
            </Table.Td>
        </Table.Tr>
    ));

    const isAdmin = roles?.includes("Admin") || roles?.includes("Administrator");
    console.log("Aktuális szerepkörök:", roles);

    return (
        <Card shadow="sm" padding="lg" radius="md" withBorder>
            <Group justify="space-between" mb="md">
                <h2>Szobák</h2>
                {isAdmin && (
                    <Button onClick={() => navigate("/app/rooms/add")}>Szoba hozzáadása</Button>
                )}
            </Group>

            <Table>
                <Table.Thead>
                    <Table.Tr>
                        <Table.Th>Név</Table.Th>
                        <Table.Th>Típusa</Table.Th>
                        <Table.Th>Státusz</Table.Th>
                        <Table.Th>Ár</Table.Th>
                        <Table.Th>Művelet</Table.Th> {/* ide jön a "Foglalás" oszlopfejléc */}
                    </Table.Tr>
                </Table.Thead>
                <Table.Tbody>{rows}</Table.Tbody>
            </Table>
        </Card>
    );
};

export default Rooms;
