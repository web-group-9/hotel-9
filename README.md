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

### No work from teammate
Julian Veit with student ID 112012066 did not do any work regarding this project despite promising to do so.

# Requirements checklist

## Hotel Frontend Website with Booking Feature

### Design Elements:
- [x] User-friendly interface.
- [x] Display of hotel rooms, amenities, and services.
- [x] An interactive booking form.
### Functionality:
- [x] Users can select room types, check-in and check-out dates.
- [x] A booking confirmation process.
- [ ] User authentication for booking (optional).

## Admin Website for Managing Bookings

### Design Elements:
- [x] A dashboard-like interface.
- [ ] Sections for different administrative tasks.
### Functionality:
- [x] Listing all bookings with details.
- [x] Capabilities to modify or cancel bookings (optional).
- [ ] Search and filter options for bookings (optional).

## PostgreSQL Database:

### Tables:
- [x] Guests: storing guest name, contact information.
- [x] Bookings: storing booking details like check-in, check-out dates, and linked to guest information.
### Integration:
- [x] Flask app connects to the PostgreSQL database for data retrieval and updates.

## Deployment:
- [x] Deploy both websites to a web server.
- [x] Using a custom domain name.

## Security and Performance:
- [ ] Implement security best practices (like SSL, input validation).
- [x] Ensure good performance and responsive design.