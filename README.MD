Master of Numbers V2 - a Number to Word package
================

###This is a Python library for converting numbers into word representation

Developed with:
```
- Python 3.9.6
```

###To Build this project

```
- python3 -m venv .venv
- .\.venv\Scripts\activate will activate the virtual environment (for windows platform)
- source .venv/bin/activate will activate the virtual environment (for macos/linux platform)
- do not worry about requirements.txt, this project has no external dependencies
```

### To RUN this project:
```
Just run main.py and give any number between 0 and 999 quintillion
```

Directory tree
```
|root
|.gitignore
|helper.py
|LICENSE
|main.py
|number_to_string.py
|README.MD
```
Inside ```numbers/number_to_string.py``` is the integer to string conversion engine.

We have 3 different lists:
* ```unique_numbers``` - lists of integers from 0 to 19 with unique nomenclatures
* ```multiples_rounded``` list of integers of multiples of 10 up to 99
* ```millions_num``` integer scale label

Inside ```MasterOfNumbers``` we have different methods to handle the given number:

* ```define_method``` will handle if a given number will be labeled with one of below tags:
```
1 to 19             - unique labeled numbers
20 to 99            - multiple ten rounded and its compositions
100 to 1.000	    - hundreds and its compositions
1.000   	    - over thousands (million, billion...)
```
After defining the tags of each given value, the corresponding method will be triggered
* input number will handle the input value
* call_methods will handle values according to the field number
* convert_unique_numbers will handle values between 0 and 19 
* convert_up_to_hundred will handle values between 20 and 99
* convert_up_to_thousand will handle values between 1000 and 999
* convert_over_thousand will handle values above 1.000
* helper.py there are auxiliary functions

Inside ```main.py``` we have a simple call to simulate an external call after package install

### Improvements
* improve Exceptions handling
* improve a code coverage and test with ```codecov```
* improve code test efficiency with some solid external package (i.e pytest)