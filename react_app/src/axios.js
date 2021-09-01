import axios from 'axios';

const baseURL = 'http://127.0.0.1:8000/api/';
const token = "";
//localStorage.getItem('token');

const axiosInstance = axios.create({
	baseURL: baseURL,
	timeout: 5000,
	headers: {
		Authorization: localStorage.getItem('token')
        ? 'Token ' + localStorage.getItem('token')
        : null,
		'Content-Type': 'application/json',
		accept: 'application/json',
	}, 

});

export default axiosInstance;
