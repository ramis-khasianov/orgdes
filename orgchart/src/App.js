import React, {useEffect, useState} from 'react';
import {BrowserRouter, Route, Switch} from 'react-router-dom'
import OrgChart from './components/orgchart/MainChart';
import axios from 'axios';
import Layout from "./components/layout/Layout";

const API_ROOT = 'http://127.0.0.1:8000/';
const getUrl = url => `${API_ROOT}${url}`;

const App = () => {
    const [isLoading, setLoading] = useState(true);
    const [employees, setEmployees] = useState();

    const prepOrgchart = (apiResults) => {
        let orgchartData = []

        for (let i = 0; i < apiResults.length; i++) {
            let staffPosition = apiResults[i]

            if (staffPosition.employees.length > 0) {
                let employees = apiResults[i].employees

                for (let e = 0; e < apiResults[i].employees.length; e++) {
                    console.log(staffPosition.managerGuid)
                    let pid = '0'
                    if (staffPosition.managerGuid != null) {
                        pid = `${staffPosition.managerGuid}_${staffPosition.managerEmployeeGuid}`
                    }

                    let orgchartEmployee = {
                        'id': `${staffPosition.guid}_${employees[e].guid}`,
                        'pid': pid,
                        'title': `${staffPosition.title}`,
                        'img': `${API_ROOT}media/${employees[e].img}`
                    }
                    orgchartData.push(orgchartEmployee)
                }
            }
        }

        console.log(orgchartData)
        return orgchartData
    }


    useEffect(() => {
        const headers = {'Content-Type': 'application/json'}
        axios
            .get(getUrl('api/orgchart/'), {headers})
            .then(response => {
                const orgchartData = prepOrgchart(response.data.results);
                setEmployees(orgchartData);
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
