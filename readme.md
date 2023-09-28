# MySQL Connector Python Example

This program is a simple example of how to set up a MySQL connection with Python. Below is a brief description of how to use the code and what is required for it to work.

## Usage

### Install MySQL Connector

Before running the code, you need to install the MySQL Connector package. Open your terminal or command prompt and run the following command.

```shell
pip install mysql-connector-python
```

To use this program, you need to have Python installed on your computer. If you don't have Python installed, you can download it from the [Python official website](https://www.python.org/downloads/).

Additionally, you should have a MySQL server installed and running. You can download and install MySQL from the [MySQL official website](https://dev.mysql.com/downloads/installer/).

### How the example code works

This Python script demonstrates how to establish a connection to a MySQL database and retrieve information from it. Here's an overview of how the code functions:

1. **Importing Required Libraries:** The code begins by importing the `mysql.connector` library, which is necessary for connecting to and interacting with the MySQL database.

2. **Establishing a Database Connection:** To establish a connection to the MySQL server, the script uses the `mysql.connector.connect()` function. You need to provide the following parameters:
   - `user`: Your MySQL username.
   - `password`: Your MySQL password.
   - `host`: The address of your MySQL server.
   - `database`: The name of the database you want to connect to.

3. **Creating a Cursor:** A cursor is created using `cnx.cursor()`. This cursor allows you to execute SQL queries on the connected database.

4. **Executing SQL Queries:** Inside a try-except-finally block, the code demonstrates how to execute SQL queries. In this example, the script runs `SHOW TABLES` to retrieve a list of table names from the selected database.

5. **Displaying Results:** If the query is successful, the script fetches the results and prints the table names to the console.

6. **Handling Errors:** If any errors occur during the execution of the SQL query, they are caught and displayed with an error message.

7. **Closing the Cursor and Connection:** Finally, the cursor and database connection are closed in the `finally` block to ensure proper cleanup.

By following these steps, you can establish a connection to your MySQL database and perform various operations as needed.


```python
# Import the mysql.connector library
import mysql.connector

# Provide the username (user), password (password), host (host), and database (database) in the connection parameters.
# Ensure that these values are correct for your MySQL server.
cnx = mysql.connector.connect(user='YOUR_USERNAME', password='YOUR_PASSWORD', host='YOUR_SERVER_ADDRESS', database='YOUR_DATABASE_NAME')

# Create a cursor to execute SQL queries
cursor = cnx.cursor()

# Inside a try-except-finally structure, you can perform your SQL queries.
# In this example, table names in the selected database are displayed.
try:
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    print("Table names:")
    for table in tables:
        print(table[0])

except mysql.connector.Error as err:
    print("Error fetching table names: ", err)

finally:
    cursor.close()
    cnx.close()
