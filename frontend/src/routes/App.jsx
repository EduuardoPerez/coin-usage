import React from 'react';
import { BrowserRouter } from 'react-router-dom';
import AppContext from '@context/AppContext';
import useInitialState from '@hooks/useInitialState';
import '@styles/global.css';

const App = () => {
	const initialState = useInitialState();
	return (
		<AppContext.Provider value={initialState}>
			<BrowserRouter>
			</BrowserRouter>
		</AppContext.Provider>
	);
}

export default App;
