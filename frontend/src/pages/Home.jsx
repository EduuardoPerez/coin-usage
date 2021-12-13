import React from 'react';
import { Link } from 'react-router-dom';
import '@styles/Home.scss';

const Home = () => {
	return (
		<div className="home">
			<div className="home-container">
				<Link to="/send-coin">
					<button className="primary-button">
						Send coins
					</button>
				</Link>
				<Link to="/balances">
					<button className="primary-button">
						Show balances
					</button>
				</Link>
				<Link to="/account-transactions">
					<button className="primary-button">
						Show account transactions
					</button>
				</Link>
				<Link to="/global-transactions">
					<button className="primary-button">
						Show global transactions
					</button>
				</Link>
			</div>
		</div>
	);
}

export default Home;
