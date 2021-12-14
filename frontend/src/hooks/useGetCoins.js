import { useEffect, useState } from "react";
import { getCoins } from '@services'

const useGetCoins = () => {
    const [coins, setCoins] = useState([]);

    useEffect(() => {
        getCoins()
            .then((res) => {
                setCoins(res.data.results);
            })
    }, []);

    return coins;
};

export default useGetCoins;
