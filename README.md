# README

A python (2 or 3) class to load JSON data from a url. 

To use either:
1) Intialise the class with a url and call get_data.
or 
2) Intiailise the class without a url and call set_url when you are ready. Then call get_data.

Calling get_data with to_file=True sends the data to a file after being formatted. Calling get_data with no parameters or to_file=False returns the data as a string.