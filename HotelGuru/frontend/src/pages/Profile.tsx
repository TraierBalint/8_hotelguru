import { Title, Text, Stack, Divider } from "@mantine/core";
import useAuth from "../hooks/useAuth";

const Profile = () => {
    const { name, email, phone } = useAuth();

    return (
        <Stack>
            <Title order={2}>Profil</Title>
            <Divider />

            <Text><strong>Név:</strong> {name || "Nincs megadva"}</Text>
            <Text><strong>E-mail:</strong> {email || "Nincs megadva"}</Text>
            <Text><strong>Telefonszám:</strong> {phone || "Nincs megadva"}</Text>
        </Stack>
    );
};

export default Profile;
