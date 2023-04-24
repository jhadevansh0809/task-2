API Endpoints
---------------------------------------------------
Note: Please look through the steps below to know how following API endpoints are working:

To create a new user(method:POST): http://127.0.0.1:8000/api/users/

To list all users(method:GET): http://127.0.0.1:8000/api/users/

To get uers list using limit and offset(method:GET): http://127.0.0.1:8000/api/users/?limit=4&&offset=1

To get all users with particular name(method:GET): http://127.0.0.1:8000/api/userswithname/?name=Devansh+Jha

To fetch a single user(method:GET): http://127.0.0.1:8000/api/userdetail/?email=devansh@gmail.com


----------------------------------------------------------------------------------------------

To create a new organisation(method:POST): http://127.0.0.1:8000/api/organisations/

To list out all organisations(method:GET): http://127.0.0.1:8000/api/organisations/

To get organisations list using limit and offset(method:GET): http://127.0.0.1:8000/api/organisations/?limit=4&&offset=2

To fetch a single organisation(method:GET): http://127.0.0.1:8000/api/organisationdetail/?name=TheDebuggers

-----------------------------------------------------------------------------------------------------


To create/update permission for a user on an organisation(method:POST): http://127.0.0.1:8000/api/createupdatepermissions/

To delete permission for a user on an organisation(method:POST): http://127.0.0.1:8000/api/deletepermissions/

To list out all the permissions for the users on each organisation(method:GET): http://127.0.0.1:8000/api/permissionslist/


To run the code follow the following steps:
---------------------------------------------------
1.pip install -r requirements.txt

2.Setup your database credentials in settings.py

Example:

DATABASES = {
            'default': {
                'ENGINE': 'djongo',
                'NAME': 'accesscontrolsys', 
            }
} 

3.python manage.py migrate

4.python manage.py runserver
