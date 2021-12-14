import { useEffect, useState } from "react";
import { getCoinBalancesByUsers } from '@services'

const useGetCoinsBalanceByUsers = () => {
    const [coinBalancesByUsers, setCoinBalancesByUsers] = useState([]);

    useEffect(() => {
        getCoinBalancesByUsers()
            .then((res) => {
                setCoinBalancesByUsers(res.data);
            })
    }, []);

    return coinBalancesByUsers;
};

export default useGetCoinsBalanceByUsers;
