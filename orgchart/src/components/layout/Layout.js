import MainNavigation from './MainNavigation';
import classes from './Layout.module.css'
import Toolbar from "./Toolbar";

const Layout = (props) => {
    return (
        <div>
            <MainNavigation/>
            <Toolbar/>
            <main className={classes.main}>{props.children}</main>
        </div>
    )
}

export default Layout;
