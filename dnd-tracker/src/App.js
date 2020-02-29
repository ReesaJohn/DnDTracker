
import 'bootstrap/dist/css/bootstrap.min.css';
import React, { Component } from 'react'
import logo from './logo.svg';
import './App.css';
import { Navbar, Nav, NavDropdown, Form,  FormControl, Button, Table, Container, Row, Col} from 'react-bootstrap';
import Tabs from 'react-bootstrap/Tabs'
import Tab from 'react-bootstrap/Tab'
import CombatantTabs from './initiative/CombatantTabs'
import InitiativeList from './initiative/InitiativeList'
import './initiative/test.css';


class App extends Component {
  render() {
    return (
        
    
      <Container fluid="md">
        
        <Row id="row-id">
        </Row>
        <Row>
            <Col sm={3}><InitiativeList/></Col>
            <Col sm={9}><CombatantTabs/></Col>
        </Row>
        
      </Container>
    )
  }
}

export default App;
