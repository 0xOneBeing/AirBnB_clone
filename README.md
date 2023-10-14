# `GROUP PROJECT - 0X00. AirBnB clone - The console`

# `Description of Project`

# This is a team project of an AirBnB clone done by Sunday Oruwhone and Adaugo Onuecheghekwu.

The console functions as a command interpreter for overseeing the abstraction of objects and their storage management.

* The console is tasked with the following operations:

* Creating a new object
* Retrieving an object from a file
* Performing operations on objects
* Destroying objects.


# `AirBnB clone`

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/263/HBTN-hbnb-Final.png)

# `AirBnB clone - The console`
The goal of the project is to deploy on a server a simple copy of the AirBnB website.
It will not implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

# `Initial Phase:` Develop a command interpreter to oversee the management of your AirBnB objects.

This initial stage holds significant importance, as it serves as the foundation for subsequent projects, including HTML/CSS templating, database storage, API integration, and front-end development.

# `What is a command interpreter? :`

Think of it as the Shell you're familiar with, but tailored for a specific purpose. In our context, it's designed for handling the various objects within our project:

1. Creating new objects, such as a new User or a new Place.
2. Retrieving objects from sources like files or databases.
3. Performing operations on objects, such as counting and computing statistics.
4. Updating attributes of objects.
5. Deleting objects when necessary.

# `Execution`

You can operate as follows in interactive mode:

	$ ./console.py
	(hbnb) help

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit

	(hbnb) 
	(hbnb) 
	(hbnb) quit
	$

But also in non-interactive mode: (like the Shell project in C)

	$ echo "help" | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb) 
	$
	$ cat test_help
	help
	$
	$ cat test_help | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb) 
	$

# `Commands:`
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* update - Updates an instance based on the class name and id
* quit/EOF - quit the console
* help - see descriptions of commands

To start console type in shell

    AirBnB_clone$ ./console.py
    (hbnb) 

## `Create`
To create an object use format "create <ClassName>" ex:

	(hbnb) create BaseModel

## `Show`
To show an instance based on the class name and id. Ex: 

	(hbnb) show BaseModel 1234-1234-1234.

## `Destroy`
To Delete an instance of an object use "destroy <ClassName> id". Ex: 

	(hbnb) destroy BaseModel 1234-1234-1234.

## `All`
all or all <class name> Ex: 

	(hbnb) all or all State

## `Update`
Updates an instance based on the class name and id:

	(hbnb) update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"

## `Quit`
quit or EOF

## `Help`
help or help <command> Ex: 

	(hbnb) help or help quit
	 Defines quit option
	(hbnb) 

# `Supported classes:`
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

# `Authors`

* Adaugo Sandra Onuecheghekwu <onuecheghekwuadaugo@gmail.com>

* Sunday Oruwhone <sundayoruwhone@gmail.com>
