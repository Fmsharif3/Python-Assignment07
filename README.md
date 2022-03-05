###### Fatima Sharif
###### February 27, 2022
###### Foundations Of Programming: Python 
###### Assignment07 
###### https://github.com/Fmsharif3/Python-Assignment07

# Exception Handling and Pickling in Python
## Introduction:
In this paper I will explain to you the steps I took to create a new script that demonstrates how Structured error handling and Pickling work in Python.
## Exception Handling: 
While programming we sometimes run into syntax or exception errors. Syntax errors occur when using the wrong indentation or when there are too many brackets. Exception errors on the other hand occurs when syntactically correct code results in an error.
## Exceptions Versus Syntax Error: 
Below are some examples of exception and syntax errors that I found very useful at https://realpython.com/python-exceptions/. Figure 1 displays a syntax error due to the use of too many brackets. While Figure 2 displays an exception error. You’ll notice that in figure two Python doesn’t display this error as an “exception error” but rather displays the specific exception type as, “ZeroDivisionError.” This is because Python comes with many built- in exceptions.

<img width="281" alt="image" src="https://user-images.githubusercontent.com/86077092/156899021-e9c5367a-66a0-46a5-8142-f5d8a73121bd.png">
Figure 1: Syntax Error 

<img width="281" alt="image" src="https://user-images.githubusercontent.com/86077092/156899079-dfb5e5ae-a7b8-4229-89c5-61652475f820.png">
Figure 2: Exception Error

## The try and except Block - Handling Exceptions: 
The easiest way to handle exceptions is to use the try statement with an except clause. The try statement allows you to section off some code that could potentially raise an exception. While the except clause allows you to provide a block of statements that are executed only if an exception is raised.    

## Example of an Exception Error: 
After doing some research and going through examples from this week’s lecture video I decided to try out the try and except block. I first opened PyCharm created a new project then, in that project file I opened a new python file and began to test out the try and except block. Using the try statement, I ask python to open a text file then decided to use the except clause to print a message to the user if the text file is found. Lastly, using the else clause to print a message if the file cannot be found.  

<img width="281" alt="image" src="https://user-images.githubusercontent.com/86077092/156899124-fc5abfb5-c258-4310-89dd-2b564f58d0f6.png">
Figure 3: My example Using the try Statement With an except clause

## Pickling In Python: 
Moving onto pickling, I searched the internet for webpages with examples of how to read, write, and save a binary file.  While exploring the pickling method, I learned that pickling is the best way to save complex data then converting to text files and that you could also use the pickle method on tuples, list, and dictionaries. After watching a few YouTube video’s, I then decided to try pickling on my own in PyCharm. Below is my example.

<img width="284" alt="image" src="https://user-images.githubusercontent.com/86077092/156899226-2cd5e684-a645-4e11-a0fc-a2c567acacc6.png">
Figure 4: Pickling Method example

## Outout: 
<img width="310" alt="image" src="https://user-images.githubusercontent.com/86077092/156899300-bb2bf949-1876-4b4a-b598-8f2520dcc479.png">

## Pickling File: 

<img width="309" alt="image" src="https://user-images.githubusercontent.com/86077092/156899321-2a9acc10-4b23-49ff-b4b1-3b089e53df9d.png">

## Terminal Output: 

<img width="468" alt="image" src="https://user-images.githubusercontent.com/86077092/156899329-1d43c40e-2e3f-49b3-87a3-8b330bdfebd0.png">

## Summary:
In this paper I explained to you the steps I took to create a new script that demonstrates how Pickling and Structured error handling work.

