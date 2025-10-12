# 代码生成时间: 2025-10-13 02:50:28
import quart
from quart import jsonify
import cv2
import numpy as np
import os

# 定义视频编解码器服务
class VideoEncoderService:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def encode_video(self, video_name):
        """
        编码视频文件
        :param video_name: 视频文件名
        :return: 编码后的视频文件路径
        """
        try:
            # 读取视频文件
            video_path = os.path.join(self.input_path, video_name)
            if not os.path.exists(video_path):
                return f"Video file {video_name} not found."

            # 读取视频帧
            cap = cv2.VideoCapture(video_path)
            frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            fps = cap.get(cv2.CAP_PROP_FPS)
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

            # 创建编码器
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out_path = os.path.join(self.output_path, f"{video_name}.mp4")
            out = cv2.VideoWriter(out_path, fourcc, fps, (width, height))

            # 编码视频帧
            success, frame = cap.read()
            while success:
                out.write(frame)
                success, frame = cap.read()

            # 释放资源
            cap.release()
            out.release()

            return f"Encoded video saved to {out_path}"
        except Exception as e:
            return f"Error encoding video: {str(e)}"

    def decode_video(self, video_name):
        """
        解码视频文件
        :param video_name: 视频文件名
        :return: 解码后的视频帧列表
        """
        try:
            # 读取视频文件
            video_path = os.path.join(self.output_path, video_name)
            if not os.path.exists(video_path):
                return f"Video file {video_name} not found."

            # 读取视频帧
            cap = cv2.VideoCapture(video_path)
            frames = []
            while True:
                success, frame = cap.read()
                if not success:
                    break
                frames.append(frame)

            # 释放资源
            cap.release()

            return frames
        except Exception as e:
            return f"Error decoding video: {str(e)}"

# 创建Quart应用
app = quart.Quart(__name__)

# 创建视频编解码器服务实例
video_encoder_service = VideoEncoderService(
    input_path='./input_videos',
    output_path='./output_videos'
)

# 定义编解码视频的路由
@app.route('/encode_video/<string:video_name>', methods=['POST'])
async def encode_video(video_name):
    response = video_encoder_service.encode_video(video_name)
    return jsonify({'message': response})

@app.route('/decode_video/<string:video_name>', methods=['POST'])
async def decode_video(video_name):
    response = video_encoder_service.decode_video(video_name)
    return jsonify({'message': response})

# 运行Quart应用
if __name__ == '__main__':
    app.run(debug=True)