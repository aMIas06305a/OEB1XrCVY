# 代码生成时间: 2025-09-29 18:40:44
# 使用Quart框架和Python实现蒙特卡洛模拟器
# 该程序通过模拟大量随机事件来估计某些事件发生的概率

from quart import Quart, jsonify, request
import random
import math

app = Quart(__name__)

# 蒙特卡洛模拟函数，用于估计pi值
def monte_carlo_pi(iterations: int) -> float:
    """
    使用蒙特卡洛方法估计pi值
    :param iterations: 迭代次数
    :return: 估计的pi值
    """
    points_inside_circle = 0
    for _ in range(iterations):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            points_inside_circle += 1
    return 4 * points_inside_circle / iterations

# 路由处理函数，接受请求并返回pi的估计值
@app.route("/pi", methods=["GET"])
async def estimate_pi():
    """
    根据请求参数返回pi的估计值
    :return: JSON响应，包含pi的估计值
    """
    try:
        iterations = request.args.get("iterations", type=int, default=1000)
        if iterations <= 0:
            raise ValueError("Iterations must be positive")
        pi_estimate = monte_carlo_pi(iterations)
        return jsonify({"pi_estimate": pi_estimate})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# 启动服务器
if __name__ == '__main__':
    app.run()
