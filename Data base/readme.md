Following information is necessary to utilize the database

You need to have a running mysql server.

username: "username"
password: "password"
host: "localhost"
database: "mydatabase"

Run the following on the terminal:
mysql> GRANT ALL PRIVILEGES ON mydatabase.* TO 'username'@'localhost';

After that the notebook should work just fine.


