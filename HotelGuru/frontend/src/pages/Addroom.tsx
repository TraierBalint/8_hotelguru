import { TextInput, NumberInput, Button, Stack, Select } from "@mantine/core";
import { useForm } from "@mantine/form";
import api from "../api/api.ts";
import { useNavigate } from "react-router-dom";

const AddRoom = () => {
  const navigate = useNavigate();

  const form = useForm({
    initialValues: {
      name: "",
      type: "",
      status: "free", // vagy "occupied"
      price: 0,
    },
    validate: {
      name: (value) => value.trim() === "" ? "Név kötelező" : null,
      price: (value) => value <= 0 ? "Az ár nagyobb kell legyen 0-nál" : null,
    }
  });

  const submit = async () => {
    try {
      await api.Room.addRoom(form.values); // POST /api/rooms/add
      navigate("/app/rooms");
    } catch (err) {
      console.error("Hiba szoba létrehozásakor:", err);
    }
  };

  return (
    <form onSubmit={form.onSubmit(submit)}>
      <Stack>
        <TextInput label="Szoba neve" {...form.getInputProps("name")} required />
        <Select
                label="Típus"
                data={[
                    { value: "single", label: "Single" },
                    { value: "double", label: "Double" },
                    { value: "suite", label: "Suite" },
                ]}
                {...form.getInputProps("type")}
                required
                />

        <Select
                        label="Státusz"
                        data={[
                            { value: "available", label: "Available" },
                            { value: "reserved", label: "Reserved" },
                            { value: "maintenance", label: "Maintenance" },
                        ]}
                        {...form.getInputProps("status")}
                        required
                        />
        <NumberInput label="Ár (Ft)" {...form.getInputProps("price")} required min={0} />
        <Button type="submit">Szoba hozzáadása</Button>
      </Stack>
    </form>
  );
};

export default AddRoom;
