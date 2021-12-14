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

export const depositCoins = (data) => {
  return axios.patch('/accounts/deposit/', data);
};

export const sendCoins = (data) => {
  return axios.patch('/accounts/send/', data);
};

export const getAccountBalances = () => {
  return axios.get('/accounts/balances/');
};

export const getAccountTransactions = () => {
  return axios.get('/transactions/accounts/');
};

export const getGlobalTransactions = () => {
  return axios.get('/transactions/');
};
