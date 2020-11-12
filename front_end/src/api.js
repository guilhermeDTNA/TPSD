import axios from 'axios';

const api = axios.create({
    baseURL: 'http://localhost:8000/consulta_objetos?&format=json&'
});

export default api;