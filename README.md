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
postgres=# insert into users values (1, 'amy', 'xxx.US'),(2, 'john', 'xxx,AU'),(3, 'emily','xxx,JP');
```
try if you can get data by pinging 
```
http://localhost:7071/api/user?name=amy
```
SQL injection:
```
http://localhost:7071/api/user?name=' or '1'='1'--
```

Refer to this blog to see how you can automatically detect the vulnerabilies in your azure functions app using owasp zap:
https://medium.com/@shervyna/penetration-test-for-azure-functions-using-zap-api-scan-5a3bfc21b7e6

