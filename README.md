Base URL:http://127.0.0.1:8000/

Endpoints
✅ Get All Students
URL: /stuInfo/

Method: GET

Description: Returns a list of all student records.

GET http://127.0.0.1:8000/stuInfo/

Get Student by ID
URL: /stuInfo/<int:id>

Method: GET

Description: Returns a single student record by ID.
GET http://127.0.0.1:8000/stuInfo/1

Notes
Ensure the Django server is running:

python manage.py runserver

