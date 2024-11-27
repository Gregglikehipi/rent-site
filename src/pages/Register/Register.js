// src/pages/Register/Register.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Register.css';

const Register = () => {
    const navigate = useNavigate();

    const [fullName, setFullName] = useState('');
    const [city, setCity] = useState('');
    const [address, setAddress] = useState('');
    const [email, setEmail] = useState('');
    const [phone, setPhone] = useState('');
    const [password, setPassword] = useState('');
    const [errors, setErrors] = useState({}); // Состояние для ошибок

    const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    const phonePattern = /^[0-9]{10}$/;

    const handleSubmit = (e) => {
        e.preventDefault();
        const newErrors = {};

        if (!fullName) newErrors.fullName = 'Введите ФИО';
        if (!city) newErrors.city = 'Введите город';
        if (!address) newErrors.address = 'Введите полный адрес';
        if (!email) newErrors.email = 'Введите почту';
        else if (!emailPattern.test(email)) newErrors.email = 'Введите корректный email';
        if (!phone) newErrors.phone = 'Введите номер телефона';
        else if (!phonePattern.test(phone)) newErrors.phone = 'Введите корректный номер телефона (10 цифр)';
        if (!password) newErrors.password = 'Введите пароль';

        setErrors(newErrors);

        if (Object.keys(newErrors).length === 0) {
            console.log('Форма отправлена');
            // Логика регистрации
        }
    };

    return (
        <div className="container">
            <h1>Регистрация</h1>
            <form className="form" onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="ФИО"
                    value={fullName}
                    onChange={(e) => setFullName(e.target.value)}
                />
                {errors.fullName && <div className="error">{errors.fullName}</div>}
                <input
                    type="text"
                    placeholder="Город"
                    value={city}
                    onChange={(e) => setCity(e.target.value)}
                />
                {errors.city && <div className="error">{errors.city}</div>}
                <input
                    type="text"
                    placeholder="Полный адрес"
                    value={address}
                    onChange={(e) => setAddress(e.target.value)}
                />
                {errors.address && <div className="error">{errors.address}</div>}
                <input
                    type="email"
                    placeholder="Почта"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
                {errors.email && <div className="error">{errors.email}</div>}
                <input
                    type="tel"
                    placeholder="Номер телефона"
                    value={phone}
                    onChange={(e) => setPhone(e.target.value)}
                />
                {errors.phone && <div className="error">{errors.phone}</div>}
                <input
                    type="password"
                    placeholder="Пароль"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                {errors.password && <div className="error">{errors.password}</div>}
                <button type="submit" className="button">
                    Зарегистрироваться
                </button>
            </form>
            <button onClick={() => navigate('/')} className="link-button">
                Вернуться ко входу
            </button>
        </div>
    );
};

export default Register;
