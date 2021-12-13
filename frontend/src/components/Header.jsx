import React, { useState, useEffect } from 'react';
import '@styles/Header.scss';
import logo from '@logos/rpc_coin.svg';

const Header = () => {
	const [isLoggedIn, setIsLoggedIn] = useState(false);

	useEffect(() => {
		if (localStorage.getItem('COIN_USAGE_TOKEN') !== null) {
			setIsLoggedIn(true);
		}
	}, []);

	const handleLogout = () => {
		localStorage.removeItem('COIN_USAGE_TOKEN')
		localStorage.removeItem('username')
		setIsLoggedIn(false);
	}


	const logOutComponent = (isLoggedIn) ? <a href="/login">logout</a> : null;

	return (
		<nav>
			<div className="navbar-left">
				<a href="/">
					<img src={logo} alt="logo" className="nav-logo" />
				</a>
			</div>
			<div className="navbar-right">
				<ul>
					<li
						className="navbar-email"
						onClick={handleLogout}
					>
						{logOutComponent}
					</li>
				</ul>
			</div>
		</nav>
	);
}

export default Header;
