import { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";
import {
  ChakraProvider,
  Heading,
  Center,
  Box,
  Text,
  Container,
  Tag,
  TagLabel,
} from "@chakra-ui/react";

const App = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:8000/v1/list/")
      .then((res) => {
        setData(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
    // eslint-disable-next-line
  }, []);

  console.log(data);

  const title = "titletitletitletitle";
  const tags = ["tag", "tag", "tag"];

  const Content = ({ title, tags }) => {
    return (
      <Container mb={20}>
        <Text as="h2" fontSize="2xl" my={7}>
          {title}
        </Text>
        {tags.map((tag) => (
          <Tag
            size="md"
            borderRadius="full"
            variant="solid"
            colorScheme="green"
            mr={1}
          >
            <TagLabel>{tag}</TagLabel>
          </Tag>
        ))}
      </Container>
    );
  };

  return (
    <ChakraProvider>
      <Box py={350}>
        <Center>
          <Heading as="h1" size="2xl">
            ururls
          </Heading>
        </Center>
      </Box>
      <Box>
        <Content title={title} tags={tags} />
        <Content title={title} tags={tags} />
        <Content title={title} tags={tags} />
      </Box>
    </ChakraProvider>
  );
};

export default App;
