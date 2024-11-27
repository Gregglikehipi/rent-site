import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const HomePage = () => {
    const [search, setSearch] = useState('');
    const [products] = useState([
        { id: 1, name: 'Товар 1', category: 'Категория A', price: 100, description: 'Описание товара 1', status: 'Свободно' },
        { id: 2, name: 'Товар 2', category: 'Категория B', price: 200, description: 'Описание товара 2', status: 'В аренде' },
        { id: 3, name: 'Товар 3', category: 'Категория A', price: 150, description: 'Описание товара 3', status: 'Свободно' },
    ]);

    const filteredProducts = products.filter((product) =>
        product.name.toLowerCase().includes(search.toLowerCase()) ||
        product.category.toLowerCase().includes(search.toLowerCase())
    );

    return (
        <div>
            <h1>Главная страница</h1>
            <input
                type="text"
                placeholder="Поиск"
                value={search}
                onChange={(e) => setSearch(e.target.value)}
            />
            <div>
                {filteredProducts.map((product) => (
                    <div key={product.id}>
                        <h2>{product.name}</h2>
                        <p>Категория: {product.category}</p>
                        <p>Цена: {product.price}₽</p>
                        <Link to={`/product/${product.id}`}>Подробнее</Link>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default HomePage;
