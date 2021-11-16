import React from 'react';
import ReactDOM from 'react-dom';
import {BrowserRouter} from 'react-router-dom'
import './index.css';
import App from './App';
import {OptionsContextProvider} from "./components/options/options-context";
import {ChangeContextProvider} from "./components/changes/changes-contex";

ReactDOM.render(
    <OptionsContextProvider>
        <ChangeContextProvider>
            <BrowserRouter>
                <App />
            </BrowserRouter>
        </ChangeContextProvider>
    </OptionsContextProvider>,
    document.getElementById('root')
);
