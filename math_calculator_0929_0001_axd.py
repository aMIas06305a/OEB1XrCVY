# 代码生成时间: 2025-09-29 00:01:13
import quart

from quart import jsonify

app = quart.Quart(__name__)

# 异常处理类
class MathError(Exception):
    pass

# 计算器工具集
class Calculator:
    def add(self, a, b):
        """Add two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The sum of a and b.
        """
        return a + b

    def subtract(self, a, b):
        """Subtract two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The difference of a and b.
        """
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The product of a and b.
        """
        return a * b

    def divide(self, a, b):
        """Divide two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The quotient of a and b.

        Raises:
            MathError: If b is zero.
        """
        if b == 0:
            raise MathError("Cannot divide by zero.")
        return a / b

# 实例化计算器
calculator = Calculator()

@app.route('/add/<float:a>/<float:b>', methods=['GET'])
async def add(a, b):
    try:
        result = calculator.add(a, b)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/subtract/<float:a>/<float:b>', methods=['GET'])
async def subtract(a, b):
    try:
        result = calculator.subtract(a, b)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/multiply/<float:a>/<float:b>', methods=['GET'])
async def multiply(a, b):
    try:
        result = calculator.multiply(a, b)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/divide/<float:a>/<float:b>', methods=['GET'])
async def divide(a, b):
    try:
        result = calculator.divide(a, b)
        return jsonify({'result': result})
    except MathError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)