import axios from '@util/axios';

export const signup = (data) => {
    return axios.post('/users/signup/', data);
};

export const login = (data) => {
    return axios.post('/users/login/', data);
};

export const getCoins = () => {
    return axios.get('/coins/');
};

export const createCoin = (data) => {
    return axios.post('/coins/', data);
};

export const depositCoins = (data) => {
    return axios.patch('/accounts/deposit/', data);
};

export const sendCoins = (data) => {
    return axios.patch('/accounts/send/', data);
};

export const getAccountBalances = () => {
    return axios.get('/accounts/balances/');
};

export const getCoinUserBalance = (coin) => {
    return axios.get(`/accounts/coins/?coin=${coin}`);
};

export const getAccountTransactions = () => {
    return axios.get('/transactions/accounts/');
};

export const getGlobalTransactions = () => {
    return axios.get('/transactions/');
};

export const getCoinBalancesByUsers = () => {
    return axios.get('/balances/');
};
