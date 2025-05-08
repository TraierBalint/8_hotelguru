import { useEffect, useState } from "react";
import api from "../api/api.ts";
import { Card, Stack, Title, Text, Loader ,Button} from "@mantine/core";


const Reservations = () => {
  const [reservations, setReservations] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchReservations = async () => {
      try {
        const res = await api.Reservation.getReservations();
        setReservations(res.data);
      } catch (error) {
        console.error("Hiba a foglalások lekérésekor:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchReservations();
  }, []);

  if (loading) {
    return <Loader variant="dots" />;
  }

  return (
    <Stack>
      <Title order={2}>Foglalásaid</Title>
      {reservations.length === 0 ? (
        <Text>Nincs még foglalásod.</Text>
      ) : (
        reservations.map((reservation) => (
            <Card key={reservation.id} shadow="sm" padding="md" radius="md" withBorder>
            <Text fw={500}>Foglalás #{reservation.id}</Text>
            <Text>Érkezés: {reservation.check_in}</Text>
            <Text>Távozás: {reservation.check_out}</Text>
            <Text>Állapot: {reservation.status}</Text>
            <Text mt="sm">Szobák:</Text>
            <ul>
              {(reservation.items ?? []).map((room: any) => (
                <li key={room.id}>
                  {room.name} – {room.price} Ft
                </li>
              ))}
            </ul>
          
            {reservation.status === "ReservationStatus.ACTIVE" && (
              <Button
                color="red"
                size="xs"
                mt="sm"
                onClick={async () => {
                  try {
                    await api.Reservation.cancelReservation(reservation.id);
                    alert("Foglalás sikeresen lemondva!");
                    // Frissítjük a foglaláslistát
                    const res = await api.Reservation.getReservations();
                    setReservations(res.data);
                  } catch (error) {
                    console.error("Hiba lemondáskor:", error);
                    alert("Nem sikerült lemondani a foglalást.");
                  }
                }}
              >
                Lemondás
              </Button>
            )}
          </Card>
          
        ))
      )}
    </Stack>
  );
};

export default Reservations;
