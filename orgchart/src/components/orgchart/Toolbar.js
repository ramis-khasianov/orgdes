import {useContext} from 'react';
import classes from './Toolbar.module.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCog } from '@fortawesome/free-solid-svg-icons'
import OptionsContext from "../options/options-context";

const Toolbar = () => {

    const optionsContext = useContext(OptionsContext);

    return (
        <div className={classes.toolbar}>
            <div className={classes.btn_group}>
                <button
                    onClick={optionsContext.toggleViewType}
                    className={optionsContext.viewType === 'organigramm' ? classes.btn_active : classes.btn_not_active}
                >Органиграмма
                </button>
                <button
                    onClick={optionsContext.toggleViewType}
                    className={optionsContext.viewType === 'table' ? classes.btn_active : classes.btn_not_active}
                >Таблица</button>
            </div>
            <div className={classes.btn_group}>
                <button
                    onClick={optionsContext.toggleHierarchyType}
                    className={optionsContext.hierarchyType === 'administrative' ? classes.btn_active : classes.btn_not_active}
                >Административная
                </button>
                <button
                    onClick={optionsContext.toggleHierarchyType}
                    className={optionsContext.hierarchyType === 'functional' ? classes.btn_active : classes.btn_not_active}
                >Функциональная
                </button>
            </div>
            <div className={classes.btn_group}>
                <button
                    onClick={optionsContext.toggleVersionType}
                    className={optionsContext.versionType === 'asis' ? classes.btn_active : classes.btn_not_active}>
                    Фактическая
                </button>
                <button
                    onClick={optionsContext.toggleVersionType}
                    className={optionsContext.versionType === 'modeled' ? classes.btn_active : classes.btn_not_active}>
                    С изменениями
                </button>
            </div>
            <div className={classes.btn}>
                <button className={classes.btn}>
                    <FontAwesomeIcon icon={faCog} />
                </button>
            </div>

            <div>
                <button
                    className={classes.btn}
                >Изменения
                </button>
            </div>
        </div>
    );
}

export default Toolbar;