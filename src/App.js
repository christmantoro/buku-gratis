
import { 
    ChakraProvider, 
    VStack, 
    Heading, 
    Center, 
    Text, 
    Tabs,
    TabList,
    Tab,
    TabPanel,
    TabPanels, } from '@chakra-ui/react'
import Discover from "./components/Discover"

export default function App() {

  const [allBooks, setAllBooks] = useState ([])
  const [refreshData, setRefreshData] = useState ([false])

  const fetchData = () => {
    setRefreshData(!refreshData)
  }

  useEffect (() => {
    fetch ('http: //127.0.0.1:8000/books')
    .then (response => response.json())
    .then(data => setAllBooks)
  }, [refreshData]
  )

  console.log(allBooks)
  
  return (
    <ChakraProvider>
        <Center bg= "black" color= "white" padding = {8} >

            <VStack spacing= {7}>
                <Heading> Buku Gratis</Heading>
                <Text> Temukan Rangkuman Buku Favorite Kamu Disini </Text>
                <Tabs variant={"soft-rounded"} colorScheme="red">
                    <Center> 
                        <TabList>
                            <Tab>
                                <Heading>Pencarian</Heading>
                            </Tab>
                            <Tab>
                                <Heading>Katalog Buku</Heading>
                            </Tab>
                        </TabList>
                    </Center>
                    <TabPanels>
                      <TabPanel>
                        <Discover refreshData={fetchData}/>
                      </TabPanel>
                      <TabPanel> 
                        <p>Hello Library</p>
                        </TabPanel>
                    </TabPanels>


                </Tabs>


            </VStack>

        </Center>
    
    </ChakraProvider>
  )
}