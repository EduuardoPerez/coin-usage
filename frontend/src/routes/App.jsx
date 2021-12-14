import React, { useContext } from 'react';
import { BrowserRouter, Switch, Redirect } from 'react-router-dom';
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
import { AppContext } from '@context/AppContext';
import '@styles/global.css';

const App = () => {
	const { isAuth, isAdmin } = useContext(AppContext)

	return (
		<BrowserRouter>
			<Layout>
				<Switch>
					<GlobalTransactions exact path="/global-transactions" />
					{!isAuth && <CreateAccount exact path="/signup" />}
					{!isAuth && <Login exact path="/login" />}
					{!isAuth && <Redirect from="/" to='/login' />}
					{!isAuth && <Redirect from="/deposit-coins" to='/login' />}
					{(!isAuth || !isAdmin) && < Redirect from="/create-coin" to='/login' />}
					{!isAuth && <Redirect from="/send-coins" to='/login' />}
					{!isAuth && <Redirect from="/account-balances" to='/login' />}
					{!isAuth && <Redirect from="/coin-balance" to='/login' />}
					{!isAuth && <Redirect from="/account-transactions" to='/login' />}
					{(!isAuth || !isAdmin) && <Redirect from="/coins-balances" to='/login' />}
					{isAuth && <Redirect from='/signup' to='/' />}
					{isAuth && <Redirect from='/login' to='/' />}
					<Home exact path="/" />
					<DepositCoins exact path="/deposit-coins" />
					<CreateCoin exact path="/create-coin" />
					<SendCoins exact path="/send-coins" />
					<AccountBalances exact path="/account-balances" />
					<CoinBalance exact path="/coin-balance" />
					<AccountTransactions exact path="/account-transactions" />
					<CoinsBalancesByUsers exact path="/coins-balances" />
					<NotFound default />
				</Switch>
			</Layout>
		</BrowserRouter>
	);
}

export default App;
