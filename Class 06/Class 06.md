`Topics`
- If, Else and Elif overview
- Loops
  - For loop
  - While Loop
  - Do While Loop (Only definition)
  - Nested Loops
 
`Class Notes`

* **Definition of Loops:** Loops allow you to repeat a block of code multiple times, making programs efficient and dynamic.
* **Types Of Loops**
    - `While Loop:` The while loop executes a block of code as long as a condition is true.
    - `For Loop:` The for loop is used to iterate over a sequence (like a list, tuple, or range).

### For Loop
`Syntax`

```python
for variable in sequence:
    # code block
```
`Example`

```python
for i in range(5):
    print("Iteration:", i)
```
> `range(5)` generates values from `0` to `4`.

### While Loop
`Syntax`

```python
while condition:
    # code block
```
`Example`

```python
count = 1
while count <= 5:
    print("Count:", count)
    count += 1
```
> **Note:** Always ensure the condition eventually becomes `False` to avoid infinite loops.

### Nested Loops
You can place one loop inside another to work with multi-dimensional data or repeated iterations.

`Example`

```python
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")
```

### Indentation in Loops

- Indentation defines which block of code belongs to the loop.
- Python uses indentation (usually 4 spaces) instead of braces `{}`.

`Example`

```python
for i in range(3):
    print("Inside loop")
print("Outside loop")
```
> The second print statement runs once because it’s outside the loop.
