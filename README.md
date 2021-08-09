# Arthology API

### Front-end Test Users
https://app.arthology.io

Artist\
Email: artist@arthology.io\
Pass: Arth2021

Curator / Gallery\
Email: curator@arthology.io\
Pass: Arth2021

User / Costumer\
Email: user@arthology.io\
Pass: Arth2021

### User Auth

Create New User\
POST - https://api.arthology.io/auth/users/
```json
{
    "email": "",
    "first_name": "",
    "last_name": "",
    "password": "",
    "re_password": ""
}
```
New User Account Activation\
POST - https://api.arthology.io/auth/users/activation/
```json
{
    "uid": "",
    "token": ""
}
```
Get Json Web Tokens - Jwt Create\
POST - https://api.arthology.io/auth/jwt/create/
```json
{
    "email": "",
    "password": ""
}
```
Get New Access Token - Jwt Refresh\
POST - https://api.arthology.io/auth/jwt/refresh/
```json
{
    "refresh": ""
}
```
### Plataform API
Plataform API EndPoint\
GET - https://api.arthology.io/v1/
