from flask import Flask, request, render_template
import os
import math


app = Flask(__name__)


@app.route('/')
def root():
    return render_template('calc.html')

class Calculator:
    @app.route('/calcula', methods=["POST", "GET"])
    def calcula():
        val1 = int(request.form["valor1"])
        operacao = request.form["operacao"]
        result = 0
        if(operacao == '**'):
            result = val1 ** 2
        elif (operacao == "V"):
            result = math.pow(val1,1/2)
        elif(operacao == "log"):
            result = math.log(val1)
        else:
            result = 'Operacao Inválida'
        return str(result)


   
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port,debug = True)
