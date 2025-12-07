// src/utils/apiConfig.js
import axios from 'axios';

// PRODUCTION: Use production URL
// const api = axios.create({
//   baseURL: 'https://tutomart.com/api',
//   withCredentials: true,
//   headers: {
//     'Content-Type': 'application/json'
//   }
// });

// LOCALHOST: Use local development URL
const api = axios.create({
  baseURL: 'http://localhost:8080/api',
  withCredentials: true,
  headers: {
    'Content-Type': 'application/json'
  }
});

// Add response interceptor for better error handling
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Auto-logout on 401
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export default api;