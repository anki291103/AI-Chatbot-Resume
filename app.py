from flask import Flask, render_template, request, jsonify, send_from_directory
from fuzzywuzzy import process
import datetime

app = Flask(__name__)

# Knowledge Base: AI Chatbot Resume Data
responses = {
    "name": "My name is Ankita Jha.",
    "Roll no.": "Roll No. is A082.",
    "college": "I am studying at NMIMS, Mumbai.",
"linkedin": '<a href="https://www.linkedin.com/in/ankita-jha" target="_blank">Ankita Jha</a>',
    "branch": "I am pursuing BTech in Information Technology.",
        "coursework": "Here are some of the key courses I have completed:\n- Data Structures and Algorithms\n- Database Management Systems\n- Operating Systems\n- Computer Networks\n- Artificial Intelligence\n- Web Development\n- Software Engineering",
    
    "cgpa": "My current CGPA is 3.85.",
    "SAP Id": "My SAP Id is 70012300115.",
    "education": "I am pursuing BTech IT at NMIMS, Mumbai (2023-2026), with a CGPA of 3.85.",
 "10th": "🏫 <b>Muljibhai Mehta International School</b> (2019)<br>📖 Board: CBSE<br>📍 Location: Maharashtra<br>📊 Percentage: 94.2%",
    
    "12th": "🏫 <b>MGM Junior College</b> (2021)<br>🎓 Board: Maharashtra HSC<br>📍 Location: Maharashtra<br>📊 Percentage: 90%",

    
    "skills": "💡 *Do you want to know about my* 'Technical Skills' *or* 'Soft Skills'?",
    
    "technical skills": """
🛠️ **Technical Skills**
- 💻 Programming: Java, Python, SQL, JavaScript
- ⚙️ Frameworks: Spring Boot, Node.js, AngularJS
- 🗄️ Databases: MySQL, Firebase, Oracle
- ☁️ Cloud: Google Firebase, Oracle Cloud
""",
    
    "soft skills": """
💡 **Soft Skills**
- 🤝 Teamwork
- 🎙️ Communication
- 🎯 Problem-Solving
- 🔥 Leadership
""",
    
    "projects": "Here are some of my projects:\n- LogiSphere: A logistics management system\n- Caravan Booking Website: A rental system for caravans\n- AI Chatbot Resume: An interactive chatbot for showcasing my resume\n- Crime Dashboard: A Power BI dashboard analyzing crime statistics\n- Reader-Writer Problem: A Java RMI-based system to optimize data access",
    
    "interests": "I am passionate about:\n- Software Development\n- Web Development\n- AI/ML\n- Data Analysis",
    
    "hobbies": "I enjoy:\n- Listening to music\n- Dancing",
    
    "email": "You can reach me at: ajha.binodjha@gmail.com",

    "Phone Number": "You can reach me at: 7058825161",

    "logistics project/logisphere": "LogiSphere is a logistics management system for tracking shipments, managing orders, and automating the supply chain. It is built with HTML, CSS, JavaScript, Node.js, PHP, and MySQL.",

    "caravan project": "The caravan booking website helps users book caravans for travel and events. It simplifies the booking process and improves user experience.",
    
    "reader-writer problem": "I implemented the Reader-Writer problem using Java RMI, reducing access conflicts in distributed systems by 20%.",
    
    "crime dashboard": "The Crime Against Women Dashboard is built in Power BI to analyze crime statistics and reduce data processing time by 30%.",

    "why software engineering": "I love solving real-world problems with technology. Software engineering lets me innovate and create impactful solutions.",
        "who is the best candidate for this job": "Ankita Jha, obviously! 😎",

"programming languages": """
💻 **Programming Languages:**  
- Python 🐍  
- Java ☕  
- JavaScript ⚡  
- C/C++ 🚀  
- SQL & R 📊  
""",
"fun fact": "I once built an entire project overnight just for fun! 🚀 Ask me about it!",

"favorite project": """
🌟 **Favorite Project: AI Chatbot Resume**  
- Built an interactive AI-powered resume chatbot
- Uses Flask + JavaScript for real-time responses  
- Deployed on "Render / AWS" for recruiters to access globally!  
""",
"who is your creator": "Ankita Jha, of course! 😎",
"tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs! 🐛😆",
"do you sleep?": "Nope! I'm an AI, always ready to chat. But you should get some rest! 😴",
"feedback": """
📝 I’d love to improve!
If you have any feedback on my AI resume, let me know! 😊  
""",
"thank you": "Glad I could help! So… when do I start working for you ? 🤩",

    # Resume Download Feature
    "download resume": 'You can download my resume from here: <a href="/download_resume" target="_blank">Download Resume 📄</a>',
}
# Function to get the best-matching response
def get_response(user_input):
    user_input = user_input.lower()
    
    # Get current hour for personalized greeting
    hour = datetime.datetime.now().hour
    greeting = "Good morning! ☀️" if hour < 12 else "Good afternoon! 🌞" if hour < 18 else "Good evening! 🌙"
    
    # Add greetings when user says hello or hi
    if user_input in ["hello", "hi", "hey", "hiii", "hii"]:
        return f"Hello! {greeting} How can I assist you today? 😊"
    
    # Check if question contains skill-related words
    skill_keywords = ["python", "machine learning", "data analysis", "web development"]
    matched_skills = [skill for skill in skill_keywords if skill in user_input]

    
    # Check if user wants to see skill visualization
    if "skill chart" in user_input or "visualize skills" in user_input:
        return "SHOW_SKILL_CHART"

  

    best_match, confidence = process.extractOne(user_input, responses.keys())

    if confidence > 70:  # If confidence is high
        return responses[best_match]
    else:
        return "I'm still learning! Can you ask me something else?"
  

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()
    response = get_response(user_message)
    return jsonify({"response": response})

# Resume Download Route
@app.route("/download_resume")
def download_resume():
    return send_from_directory("static", "Ankita_jha_Resume.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
