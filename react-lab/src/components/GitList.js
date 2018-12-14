import React from 'react'
import '../style.css'
import {ListGroup,ListGroupItem} from 'react-bootstrap';
import propTypes from 'prop-types';

const GitList = props => {
    const {repos} = props;
        const reposList = repos.length ? (
            repos.map(repo => {
                return(
                    <div key={repo.id}>
                          <ListGroupItem header = {repo.name} href = {repo.html_url}>{repo.created_at.split('T')[0]}</ListGroupItem>
                    </div>
                )
            })
        ) : (<div>No repos</div>)

        return (
            <div>           
            <ListGroup>{reposList}</ListGroup>
        </div>
        )
} 



GitList.propTypes = {
    repos : propTypes.array.isRequired
}


export default GitList;


