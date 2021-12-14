import React, { useRef, useState } from 'react';
import Error from '@components/Error';
import Success from '@components/Success';
import CoinOption from '@components/CoinOption';
import useGetCoins from '@hooks/useGetCoins';
import { depositCoin } from '@services'
import '@styles/DepositCoins.scss';

const DepositCoins = () => {
    const coins = useGetCoins();
    const form = useRef(null);
    const [error, setError] = useState(false);
    const [errorMessage, setErrorMessage] = useState('');
    const [depositSuccess, setDepositSuccess] = useState(false);
    const [successMessage, setSuccessMessage] = useState('');
    const errorComponent = (error) ? <Error message={errorMessage} /> : null;

    const handleSubmit = (e) => {
        e.preventDefault();
        const formData = new FormData(form.current);

        const coin = formData.get('coin');
        const amount = formData.get('amount');

        if (coin === '' || amount === '' || amount <= 0) {
            setError(true);
            setErrorMessage('Coin and amount are required and amount must be greater than 0.');
            return;
        }
        const data = {
            balance: {
                coin: coin,
                amount: amount
            }
        }
        depositCoin(data)
            .then((res) => {
                setDepositSuccess(true);
                setError(false);
                let successMsg = '';
                Object.entries(res.data.balances).forEach((balance) => {
                    successMsg += `${balance[1].coin} balance: ${balance[1].amount} \n`;
                });
                setSuccessMessage(successMsg);
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

    const depositButton = <button type="submit" className="primary-button" onClick={handleSubmit}>Deposit</button>
    const depositComponent = (depositSuccess) ? <Success message={`Deposit done! \n\n${successMessage}`} /> : depositButton;


    return (
        <div className="deposit-coins">
            <div className="deposit-coins-container">
                <h1 className="title">Deposit Coins</h1>
                <form action="/" className="form" ref={form}>
                    {errorComponent}
                    <div>
                        <label htmlFor="coin" className="label">Coin</label>
                        <select type="number" name="coin" id="coin" placeholder="Coin to deposit" className="input input-coin">
                            {coins.map(coin => (
                                <CoinOption coin={coin} key={coin.ticker_symbol} />
                            ))}
                        </select>
                        <label htmlFor="amount" className="label">Amount</label>
                        <input type="number" name="amount" id="amount" placeholder="Amount to deposit" className="input input-amount" />
                    </div>
                    {depositComponent}
                </form>
            </div>
        </div>
    );
}

export default DepositCoins;
