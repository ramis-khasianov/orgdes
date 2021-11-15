import React, {useEffect, useState} from 'react';
import {Route, Switch, Redirect, useHistory} from 'react-router-dom'
import OrgChart from './components/orgchart/MainChart';
import axios from 'axios';
import Layout from "./components/layout/Layout";
import Cookies from "universal-cookie/lib";
import LoginForm from "./components/auth/LoginForm";
import Toolbar from "./components/orgchart/Toolbar";

const API_ROOT = 'http://127.0.0.1:8000/';
const getUrl = url => `${API_ROOT}${url}`;

const App = () => {
    const [isLoading, setLoading] = useState(true);
    const [employees, setEmployees] = useState();
    const [userToken, setUserToken] = useState('')
    const [username, setUsername] = useState('')

    const history = useHistory();

    const isAuthenticated = () => {
        return userToken !== ''
    }

    const getTokenFromStorage = () => {
        const cookies = new Cookies()
        const token = cookies.get('token')
        const username = cookies.get('username')
        if (token !== null && username !== null) {
            setUserToken(token)
            setUsername(username)
        }
    }

    const getToken = (username, password) => {
        axios.post(getUrl('api/token-auth/'), {username: username, password: password})
            .then(response => {
                const token = response.data['token']
                const cookies = new Cookies()
                cookies.set('token', token)
                cookies.set('username', username)
                history.push('/')
                setUsername(username)
                setUserToken(token)
            })
            .catch(error => {
                console.log(error)
                alert('Неверный логин или пароль')
            })
    }

    const logout = () => {
        console.log('wtf')
        setUserToken('')
        setEmployees([])
        console.log(employees)
    };

    const loadData = () => {
        const headers = {'Content-Type': 'application/json'}
        axios
            .get(getUrl('api/orgchart/'), {headers})
            .then(response => {
                setEmployees(response.data.results);
                setLoading(false)
            })
            .catch((error) => console.log(error));
    }

    useEffect(() => {
        getTokenFromStorage()
        loadData()
    }, [])

    if(isLoading){
        return <div className="App">Loading...</div>;
    }

    return (
        <Layout isAuthenticated={isAuthenticated()} logoutAction={() => logout()} username={username}>
            <Switch>
                <Route exact path='/'>
                    <Toolbar/>
                    <OrgChart nodes={employees}/>
                </Route>
                <Route exacc path='/login'>
                    <LoginForm getToken={(username, password) => getToken(username, password)}/>
                </Route>
                <Redirect from={'/authenticated'} to={'/'}/>
            </Switch>
        </Layout>
    );
}

export default App;
