import { Box, Burger, Flex, Title } from "@mantine/core";
import UserMenuDropdown from "./UserMenuDropdown.tsx";

const Header = ({ opened, toggle }: any) => {
  return (
    <Flex
      justify="space-between"
      align="center"
      style={{ height: "100%", paddingLeft: 20, paddingRight: 20 }}
    >
      {/* Bal oldali user dropdown */}
      <Box>
        <UserMenuDropdown />
      </Box>

      {/* Középen a cím */}
      <Title order={2} style={{ flexGrow: 1, textAlign: "center" }}>
        HotelGuru
      </Title>

      {/* Jobb oldali hamburger */}
      <Burger
        opened={opened}
        onClick={toggle}
        hiddenFrom="sm"
        size="sm"
        ml="auto"
      />
    </Flex>
  );
};

export default Header;
