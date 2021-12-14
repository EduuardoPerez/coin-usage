import React from 'react';

const CoinOption = ({ coin }) => {

    return (
        <option value={coin.ticker_symbol}>{coin.ticker_symbol}</option>
    )
}

export default CoinOption;
