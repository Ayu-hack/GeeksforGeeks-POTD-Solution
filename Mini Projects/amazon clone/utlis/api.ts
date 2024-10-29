import axios from 'axios';

const api = axios.create({
    baseURL: 'http://localhost:5000', // Flask API endpoint
});

export const getProducts = async () => {
    const response = await api.get('/products');
    return response.data;
};

export const getProductById = async (id: string) => {
    const response = await api.get(`/products/${id}`);
    return response.data;
};

export const createProduct = async (product: { id: string; title: string; description: string; price: number; image: string }) => {
    const response = await api.post('/products', product);
    return response.data;
};

export const updateProduct = async (id: string, product: { title?: string; description?: string; price?: number; image?: string }) => {
    const response = await api.put(`/products/${id}`, product);
    return response.data;
};

export const deleteProduct = async (id: string) => {
    const response = await api.delete(`/products/${id}`);
    return response.data;
};
