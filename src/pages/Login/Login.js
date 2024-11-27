// src/pages/Login/Login.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Login.css';

const Login = () => {
    const navigate = useNavigate();

    const [login, setLogin] = useState('');
    const [password, setPassword] = useState('');
    const [errors, setErrors] = useState({}); // Состояние для ошибок

    const handleSubmit = (e) => {
        e.preventDefault();
        const newErrors = {};

        if (!login) newErrors.login = 'Введите логин';
        if (!password) newErrors.password = 'Введите пароль';

        setErrors(newErrors);

        if (Object.keys(newErrors).length === 0) {
            navigate('/product');
        }
    };




    return (
        <div className="container">
            <h1>Вход</h1>
            <form className="form" onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Логин"
                    value={login}
                    onChange={(e) => setLogin(e.target.value)}
                />
                {errors.login && <div className="error">{errors.login}</div>}
                <input
                    type="password"
                    placeholder="Пароль"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                {errors.password && <div className="error">{errors.password}</div>}
                <button type="submit" className="button">
                    Войти
                </button>
            </form>
            <button onClick={() => navigate('/register')} className="link-button">
                Регистрация
            </button>
        </div>
    );
};

export default Login;
