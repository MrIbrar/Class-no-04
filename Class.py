# Let's Practice
# Store following word meanings in a python dictionary:
# table: "a piece of furniture", "list of facts & figures"
# cat: "a small animal"

dic = {
    "table": ["a piece of furniture", "list of facts & figures"],
"cat": "a small animal"
}

print(dic)


# You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
# "python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"

Set = {
    "python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"
}

print(len(Set))


# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
Dir = {}
def subjects():
    for subject in ["Chemistry", "Bio", "Maths"]:
        n=input(f"enter marks of {subject} subjects: ")
        Dir[subject] = n
    return Dir

print("The Dictionary is:",subjects())
        

# Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)

# one way to solve these Question by using String concept
Set = {9.0, "9"}
print(Set)

# Another way to solve these Question by using tuples concept
Set = {("float",9.0), ("int",9)}
print(Set)
