import React from 'react';
import useGetGlobalTransactions from '@hooks/useGetGlobalTransactions';
import '@styles/GlobalTransactions.scss';

const formatDateTime = (dateTime) => {
    const d = new Date(dateTime);
    const ye = new Intl.DateTimeFormat('en', { year: 'numeric' }).format(d)
    const mo = new Intl.DateTimeFormat('en', { month: 'short' }).format(d)
    const da = new Intl.DateTimeFormat('en', { day: '2-digit' }).format(d)
    return `${da}-${mo}-${ye} ${d.getHours()}:${d.getMinutes()}:${d.getSeconds()}`;
}

const AccountBalances = () => {
    const transactions = useGetGlobalTransactions();

    return (
        <div className="global-transactions">
            <div className="global-transactions-container">
                <h1 className="title">Global transactions</h1>
                <table className="transactions">
                    <thead>
                        <tr>
                            <th>Date time</th>
                            <th>Account from</th>
                            <th>Account to</th>
                            <th>Coin</th>
                            <th>Amount</th>
                        </tr>
                    </thead>
                    <tbody>
                        {transactions.map((val, key) => {
                            return (
                                <tr key={key}>
                                    <td>{formatDateTime(val.created)}</td>
                                    <td>{val.account_from}</td>
                                    <td>{val.account_to}</td>
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
