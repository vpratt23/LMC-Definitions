# examples
How This Code is Organized

The basic structure of this code is based off of .py files, which are named after whatever key investigative purpose they serve. The majority of the .py files consist of various methods which one can use to produce the same or similar analysis as I did. Some of the .py files contain functions and some key dictionaries which I used (use) as a reference point within my own analysis. 

There are also two notebook, one of some key plots I made from the SAGA and simulation and the other of key plots of the environmental data around the SAGA hosts. Running those notebook reproduces those plots. The environment notebook in particular also serves as an example of how 


How to Use the Code

For specific instructions on the .py functions themselves, see the various docstrings that are attached to each. In general, you can import each of the functions in the .py files and use their methods in a way that mirrors my own analysis, though streamlined slightly, simplifying the process for future papers. 

Each .py file or Jupiter notebook has certain dependencies, which are imported at the start of the code. The initializing_saga.py file initializes the SAGA code and imports most of the python packages that will be used in subsequent methods. 

Dependency Note

While the rest of the imports can be called through a general import statement, one dependency for the notebook entitled "Environment Time" must be edited to match your own computer setup. Namely, to call and use master_list_v2.csv, I employed a command that traced the specific path in my file system to where I had downloaded that master list. If you wish to use that command, you must change the path from mine to yours.  


