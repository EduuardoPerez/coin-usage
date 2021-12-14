import React from 'react';
import ReactDOM from 'react-dom';
import AppContext from '@context/AppContext';
import App from '@routes/App';

ReactDOM.render(
    <AppContext.Provider>
        <App />
    </AppContext.Provider>,
    document.getElementById('app')
);
