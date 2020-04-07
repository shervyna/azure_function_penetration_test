# Azure Functions Penetration Test Pattern

1. setup your own postgresdb with a ```users``` table
[](./images/usersTable.png)
2. func host start
3. penetrate by using
```
http://localhost:7071/api/user/' or '1'='1' -- 
```
then you will get all user info from db


#TODO:
- open api definition (+ api management(optional))
- zap api scan steps
- pipeline