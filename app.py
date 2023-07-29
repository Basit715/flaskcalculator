from flask import Flask, request, render_template
app = Flask(__name__)



@app.route('/')
def welcome():
     return render_template('calculator.html')

@app.route('/',methods=['POST'])    
def math_operator():
     
     # operation = request.json["operation"]      # requesting from postman in the form of json
     # number1 = request.json["number1"]
     # number2 = request.json["number2"]  
     
          operation = request.form.get('operation') 
          n1 = request.form.get('number1', type=int, default=0)
          n2 = request.form.get('number2', type=int, default=0)   
          if operation == 'Addition':
               result = n1 + n2  
          elif operation == 'Subtraction':
               result = n1 - n2
          elif operation == 'Multiplication': 
               result = n1 * n2
          elif operation == 'Division': 
               result = n1/n2
          else:
              result = 10
               
          entry = result      
          return render_template('calculator.html', entry = entry)     
      
            




if __name__ == "__main__":
     app.run(debug=True)  