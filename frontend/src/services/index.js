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

export const depositCoin = (data) => {
  return axios.patch('/accounts/deposit/', data);
};
