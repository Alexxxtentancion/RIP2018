import React from 'react'
import './style.css'
import Title from './components/Title';
import axios from 'axios';
import InputBar from './components/InputBar'
import GitList from './components/GitList';
   

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            repos: []
        }
    }
    componentDidMount() {
        axios.get('https://api.github.com/users/linus/repos').then(
            res => {
                console.log(res.data)
                this.setState({
                    repos: res.data,
                    isLoading: false
                })
            }

        )
    }
   
    render() {
        return (
            <div>           
            <Title color = "silver" />
            {/* <InputBar /> */}
            {this.state.isLoading && <div>Loading...</div>}
            <GitList repos= {this.state.repos} />
        </div>
        )
    };
    
}

export default App;