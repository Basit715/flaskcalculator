from flask import Flask, request, render_template, jsonify
import json
app = Flask(__name__)

@app.route('/')
def welcome():
     return "Welcome to new flask app"

@app.route('/cal', methods = ["GET"])
def math_operator():
     operation = request.json["operation"]      # requesting from postman in the form of json
     number1 = request.json["number1"]
     number2 = request.json["number2"]
     
     if operation == "add":
          result = int(number1) + int(number2)
     elif operation == "minus":
          result = int(number1) - int(number2)
     elif operation == "multiply":
          result = int(number1)*int(number2)
     elif operation == "division":
          result = int(number1)/int(number2)
     elif operation == "floor":
          result = int(number1)//int(number2)
     elif operation == "raised":
          result = int(number1)**int(number2)
     elif operation == "mod":
          result = int(number1)%int(number2)
     else:
          print("operation not found")
     
     return jsonify(result)
      



if __name__ == "__main__":
     app.run(debug=True)