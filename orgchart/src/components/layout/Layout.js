import MainNavigation from './MainNavigation';
import classes from './Layout.module.css'

const Layout = (props) => {
    return (
        <div>
            <MainNavigation
                isAuthenticated={props.isAuthenticated}
                logoutAction={() => {props.logoutAction()}}
                username={props.username}
            />
            <main className={classes.main}>{props.children}</main>
        </div>
    )
}

export default Layout;
