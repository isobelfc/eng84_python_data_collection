# Data Collections in Python
- Lists and Tuples
- Dictionaries
- Sets

### What is a list?
- Lists are commonly used to store data
- They are mutable
- Syntax `[]` used to create a list
- List items are also indexed
- Different data types can be mixed in the same list
  
### List methods
- List values can be changed with e.g. `ex_list[0] = "first"` to change the first value to "first"
- `ex_list.append("new")` adds the value "new" to the end of the list
- `ex_list.pop(0)` removes the value at the given index, or the last value if no index is specified, and returns the popped value
- `ex_list.remove("item")` removes the value "item" from the list
- We can also use slices with lists

### What is a tuple?
- A collection of data, similar to a list
- Syntax `()`
- The difference between lists and tuples is that tuples are immutable
- Used for data that will never change
- Trying to change data in a tuple will result in an error
- The same methods can be applied to tuples and lists (except for those which change data)

### Dictionaries
- Uses key value pairs
- Syntax `{}`
- ```python
  example_dictionary = {
    "key": "value",
    "name": "James",
    "skills": ["spy", "kill"]
  }
  ```
- Values can be lists
- The data can be retrieved by its value or the key
- `print(example_dictionary["name"])`
- To retrieve a specific list value, add its index in square brackets after the key
- `print(example_dictionary["skills"][0])`
- Dictionary values can be changed in the same way as list values

### Sets
- Syntax `{}`
- Sets are unordered
- They return the values in a random order each time
- Remove values using `ex_set.discard("value")`
- Rarely used