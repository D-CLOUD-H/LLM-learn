import os
from dotenv import load_dotenv, find_dotenv
from zhipuai import ZhipuAI

def get_zhipuai_key():
    """安全读取 .env 文件中的智谱 API Key"""
    # 1. 查找 .env 路径
    dotenv_path = find_dotenv()
    if not dotenv_path:
        print("⚠️ 警告: 未找到 .env 文件，请确保在项目根目录下已创建。")
        return None
        
    # 2. 加载环境变量（override=True 确保覆盖已存在的同名变量）
    load_dotenv(dotenv_path, override=True)
    
    # 3. 安全获取 Key（使用 getenv 避免 KeyError 崩溃）
    api_key = os.getenv("ZHIPUAI_API_KEY")
    if not api_key or api_key.strip() == "":
        print("❌ 错误: 环境变量 ZHIPUAI_API_KEY 未找到或为空。")
        return None
        
    return api_key