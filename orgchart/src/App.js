import React, { Component } from 'react';
import OrgChart from './mychart';

class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div style={{height: '100%'}}>

                <OrgChart nodes={
                    [{id: 1, name: "Name1" , title: "Tytle1" },
                    {id: 2, pid: 1, name: "Name2" , title: "Tytle2" },
                    {id: 3, pid: 1, name: "Name3" , title: "Tytle3" }]} />
            </div>
        );
    }
}

export default App;
