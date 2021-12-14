import { useEffect, useState } from "react";
import { getAccountTransactions } from '@services'

const useGetAccountTransactions = () => {
    const [transactions, setTransactions] = useState([]);

    useEffect(() => {
        getAccountTransactions()
            .then((res) => {
                setTransactions(res.data);
            })
    }, []);

    return transactions;
};

export default useGetAccountTransactions;
