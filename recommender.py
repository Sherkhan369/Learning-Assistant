

class Recommender:
    def __init__(self):
        self.topics = {
            "monday": {
                "topic": "function",
                "code": "def greet(name):\n    return f\"Hello, {name}\" \n print(greet(\"World\"))",
                 "youtube": "https://www.youtube.com/watch?v=9Os0o3wzS_I"
                
            },
            "tuesday": {
                "topic": "loops",
                "code": "for i in range(5):\n    print(i)\nwhile i < 5:\n    print(i)\n    i += 1",
                "youtube": "https://www.youtube.com/watch?v=6iF8Xb7Z3wQ"
                
            },
            "wednesday": {
                "topic": "data structures",
                "code": "my_list = [1, 2, 3] \nmy_dict = {'a': 1, 'b': 2} \nmy_set = {1, 2, 3}",
               "youtube": "https://www.youtube.com/watch?v=R-HLU9Fl5ug"
            },
            "thursday": {
                "topic": "oop",
                "code": "class MyClass:\n    def __init__(self, name):\n        self.name = name\n    def greet(self):\n        return f\"Hello, {self.name}\" \nobj = MyClass(\"World\")\nprint(obj.greet())",
                "youtube": "https://www.youtube.com/watch?v=JeznW_7DlB0"
            },
            "friday": {
                "topic": "Modules and Packages",
                "code": "import math\nprint(math.pi)\nfrom datetime import datetime\nprint(datetime.now())",
                 "youtube": "https://www.youtube.com/watch?v=CqvZ3vGoGs0"
            },
            "saturday": {
                "topic": "File Handling",
                "code": "with open('file.txt', 'r') as file:\n    content = file.read()\nprint(content)\nwith open('file.txt', 'w') as file:\n    file.write('Hello, World!')",
                 "youtube": "https://www.youtube.com/watch?v=Uh2ebFW8OYM"
            },
            "sunday": {
                "topic": "Error Handling",
                "code": "try:\n    x = 1 / 0\nexcept ZeroDivisionError:\n    print(\"Cannot divide by zero\")\nfinally:\n    print(\"Execution completed\")",
                "youtube": "https://www.youtube.com/watch?v=NIWwJbo-9_8"
            },
            "default": {
                "topic": "operators",
                "code": "a = 10\nb = 20\nprint(a + b)\nprint(a - b)\nprint(a * b)\nprint(a / b)",
                "youtube": "https://www.youtube.com/watch?v=0oThl1_7uSo",
            
        },
            "error handling": {
                "topic": "error handling",
                "code": "try:\n    x = 1 / 0\nexcept ZeroDivisionError:\n    print(\"Cannot divide by zero\")\nfinally:\n    print(\"Execution completed\")",
                "youtube": "https://www.youtube.com/watch?v=NIWwJbo-9_8"
            },
            
        }
        
        
        # Quiz data for each topic
        self.quizzes = {
    "Functions": [
        {
            "question": "What keyword is used to define a function in Python?",
            "options": ["func", "def", "define", "function"],
            "answer": "def"
        },
        {
            "question": "Which symbol is used to define a function’s parameter?",
            "options": ["{}", "[]", "()", "<>"],
            "answer": "()"
        },
        {
            "question": "What does a function return by default if no return statement is used?",
            "options": ["0", "None", "Empty string", "False"],
            "answer": "None"
        }
    ],
    "Loops": [
        {
            "question": "Which loop is used for iterating a known number of times?",
            "options": ["while", "for", "loop", "repeat"],
            "answer": "for"
        },
        {
            "question": "What does the `break` keyword do in a loop?",
            "options": ["Skips to next iteration", "Ends the loop", "Restarts the loop", "None"],
            "answer": "Ends the loop"
        }
    ],
    "Error Handling": [
        {
            "question": "What keyword is used to handle exceptions in Python?",
            "options": ["try", "catch", "handle", "except"],
            "answer": "try"
        },
        {
            "question": "Which block must always come after `try`?",
            "options": ["finally", "else", "except", "end"],
            "answer": "except"
        }
    ],
    "data structures": [
        {
            "question": "Which data structure is mutable?",
            "options": ["Tuple", "String", "List", "Set"],
            "answer": "List"
        },
        {
            "question": "What is the output of `len([1, 2, 3])`?",
            "options": ["3", "2", "1", "0"],
            "answer": "3"
        }
    ],
    "oop": [
        {
            "question": "What does OOP stand for?",
            "options": ["Object Oriented Programming", "Object Oriented Process", "Object Oriented Protocol", "None"],
            "answer": "Object Oriented Programming"
        },
        {
            "question": "Which keyword is used to create a class in Python?",
            "options": ["class", "def", "object", "new"],
            "answer": "class"
        }
    ],
}


    def get_quiz(self, quiz):
        return self.quizzes.get(quiz, None)
    
    def check_answer(self, topic, user_answer):
        quiz = self.get_quiz(topic)
        if quiz:
            return quiz["answer"].lower() == user_answer.lower()
        return False
   
    def get_today_topic(self):
        import datetime
        today = datetime.datetime.today().strftime('%A').lower()
        return self.topics.get(today, None)

    def get_topic_info(self, topic_name):
        for day_info in self.topics.values():
            if day_info["topic"].lower() == topic_name.lower():
                return day_info
        return None

    def search_topic(self, query):
        """Search for a topic by its name."""
        query = query.lower().strip()
        for day, day_info in self.topics.items():
            if query in day_info["topic"].lower():
                return day_info
        return None
    
    
