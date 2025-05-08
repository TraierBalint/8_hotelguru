import { Title, Image, Center } from "@mantine/core";

const Dashboard = () => {
  return (
    <Center style={{ flexDirection: "column", paddingTop: "2rem" }}>
      <Title order={2}>Kezdőoldal</Title>
      <Image
        src="/asd.jpg"
        alt="HotelGuru főoldal"
        width={400}
        radius="md"
        mt="md"
      />
    </Center>
  );
};

export default Dashboard;
