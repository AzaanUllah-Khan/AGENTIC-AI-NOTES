`Topics`

- List
- Tuples
- Sets
- Dictionary

___


`Notes`

### Lists

**Definition:** Lists are used to store multiple items in a single variable.

**Example :**

```python
mylist = ["apple", "banana", "cherry"]
```


> List items are ordered, changeable, and allow duplicate values.
___

> List items are indexed, the first item has index [0], the second item has index [1] etc.
- To determine how many items a list has, use the `len()` function
```python
print(len(this_list))
```
___

- List items are indexed and you can access them by referring to the index number
```python
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
```
___

- You can specify a range of indexes by specifying where to start and where to end the range.
``` python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
```
> This print elements of 2nd 3rd and 4th index
___

- To determine if a specified item is present in a list use the `in` keyword
```python
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
```
___

- To change the value of a specific item, refer to the index number
```python
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
```
> This replaces banana with blackcurrant
___

- To add an item to the end of the list, use the `append()` method
```python
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
```
> This adds orange to the last of the list
___

- To insert a list item at a specified index, use the `insert()` method.
```python
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
```
> Adds Orange at index 1
___

- To append elements from another list to the current list, use the `extend()` method.
> The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
___

- The remove() method removes the specified item.
```python
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
```
> If there are more than one item with the specified value, the remove() method removes the first occurrence
___

- The pop() method removes the specified index
```python
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
```
> This removes the second element ie: banana
___

- The del keyword also removes the specified index
```python
thislist = ["apple", "banana", "cherry"]
del thislist[0]
```
- The del keyword can also delete the list completely.

```python
thislist = ["apple", "banana", "cherry"]
del thislist
```
___

- The `clear()` method empties the list.

```python
thislist = ["apple", "banana", "cherry"]
thislist.clear()
```
___

- You can loop through the list items by using a `for` loop
```python
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
```
___

- List comprehension offers a **shorter syntax** when you want to create a new list based on the values of an existing list.
___

- List objects have a `sort()` method that will sort the list alphanumerically, ascending, by default
> By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
___

- The reverse() method reverses the current sorting order of the elements.
___

### List Methods

| Method     | Description                                                                 |
|------------|-----------------------------------------------------------------------------|
| append()   | Adds an element at the end of the list                                      |
| clear()    | Removes all the elements from the list                                      |
| copy()     | Returns a copy of the list                                                  |
| count()    | Returns the number of elements with the specified value                     |
| extend()   | Adds the elements of another list (or iterable) to the end of the list      |
| index()    | Returns the index of the first element with the specified value             |
| insert()   | Adds an element at the specified position                                   |
| pop()      | Removes the element at the specified position                               |
| remove()   | Removes the item with the specified value                                   |
| reverse()  | Reverses the order of the list                                              |
| sort()     | Sorts the list                                                              |
