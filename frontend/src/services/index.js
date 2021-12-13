import axios from '@util/axios';

export const signup = data => {
  return axios.post('/users/signup/', data);
};

export const login = data => {
  return axios.post('/users/login/', data);
};
