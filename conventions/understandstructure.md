## PhpMyAdmin automation structure:
##### will be updated

* tests
    * test_helpers
        * set of test helpers
    * all set of tests
* conventions
    * markdown files about conventions
* page_objects
    * pages classes and files
* Application. py
* conftest. py
* wrapper. py


## tests
Contains tests and methods that are using in tests

### test_helpers
Contain all set of test helpers files. Every test helper file needs to have methods from one set of functionality (create database, managing settings, login functions).

### all set of tests
Files typically named like "test_name_of_test.py" that contains tests using "AAA" method https://habr.com/ru/post/169381/

## conventions 
Files with project conventions

## page_objects

### pages classes and files
Contain files (name_page.py) with pages classes (NamePage) and pages locators (NamePageLocator) that are used in pages. 

Pages classes have basic methods which we can use while interacting with application (typing in inpux, check in checkbox, click submit)

## Application 
Contains instances of all pages that are used

## conftest 
Contains fixtures

## wrapper
Contains basic wrapped functions (find_element, click, find_elements)




