import {createContext, useState} from 'react';

const ChangesContext = createContext({
    changes_count: 0,
    changes: [],
    addChange: (change) => {}
});

export const ChangeContextProvider = (props) => {
    const [changes, setChanges] = useState([]);

    const addChangeHandler = (change) => {
        setChanges((previousChanges) => {
            return previousChanges.concat(change);
        });
    }

    const context = {
        changes_count: changes.length,
        addChange: addChangeHandler
    }

    return (
        <ChangesContext.Provider value={context}>
            {props.children}
        </ChangesContext.Provider>
    );
}

export default ChangesContext;
