#!/bin/bash
# Ren'Py Web 自动打包并部署到GitHub Pages
# 作者：Luna
# 用途：自动化构建并部署《漩涡与萤火》到网页版本

set -e  # 遇到错误立即退出

echo "=========================================="
echo "《漩涡与萤火》Web版本自动部署脚本"
echo "=========================================="
echo ""

# 颜色定义
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# 配置变量
PROJECT_NAME="vortex_and_firefly"
GITHUB_REPO="https://github.com/Ritori2022/Visual-Novel.git"
VERSION="1.0"

# 检测Ren'Py SDK
echo -e "${YELLOW}步骤 1/5: 检测Ren'Py SDK...${NC}"

# 尝试多个可能的Ren'Py位置
RENPY_PATHS=(
    "./renpy-8.2.1-sdk/renpy.sh"
    "../renpy-8.2.1-sdk/renpy.sh"
    "./renpy.sh"
    "/opt/renpy/renpy.sh"
    "$HOME/renpy/renpy.sh"
)

RENPY_FOUND=false
for path in "${RENPY_PATHS[@]}"; do
    if [ -f "$path" ]; then
        RENPY_SH="$path"
        RENPY_FOUND=true
        echo -e "${GREEN}✓ 找到Ren'Py SDK: $path${NC}"
        break
    fi
done

if [ "$RENPY_FOUND" = false ]; then
    echo -e "${RED}✗ 错误: 未找到Ren'Py SDK${NC}"
    echo ""
    echo "请确保Ren'Py SDK在以下位置之一："
    echo "  1. 当前目录下的 renpy-8.2.1-sdk/"
    echo "  2. 上级目录的 renpy-8.2.1-sdk/"
    echo "  3. /opt/renpy/"
    echo "  4. $HOME/renpy/"
    echo ""
    echo "下载Ren'Py SDK: https://www.renpy.org/latest.html"
    exit 1
fi

# 检查项目是否存在
echo ""
echo -e "${YELLOW}步骤 2/5: 检查项目文件...${NC}"

if [ ! -d "$PROJECT_NAME" ]; then
    echo -e "${RED}✗ 错误: 找不到项目目录 '$PROJECT_NAME'${NC}"
    echo "请确保此脚本在 Visual-Novel 仓库根目录运行"
    exit 1
fi

echo -e "${GREEN}✓ 项目目录存在${NC}"

# 构建Web版本
echo ""
echo -e "${YELLOW}步骤 3/5: 构建Web版本...${NC}"
echo "这可能需要5-15分钟，请耐心等待..."

# 使用Ren'Py命令行构建web版本
"$RENPY_SH" launcher distribute "$PROJECT_NAME" --package web

# 检查构建是否成功
WEB_BUILD="${PROJECT_NAME}-${VERSION}-web.zip"
if [ ! -f "$WEB_BUILD" ]; then
    echo -e "${RED}✗ 构建失败: 找不到 $WEB_BUILD${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Web版本构建成功!${NC}"

# 解压Web版本
echo ""
echo -e "${YELLOW}步骤 4/5: 解压Web版本...${NC}"

# 清理旧的部署目录
rm -rf web_deploy
mkdir -p web_deploy

# 解压
unzip -q "$WEB_BUILD" -d web_deploy

# 找到解压后的实际目录名
WEB_DIR=$(find web_deploy -maxdepth 1 -type d -name "${PROJECT_NAME}*" | head -1)

if [ -z "$WEB_DIR" ]; then
    echo -e "${RED}✗ 错误: 找不到解压后的目录${NC}"
    exit 1
fi

echo -e "${GREEN}✓ 解压成功: $WEB_DIR${NC}"

# 部署到GitHub Pages
echo ""
echo -e "${YELLOW}步骤 5/5: 部署到GitHub Pages...${NC}"

cd "$WEB_DIR"

# 初始化git仓库
git init
git checkout -b gh-pages

# 添加所有文件
git add .

# 提交
COMMIT_MSG="Deploy web build $(date +'%Y-%m-%d %H:%M:%S')"
git commit -m "$COMMIT_MSG"

# 推送到GitHub Pages
echo ""
echo -e "${YELLOW}正在推送到GitHub Pages...${NC}"

# 添加远程仓库（如果已存在会失败，但不影响）
git remote add origin "$GITHUB_REPO" 2>/dev/null || true

# 强制推送到gh-pages分支
git push -f origin gh-pages

echo ""
echo -e "${GREEN}=========================================="
echo "✓ 部署完成!"
echo "==========================================${NC}"
echo ""
echo "你的游戏将在5-10分钟后可访问："
echo -e "${GREEN}https://ritori2022.github.io/Visual-Novel/${NC}"
echo ""
echo "提示："
echo "  - 如果无法访问，请到GitHub仓库设置中启用GitHub Pages"
echo "  - Settings → Pages → Source: gh-pages 分支"
echo ""

# 返回原目录
cd - > /dev/null

# 清理临时文件（可选）
read -p "是否删除临时文件? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    rm -rf web_deploy
    rm -f "$WEB_BUILD"
    echo -e "${GREEN}✓ 临时文件已清理${NC}"
fi

echo ""
echo "脚本执行完毕！"
