import React, { useRef, useState } from 'react';
import { Link } from 'react-router-dom';
import { login } from '@services'
import Error from '@components/Error';
import '@styles/Login.scss';
import logo from '@logos/rpc_coin.svg'

const Login = () => {
	const form = useRef(null);
	const [error, setError] = useState(false);
	const [errorMessage, setErrorMessage] = useState('');

	const handleSubmit = (e) => {
		e.preventDefault();
		const formData = new FormData(form.current);
		const username = formData.get('username');
		const password = formData.get('password');

		if (username === '' || password === '') {
			setError(true);
			setErrorMessage('username and password are required.');
			return;
		}

		const data = {
			username: username,
			password: password,
		}

		login(data)
			.then((res) => {
				setError(false);
				localStorage.setItem('username', username);
				localStorage.setItem('COIN_USAGE_TOKEN', res.data.access_token);
				window.location.href = '/';
			})
			.catch((error) => {
				setError(true);
				const res = error.response.data;
				let errMsgs = '';
				Object.entries(res).forEach((err) => {
					const [key, value] = err;
					errMsgs += `${key}: ${value}\n`;
				});
				setErrorMessage(errMsgs);
			});
	}

	const errorComponent = (error) ? <Error message={errorMessage} /> : null;

	return (
		<div className="Login">
			<div className="Login-container">
				<img src={logo} alt="logo" className="logo" />
				<form action="/" className="form" ref={form}>
					{errorComponent}
					<label htmlFor="username" className="label">Username</label>
					<input type="text" name="username" placeholder="SatNak" className="input input-email" />
					<label htmlFor="password" className="label">Password</label>
					<input type="password" name="password" placeholder="*********" className="input input-password" />
					<button
						onClick={handleSubmit}
						className="primary-button login-button">
						Log in
					</button>
				</form>
				<Link to="/signup">
					<button className="secondary-button signup-button">
						Sign up
					</button>
				</Link>
			</div>
		</div >
	);
}

export default Login;
