# Desenvolvimento em aplicações webs - Micro Framework Flask
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return "Main page."

# @app.route("/hello/")
# @app.route("/hello/<name>")
# def hello(name="World"):
#     return "Hello " + name + "!"

# if __name__ == "__main__":
#     app.run()

# Exercício 01
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def index():
#     welcome = "<h1>Hello programers</h1>"
#     link = "<p><a href=user/programer>Click here</a></p>"
#     return welcome + link

# @app.route("/user/") 
# @app.route("/user/<name>")
# def user(name="programer"):
#     welcome = f"<h1>hello, {name}</h1>"
#     instruction = "<p>Change the name in <em>browser address</em> and reload the page!</p>"
#     return welcome + instruction

# if __name__ == "__main__":
#     app.run(debug=True)

# Exercício 02
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    title = "<h1>Hello, World!</h1>"
    instruction = "<p>Enter with two numbers</p>"
    return title + instruction

@app.route("/sum/")    
@app.route("/sum/<num1>/<num2>")
def sum(num1=0,num2=0):
    sum = float(num1) + float(num2)
    result = f"<p>The result of the sum is {sum}</p>"
    return result

if __name__ == "__main__":
    app.run(debug=True)