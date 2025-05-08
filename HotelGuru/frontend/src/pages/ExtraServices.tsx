import { useEffect, useState } from "react";
import { Card, Stack, Title, Text, Loader } from "@mantine/core";
import api from "../api/api";

const ExtraServices = () => {
  const [services, setServices] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchServices = async () => {
      try {
        const res = await api.Reservation.getExtraServices();
        setServices(res.data);
      } catch (error) {
        console.error("Hiba az extra szolgáltatások lekérésekor:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchServices();
  }, []);

  if (loading) return <Loader variant="dots" />;

  return (
    <Stack>
      <Title order={2}>Elérhető extra szolgáltatások</Title>
      {services.length === 0 ? (
        <Text>Nincsenek extra szolgáltatások.</Text>
      ) : (
        services.map((service: any) => (
          <Card key={service.id} shadow="sm" padding="md" radius="md" withBorder>
            <Text fw={500}>{service.name}</Text>
            <Text>Ár: {service.price} Ft</Text>
          </Card>
        ))
      )}
    </Stack>
  );
};

export default ExtraServices;
