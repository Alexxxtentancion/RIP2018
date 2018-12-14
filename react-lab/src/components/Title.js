import React from 'react';
import '../style.css';
import {PageHeader} from 'react-bootstrap';
export default (props) => {
     const className = `title title_${props.color}`;
    return (
        <div className={className}>
        <PageHeader>Repo list <small>{(new Date()).toDateString()}</small></PageHeader>
        </div>
    );
}
