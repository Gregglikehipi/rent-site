// src/pages/Login/Login.js
import React from 'react';
import LoginForm from './LoginForm';
import './Login.css';

const Login = () => {
    return (
        <div className="login-container">
            <h2>Вход</h2>
            <LoginForm />
        </div>
    );
};

export default Login;
