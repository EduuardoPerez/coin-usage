# Coin-Usage App

---

Application developed to manage the handling of coins.

# **Postman Collection**

---

To start testing the API download the postman collection clicking [here](https://www.postman.com/eduuardoperez/workspace/shared-workspace/collection/9295619-05f2cc07-a230-42ef-ab44-e99a08cec610)

# Setup

---

## **Prerequisites**

- Docker; if you don’t have it yet, follow the [installation instructions](https://docs.docker.com/install/#supported-platforms).
- Docker Compose; refer to the official documentation for the [installation guide](https://docs.docker.com/compose/install/).

## **Build the stack and execute it**

This can take a while, especially the first time you run this particular command on your development system.

### Backend

Run:

```bash
docker-compose -f backend/local.yml up --build
```

If you want to emulate production environment use `backend/production.yml` instead.

After the stack is created you can run it only with `docker-compose -f backend/local.yml up`

Runs on `http://localhost:8000`

### Frontend

Run:

```bash
docker-compose -f frontend/local.yml up --build
```

After the stack is created you can run it only with `docker-compose -f frontend/local.yml up`

Runs on `http://localhost:3000`

# Tests

---

### Run backend tests

```bash
docker-compose -f backend/local.yml run --rm --service-ports django pytest
```

# Considerations

---

1. For security reasons, only superuser can create coins or list coins balances.
    1. The superusers has to be created from django admin, or executing:
        
        ```bash
        docker-compose -f backend/local.yml run --rm --service-ports django python manage.py createsuperuser
        ```
        
2. Before send money to other user the account has to have balance. Use the `/accounts/deposit/` endpoint to found the account.
3. Anyone can view the transactions list.

# Endpoints

---

💡 Most of the endpoints (except `/users/signup`, `/users/login` and `/transactions/`) require an authorization header with a token value. The content of the header should look like the following: `Authorization: Token <token>`


- Create account: POST → /users/signup
    - Payload:
        
        ```json
        {
        	"username": "someusername",
        	"email": "some@email.test",
        	"first_name": "some first name",
        	"last_name": "some last name",
        	"password": "Test1234strong*",
        	"password_confirmation": "Test1234strong*",
        }
        ```
        
    - Response:
        
        ```json
        
        {
            "email": "some@email.test",
            "username": "someusername",
            "first_name": "some first name",
            "last_name": "some last name",
        }
        ```
        

- Login into account: POST → /users/login
    - Payload:
        
        ```json
        {
        	"username": "someusername",
        	"password": "Test1234strong*",
        }
        ```
        
    - Response:
        
        ```json
        
        {
            "user": {
                "email": "some@email.test",
        	    "username": "someusername",
        	    "first_name": "some first name",
        	    "last_name": "some last name",
            }
            "access_token": "acb81534a08d135064c96963b546ed520b6ab4d4"
        }
        ```
        

- Create coin: POST → /coins
    - Payload:
        
        ```json
        {
        	"ticker_symbol": "RPC",
        	"name": "Ripio Coin",
        }
        ```
        
    - Response:
        
        ```json
        {
        	"ticker_symbol": "RPC",
        	"name": "Ripio Coin",
        }
        ```
        

- Deposit in an account: PATCH → /accounts/deposit/
    - Payload:
        
        ```json
        {
            "balance":{
                "coin": "RPC",
                "amount": 100
            }
        }
        ```
        
    - Response:
        
        ```json
        {
            "address": "t2YrlMiDL47Gl6g85LhTiWoIoj0jHQf1Ish",
            "balances": [
                {
                    "coin": "BTC",
                    "amount": 100.0
                },
                {
                    "coin": "RPC",
                    "amount": 223.4
                }
            ]
        }
        ```
        

- Send coin: PATCH → /accounts/send
    - Payload:
        
        ```json
        {
            "address": "xh4tigzr9wQ4UaBZSoDGySxZSSXOkCQgYrA",
            "balance": {
                "coin": "RPC",
                "amount": 100
            }
        }
        ```
        
    - Response:
        
        ```json
        {
            "address": "t2YrlMiDL47Gl6g85LhTiWoIoj0jHQf1Ish",
            "balances": [
                {
                    "coin": "BTC",
                    "amount": 67.0
                },
                {
                    "coin": "RPC",
                    "amount": 123.4
                }
            ]
        }
        ```
        

- Get transactions list: GET → /transactions/
    - Response:
        
        ```json
        {
            "count": 5,
            "next": null,
            "previous": null,
            "results": [
                {
                    "created": "2021-12-07T00:35:56.984592Z",
                    "account_from": "t2YrlMiDL47Gl6g85LhTiWoIoj0jHQf1Ish",
                    "account_to": "m9r2S1PdcbskYSmDT3HHKM5j4w2xxVN2vXl",
                    "coin": "BTC",
                    "amount": 1.0
                },
                {
                    "created": "2021-12-07T00:35:47.171521Z",
                    "account_from": "t2YrlMiDL47Gl6g85LhTiWoIoj0jHQf1Ish",
                    "account_to": "m9r2S1PdcbskYSmDT3HHKM5j4w2xxVN2vXl",
                    "coin": "RPC",
                    "amount": 33.0
                },
                {
                    "created": "2021-12-07T00:35:11.347981Z",
                    "account_from": "t2YrlMiDL47Gl6g85LhTiWoIoj0jHQf1Ish",
                    "account_to": "xh4tigzr9wQ4UaBZSoDGySxZSSXOkCQgYrA",
                    "coin": "RPC",
                    "amount": 578.0
                },
                {
                    "created": "2021-12-07T00:35:00.204685Z",
                    "account_from": "t2YrlMiDL47Gl6g85LhTiWoIoj0jHQf1Ish",
                    "account_to": "xh4tigzr9wQ4UaBZSoDGySxZSSXOkCQgYrA",
                    "coin": "BTC",
                    "amount": 10.0
                },
                {
                    "created": "2021-12-07T00:34:02.705400Z",
                    "account_from": "t2YrlMiDL47Gl6g85LhTiWoIoj0jHQf1Ish",
                    "account_to": "xh4tigzr9wQ4UaBZSoDGySxZSSXOkCQgYrA",
                    "coin": "RPC",
                    "amount": 100.0
                }
            ]
        }
        ```
        

- Get user coins balances: GET → /accounts/balances
    - Response:
        
        ```json
        {
            "address": "t2YrlMiDL47Gl6g85LhTiWoIoj0jHQf1Ish",
            "balances": [
                {
                    "coin": "BTC",
                    "amount": 26
                },
                {
                    "coin": "RPC",
                    "amount": 412.4000000000001
                }
            ]
        }
        ```
        

- Get balance of a coin of an account: GET → /accounts/coins/?coin={coin.ticker_symbol}
    - Response
        
        ```json
        {
            "coin": "RPC",
            "amount": 412.4000000000001
        }
        ```
        

- Get balance of each coin by user: GET → /balances/
    - Response
        
        ```json
        [
            {
                "username": "other3",
                "coin": "BTC",
                "amount": 1
            },
            {
                "username": "other3",
                "coin": "RPC",
                "amount": 33
            },
            {
                "username": "newsuperuser",
                "coin": "BTC",
                "amount": 73
            },
            {
                "username": "newsuperuser",
                "coin": "RPC",
                "amount": 778
            },
            {
                "username": "eperez",
                "coin": "BTC",
                "amount": 26
            },
            {
                "username": "eperez",
                "coin": "RPC",
                "amount": 412.4000000000001
            }
        ]
        ```
        

- Get transactions of the account: GET → /transactions/accounts/
    - Response
        
        ```json
        [
            {
                "created": "2021-12-07T00:35:56.984592Z",
                "account_from": "t2YrlMiDL47Gl6g85LhTiWoIoj0jHQf1Ish",
                "account_to": "m9r2S1PdcbskYSmDT3HHKM5j4w2xxVN2vXl",
                "coin": "BTC",
                "amount": 1.0
            },
            {
                "created": "2021-12-07T00:35:47.171521Z",
                "account_from": "t2YrlMiDL47Gl6g85LhTiWoIoj0jHQf1Ish",
                "account_to": "m9r2S1PdcbskYSmDT3HHKM5j4w2xxVN2vXl",
                "coin": "RPC",
                "amount": 33.0
            },
            {
                "created": "2021-12-07T00:35:11.347981Z",
                "account_from": "t2YrlMiDL47Gl6g85LhTiWoIoj0jHQf1Ish",
                "account_to": "xh4tigzr9wQ4UaBZSoDGySxZSSXOkCQgYrA",
                "coin": "RPC",
                "amount": 578.0
            },
            {
                "created": "2021-12-07T00:35:00.204685Z",
                "account_from": "t2YrlMiDL47Gl6g85LhTiWoIoj0jHQf1Ish",
                "account_to": "xh4tigzr9wQ4UaBZSoDGySxZSSXOkCQgYrA",
                "coin": "BTC",
                "amount": 10.0
            },
            {
                "created": "2021-12-07T00:34:02.705400Z",
                "account_from": "t2YrlMiDL47Gl6g85LhTiWoIoj0jHQf1Ish",
                "account_to": "xh4tigzr9wQ4UaBZSoDGySxZSSXOkCQgYrA",
                "coin": "RPC",
                "amount": 100.0
            }
        ]
        ```
