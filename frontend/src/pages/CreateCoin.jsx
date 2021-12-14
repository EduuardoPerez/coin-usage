import React, { useRef, useState } from 'react';
import Error from '@components/Error';
import Success from '@components/Success';
import { createCoin } from '@services'
import '@styles/CreateCoin.scss';

const CreateCoin = () => {
    const form = useRef(null);
    const [error, setError] = useState(false);
    const [errorMessage, setErrorMessage] = useState('');
    const [createSuccess, setCreateSuccess] = useState(false);
    const [successMessage, setSuccessMessage] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        const formData = new FormData(form.current);

        const tickerSymbol = formData.get('ticker-symbol');
        const name = formData.get('name');

        if (tickerSymbol === '' || tickerSymbol.length > 5 || name === '' || name.length > 50) {
            setError(true);
            setErrorMessage('Ticker symbol must be between 1 and 5 characters, and name must be between 1 and 50 characters. Both are required.');
            return;
        }
        const data = {
            ticker_symbol: tickerSymbol,
            name: name
        }
        createCoin(data)
            .then((res) => {
                setCreateSuccess(true);
                setError(false);
                setSuccessMessage(`Ticker symbol: ${res.data.ticker_symbol}\nName: ${res.data.name}`);
            })
            .catch((error) => {
                setError(true);
                const res = error.response.data;
                let errMsgs = '';
                Object.entries(res).forEach((err) => {
                    const [key, value] = err;
                    errMsgs += `${key}: ${value}\n`;
                });
                setErrorMessage(errMsgs);
            });
    };

    const errorComponent = (error) ? <Error message={errorMessage} /> : null;
    const createButton = <button type="submit" className="primary-button" onClick={handleSubmit}>Create</button>
    const createComponent = (createSuccess) ? <Success message={`Coin created! \n\n${successMessage}`} /> : createButton;

    return (
        <div className="create-coin">
            <div className="create-coin-container">
                <h1 className="title">Create Coin</h1>
                <form action="/" className="form" ref={form}>
                    {errorComponent}
                    <div>
                        <label htmlFor="ticker-symbol" className="label">Ticker symbol</label>
                        <input type="text" name="ticker-symbol" id="ticker-symbol" placeholder="Ticker symbol of the coin" className="input input-ticker-symbol" />
                        <label htmlFor="name" className="label">Name</label>
                        <input type="text" name="name" id="name" placeholder="Name of the coin" className="input input-name" />
                    </div>
                    {createComponent}
                </form>
            </div>
        </div>
    );
}

export default CreateCoin;