`Topics`

* List
* Tuples
* Sets
* Dictionary

---

`Notes`

### Lists

**Definition:** Lists are used to store multiple items in a single variable.

**Example :**

```python
mylist = ["apple", "banana", "cherry"]
```

> List items are ordered, changeable, and allow duplicate values.

---

> List items are indexed, the first item has index [0], the second item has index [1] etc.

* To determine how many items a list has, use the `len()` function

```python
print(len(this_list))
```

---

* List items are indexed and you can access them by referring to the index number

```python
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
```

---

* You can specify a range of indexes by specifying where to start and end the range.

```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
```

> This prints elements of index 2, 3, and 4

---

* To determine if a specified item is present, use the `in` keyword

```python
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
```

---

* To change a specific item, refer to the index number

```python
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
```

---

* Add item to end using `append()`

```python
thislist.append("orange")
```

---

* Insert at a specific index using `insert()`

```python
thislist.insert(1, "orange")
```

---

* Extend a list using `extend()`

* Remove an item using `remove()`

```python
thislist.remove("banana")
```

---

* Remove using index with `pop()`

```python
thislist.pop(1)
```

---

* Delete using `del` keyword

```python
del thislist[0]
```

---

* Clear list using `clear()`

```python
thislist.clear()
```

---

* Loop through list using `for` loop

```python
for x in thislist:
  print(x)
```

---

### List Methods

| Method    | Description                                                     |
| --------- | --------------------------------------------------------------- |
| append()  | Adds an element at the end of the list                          |
| clear()   | Removes all the elements from the list                          |
| copy()    | Returns a copy of the list                                      |
| count()   | Returns the number of elements with the specified value         |
| extend()  | Adds the elements of another iterable to the end of the list    |
| index()   | Returns the index of the first element with the specified value |
| insert()  | Adds an element at the specified position                       |
| pop()     | Removes the element at the specified position                   |
| remove()  | Removes the item with the specified value                       |
| reverse() | Reverses the order of the list                                  |
| sort()    | Sorts the list                                                  |

---

### Tuples

**Definition:** Tuples are used to store multiple items in a single variable. They are similar to lists but **unchangeable**.

**Example:**

```python
mytuple = ("apple", "banana", "cherry")
```

> Tuple items are ordered, unchangeable, and allow duplicates.

---

* Tuples are indexed like lists

```python
print(mytuple[1])
```

---

* Tuples allow slicing

```python
print(mytuple[1:3])
```

---

* Check if an item exists in a tuple

```python
if "apple" in mytuple:
  print("Yes")
```

---

* Tuples cannot be changed, but you can convert them to lists and back

```python
y = list(mytuple)
y.append("orange")
mytuple = tuple(y)
```

---

* Loop through tuples

```python
for x in mytuple:
  print(x)
```

---

### Tuple Methods

| Method  | Description                             |
| ------- | --------------------------------------- |
| count() | Returns number of times a value appears |
| index() | Returns index of first occurrence       |

---

### Sets

**Definition:** Sets are used to store multiple items in a single variable. Sets are **unordered**, **unindexed**, and **do not allow duplicates**.

**Example:**

```python
myset = {"apple", "banana", "cherry"}
```

> Items cannot be accessed using index numbers.

---

* Add items using `add()`

```python
myset.add("orange")
```

---

* Add multiple items using `update()`

```python
myset.update(["mango", "grapes"])
```

---

* Remove an item using `remove()`

```python
myset.remove("banana")
```

> Raises error if item doesn't exist.

---

* Remove item using `discard()` (no error raised)

```python
myset.discard("banana")
```

---

* Remove last item using `pop()`

```python
myset.pop()
```

---

* Clear a set

```python
myset.clear()
```

---

* Loop through a set

```python
for x in myset:
  print(x)
```

---

* Perform set operations: union, intersection, difference

```python
set1.union(set2)
set1.intersection(set2)
set1.difference(set2)
```

---

### Set Methods

| Method         | Description                                |
| -------------- | ------------------------------------------ |
| add()          | Adds an element to the set                 |
| clear()        | Removes all elements                       |
| copy()         | Returns a copy of the set                  |
| difference()   | Returns the difference of two sets         |
| discard()      | Removes specified item if present          |
| intersection() | Returns items that exist in both sets      |
| isdisjoint()   | Returns True if no items in common         |
| issubset()     | Returns True if set is subset              |
| issuperset()   | Returns True if set is superset            |
| pop()          | Removes a random item                      |
| remove()       | Removes specified item                     |
| union()        | Returns the union of sets                  |
| update()       | Adds elements from another set or iterable |

---

### Dictionary

**Definition:** Dictionaries store data in **key: value** pairs. They are **ordered**, **changeable**, and do not allow duplicate keys.

**Example:**

```python
mydict = {
  "name": "John",
  "age": 25,
  "city": "Lahore"
}
```

---

* Access items by key

```python
print(mydict["name"])
```

---

* Get all keys

```python
print(mydict.keys())
```

---

* Get all values

```python
print(mydict.values())
```

---

* Change a value

```python
mydict["age"] = 30
```

---

* Add a new key-value pair

```python
mydict["country"] = "Pakistan"
```

---

* Remove item using `pop()`

```python
mydict.pop("age")
```

---

* Remove last inserted item using `popitem()`

```python
mydict.popitem()
```

---

* Loop through keys, values, items

```python
for x in mydict:
  print(x)

for v in mydict.values():
  print(v)

for k, v in mydict.items():
  print(k, v)
```

---

### Dictionary Methods

| Method       | Description                                            |
| ------------ | ------------------------------------------------------ |
| clear()      | Removes all the elements                               |
| copy()       | Returns a copy                                         |
| fromkeys()   | Returns dict with specified keys and default value     |
| get()        | Returns value of specified key                         |
| items()      | Returns list of tuples (key, value)                    |
| keys()       | Returns list of keys                                   |
| pop()        | Removes item with specified key                        |
| popitem()    | Removes the last inserted key-value pair               |
| setdefault() | Returns value of key; inserts if not present           |
| update()     | Updates dictionary with another dictionary or iterable |
| values()     | Returns list of values                                 |
