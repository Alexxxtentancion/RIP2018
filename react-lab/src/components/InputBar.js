import React from 'react'
import {InputGroup,FormGroup,FormControl} from 'react-bootstrap';

export default(propps) => {
    return (
              <FormGroup>
                <InputGroup>
                <InputGroup.Addon>@</InputGroup.Addon>
                <FormControl type = "text" placeholder = "Enter username"/>
                </InputGroup>
            </FormGroup>
    )
}