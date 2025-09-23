# 代码生成时间: 2025-09-23 18:56:38
# hash_calculator.py
# A simple hash calculator tool using the Quart framework.

from quart import Quart, request, jsonify
from hashlib import md5, sha1, sha256, sha512
from typing import Any

app = Quart(__name__)

# Define available hash functions
HASH_FUNCTIONS = {
    "md5": md5,
    "sha1": sha1,
    "sha256": sha256,
    "sha512": sha512
}

@app.route("/hash", methods=["POST"])
async def calculate_hash():
    """
    Calculate the hash of the given input.
    
    Request body should contain:
    - input: the string to be hashed
    - algorithm: the hash algorithm to use (md5, sha1, sha256, sha512)
    
    Response:
    - hash: the calculated hash value
    """
    data = await request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    
    input_string = data.get("input")
    algorithm = data.get("algorithm\)
    
    if not input_string:
        return jsonify({"error": "Input string is required"}), 400
    if algorithm not in HASH_FUNCTIONS:
        return jsonify({"error": f"Unsupported algorithm: {algorithm}"}), 400
    
    hash_function = HASH_FUNCTIONS[algorithm]
    hash_value = hash_function(input_string.encode()).hexdigest()
    
    return jsonify({"hash": hash_value})

if __name__ == '__main__':
    app.run(debug=True)