import {useState} from "react";
import classes from './LoginForm.module.css'

const LoginForm = ({getToken}) => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');


    const handleUsernameChange = (event) => {
        setUsername(event.target.value)
    }

    const handlePasswordChange = (event) => {
        setPassword(event.target.value)
    }

    const handleSubmit = (event) => {
        event.preventDefault()
        console.log(username, password)
        getToken(username, password)
    }

    return (
        <div className={classes.form_box} >
            <div className={classes.header}>Войти в систему</div>
            <form className={classes.form} onSubmit={(event) => handleSubmit(event)}>
                    <label htmlFor={'username'}>Логин</label>
                    <input type={'text'} name={'username'} id={'username'} placeholder={'ivan.petrov'}
                           value={username}
                           onChange={(event => handleUsernameChange(event))}/>
                    <label htmlFor={'password'}>Пароль</label>
                    <input type={'password'} name={'password'} id={'password'} placeholder={'Ваш пароль'}
                           value={password}
                           onChange={(event => handlePasswordChange(event))}/>
                <input type={'submit'} value={'Войти'}/>
            </form>
        </div>
    )
}

export default LoginForm