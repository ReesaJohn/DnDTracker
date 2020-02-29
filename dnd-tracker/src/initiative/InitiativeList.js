import 'bootstrap/dist/css/bootstrap.min.css';
import React, { Component } from 'react'
import ListGroup from 'react-bootstrap/ListGroup'
import { Navbar, Nav, NavDropdown, Form,  FormControl, Button, Table, Container, Row, Col} from 'react-bootstrap';
class InitiativeList extends Component{
    
    render(){
        const { characters } = this.props
        return (
            <Container>
            <Row> Current Initiative Order </Row>
            <Row>
            
                <ListGroup>
                  <ListGroup.Item>Cras justo odio</ListGroup.Item>
                  <ListGroup.Item>Dapibus ac facilisis in</ListGroup.Item>
                  <ListGroup.Item>Morbi leo risus</ListGroup.Item>
                  <ListGroup.Item>Porta ac consectetur ac</ListGroup.Item>
                  <ListGroup.Item>Vestibulum at eros</ListGroup.Item>
                </ListGroup>
            </Row>
            </Container>
  );
        
    }
}
    
export default InitiativeList