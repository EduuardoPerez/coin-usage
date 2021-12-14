import React from 'react';
import { Link } from 'react-router-dom';
import '@styles/Home.scss';

const Home = () => {
	return (
		<div className="home">
			<div className="home-container">
				<Link to="/create-coin">
					<button className="primary-button">
						Create a coin
					</button>
				</Link>
				<Link to="/deposit-coins">
					<button className="primary-button">
						Deposit coins
					</button>
				</Link>
				<Link to="/send-coins">
					<button className="primary-button">
						Send coins
					</button>
				</Link>
				<Link to="/account-balances">
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
