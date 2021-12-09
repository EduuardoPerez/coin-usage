import React, { useState, useContext } from 'react';
import '@styles/Header.scss';
import logo from '@logos/rpc_coin.svg';
import AppContext from '@context/AppContext';

const Header = () => {

	return (
		<nav>
			<div className="navbar-left">
				<img src={logo} alt="logo" className="nav-logo" />
			</div>
			<div className="navbar-right">
				<ul>
					<li className="navbar-email">
						coin-usage@example.com
					</li>
				</ul>
			</div>
		</nav>
	);
}

export default Header;
