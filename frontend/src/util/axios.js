import axios from 'axios';

const BASE_API_URL = 'http://localhost:8000';

const api = axios.create({
    baseURL: BASE_API_URL,
});

api.interceptors.request.use(
    config => {
        const token = localStorage.getItem('COIN_USAGE_TOKEN') || null;
        if (token) {
            if (!config.headers['Content-type']) {
                config.headers['Content-type'] = 'application/json';
            }
            config.headers.Authorization = `Token ${token}`;
        }
        return config;
    },
    err => Promise.reject(err)
);

api.interceptors.response.use(
    response => response,
    error => {
        if (!error.response) {
            console.log('Please check your internet connection.');
        }

        if (error.response.status === 401) {
            console.log('error 401?');
            localStorage.removeItem('COIN_USAGE_TOKEN');
            localStorage.removeItem('username');
            window.location.href = '/login';
        }
        return Promise.reject(error);
    }
);

export default api;
