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
  Link,
} from "@chakra-ui/react";

const Content = ({ id, title, url, tags, category, rate }) => {
  return (
    <Container mb={20}>
      <Link href={url} isExternal>
        <Text as="h2" fontSize="2xl" my={3}>
          {id}.{title}
        </Text>
      </Link>
      <Text as="h3" fontSize="md" mb={2}>
        {category}
      </Text>
      <Box my={3}>
        {tags.map((tag, index) => (
          <Tag
            key={index}
            size="md"
            borderRadius="full"
            variant="solid"
            colorScheme="green"
            mr={2}
          >
            <TagLabel>{tag}</TagLabel>
          </Tag>
        ))}
      </Box>
      <Text as="h3" fontSize="md">
        {rate}
      </Text>
    </Container>
  );
};

const App = () => {
  const [data, setData] = useState([
    { id: "", alias: "", url: "", tags: [], category: "", rate: "" },
  ]);

  useEffect(() => {
    axios
      .get("http://localhost:8000/v1/summary_1")
      .then((res) => {
        setData(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
    // eslint-disable-next-line
  }, []);

  return (
    <ChakraProvider>
      <Box py={400}>
        <Center>
          <Heading as="h1" size="2xl">
            ururls
          </Heading>
        </Center>
      </Box>
      <Box>
        {data.map((item) => (
          <Content
            key={item.id}
            id={item.id}
            title={item.alias}
            url={item.url}
            tags={item.tags}
            category={item.category}
            rate={item.rate}
          />
        ))}
      </Box>
    </ChakraProvider>
  );
};

export default App;
