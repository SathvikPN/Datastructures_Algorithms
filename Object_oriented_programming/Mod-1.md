A program can be organized in one of two ways: around its code (what is happening) or around its data (who is being affected).

structured programming: organized around code ("code acting on data")

Object oriented programming: organized around data ("data controlling access to code"). [all OOP languages have three traits in common: encapsulation, polymorphism, and inheritance]

**1. Encapsulation:**
- mechanism that binds together code and the data it manipulates, and keeps both safe from outside interference and misuse. (`private` `public`)
- object is the device that supports encapsulation. object is a variable of a user-defined type, Each time you define a new type of object, you are creating a new data type.
- Typically, the public parts of an object are used to provide a controlled interface to the private elements of the object.

**2. Polymorphism:**
- "one interface, multiple methods."
- reduce complexity by allowing the same interface to be used to access a general class of actions
- One stack is used for integer values, one for character values, and one for floating-point values. Because of polymorphism, you can define one set of names, push( ) and pop( ), that can be used for all three stacks.
- In C++, both run-time and compile-time polymorphism are supported

**3. Inheritance**
- process by which one object can acquire the properties of another object
- through the use of classifications, an object need only define those qualities that make it unique within its class.
- possible for one object to be a specific instance of a more general case

---
**Classes and Objects**
- A class declaration defines a new type that links code and data.
- a class is a logical abstraction, but an object has physical existence (instance of a class)
- By default, functions and data declared within a class are `private` to that class.
- Others: `public` `protected`(private except for it's subclasses)

**Constructor and Destructor (include: Parameterised constructor, Copy Constructor**
 - automatic initialization of obj via constructor function
 - A constructor is a special function that is a member of a class and has the same name as that class.
 - An object's constructor is automatically called when the object is created. (when obj declaration executed)
 - Destructor: perform some action or actions when obj is destroyed. (deallocate the allocated memory or close an opened file)
 - constructors, destructors do not have return values and are public. [Private Constructor Destructor](https://www.geeksforgeeks.org/can-constructor-private-cpp/)
 - Destructor never takes parameters. Constructor can.
Code example: Stack class implementation.

Parameterised Constructor: params to initialise obj.
```cpp
myclass ob(1,2);
myclass ob = myclass(1,2);

myclass ob = 1; // only 1 param case
```
---

**`this` pointer**
- When a member function is called, it is automatically passed an implicit argument that is a pointer to the invoking object.
- Important when: operators overloaded. member func utilise pointer to obj which invoked it.
- Points: 
- friend functions are not members of a class and, therefore, are not passed a `this` pointer
- static member functions do not have a `this` pointer.

---

**Friend classes**
- friend class and all of its member functions have access to the private members defined within the other class.
- it only has access to names defined within the other class. It does not inherit the other class.
- members of the first class do not become members of the friend class.

```cpp
// Using a friend class.
#include <iostream>
using namespace std;
class TwoValues 
{
    int a,b;
public:
    TwoValues(int i, int j) { a = i; b = j; }
    friend class Min;
};

class Min 
{
public:
    int min(TwoValues x) {return x.a < x.b ? x.a : x.b;};
    /* class Min has access to the private variables 
    a and b declared within the TwoValues class.*/
};

int main()
{
    TwoValues ob(10, 20);
    Min m;
    cout << m.min(ob);
    return 0;
}
```
