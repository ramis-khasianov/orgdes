import {createContext, useState} from 'react';

const OptionsContext = createContext({
    viewType: 'organigramm',
    hierarchyType: 'administrative',
    versionType: 'asis',
    toggleViewType: () => {},
    toggleHierarchyType: () => {},
    toggleVersionType: () => {}
});

export const OptionsContextProvider = (props) => {
    const [selectedViewType, setViewType] = useState('organigramm');
    const [selectedHierarchyType, setHierarchyType] = useState('administrative');
    const [selectedVersionType, setVersionType] = useState('asis');

    const toggleViewTypeHandler = () => {
        if(selectedViewType === 'organigramm'){
            setViewType('table')
        } else {
            setViewType('organigramm')
        }
    }

    const toggleHierarchyTypeHandler = () => {
        if(selectedHierarchyType === 'administrative'){
            setHierarchyType('functional')
        } else {
            setHierarchyType('administrative')
        }
    }

    const toggleVersionTypeHandler = () => {
        if(selectedVersionType === 'asis'){
            setVersionType('modeled')
        } else {
            setVersionType('asis')
        }
    }

    const context = {
        viewType: selectedViewType,
        hierarchyType: selectedHierarchyType,
        versionType: selectedVersionType,
        toggleViewType: toggleViewTypeHandler,
        toggleHierarchyType: toggleHierarchyTypeHandler,
        toggleVersionType: toggleVersionTypeHandler
    };

    return (
        <OptionsContext.Provider value={context}>
            {props.children}
        </OptionsContext.Provider>
    );
}

export default OptionsContext;
