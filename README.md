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


API Endpoints
---------------------------------------------------
Note: Please look through the steps below to know how following API endpoints are working:

To create a new user(method:POST): http://127.0.0.1:8000/api/users/

To list all users(method:GET): http://127.0.0.1:8000/api/users/

To get uers list using limit and offset(method:GET): http://127.0.0.1:8000/api/users/?limit=4&&offset=1

To get all users with particular name(method:GET): http://127.0.0.1:8000/api/userswithname/?name=Devansh+Jha

To fetch a single user(method:GET): http://127.0.0.1:8000/api/userdetail/?email=devanshjha@gmail.com


----------------------------------------------------------------------------------------------

To create a new organisation(method:POST): http://127.0.0.1:8000/api/organisations/

To list out all organisations(method:GET): http://127.0.0.1:8000/api/organisations/

To get organisations list using limit and offset(method:GET): http://127.0.0.1:8000/api/organisations/?limit=4&&offset=2

To fetch a single organisation(method:GET): http://127.0.0.1:8000/api/organisationdetail/?name=TheDebuggers

-----------------------------------------------------------------------------------------------------


To create/update permission for a user on an organisation(method:POST): http://127.0.0.1:8000/api/createupdatepermissions/

To delete permission for a user on an organisation(method:POST): http://127.0.0.1:8000/api/deletepermissions/

To list out all the permissions for all the users on each organisation(method:GET): http://127.0.0.1:8000/api/permissionslist/




Let's look each API endpoint by taking example cases:
------------------------------------------------------------


Create a new user
-----------------------------------------------------------
1.Go to http://127.0.0.1:8000/api/users/ ,you will get interface like this.Fill the required details.
![image](https://user-images.githubusercontent.com/62210359/233945319-1b97fda1-0f32-4fb0-a968-4f8ef567d1bf.png)

2.We will get response like this.
![image](https://user-images.githubusercontent.com/62210359/233945467-b32f3c90-e1fd-4d6e-9aa7-e82b712e0071.png)


To list all users
---------------------------------------------------
1.Go to http://127.0.0.1:8000/api/users/ ,and select the GET method by clicking the button below:
![image](https://user-images.githubusercontent.com/62210359/233945865-b9390f4c-f1c5-4d82-8508-1ea3ab92c454.png)

2.We will get response like this.

![image](https://user-images.githubusercontent.com/62210359/233946053-1bc6771d-0d03-49b3-b831-b0e77b5be972.png)


To get users list using limit and offset
---------------------------------------------------
Follow the same method as above, just mention limit and offset in url.


To get all users with particular name
--------------------------------------------------------
1.Let's say we want all the users with name "Devansh Jha", we will go to http://127.0.0.1:8000/api/userswithname/?name=Devansh+Jha

2.We will get response like this.

![image](https://user-images.githubusercontent.com/62210359/233946880-75c7856d-403c-46e3-807b-3be845ca9eba.png)


To fetch a single(unique) user
---------------------------------------------------------------
1.Each unique user will be identified by his/her email, so we will provide email of the user in th url. Example: http://127.0.0.1:8000/api/userdetail/?email=devanshjha@gmail.com

2.We will get response like this.

![image](https://user-images.githubusercontent.com/62210359/233947569-250c4c3d-b665-456e-8454-414e678e2cfa.png)


---------------------------------------------------------------------------------------------------------------

To create a new organisation
---------------------------------------------
1.Go to http://127.0.0.1:8000/api/organisations/, you will get interface like this.Fill the required details.

![image](https://user-images.githubusercontent.com/62210359/233948554-96542c3d-7e62-483d-ae62-a3d98a22d59b.png)

2.We will get response like this.

![image](https://user-images.githubusercontent.com/62210359/233948669-47c24c15-7c73-4192-85e6-32d8ed7c32a6.png)


To list all organisations
-----------------------------------------------

1.Go to http://127.0.0.1:8000/api/users/ ,and select the GET method by clicking the button below.

2.We will get response like this.

![image](https://user-images.githubusercontent.com/62210359/233949152-47b808ac-7c39-4621-b7fa-2b812c57459e.png)


To get organisations list using limit and offset
---------------------------------------------------

Follow the same method as above, just mention limit and offset in url.


To fetch a single(unique) organisation
----------------------------------------

1. Each unique organisation will be identified by its name, so we will provide name of the organisation in the url. Example: http://127.0.0.1:8000/api/organisationdetail/?name=TheDebuggers

2.We will get response like this.

![image](https://user-images.githubusercontent.com/62210359/233950091-c18bf7ae-e1b1-4ca9-a9b6-2059bfcf6260.png)



To create/update permission for a user on an organisation
-----------------------------------------------------------

1.Go to http://127.0.0.1:8000/api/createupdatepermissions/, you will get interface like this.Fill the required details.
Make sure that the organisation and the user exists.

![image](https://user-images.githubusercontent.com/62210359/233951601-93b67842-713d-45c6-9697-c1c5e4d223e5.png)

2. We will get response like this.

![image](https://user-images.githubusercontent.com/62210359/233952336-f159d123-8650-4a7f-b517-a1e5c874da68.png)


 
To delete permission for a user on an organisation
------------------------------------------------------------
1.Go to http://127.0.0.1:8000/api/deletepermissions/, you will get interface like this.Fill the required details.
Make sure that the organisation and the user exists.

![image](https://user-images.githubusercontent.com/62210359/233952701-1b1220fc-bc05-4a81-af7a-460421d4d8bb.png)

2.We will get response like this.

![image](https://user-images.githubusercontent.com/62210359/233952866-19c61756-7d2c-45d2-aed9-5234a459863d.png)


To list out all the permissions for all the users on each organisation
-------------------------------------------------------------------------

1.Go to http://127.0.0.1:8000/api/permissionslist/

2.We will get response like this.

![image](https://user-images.githubusercontent.com/62210359/233953416-18af2ab8-cf85-40b5-9d89-dba1cd05d3fb.png)




Code and API structure
---------------------------------------

1.Firstly I connected my django project to MongoDB with the help of djongo and pymongo packages.

2.I created models for users and organisations.Though django provides built in table for users ,but I created a separate table for that.

3.The ID for each user and organisation will be provided automatically when stored in database.

4.I created serializers for User and Organisation model.

5.Then, created API endpoints for User and Organisation to take data from a POST request and store it in the database.

6.For GET request, I designed and added functionality like providing limit and offset.

7.To write the logic, I took help from the documentation and implemented API using GenericAPIView(ListCreateAPIView,CreateAPIView,etc.)

8.To allot different permissions to different users for an organisation or multiple organisations, I created separate model called Permission.

9.In this, I added functionalities like creating or updating permissions and deleting permissions.

10.For that, I defined serializers i.e. PermissionSerializers to create/update permission and DeletePermissionSerializers to delete permission.

11.Then, created API endpoints for permissions.
