import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './pages/Login/Login';
import Register from './pages/Register/Register';
import HomePage from './pages/HomePage/HomePage';
import ProductPage from './pages/ProductPage/ProductPage';
import Layout from './components/Layout/Layout';

function App() {
    return (
        <Router>
            <Routes>
                <Route element={<Layout />}>
                    {/* Страница главная */}
                    <Route path="/" element={<HomePage />} />

                    {/* Страница товара */}
                    <Route path="/product/:id" element={<ProductPage />} />

                </Route>

                {/* Страница входа */}
                <Route path="/login" element={<Login />} />

                {/* Страница регистрации */}
                <Route path="/register" element={<Register />} />
            </Routes>
        </Router>
    );
}

export default App;

