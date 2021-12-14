import React from 'react';
import useGetCoinBalancesByUsers from '@hooks/useGetCoinBalancesByUsers';
import '@styles/CoinBalancesByUsers.scss';

const CoinsBalancesByUsers = () => {
    const transactions = useGetCoinBalancesByUsers();

    return (
        <div className="coins-balances">
            <div className="coins-balances-container">
                <h1 className="title">Coin balances by users</h1>
                <table className="transactions">
                    <thead>
                        <tr>
                            <th>Username</th>
                            <th>Coin</th>
                            <th>Amount</th>
                        </tr>
                    </thead>
                    <tbody>
                        {transactions.map((val, key) => {
                            return (
                                <tr key={key}>
                                    <td>{val.username}</td>
                                    <td>{val.coin}</td>
                                    <td>{val.amount}</td>
                                </tr>
                            )
                        })}
                    </tbody>
                </table>
            </div>
        </div>
    );
}

export default CoinsBalancesByUsers;
