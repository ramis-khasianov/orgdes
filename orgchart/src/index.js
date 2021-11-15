import React from 'react';
import ReactDOM from 'react-dom';
import {BrowserRouter} from 'react-router-dom'
import './index.css';
import App from './App';
import {OptionsContextProvider} from "./components/options/options-context";

ReactDOM.render(
    <OptionsContextProvider>
        <BrowserRouter>
            <App />
        </BrowserRouter>
    </OptionsContextProvider>,
    document.getElementById('root')
);
