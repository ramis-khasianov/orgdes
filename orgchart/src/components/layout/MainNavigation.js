import {Link} from 'react-router-dom';
import classes from './MainNavigation.module.css'

const MainNavigation = () => {

    return (
        <header className={classes.header}>
            <div className={classes.logo}>Ural Talent Manager</div>
            <nav>
                <ul>
                    <li>
                        <Link to="/">Структура</Link>
                    </li>
                    <li>
                        <Link to="/change-requests">Заявки</Link>
                    </li>
                    <li>
                        <Link to="/forecast">Прогноз</Link>
                    </li>
                </ul>
            </nav>
        </header>
    );
}

export default MainNavigation;
