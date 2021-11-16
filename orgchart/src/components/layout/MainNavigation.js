import {Link} from 'react-router-dom';
import classes from './MainNavigation.module.css'

const MainNavigation = ({isAuthenticated, logoutAction, username}) => {
    let loginButton = ''
    if (isAuthenticated) {
        loginButton = <div className={classes.user_profile_items}>
            <div className={classes.user_profile_item}>{username}</div>
            <div className={classes.user_profile_item} onClick={logoutAction}>Выйти</div>
        </div>
    } else {
        loginButton = <div className={classes.user_profile_items}><Link to={'/login'}>Войти</Link></div>
    }

    return (
        <header className={classes.header}>
            <div className={classes.logo}>Orgdes Talent Manager</div>
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
            <div className={classes.user_profile}>
                {loginButton}
            </div>
        </header>
    );
}

export default MainNavigation;
