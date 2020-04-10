# Azure Functions Penetration Test Pattern
This is a sample azure functions app that has SQL Injection vulnerability on purpose to demonstrate how OWASP ZAP is able to detect this vulnerability and give an alert.

## Setup
```
docker-compose up
docker exec -it docker_postgres psql -U postgres
```
then, insert some sample data:
```
postgres=# \c penTestDB
postgres=# create table users (id int, name varchar(50), address varchar(50));
postgres=# insert into users values (1, ’amy’, ‘xxx.US’),(2, 'john', 'xxx,AU'),(3, 'emily','xxx,JP');
```
try if you can get data by pinging 
```
http://localhost:7071/api/user?name=amy
```
SQL injection:
```
http://localhost:7071/api/user?name=' or '1'='1'--
```
## Bug Issues:
### ZAP detects sql injection (using params)
you can:
1. docker-compose up
2. penetrate function by using 
```
http://localhost:7071/api/user?name=' or '1'='1' -- 
```
then you will get all user info from db

3. try to attack using OWASP ZAP tool
    - ZAP is able to detect sql injection.
    - ![](./images/can_detect_sql_injection.png)
    - the zap report for this is under ```reports/can_detect_sql_injection.html```
4. ```docker-compose down```
## ZAP not able to detect sql injection (using route params)
1. add ```route``` to function.json as below:
```
"bindings": [
    {
      "authLevel": "anonymous",
      "type": "httpTrigger",
      "direction": "in",
      "name": "req",
      "methods": [
        "get"      
      ],
      "route": "user/{name}"
    },
    {
      "type": "http",
      "direction": "out",
      "name": "$return"
    }
  ]
```
2. change ```name = req.params.get('name')``` to ```name = req.route_params.get('name')``` in ```__init__.py```
3. ```docker-compose build```
4. ```docker-compose up```
5. penetrate function by using
```
http://localhost:7071/api/user/' or '1'='1' -- 
```
then you will get all user info from db

6. try to attack using OWASP ZAP tool
    - From above steps you might realize that ZAP does not detect sql injection.
    - ![](./images/cannot_detect_sql_injection.png)
    - (you see that the + sign (whitespace encoding) is not decoded and causes an syntax error instead of penetrating the function)
    - the zap report for this is under ```reports/cannot_detect_sql_injection.html```
6. ```docker-compose down```
