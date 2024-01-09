# hotel-9
Hotel repository for the front- and backend application

# Execute hotel-9 application
This documentation assumes that you already have a postgres database setup with the schemes for the hotel

## Restore Database schema
Using pgAdmin:

1. Open pgAdmin.

2. Connect to your PostgreSQL server.

3. Right-click on the target database and choose Restore....

4. In the Filename field, browse and select backup file "hotel9".

5. Click Restore.

## Create environment
```
py -3 -m venv .venv
```

## Active environment
```
.\.venv\Scripts\activate
```

## Install pip dependencies
```
pip install -r .\dependencies.txt
```

## Update .env configuration
Update the .env files in '\frontend\.env' and '\backend\.env' with the correct information according to your machine.
Once updated enter the follow commands into your git terminal so that the .env files will not be tracked by github.
```
git update-index --assume-unchanged .\frontend\.env
git update-index --assume-unchanged .\backend\.env
```

## Run the application
Enter the following commands in seperate terminals to run the application backend and/or frontend
### Backend:
```
py .\backend\backend.py
```
### Frontend:
```
py .\frontend\frontend.py
```

## Enjoy
The applications should now be running on your specified host and port, enjoy!