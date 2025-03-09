from fuzzywuzzy import process

# Predefined responses
responses = {
    "projects": "I have worked on multiple projects, including a logistics management system, an AI chatbot resume, and a tour and travel website.",
    "tech stack": "I have experience with Python, Flask, JavaScript, React, Node.js, and databases like MySQL and MongoDB.",
    "skills": "My core skills include software development, web development, backend programming, and AI integration.",
    "why software engineering": "I am passionate about solving real-world problems with technology. Software engineering allows me to create innovative solutions."
}

# Function to get best-matching response
def get_response(user_input):
    user_input = user_input.lower()
    best_match, confidence = process.extractOne(user_input, responses.keys())

    if confidence > 60:  # If confidence is above 60%
        return responses[best_match]
    else:
        return "I'm still learning! Can you ask me something else?"
