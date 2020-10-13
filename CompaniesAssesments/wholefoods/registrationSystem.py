'''
Create the username portion of a registration system that requires all usernames are unique.
If a new user requests a name that is already used, an integer should be added to the end of the username to make it
unique The numbering begins with 1 and is incremented by 1 for each new instance per user name.

Example1:

Input
alex xylos alex alan

Output
alex xylos alex1 alan

Example2:

Input
John Peter Sam John Sam Rock John

Output
John Peter Sam John1 Sam1 Rock John2
'''

class Solution:
    def clean(self, usernames):
        pass


if __name__ == "__main__":
    arr = ["John", "Peter", "Sam", "John," "Sam", "Rock", "John"]
