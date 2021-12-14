import { useEffect, useState } from "react";
import { getAccountBalances } from '@services'

const useGetAccountBalances = () => {
    const [accountAddress, setAccountAddress] = useState([]);
    const [balances, setBalances] = useState([]);

    useEffect(() => {
        getAccountBalances()
            .then((res) => {
                setAccountAddress(res.data.address);
                setBalances(res.data.balances);
            })
    }, []);

    return {
        accountAddress,
        balances
    }
};

export default useGetAccountBalances;
