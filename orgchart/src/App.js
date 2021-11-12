import React, {useEffect, useState} from 'react';
import OrgChart from './mychart';
import axios from 'axios';

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
        <div style={{height: '100%'}}>
            <OrgChart nodes={employees}/>
        </div>
    );
}

export default App;
