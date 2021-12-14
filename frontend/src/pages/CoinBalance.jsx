import React, { useRef, useState } from 'react';
import Error from '@components/Error';
import Success from '@components/Success';
import CoinOption from '@components/CoinOption';
import { getCoinUserBalance } from '@services'
import useGetCoins from '@hooks/useGetCoins';
import '@styles/CoinBalance.scss';

const CoinBalance = () => {
    const coins = useGetCoins();
    const form = useRef(null);
    const [error, setError] = useState(false);
    const [errorMessage, setErrorMessage] = useState('');
    const [coinBalanceSuccess, setCoinBalanceSuccess] = useState(false);
    const [successMessage, setSuccessMessage] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        const formData = new FormData(form.current);

        const coin = formData.get('coin');

        if (coin === '' || coin.length > 5) {
            setError(true);
            setErrorMessage('Ticker symbol is required and must be between 1 and 5 characters.');
            return;
        }
        getCoinUserBalance(coin)
            .then((res) => {
                setCoinBalanceSuccess(true);
                setError(false);
                setSuccessMessage(`${res.data.coin} ${res.data.amount}`);
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
    const getCoinBalanceButton = <button type="submit" className="primary-button" onClick={handleSubmit}>Get balance</button>
    const getCoinBalanceComponent = (coinBalanceSuccess) ? <Success message={`The coin balance is: \n\n${successMessage}`} /> : getCoinBalanceButton;

    return (
        <div className="coin-balance">
            <div className="coin-balance-container">
                <h1 className="title">Coin balance</h1>
                <form action="/" className="form" ref={form}>
                    {errorComponent}
                    <label htmlFor="coin" className="label">Coin</label>
                    <select type="number" name="coin" id="coin" placeholder="Coin to deposit" className="input input-coin">
                        {coins.map(coin => (
                            <CoinOption coin={coin} key={coin.ticker_symbol} />
                        ))}
                    </select>
                    {getCoinBalanceComponent}
                </form>
            </div>
        </div>
    );
}

export default CoinBalance;