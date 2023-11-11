
# Operator Precedence
- Order of evaluation for the operators. Each operator will be executed
in different time even they are in the same line.

### Precedence
**1**. Parenthesis
**2**. Exponentiation
**3**. Remainder(Modules), Division, Multiplication
**4**. Addition, Substraction

#### Note! If the operators have the same precedence they will be evaluated
#### from left to right.

-- '3 + 7 * 2 - 10 + 10 / 1 -> 


#### Note! When in doubt you can use paranthesis to make sure 
#### things are evaluated in order you wanted.


## ---------------------------------------------

# Reassignment in Python
In python variables are simply names pointing to objects.
Reassignment refers to changing the object a variable points to after its
intitial assignment.


python
var1 = "s"
print(var1) # s
var1 = 10 # This is the reassignment.
print(var1) # 10 
### Compound reassignment operators in python
Compound assignment operators are shortcuts that combine a basic operation like addition, subtraction, multiplication, etc. with reassignment. 

- **`+=`**:  Add the value on the right side and reassign it. 
- **`-=`**:  Subtract the value on the right side and reassign it. 
- **`*=`**:  Multiply the value and then reassign it
- **`/=`**:  Divide the value and then reassign it.
- **`%=`**:  Find the remainder and then reassign it.
- **`**=`**: Exponentiate the value and then reassign it.

**+=**
python
x = 5
x += 10 # same as x = x + 10
print(x) #15
**-=**
python
x = 5
x -= 10 # same as x = x - 10
print(x) # -5
**\*=**
python
x = 5
x = 10 # same as x = x 10
print(x) # 50
**/=**
python
x = 5
x /= 10 # same as x = x / 10
print(x) # 0.5
**%=**
python
x = 5
x %= 10 # same as x = x % 10
print(x) # 5
**\*\*=**
python
x = 5
x = 3 # same as x = x  3
print(x) # 5 * 5 * 5 -> 125







