import { useState, useEffect } from "react"
import 'bootstrap/dist/css/bootstrap.min.css'
import { Container, Row, Col } from 'reactstrap'
import Flow from "./flow"


function Perso () {

    const [persoList, setPersoList] = useState([])
    const [activeCategory, setActiveCategory] = useState("Stark")
    const maison = persoList.reduce(
        (acc, perso) => acc.includes(perso.maison_nom) ? acc : acc.concat(perso.maison_nom), 
        []   
    )


    useEffect(() => {
        async function fetchDatas () {
            console.log("Recherche des données")
            try {
                const response = await fetch('http://localhost:8000/api/persos')
                const data = await response.json()
                setPersoList(data)
                console.log({persoList})
            } catch (err) {
                console.log(err)
            }
        
        }

        fetchDatas()
    }, [])
    

    return ( <Container>
                <Row>
                    <Col>
                        <ul>
                            {maison.map((cat) => cat ? (<li key={cat} onClick={() => setActiveCategory(cat)}>{cat}</li>) : null) }
                        </ul>
                    </Col>
                    <Col>
                        <ul>
                            {persoList.map(({id, nom, maison_nom, maisonnaissance_nom}) => 
                            activeCategory === maison_nom || activeCategory === maisonnaissance_nom ? (<li key={id}>{nom} de la maison {maison_nom}</li>) : null)}
                        </ul>
                    </Col>
                    <Col>
                        <Flow />
                    </Col>
                </Row>
            </Container>)
}



export default Perso