import { useEffect, useState } from "react";
import api from "../api/api.ts";
import {
  Card,
  Stack,
  Title,
  Text,
  Loader,
  Button,
  Modal,
  Select,
  NumberInput,
} from "@mantine/core";
import { useDisclosure } from "@mantine/hooks";

const Reservations = () => {
  const [reservations, setReservations] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  const [opened, { open, close }] = useDisclosure(false);
  const [selectedReservationId, setSelectedReservationId] = useState<number | null>(null);
  const [extraServices, setExtraServices] = useState<any[]>([]);
  const [selectedExtra, setSelectedExtra] = useState<string | null>(null);
  const [quantity, setQuantity] = useState<number>(1);

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

    const fetchExtras = async () => {
      try {
        const res = await api.Reservation.getExtraServices();
        setExtraServices(
            res.data
              .filter((s: any) => s && s.id && s.name) // csak érvényes szolgáltatások
              .map((s: any) => ({
                value: String(s.id),
                label: `${s.name} – ${s.price} Ft`,
              }))
          );
      } catch (error) {
        console.error("Hiba az extrák lekérésekor:", error);
      }
    };

    fetchReservations();
    fetchExtras();
  }, []);

  const handleAddExtra = async () => {
    if (!selectedReservationId || !selectedExtra || quantity < 1) {
      alert("Minden mezőt ki kell tölteni!");
      return;
    }
  
    try {
      await api.Reservation.addExtraServiceToReservation({
        reservation_id: selectedReservationId,
        extraservice_id: Number(selectedExtra),
        quantity,
      });
      alert("Extra sikeresen hozzáadva!");
      const res = await api.Reservation.getReservations();
      setReservations(res.data);
      close();
    } catch (err: any) {
      console.error("Hiba extra hozzáadásakor:", err);
      console.log("Szerver válasza:", err.response?.data); // 🪵 ← IDE KELL
      alert("Nem sikerült az extra hozzáadása.");
    }
  };
  

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

            {reservation.extraservices?.length > 0 && (
              <>
                <Text mt="sm">Extra szolgáltatások:</Text>
                <ul>
                  {reservation.extraservices.map((extra: any, i: number) => (
                    <li key={i}>
                      {extra.name} – {extra.quantity} × {extra.price} Ft
                    </li>
                  ))}
                </ul>
                <Text fw={500} mt="xs">
                            Összesen:{" "}
                            {reservation.items.reduce(
                                (sum: number, room: any) => sum + room.price,
                                0
                            ) +
                                reservation.extraservices.reduce(
                                (sum: number, extra: any) => sum + extra.quantity * extra.price,
                                0
                                )} Ft
                            </Text>
              </>
            )}
                {reservation.status === "ReservationStatus.ACTIVE" && (
                <Button
                    color="blue"
                    size="xs"
                    mt="sm"
                    onClick={() => {
                    setSelectedReservationId(reservation.id);
                    open();
                    }}
                >
                    Extra hozzáadása
                </Button>
                )}

            {reservation.status === "ReservationStatus.ACTIVE" && (
              <Button
                color="red"
                size="xs"
                mt="sm"
                onClick={async () => {
                  try {
                    await api.Reservation.cancelReservation(reservation.id);
                    alert("Foglalás sikeresen lemondva!");
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

      <Modal opened={opened} onClose={close} title="Extra szolgáltatás hozzáadása">
        <Select
          label="Válassz egy szolgáltatást"
          data={extraServices}
          value={selectedExtra}
          onChange={setSelectedExtra}
          placeholder="Pl. Reggeli, Masszázs..."
        />
        <NumberInput
          label="Mennyiség"
          value={quantity}
          onChange={(val) => setQuantity(val as number)}
          min={1}
          mt="sm"
        />
        <Button fullWidth mt="md" onClick={handleAddExtra}>
          Hozzáadás
        </Button>
      </Modal>
    </Stack>
  );
};

export default Reservations;
