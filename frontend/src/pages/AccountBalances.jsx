import React from 'react';
import useGetBalances from '@hooks/useGetBalances';
import '@styles/AccountBalances.scss';

const AccountBalances = () => {
    const { accountAddress, balances } = useGetBalances();

    return (
        <div className="account-balances">
            <div className="account-balances-container">
                <h1 className="title">Account balances</h1>
                <p className="account-address">Account address: <strong>{accountAddress}</strong></p>
                <table className="balances">
                    <thead>
                        <tr>
                            <th>Coin</th>
                            <th>Balance</th>
                        </tr>
                    </thead>
                    <tbody>
                        {balances.map((val, key) => {
                            return (
                                <tr key={key}>
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

export default AccountBalances;
