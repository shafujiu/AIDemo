#!/bin/bash

# 检查是否提供了目标目录参数
if [ $# -eq 0 ]; then
  echo "请提供目标目录作为参数"
  exit 1
fi

# 获取目标目录参数
target_directory="$1"

# 切换到目标目录
cd "$target_directory" || exit

# 查找并删除不含'-Src'的文件
find . -type f ! -name '*-Src*' -exec rm {} +

echo "已删除不含'-Src'的文件"
