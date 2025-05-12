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

✅ Create a New Student
URL: /stuCreate/
Method: POST
Description: Creates a new student record with the provided data.

POST http://127.0.0.1:8000/create/

✅ Required JSON Body:

{
  "name": "John Doe",
  "roll": 101,
  "city": "New York"
}
✅ Success Response:
json
Copy
Edit
{
  "msg": "Data created"
}
🔴 Error Response (Example - Missing field):

{
  "roll": [
    "This field is required."
  ]
}
⚠️ Notes:
Make sure the Django server is running:


python manage.py runserver
The endpoint expects Content-Type: application/json.



