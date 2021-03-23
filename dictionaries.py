# Dictionaries
# Dictionaries use Key Value pairs to save the data
# The data can be retrieved by its value or the key
# Syntax {}
# Within the dictionary we can also have list declared

# Let's create one
dev_ops_student = {
    "key": "value",
    "name": "James",
    "stream": "devops",
    "completed_lesson": 3,
    "completed_lesson_names": ["variables", "data types", "collections"]
}

# print(dev_ops_student)
# # Confirm the type
# print(type(dev_ops_student))

# print(dev_ops_student["name"])
# print(dev_ops_student["completed_lesson"])
# print(dev_ops_student["completed_lesson_names"][1])
#
# print(dev_ops_student.keys())
# print(dev_ops_student.values())

# Add "operators" in completed_lesson_names
dev_ops_student["completed_lesson_names"].append("operators")
print(dev_ops_student["completed_lesson_names"])

# Change completed_lesson from 3 to 4
dev_ops_student["completed_lesson"] = 4
print(dev_ops_student["completed_lesson"])

# Remove the "data type" from completed_lesson_names
dev_ops_student["completed_lesson_names"].remove("data types")
print(dev_ops_student["completed_lesson_names"])
