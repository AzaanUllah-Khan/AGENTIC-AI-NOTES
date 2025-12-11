`Python Modules`

### What is a Module:
- Consider a module to be the same as a code library
- A file-containing a set of functions you want to include in your application

### Create a Module :
- To create a module just save the code you want in a file extension `.py`

```python
def greeting(name):
  print("hello",name)
```

### Use a  Module :
- To use a module we have to use `import` keyword

```python
import mymodule #module file name

mymodule.greeting("Azaan")
```

### Variables in Module :
- Variables can also contain variables of all types along with function

```python
person1 = {
  "name": "Azaan",
  "age": 16
}
```

- Use with Variables

```python
import mymodule #module file name

print(mymodule.person1["name"])
```

### Rename a Module

```python
import mymodule as mx

print(mx.person1["age"])
```

### Using dir() Function

- List all the defined names belonging to the platform module

```python
import platform

x = dir(platform)
print(x)
```

> The `dir()` function can be used on all modules, also the ones you create yourself.

### Import from Module

`To be completed`
