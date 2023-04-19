# Author: Brent Artuch
# Date: 04/19/2023
# Project: Binary Search Tree for Course Referencing

# Class for creating course objects.
class Course:
    course_number = ''
    title = ''

    def __init__(self):
        self.prerequisites = []


# Class for creating the nodes that the courses will be stored in.
class Node:
    course = Course()
    left = None
    right = None

    def __init__(self, a_course):
        self.course = a_course


# Binary Search Tree Class
class BST:
    root = None

    # Method called by load_courses to insert a course into a node
    def insert(self, course):

        if self.root is None:
            self.root = Node(course)
        else:
            self.add_node(self.root, course)

    # Method for adding the node to its proper position within the tree.
    def add_node(self, node, course):

        # If course_number less than root go left.
        if node.course.course_number > course.course_number:
            if node.left is None:
                node.left = Node(course)
            else:
                self.add_node(node.left, course)

        # Else go right.
        else:
            if node.right is None:
                node.right = Node(course)
            else:
                self.add_node(node.right, course)

    # Method called by main to initialize in order traversal.
    def print_schedule(self):
        self.in_order(self.root)

    # Method to output the course in alphanumeric order by course number.
    def in_order(self, node):
        if node is not None:
            self.in_order(node.left)
            print(node.course.course_number + ", " + node.course.title)
            self.in_order(node.right)

    # Method to search for a course by its course number.
    def get_course(self, course_number):
        current = self.root
        while current is not None:

            # If the course numbers match, return the current course.
            if current.course.course_number == course_number:
                return current.course

            # If not go left or right depending on the course number value comparison.
            if current.course.course_number > course_number:
                current = current.left
            else:
                current = current.right

        # If the course is not found return an empty course object.
        empty_course = Course()
        return empty_course


# Method to open the input file and read the data into the program.
def load_courses(txt_path, bst):
    fin = open(txt_path, 'rt')
    for line in fin:
        line = line.strip('\n')
        parsed_line = line.split(',')

        # Create a new course object.
        course = Course()

        course.course_number = parsed_line[0]
        course.title = parsed_line[1]

        if len(parsed_line) < 2:
            print("Not enough inputs.")
            return

        for i in range(2, len(parsed_line)):
            course.prerequisites.append(parsed_line[i])

        # Add the defined course object to the tree.
        bst.insert(course)

    fin.close()
    print("Courses loaded.")


# Method to print the selected course called by the main function.
def display_course(course):
    print(course.course_number + ", " + course.title)

    print("Prerequisites: ", end="")
    for i in range(0, len(course.prerequisites)):
        if i == len(course.prerequisites)-1:
            print(course.prerequisites[i])
        else:
            print(course.prerequisites[i], end=", ")

    return


if __name__ == '__main__':
    print("Welcome to the course planner.")

    # Define the bst and the text path for the input file.
    course_tree = BST()
    text_path = 'ABCU_Advising_Program_Input.txt'

    while True:
        print()
        print("1. Load Data Structure")
        print("2. Print Course List")
        print("3. Print Course")
        print("9. Exit")
        print()

        choice = input("What would you like to do? ")

        # Input Error handling.
        if choice != "1" and choice != "2" and choice != "3" and choice != "9":
            choice = input("Enter 1, 2, 3, or 9: ")
            print()

        # Exit condition.
        if choice == "9":
            break

        # Load Courses
        if choice == "1":
            print("Loading Data Structure...")
            load_courses(text_path, course_tree)

        # Print Course List
        elif choice == "2":
            print("Here is a sample schedule:")
            print()
            course_tree.print_schedule()

        # Print Course
        elif choice == "3":
            desired_course = input("What course do you want to know about? ").upper()

            if len(desired_course) < 7:
                desired_course = input("Error: Invalid course number format. \n"
                                       "Enter course number: ").upper()

            located_course = course_tree.get_course(desired_course)

            if located_course.course_number != '':
                display_course(located_course)
            else:
                print("Error: course not found.")

    print("Thank you for using the course planner!")
