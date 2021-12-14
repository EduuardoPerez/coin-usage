import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import { AppContext } from '@context/AppContext';
import '@styles/Home.scss';

const Home = () => {
	const { isAdmin } = useContext(AppContext)

	return (
		<div className="home">
			<div className="home-container">
				{
					isAdmin ? (
						<Link to="/create-coin">
							<button className="primary-button">
								Create a coin
							</button>
						</Link>) : null
				}
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
						Balances
					</button>
				</Link>
				<Link to="/coin-balance">
					<button className="primary-button">
						Balance of a coin
					</button>
				</Link>
				<Link to="/account-transactions">
					<button className="primary-button">
						Account transactions
					</button>
				</Link>
				<Link to="/global-transactions">
					<button className="primary-button">
						Global transactions
					</button>
				</Link>
				{
					isAdmin ? (
						<Link to="/coins-balances">
							<button className="primary-button">
								Balance of each coin by users
							</button>
						</Link>) : null
				}
			</div>
		</div>
	);
}

export default Home;
