import React, {useEffect, useState} from 'react';
import {BrowserRouter, Route, Switch} from 'react-router-dom'
import OrgChart from './components/orgchart/MainChart';
import axios from 'axios';
import Layout from "./components/layout/Layout";

const API_ROOT = 'http://127.0.0.1:8000/api/';
const getUrl = url => `${API_ROOT}${url}`;

const App = () => {
    const [isLoading, setLoading] = useState(true);
    const [employees, setEmployees] = useState();

    useEffect(() => {
        const headers = {'Content-Type': 'application/json'}
        axios
            .get(getUrl('employees/'), {headers})
            .then(response => {
                setEmployees(response.data.results);
                setLoading(false)
            })
            .catch((error) => console.log(error));
    }, [])

    if(isLoading){
        return <div className="App">Loading...</div>;
    }

    return (
        <BrowserRouter>
            <Layout>
                <Switch>
                    <Route exact path='/'>
                        <OrgChart nodes={employees}/>
                    </Route>
                </Switch>
            </Layout>
        </BrowserRouter>
    );
}

export default App;
