import React from 'react';
import { useParams } from 'react-router-dom';
import './ProductPage.css';

const ProductPage = () => {
    const { id } = useParams(); // Получаем параметр id из URL

    // Пример данных о товаре
    const product = {
        id: 1,
        name: 'Диван',
        category: 'Мебель',
        price: 3000,
        description: 'Удобный и стильный диван для вашей гостиной.',
        status: 'Свободно',
        seller: {
            name: 'Иван Иванов',
            phone: '8-800-555-35-35',
        },
        images: [
            'https://via.placeholder.com/150',
            'https://via.placeholder.com/150',
            'https://via.placeholder.com/150',
        ],
    };

    // Если товар не найден
    if (!product) {
        return <h1>Товар не найден</h1>;
    }

    return (
        <div className="product-page">
            <h1>{product.name}</h1>
            <div className="product-images">
                {product.images.map((image, index) => (
                    <img key={index} src={image} alt={`${product.name} ${index + 1}`} />
                ))}
            </div>
            <div className="product-details">
                <p><strong>Категория:</strong> {product.category}</p>
                <p><strong>Цена:</strong> {product.price}₽</p>
                <p><strong>Описание:</strong> {product.description}</p>
                <p><strong>Статус:</strong> {product.status}</p>
            </div>
            <div className="seller-info">
                <h3>Карточка продавца</h3>
                <p><strong>Имя:</strong> {product.seller.name}</p>
                <p><strong>Телефон:</strong> {product.seller.phone}</p>
                <button className="chat-button">Написать в чат</button>
            </div>
            <button className="rent-button">Арендовать</button>
        </div>
    );
};

export default ProductPage;
