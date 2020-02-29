import 'bootstrap/dist/css/bootstrap.min.css';
import React, { Component } from 'react'
import Tabs from 'react-bootstrap/Tabs'
import Tab from 'react-bootstrap/Tab'

class CombatantTabs extends Component{
    
    render(){
        return (
            <Tabs defaultActiveKey="profile" id="uncontrolled-tab-example">
                <Tab eventKey="add-new-combatant" title="Add a new Combatant">
                </Tab>
                <Tab eventKey="stored-characters" title="Previously Created Characters">
                </Tab>
                <Tab eventKey="monster-lookup" title="Monster Lookup"  >
                </Tab>
            </Tabs>
  );
        
    }
}


export default CombatantTabs