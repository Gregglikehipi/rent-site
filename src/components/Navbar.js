import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Navbar.css';

const Navbar = () => {
    const navigate = useNavigate();

    return (
        <nav className="navbar">
            <button onClick={() => navigate('/')} className="nav-button">
                Главная страница
            </button>
            <button onClick={() => navigate('/create')} className="nav-button">
                Создать публикацию
            </button>
            <button onClick={() => navigate('/filters')} className="nav-button">
                Фильтры
            </button>
            <button onClick={() => navigate('/products')} className="nav-button">
                Товары
            </button>
            <button onClick={() => navigate('/profile')} className="nav-button">
                Профиль
            </button>
        </nav>
    );
};

export default Navbar;
