import { useEffect, useState } from "react";
import { getGlobalTransactions } from '@services'

const useGetGlobalTransactions = () => {
    const [transactions, setTransactions] = useState([]);

    useEffect(() => {
        getGlobalTransactions()
            .then((res) => {
                setTransactions(res.data.results);
            })
    }, []);

    return transactions;
};

export default useGetGlobalTransactions;
