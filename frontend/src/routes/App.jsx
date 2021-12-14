import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import Layout from '@containers/Layout';
import Home from '@pages/Home';
import Login from '@pages/Login';
import CreateAccount from '@pages/CreateAccount';
import NotFound from '@pages/NotFound';
import DepositCoins from '@pages/DepositCoins';
import CreateCoin from '@pages/CreateCoin';
import SendCoins from '@pages/SendCoins';
import AccountBalances from '@pages/AccountBalances';
import CoinBalance from '@pages/CoinBalance';
import AccountTransactions from '@pages/AccountTransactions';
import GlobalTransactions from '@pages/GlobalTransactions';
import CoinsBalancesByUsers from '@pages/CoinsBalancesByUsers';
import AppContext from '@context/AppContext';
import useInitialState from '@hooks/useInitialState';
import '@styles/global.css';

const App = () => {
	const initialState = useInitialState();
	return (
		<AppContext.Provider value={initialState}>
			<BrowserRouter>
				<Layout>
					<Switch>
						<Route exact path="/" component={Home} />
						<Route exact path="/signup" component={CreateAccount} />
						<Route exact path="/login" component={Login} />
						<Route exact path="/deposit-coins" component={DepositCoins} />
						<Route exact path="/create-coin" component={CreateCoin} />
						<Route exact path="/send-coins" component={SendCoins} />
						<Route exact path="/account-balances" component={AccountBalances} />
						<Route exact path="/coin-balance" component={CoinBalance} />
						<Route exact path="/account-transactions" component={AccountTransactions} />
						<Route exact path="/global-transactions" component={GlobalTransactions} />
						<Route exact path="/coins-balances" component={CoinsBalancesByUsers} />
						<Route path="*" component={NotFound} />
					</Switch>
				</Layout>
			</BrowserRouter>
		</AppContext.Provider>
	);
}

export default App;
