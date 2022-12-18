- Necessary Information for Database

You need to have a running mysql server.

username: "username" <br />
password: "password" <br />
host: "localhost" <br />
database: "mydatabase" <br />

Run the following on the terminal: <br />
mysql> GRANT ALL PRIVILEGES ON mydatabase.* TO 'username'@'localhost';

After that the notebook should work just fine.


