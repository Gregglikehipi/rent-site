import React from 'react';
import { Outlet, Link } from 'react-router-dom';
import './Layout.css'; // Убедитесь, что стили подключены правильно

const Layout = () => {
    return (
        <div className="layout">
            <header className="header">
                <nav className="nav">
                    <Link to="/">Главная страница</Link>
                    <Link to="/create">Создать публикацию</Link>
                    <Link to="/filters">Фильтры</Link>
                    <Link to="/products">Товары</Link>
                    <Link to="/profile">Профиль</Link>
                </nav>
            </header>
            <main className="content">
                <Outlet /> {/* Рендерит контент для всех страниц */}
            </main>
        </div>
    );
};

export default Layout;
