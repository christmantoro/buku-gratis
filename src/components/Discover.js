import { 
    Center, 
    Text,
    Heading,
    VStack, 
    Button,
    Input,
    HStack,
    SimpleGrid,
    Image,
    Badge,
    useToast,

} from '@chakra-ui/react'

import { AddIcon } from "@chakra-ui/icons";

import { useState, useEffect } from "react"


// Google Book API 

const API_KEY = "";

export default function Discover(refreshData) {
    const [searchQuery, setSearchQuery]  = useState ("");
    const [searchResult, setSearchResults] = useState ([]);

    const bookAddedToast = useToast ()

    const onSearchClick = () => {
        fetch (
            'https://www.googleapis.com/books/v1/volumes?q=${searchQuery}&key=${API_KEY}$maxResults=40' 
         )
            .then((response) => response.json())
            .then((data) => setSearchResults(data["items"]));
       
        }

    return (
        <VStack spacing = {7} padingaTop = {5}>

            <Heading size = "lg"> Cari Buku </Heading>
            <Text> Temukan buku baru yang ingin kamu tambahkan ke perpustakaan pribadimu</Text>
            <HStack spacing={12}>
                <Input width="600px" value={searchQuery} onChange={(e) => setSearchQuery(e.target.value) }/>
                <Button colorScheme="red" size="lg" onClick={onSearchClick}>
                    Cari Buku
                </Button>
            </HStack>

        </VStack>
    )

    


}