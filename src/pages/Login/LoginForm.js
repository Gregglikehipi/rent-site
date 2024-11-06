// src/pages/Login/LoginForm.js
import React from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import './Login.css';
import axios from 'axios';

const LoginForm = () => {
    // Схема валидации для формы входа
    const validationSchema = Yup.object().shape({
        username: Yup.string()
            .required('Введите ваш логин'),
        password: Yup.string()
            .required('Введите ваш пароль')
    });

    // Функция отправки данных формы
    const handleSubmit = async (values, { setSubmitting }) => {
        setSubmitting(true);
        try {
            // Пример отправки данных формы на сервер (замените URL на реальный)
            const response = await axios.post('/api/login', values);
            console.log('Успешный вход:', response.data);
        } catch (error) {
            console.error('Ошибка входа:', error);
        } finally {
            setSubmitting(false);
        }
    };

    return (
        <Formik
            initialValues={{ username: '', password: '' }}
            validationSchema={validationSchema}
            onSubmit={handleSubmit}
        >
            {({ isSubmitting }) => (
                <Form className="login-form">
                    <div className="form-group">
                        <label htmlFor="username">Логин</label>
                        <Field type="text" name="username" placeholder="Введите логин" />
                        <ErrorMessage name="username" component="div" className="error" />
                    </div>
                    <div className="form-group">
                        <label htmlFor="password">Пароль</label>
                        <Field type="password" name="password" placeholder="Введите пароль" />
                        <ErrorMessage name="password" component="div" className="error" />
                    </div>
                    <button type="submit" disabled={isSubmitting}>
                        Войти
                    </button>
                </Form>
            )}
        </Formik>
    );
};

export default LoginForm;
