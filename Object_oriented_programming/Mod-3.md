**Base-Class Access Control**
- When a class inherits another, the members of the base class become members of the derived class.
```cpp
class derived-class-name : access base-class-name {
// body of class
};
```
1. access specifier for a base class is public:
- public elements of base == public of derived
- base's private elements remain private to the base and are not accessible by members of the derived class

2. base class is inherited by using the private access specifier,
- (public, protected) of base == private of derived 
- (This means that they are still accessible by
members of the derived class but cannot be accessed by parts of your program that are
not members of either the base or derived class)

3. o inherit a base class as protected: all public and protected members of the base class become protected members of the derived class

- By using protected, you can create class
members that are private to their class but that can still be inherited and accessed by a
derived class.

- any protected
member of the initial base class that is inherited (as public) by the first derived class
may also be inherited as protected again by a second derived class. 

- base were inherited as private, then all members of base would
become private members of derived1, which means that they would not be accessible
by derived2.

**Inheriting multiple base classes**
```cpp
class derived: public base1, public base2 
```

**Virtual Functions**
- compile-time polymorphism: overloading functions and operators.
- Run-time polymorphism: using inheritance and virtual functions
- A virtual function is a member function that is declared within a base class and redefined
by a derived class. keyword virtual.

**Pure Virtual Functions**
- A pure virtual function is a virtual function that has no definition within the base class.
- General Form `virtual return_type func_name(parameter_list) = 0;`
- When a virtual function is made pure, any derived class must provide its own
definition. If the derived class fails to override the pure virtual function, a compile-time
error will result.
