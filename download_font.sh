#!/bin/bash
# 中文字体下载脚本

echo "正在下载思源黑体（Noto Sans SC）..."

# 创建临时目录
TMP_DIR=$(mktemp -d)
cd "$TMP_DIR"

# 方法1：从Google Fonts下载
echo "尝试从Google Fonts下载..."
wget "https://fonts.google.com/download?family=Noto%20Sans%20SC" -O noto-sans-sc.zip 2>/dev/null

if [ -f "noto-sans-sc.zip" ] && [ -s "noto-sans-sc.zip" ]; then
    unzip -q noto-sans-sc.zip
    FONT_FILE=$(find . -name "*Regular*.ttf" -o -name "*Regular*.otf" | head -1)
    if [ -n "$FONT_FILE" ]; then
        echo "下载成功！"
        cp "$FONT_FILE" "$OLDPWD/vortex_and_firefly/game/fonts/NotoSansSC-Regular.otf"
        cd "$OLDPWD"
        rm -rf "$TMP_DIR"
        echo "字体已安装到 vortex_and_firefly/game/fonts/"
        exit 0
    fi
fi

# 方法2：从GitHub Release下载
echo "尝试从GitHub Release下载..."
cd "$TMP_DIR"
wget "https://github.com/notofonts/noto-cjk/releases/latest/download/Sans.zip" -O sans.zip 2>/dev/null

if [ -f "sans.zip" ] && [ -s "sans.zip" ]; then
    unzip -q sans.zip "SubsetOTF/SC/*Regular.otf"
    FONT_FILE=$(find . -name "*Regular.otf" | head -1)
    if [ -n "$FONT_FILE" ]; then
        echo "下载成功！"
        cp "$FONT_FILE" "$OLDPWD/vortex_and_firefly/game/fonts/NotoSansSC-Regular.otf"
        cd "$OLDPWD"
        rm -rf "$TMP_DIR"
        echo "字体已安装到 vortex_and_firefly/game/fonts/"
        exit 0
    fi
fi

# 清理
cd "$OLDPWD"
rm -rf "$TMP_DIR"

echo "自动下载失败。请手动下载："
echo "1. 访问 https://fonts.google.com/noto/specimen/Noto+Sans+SC"
echo "2. 点击 'Get font' -> 'Download' "
echo "3. 解压后将 NotoSansSC-Regular.ttf 复制到 vortex_and_firefly/game/fonts/"
