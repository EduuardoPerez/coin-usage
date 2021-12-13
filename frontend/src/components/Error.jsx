import React from 'react';
import '@styles/Error.scss';

const Error = ({ message }) => (
    <p className="error">{message}</p>
);

export default Error;