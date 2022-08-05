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
With the command interpreter,
	1. New objects can be created
	2. Existing objects can be retrieved frm the database
	3. Different operation can also be computed in the interperter
	4. Attributes of an existing object can also be updated
	5. And an existing object can also be deleted from the database

- **How to Start It**
The command interpreter is started by runing the console.py file

	python console.py


- **How to Use It**
The interactive command interpreter can be able to take in five different commans which are
	- _Create_: This command is used to create a new model class instance in the database. It returns the ID of the created instance. It takes in one argument. <br/> `(hbnb) create BaseModel`<br/>


- **Examples**
