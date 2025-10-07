# 代码生成时间: 2025-10-08 00:00:49
import asyncio
import aiohttp
from quart import Quart, jsonify, request
from urllib.parse import urlparse

# 创建Quart应用
app = Quart(__name__)


# 异步网络连接状态检查函数
async def check_connection(url):
    """检查网络连接状态"""
    try:
        # 解析URL
        parsed_url = urlparse(url)
        protocol = parsed_url.scheme
        hostname = parsed_url.hostname
        
        # 检查协议是否为http或https
        if protocol not in ["http", "https"]:
            raise ValueError("URL must be http or https protocol")
        
        # 使用aiohttp进行网络连接测试
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                # 如果响应状态码为200，表示连接成功
                if response.status == 200:
                    return {"status": "success", "message": "Connection established"}
                else:
                    return {"status": "error", "message": f"Connection failed with status code {response.status}"}
    except aiohttp.ClientError as e:
        # 处理aiohttp异常
        return {"status": "error", "message": str(e)}
    except ValueError as e:
        # 处理协议错误
        return {"status": "error", "message": str(e)}
    except Exception as e:
        # 处理其他异常
        return {"status": "error", "message": str(e)}


# Quart路由处理器
@app.route("/check", methods=["GET"])
async def check_connection_route():
    """检查网络连接状态的路由处理器"""
    # 从请求中获取URL参数
    url = request.args.get("url")
    if not url:
        return jsonify({"status": "error", "message": "URL parameter is required"}), 400
    
    # 调用异步函数检查连接
    connection_status = await check_connection(url)
    
    # 返回JSON响应
    return jsonify(connection_status)


# 程序入口点
if __name__ == "__main__":
    app.run(debug=True)