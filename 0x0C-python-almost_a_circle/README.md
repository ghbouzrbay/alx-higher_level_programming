**General**

*What is Unit testing and how to implement it in a large project*

*How to serialize and deserialize a Class*

*How to write and read a JSON file*

*What is *args and how to use it*

*What is **kwargs and how to use it*

*How to handle named arguments in a function*


** *args and **kwargs in python explained **

** Usage of *args **

*args and **kwargs are mostly used in function definitions.

*args and **kwargs allow you to pass a variable number of arguments to a function.

What does variable mean here is that you do not know before hand that how many arguments can be passed

to your function by the user so in this case you use these two keywords.

*args is used to send a non-keyworded variable length argument list to the function


** Usage of **kwargs **

**kwargs allows you to pass keyworded variable length of arguments to a function.

You should use **kwargs if you want to handle named arguments in a function


** unittest — Unit testing framework**

*(If you are already familiar with the basic concepts of testing, you might want to skip to the list of assert methods.)*

*The unittest unit testing framework was originally inspired by JUnit and has a similar flavor as major unit testing frameworks in other languages.*

*It supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework.*

*To achieve this, unittest supports some important concepts in an object-oriented way:*

**test fixture**

*A test fixture represents the preparation needed to perform one or more tests, and any associate cleanup actions.*

*This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.*

**test case**

*A test case is the individual unit of testing.*

*It checks for a specific response to a particular set of inputs.*

*unittest provides a base class, TestCase, which may be used to create new test cases.*

**test suite**

*A test suite is a collection of test cases, test suites, or both. It is used to aggregate tests that should be executed together.*

**test runner**

*A test runner is a component which orchestrates the execution of tests and provides the outcome to the user.*

*The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of executing the tests.*
