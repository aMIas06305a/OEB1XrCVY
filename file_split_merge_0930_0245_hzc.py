# 代码生成时间: 2025-09-30 02:45:23
# file_split_merge.py
# This Python script provides a file split and merge tool using the Quart framework.

from quart import Quart, request, jsonify
import os
import shutil

app = Quart(__name__)
# 改进用户体验

# Define the maximum file size for splitting
# TODO: 优化性能
MAX_SPLIT_SIZE = 1024 * 1024 * 100  # 100 MB

# Split a file into smaller parts
# 添加错误处理
def split_file(file_path, part_size=MAX_SPLIT_SIZE):
    with open(file_path, 'rb') as file:
        file_size = os.path.getsize(file_path)
        part_number = 0
        while file_size > 0:
            part_number += 1
# 增强安全性
            bytes_read = file.read(part_size)
            part_file_path = f"{os.path.splitext(file_path)[0]}_part{part_number}"
# 扩展功能模块
            with open(part_file_path, 'wb') as part_file:
                part_file.write(bytes_read)
            file_size -= len(bytes_read)
    return part_number

# Merge split files back into a single file
def merge_files(base_file_name, output_file_name):
# TODO: 优化性能
    with open(output_file_name, 'wb') as output_file:
        for part_number in range(1, split_file(base_file_name) + 1):
            part_file_path = f"{base_file_name}_part{part_number}"
            with open(part_file_path, 'rb') as part_file:
                shutil.copyfileobj(part_file, output_file)
        # Clean up the split files
        for part_number in range(1, split_file(base_file_name) + 1):
            os.remove(f"{base_file_name}_part{part_number}")

# Route for file upload and splitting
# 增强安全性
@app.route('/upload', methods=['POST'])
async def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    file.save(f'{file.filename}')
# 优化算法效率
    parts = split_file(file.filename)
# NOTE: 重要实现细节
    return jsonify({'message': f'File split into {parts} parts', 'filename': file.filename})

# Route for file merge
@app.route('/merge', methods=['POST'])
async def merge_files_route():
    file_name = request.form.get('filename')
    output_file = request.form.get('output_file')
    if not file_name or not output_file:
        return jsonify({'error': 'Missing filename or output_file parameter'})
    try:
        merge_files(file_name, output_file)
        return jsonify({'message': f'File merged into {output_file}', 'filename': output_file})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)