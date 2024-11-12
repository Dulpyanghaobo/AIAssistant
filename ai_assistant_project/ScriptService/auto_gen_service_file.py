import os
import re

# Markdown文件路径
markdown_file_path = "ServiceScript/aiKun_service.markdown"

# 读取markdown文件
with open(markdown_file_path, "r") as file:
    lines = file.readlines()

# 获取生成文件的路径（Markdown文件的第一行）
base_path = lines[0].strip()
del lines[0]  # 删除第一行

# 解析markdown文件，并创建文件夹和文件
current_dirs = []
for line in lines:
    # 计算"│   "的数量以判断层级
    indent = line.count('│   ')
    line = line.strip()

    # 匹配文件夹名或文件名
    match = re.search(r'([a-zA-Z0-9_/.]+)', line)

    if match:
        path = match.group(1)

        # 如果该行是顶层目录
        if not line.startswith("│"):
            current_dirs = []

        # 调整当前路径列表长度以匹配当前层级
        else:
            current_dirs = current_dirs[:indent-1]

        # 添加当前目录或文件到当前路径
        current_dirs.append(path)

        # 将生成文件的路径和当前路径拼接起来
        full_path = os.path.join(base_path, *current_dirs)

        # 如果路径以'/'结尾，则创建文件夹
        if path.endswith('/'):
            os.makedirs(full_path, exist_ok=True)
        else:
            # 创建文件
            with open(full_path, 'w') as file:
                pass
