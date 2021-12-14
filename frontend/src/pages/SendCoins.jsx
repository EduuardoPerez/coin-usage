import React, { useRef, useState } from 'react';
import Error from '@components/Error';
import Success from '@components/Success';
import CoinOption from '@components/CoinOption';
import useGetCoins from '@hooks/useGetCoins';
import { sendCoins } from '@services'
import '@styles/SendCoins.scss';

const SendCoins = () => {
    const ADDRESS_LENGTH = 35;
    const form = useRef(null);
    const coins = useGetCoins();
    const [sendSuccess, setSendSuccess] = useState(false);
    const [successMessage, setSuccessMessage] = useState('');
    const [error, setError] = useState(false);
    const [errorMessage, setErrorMessage] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        const formData = new FormData(form.current);

        const accountAddress = formData.get('account-address');
        const coin = formData.get('coin');
        const amount = formData.get('amount');

        if (accountAddress === '' || accountAddress.length !== ADDRESS_LENGTH || coin === '' || amount === '' || amount <= 0) {
            setError(true);
            setErrorMessage('Please fill all the fields. Address must be 35 characters long.');
            return;
        }
        const data = {
            address: accountAddress,
            balance: {
                coin: coin,
                amount: amount
            }
        }
        sendCoins(data)
            .then((res) => {
                setSendSuccess(true);
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
    }

    const sendButton = <button type="submit" className="primary-button" onClick={handleSubmit}>Send coins</button>
    const sendComponent = (sendSuccess) ? <Success message={`Coins sent! \n\n${successMessage}`} /> : sendButton;
    const errorComponent = (error) ? <Error message={errorMessage} /> : null;

    return (
        <div className="send-coins">
            <div className="send-coins-container">
                <h1 className="title">Send Coins</h1>
                <form action="/" className="form" ref={form}>
                    {errorComponent}
                    <div>
                        <label htmlFor="account-address" className="label">Account address</label>
                        <input type="text" name="account-address" id="account-address" placeholder="Account address to send coins" className="input input-account-address" />
                        <label htmlFor="coin" className="label">Coin</label>
                        <select type="number" name="coin" id="coin" placeholder="Coin to send" className="input input-coin">
                            {coins.map(coin => (
                                <CoinOption coin={coin} key={coin.ticker_symbol} />
                            ))}
                        </select>
                        <label htmlFor="amount" className="label">Amount</label>
                        <input type="number" name="amount" id="amount" placeholder="Amount to send" className="input input-amount" />
                    </div>
                    {sendComponent}
                </form>
            </div>
        </div>
    );
}

export default SendCoins;
