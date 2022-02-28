**Function Overloading**
- Two or more functions can share the same name as long as their parameter declarations are different.
- t each redefinition of the function must use either different types of parameters or a different number of parameters
-  Two functions differing only in their return types cannot be overloaded.
-  Sometimes, two function declarations will appear to differ, when in fact they do not
```cpp
void f(int *p);
void f(int p[]); // error, *p is same as p[]
```

**Friend function**
-  A friend function has access to all private and protected members of the class for which it is a friend.
-  called without the use of the dot operator.
-  a derived class does not inherit friend functions.
-  friend functions may not have a storage-class specifier. That is, they may not be declared as `static` or `extern`

**Inline functions**
- short functions that are not actually called; rather, their code is expanded in line at the point of each invocation
-  arguments are pushed onto the stack and various registers are saved when a function is called, and then restored when the function returns.
-  when a function is expanded in line, none of those operations occur.
-  o result in larger code size because of duplicated code. 
-  , inline is actually just a request, not a command, to the compiler.

**Default Function Arguments**
- assign a parameter a default value when no argument corresponding to that parameter is specified in a call to that function
- default values must be specified only once, and this must be the first time the function is declared within the file
- Once you begin to define parameters that take default values, you cannot specify a nondefaulting parameter.
- prevent you from having to provide an overloaded constructor that takes no parameters.

**Operator Overloading**
- When an operator is overloaded, none of its original meanings are lost. Instead, the type of objects it can be applied to is expanded
- `operator+( )` has only one parameter even though it overloads the binary + operator.
```cpp
// Overload + for loc.
loc loc::operator+(loc op2)
{
loc temp;
temp.longitude = op2.longitude + longitude;
temp.latitude = op2.latitude + latitude;
return temp; // loc object
```

