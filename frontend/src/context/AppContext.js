import React, { createContext, useState } from 'react'
export const AppContext = createContext({})

const Provider = ({ children }) => {
    const [isAuth, setIsAuth] = useState(() => {
        return localStorage.getItem('COIN_USAGE_TOKEN')
    })
    const [isAdmin, setIsAdmin] = useState(() => {
        return true ? localStorage.getItem('IS_ADMIN') === 'true' : false
    })

    const value = {
        isAuth,
        isAdmin,
        activateAuth: (username, token, isAdmin) => {
            setIsAuth(true)
            setIsAdmin(isAdmin)
            localStorage.setItem('USERNAME', username)
            localStorage.setItem('COIN_USAGE_TOKEN', token)
            localStorage.setItem('IS_ADMIN', isAdmin)
        },
        removeAuth: () => {
            setIsAuth(false)
            localStorage.removeItem('COIN_USAGE_TOKEN')
            localStorage.removeItem('USERNAME')
            localStorage.removeItem('IS_ADMIN')
        }
    }

    return (
        <AppContext.Provider value={value}>
            {children}
        </AppContext.Provider>
    )
}

export default {
    Provider,
    Consumer: AppContext.Consumer
}
