import {useEffect, useState} from "react";
import api from "../api/api.ts";
import {IRoom} from "../interfaces/IRooms.ts";
import {Button, Card, Table, Group} from "@mantine/core";
import {useNavigate} from "react-router-dom";
import useAuth from "../hooks/useAuth";

const Rooms = () => {
  const [rooms, setRooms] = useState<IRoom[]>([]);
  const navigate = useNavigate();
  const { roles, isLoggedIn } = useAuth();
  const isAdmin = roles?.includes("Admin") || roles?.includes("Administrator");

  useEffect(() => {
    api.Room.getRooms().then(res => {
      setRooms(res.data);
      console.log("Szerepkörök:", roles);
    });
  }, []);

  const handleDelete = async (roomId: number) => {
    if (confirm("Biztosan törölni szeretnéd ezt a szobát?")) {
      try {
        await api.Room.deleteRoom(roomId);
        alert("Szoba törölve.");
        const res = await api.Room.getRooms();
        setRooms(res.data);
      } catch (err) {
        console.error("Hiba törlés közben:", err);
        alert("Nem sikerült a törlés.");
      }
    }
  };

  const rows = rooms.map((room) => {
    const isDisabled = room.status !== "AVAILABLE";
    const rowStyle = isDisabled ? { backgroundColor: "#ffe6e6" } : {};

    return (
      <Table.Tr key={room.id} style={rowStyle}>
        <Table.Td>{room.name}</Table.Td>
        <Table.Td>{room.type}</Table.Td>
        <Table.Td>{room.status}</Table.Td>
        <Table.Td>{room.price}</Table.Td>
        <Table.Td>
          {isLoggedIn && (
            <Group gap="xs">
              <Button
                size="xs"
                disabled={isDisabled}
                variant={isDisabled ? "light" : "filled"}
                color={isDisabled ? "red" : "blue"}
                onClick={() =>
                  !isDisabled && navigate(`/app/reservations/add?room_id=${room.id}`)
                }
              >
                Foglalás
              </Button>

              {isAdmin && (
                <Button
                  size="xs"
                  color="red"
                  variant="outline"
                  onClick={() => handleDelete(room.id!)}
                >
                  Törlés
                </Button>
              )}
            </Group>
          )}
        </Table.Td>
      </Table.Tr>
    );
  });

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
            <Table.Th>Művelet</Table.Th>
          </Table.Tr>
        </Table.Thead>
        <Table.Tbody>{rows}</Table.Tbody>
      </Table>
    </Card>
  );
};

export default Rooms;
