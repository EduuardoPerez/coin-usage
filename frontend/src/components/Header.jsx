import React, { useState, useContext, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { AppContext } from '@context/AppContext';
import '@styles/Header.scss';
import logo from '@logos/rpc_coin.svg';

const Header = () => {
	const { removeAuth, isAuth } = useContext(AppContext)
	const [userName, setUserName] = useState('');

	useEffect(() => {
		localStorage.getItem('USERNAME') && setUserName(localStorage.getItem('USERNAME'));
	}, []);

	const handleLogout = () => {
		removeAuth();
		setUserName('');
	}


	const logOutComponent = (isAuth) ? <a href="/login">logout</a> : null;

	return (
		<nav>
			<div className="navbar-left">
				<Link to="/">
					<img src={logo} alt="logo" className="nav-logo" />
				</Link>
			</div>
			<div className="navbar-right">
				<ul>
					<li className="navbar-username">
						{userName}
					</li>
					<li onClick={handleLogout}>
						{logOutComponent}
					</li>
				</ul>
			</div>
		</nav>
	);
}

export default Header;
