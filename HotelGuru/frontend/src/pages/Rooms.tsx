import {useEffect, useState} from "react";
import api from "../api/api.ts";
import {IRoom} from "../interfaces/IRooms.ts";
import {Card, Table} from "@mantine/core";

const Rooms = () => {
    const [rooms, setRooms] = useState<IRoom[]>([]);

    useEffect(() => {
        api.Room.getRooms().then(res =>{
            console.log(res.data);
            setRooms(res.data);
        });
    }, []);

    const rows = rooms.map((room) => (
        <Table.Tr key={room.id}>
            <Table.Td>{room.name}</Table.Td>
            <Table.Td>{room.type}</Table.Td>
            <Table.Td>{room.status}</Table.Td>
            <Table.Td>{room.price}</Table.Td>
        </Table.Tr>
    ));

    return <>
        <Card shadow="sm" padding="lg" radius="md" withBorder>
            <Table>
                <Table.Thead>
                    <Table.Tr>
                        <Table.Th>Név</Table.Th>
                        <Table.Th>Típusa</Table.Th>
                        <Table.Th>Státusz</Table.Th>
                        <Table.Th>Ár</Table.Th>
                    </Table.Tr>
                </Table.Thead>
                <Table.Tbody>{rows}</Table.Tbody>
            </Table>
        </Card>
    </>
}

export default Rooms;