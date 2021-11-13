import {Link} from 'react-router-dom';
import classes from './Toolbar.module.css'

const Toolbar = () => {

    return (
        <div className={classes.toolbar}>
            <div className={classes.btn_group}>
                <Link to="/">Органиграмма</Link>
                <Link to="/table">Таблица</Link>
            </div>
            <div className={classes.btn_group}>
                <Link to="/admin">Административная</Link>
                <Link to="/functions">Функциональная</Link>
                <Link to="/projects">Проектные команды</Link>
            </div>
            <div className={classes.btn_group}>
                <Link to="/asis">Фактическая</Link>
                <Link to="/modeled">Моделирование</Link>
            </div>
            <div>
                <Link className={classes.btn}>Изменения</Link>
            </div>
        </div>
    );
}

export default Toolbar;