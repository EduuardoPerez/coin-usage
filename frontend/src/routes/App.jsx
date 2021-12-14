import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import Layout from '@containers/Layout';
import Home from '@pages/Home';
import Login from '@pages/Login';
import CreateAccount from '@pages/CreateAccount';
import NotFound from '@pages/NotFound';
import DepositCoins from '@pages/DepositCoins';
import SendCoins from '@pages/SendCoins';
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
						<Route exact path="/send-coins" component={SendCoins} />
						<Route path="*" component={NotFound} />
					</Switch>
				</Layout>
			</BrowserRouter>
		</AppContext.Provider>
	);
}

export default App;
