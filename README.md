# AirBnB_clone
<p align="center">
<img width="400" height="200" alt="AirBnB_clone Image" src="https://github.com/Ddilibe/AirBnB_clone/blob/ad07e6d9a59ceeec98f22e01c379c48200243bf6/download%20(1).png">
</p>

## Description
This project is the first step to take in order to make a consice clone of the AirBnB software. 
It is also the first step towards building a full web application. 
At the point, the major aim is to be able to store data in the background when the program closes, reload it when the program starts and also be able to delete data from the database.
The data is being stored in a JSON file. 
The data contained in the file is deserialized when the program is launch and serialized when the program closes.

## Description Of The Command Interpreter
The command interperter is an interactive shell used to manage the objects of the AirBnB project. It implements the basics of the python cmd library
With the command interpreter, the following can be done:<br/>
1. New objects can be created
2. Existing objects can be retrieved frm the database
3. Different operation can also be computed in the interperter
4. Attributes of an existing object can also be updated
5. And an existing object can also be deleted from the database

### - **How to Start It**

1. First of all, clone the repository

	git clone https://github.com/Ddilibe/AirBnB_clone.git

2. Enter the directory containing the details of the repository

	cd AirBnB_clone

3. Run the console file

	python console.py


### - **How to Use It**

The interactive command interpreter can be able to take in five different commans which are

- _Create_: This command is used to create a new model class instance in the database. It returns the ID of the created instance. It takes in one mandatory argument.

		(hbnb) create <class_name>

- _Show_: This command is used to diaplay the content of a existing class instance. It takes in two mandatory arguments.

		(hbnb) show <class_name> <instance_id>

- _destroy_: This command is used to completely remove an existing instance from the database. It takes also takes in two mandatory arguments.

		(hbnb) destroy <class_name> <instance_id>

- _all_: This command is used to either display all the contents of the database or if it recevies an argument, it displays the content of that instance class. This command takes in an optional argument.
		
		(hbnb) all optional = <class_name>

- _update_: This command is used to update the data of an already existing instance in the database. It takes in four mandatory arguments. 

		(hbnb) update <class_name> <instance_id> <attribute_name> <attribute_value>

**Note**: If the commands with the mandatory commands are not supplied with the mandatory command, an error will arise.


### - **Examples**

The following set of codes below illustrate the method in which the interactive command interperter works


	hp@DESKTOP-45FMCSQ ~/alx/airbnb_clone
	$ python console.py
	(hbnb) all MyModel
	** class doesn't exist **
	(hbnb) show BaseModel
	** instance id missing **
	(hbnb) show BaseModel My_First_Model
	** no instance found **
	(hbnb) create BaseModel
	49faff9a-6318-451f-87b6-910505c55907
	(hbnb) all BaseModel
	["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
	(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
	[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
	(hbnb) destroy
	** class name missing **
	(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
	(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
	[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
	(hbnb) create BaseModel
	2dd6ef5c-467c-4f82-9521-a772ea7d84e9
	(hbnb) all BaseModel
	["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
	(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
	(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
	** no instance found **
	(hbnb)


### Authors
- Fidelugwuowo Dilibe
- Yusuf Usman
