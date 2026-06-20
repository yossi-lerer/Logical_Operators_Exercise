# part 1
# step 1
is_online = True
has_access = False
print(f"is online {is_online}. has access {has_access}")
# step 2
print(f"is online or has access {is_online or has_access}")
# step 3
status = False
print(f"status {not status}")
# step 4
age = 20
has_id = True
print(f"the person can enter {age >= 18 and has_id == True}")
# step 5
level = 3
print(f"the level is between 1 and 5 {level >= 3 and level <= 5}")
# step 6
a = 0
b = "hello"
c = ""
print(f"bool: the 0 is {bool(a)}. the hello is {bool(b)}. the empty string is {bool(c)}")
# step 7
x = None
y = 42
print(f"the result of none or 42 in bool: {x == True or y == True}")
# step 8
username = ""
default = "guest"
print(username or default)
# step 9
print(f"the results of True and False or True is: {True and False or True}")
print(f"the order of True and False or True: first check True and False: {True and False}. then check or True: {True}. and if one of that is true so the result is true")
# step 10
score = 75
print(f"the score is {score} so is between 60 and 100 inclusive: {60 <= score <= 100}")

# part 2
# step 1
door_locked = True
has_key = False
admin_override = True
print(f"the door can open or not: {has_key or admin_override and door_locked}")
# step 2
message = "" 
backup_message = "No message found"
print(message or backup_message)
# step 3
x = None
print("x is None This is useful for cases where a user is defined as empty.")
# step 4
a = 0
b = "ready"
c = 42
print(f"The test performed on a or b or c checks the first one that is True and returns it: {a or b or c}")
# step 5
score = 50
print("pass" if score >= 60 else "fail")