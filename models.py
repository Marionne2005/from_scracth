class Student():
    def __init__(self, name, email, gpa, program):
        self.name = name
        self.email = email
        self.gpa = gpa
        self.program = program

    def __str__(self):
        return f"Student(name={self.name}, email={self.email}, gpa={self.gpa}, program={self.program})"    
    
    # Getters and setters for name
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    # Getters and setters for email
    def get_email(self):
        return self.email
    def set_email(self, email):
        self.email = email

    # Getters and setters for gpa
    def get_gpa(self):
        return self.gpa
    def set_gpa(self, gpa):
        if 0.0 <= gpa <= 4.0:
            self.gpa = gpa
        else: 
            raise ValueError("GPA must be between 0.0 and 4.0")    

    # Getters and setters for program
    def get_program(self):
        return self.program
    def set_program(self, program):
        self.program = program

    """ init is the constructor it runs automatically when an object is created, initializing its attributes.
        str defines a readable string representation of the object, useful for debugging and display. 
        Getters and setters control access to attributes, allowing validation logic for example, 
        ensuring a GPA stays within a valid range, which is a core principle of encapsulation."""
    