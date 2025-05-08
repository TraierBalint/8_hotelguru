import { DateInput } from "@mantine/dates";
import { Button, Stack, MultiSelect } from "@mantine/core";
import { useForm } from "@mantine/form";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import useAuth from "../hooks/useAuth";
import api from "../api/api.ts";
import { AxiosError } from "axios";

const AddReservation = () => {
  const { user,token } = useAuth();
  const navigate = useNavigate();
  const [userId, setUserId] = useState<number | null>(null); // Ezt backendből JWT alapján is szedheted
  const [rooms, setRooms] = useState<{ value: string; label: string }[]>([]);

  const form = useForm({
    initialValues: {
      check_in: null,
      check_out: null,
      items: [], // room_id-k listája
    },
    validate: {
      check_in: (value) => (!value ? "Érkezési dátum kötelező" : null),
      check_out: (value) => (!value ? "Távozási dátum kötelező" : null),
      items: (value) => (value.length === 0 ? "Legalább egy szobát ki kell választani" : null),
    },
  });

  // Szobák betöltése (lehetne csak elérhető is)
  useEffect(() => {
    api.Room.getRooms().then((res) => {
        const transformed = res.data.map((room) => ({
            value: String(room.id),
            label: `${room.name} (${room.type}) - ${room.price} Ft`,
            disabled: room.status !== "AVAILABLE", // csak az elérhető választható
          }));
          setRooms(transformed);
      });
  }, []);

  const submit = async () => {
    try {
      const payload = {
        user_id: user?.id,
        check_in: form.values.check_in,
        check_out: form.values.check_out,
        items: form.values.items.map((roomId) => ({ room_id: Number(roomId) })),
      };
  
      console.log("Küldött adat: ", payload);
  
      await api.Reservation.addReservation(payload);
      
      alert("Sikeres foglalás!"); // <-- Itt írja ki a visszajelzést
      
      navigate("/app/reservations"); // <-- Utána mehet az átirányítás
    } catch (err) {
      if ((err as AxiosError).response) {
        console.error("Backend hiba:", (err as AxiosError).response?.data);
      }
      console.error("Hiba foglaláskor:", err);
    }
  };
  
  
  

  return (
    <form onSubmit={form.onSubmit(submit)}>
      <Stack>
        <DateInput label="Érkezés" {...form.getInputProps("check_in")} required />
        <DateInput label="Távozás" {...form.getInputProps("check_out")} required />
        <MultiSelect
          label="Foglalni kívánt szobák"
          data={rooms}
          {...form.getInputProps("items")}
          required
        />
        <Button type="submit">Foglalás</Button>
      </Stack>
    </form>
  );
};

export default AddReservation;
