import React, { useRef, useState } from 'react';
import { Link } from 'react-router-dom';
import { signup } from '@services'
import Error from '@components/Error';
import CreateAccountSuccessfully from '@components/CreateAccountSuccessfully';
import '@styles/CreateAccount.scss';

const CreateAccount = () => {
	const form = useRef(null);
	const [error, setError] = useState(false);
	const [errorMessage, setErrorMessage] = useState('');
	const [signupSuccess, setSignupSuccess] = useState(false);

	const handleSubmit = (e) => {
		e.preventDefault();
		const formData = new FormData(form.current);

		const firstName = formData.get('first-name');
		const lastName = formData.get('last-name');
		const username = formData.get('username');
		const email = formData.get('email');
		const password = formData.get('password');
		const passwordConfirmation = formData.get('password-confirmation');

		if (username === '' || email === '' || password === '' || passwordConfirmation === '') {
			setError(true);
			setErrorMessage('username, email, password and password confirmation are required.');
			return;
		}
		if (password !== passwordConfirmation) {
			setError(true);
			setErrorMessage('password and password confirmation don\'t match.');
			return;
		}

		const data = {
			first_name: firstName,
			last_name: lastName,
			username: username,
			email: email,
			password: password,
			password_confirmation: passwordConfirmation,
		};

		signup(data)
			.then(() => {
				setSignupSuccess(true);
				setError(false);
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
	const signupButton = <button type="submit" className="primary-button login-button" onClick={handleSubmit}>Create account</button>
	const signupComponent = (signupSuccess) ? <CreateAccountSuccessfully /> : signupButton;

	return (
		<div className="CreateAccount">
			<div className="CreateAccount-container">
				<h1 className="title">New account</h1>
				<form action="/" className="form" ref={form}>
					{errorComponent}
					<div>
						<label htmlFor="first-name" className="label">First name</label>
						<input type="text" name="first-name" id="first-name" placeholder="Satoshi" className="input input-name" />
						<label htmlFor="last-name" className="label">Last name</label>
						<input type="text" name="last-name" id="last-name" placeholder="Nakamoto" className="input input-name" />
						<label htmlFor="username" className="label">Username</label>
						<input type="text" name="username" id="username" placeholder="SatNak" className="input input-name" />
						<label htmlFor="email" className="label">Email</label>
						<input type="text" name="email" id="email" placeholder="satoshi@nakamoto.com" className="input input-email" />
						<label htmlFor="password" className="label">Password</label>
						<input type="password" name="password" id="password" placeholder="*********" className="input input-password" />
						<label htmlFor="password-confirmation" className="label">Password confirmation</label>
						<input type="password" name="password-confirmation" id="password-confirmation" placeholder="*********" className="input input-password" />
					</div>
					{signupComponent}
					<Link to="/login">
						<button className="secondary-button signup-button">
							Login
						</button>
					</Link>
				</form>
			</div>
		</div>
	);
}

export default CreateAccount;
