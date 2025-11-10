Todays Lab: Azure SQL database
 
Create and configure a cloud-based SQL Database in Microsoft Azure.
Manage and query the database using SQL Server Management Studio (SSMS).
Connect a Django application to the Azure SQL Database.
Create a simple Django model (e.g., a Book or Student model) (code-first).
Apply migrations again and verify the new table in SSMS.
Add a few records using the Django Admin interface or the shell.
Query the same records directly from SSMS — confirm that the data matches.

Dont hesitate to ask us any questions you might have. 
Good luck! 
Links:
SMSS:
https://learn.microsoft.com/en-us/ssms/release-notes-20
Quickstart:
https://learn.microsoft.com/en-us/azure/azure-sql/database/single-database-create-quickstart?view=a…

# Books Project (minimal)

This is a minimal Django project with an app `library` that defines a `Book` model.

Files of interest:

- `library/models.py` - defines the `Book` model (name, author, publication_year)
- `library/admin.py` - registers the model for the admin
- `library/tests.py` - basic unit test for the model

To run locally:

1. Create a virtualenv and activate it
2. pip install -r requirements.txt
3. python manage.py migrate
4. python manage.py test

Using Azure SQL instead of the local SQLite file
------------------------------------------------

1. Install the Microsoft ODBC driver for SQL Server on your host. On Debian/Ubuntu the steps are roughly:

```bash
# import the Microsoft signing key and repository then install
curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list
sudo apt update
sudo ACCEPT_EULA=Y apt install msodbcsql18
```

2. Install the Python DB backend and dependencies in your virtualenv:

```bash
pip install mssql-django pyodbc
```

3. Set environment variables (use `.env` or export them in the shell). You can use the `.env.example` file as a template.

```
AZURE_DB_SERVER=yourserver.database.windows.net
AZURE_DB_NAME=yourdatabasename
AZURE_DB_USER=youruser@yourserver
AZURE_DB_PASSWORD=yourpassword
AZURE_DB_DRIVER="ODBC Driver 18 for SQL Server"
```

4. Run migrations against Azure SQL:

```bash
python manage.py makemigrations
python manage.py migrate
```

Notes & troubleshooting:
- Make sure the Azure SQL server firewall allows your client IP (or the VM's outbound IP).
- If you get TLS/SSL errors, check the ODBC driver version and the `OPTIONS['extra_params']` in `books_project/settings.py`.
- For production, store secrets securely (Azure Key Vault or environment variables) and set `DEBUG=False`.

