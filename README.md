# Artyste Demo API

### Front-end
https://demo.artyste.io

### Backend-end
Plataform API EndPoint\
https://api.artyste.info/v1/

### Test Users

Artist\
Email: artist@artyste.io\
Pass: Arth2021

Gallery\
Email: gallery@artyste.io\
Pass: Arth2021

User / Costumer\
Email: user@artyste.io\
Pass: Arth2021

### VR Module's Repository

https://github.com/artyste/artyste-virtual

### User Auth API

Create New User\
POST - https://api.artyste.info/auth/users/
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
POST - https://api.artyste.info/auth/users/activation/
```json
{
    "uid": "",
    "token": ""
}
```
Get Json Web Tokens - Jwt Create\
POST - https://api.artyste.info/auth/jwt/create/
```json
{
    "email": "",
    "password": ""
}
```
Get New Access Token - Jwt Refresh\
POST - https://api.artyste.info/auth/jwt/refresh/
```json
{
    "refresh": ""
}
```