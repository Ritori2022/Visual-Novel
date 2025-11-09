# 中文字体文件放置位置

此目录用于存放中文字体文件，以支持游戏中的中文显示。

## 推荐字体：Noto Sans SC（思源黑体简体中文）

### 下载方式1：直接下载
访问以下链接下载字体文件：
https://github.com/googlefonts/noto-cjk/raw/main/Sans/OTF/SimplifiedChinese/NotoSansSC-Regular.otf

### 下载方式2：从 Google Fonts 下载
1. 访问 https://fonts.google.com/noto/specimen/Noto+Sans+SC
2. 点击 "Download family" 下载字体包
3. 解压后将 NotoSansSC-Regular.otf 复制到此目录

### 下载方式3：使用命令行（Linux/Mac）
```bash
cd vortex_and_firefly/game/fonts/
wget https://github.com/googlefonts/noto-cjk/raw/main/Sans/OTF/SimplifiedChinese/NotoSansSC-Regular.otf
```

### 下载方式4：使用命令行（Windows PowerShell）
```powershell
cd vortex_and_firefly\game\fonts\
Invoke-WebRequest -Uri "https://github.com/googlefonts/noto-cjk/raw/main/Sans/OTF/SimplifiedChinese/NotoSansSC-Regular.otf" -OutFile "NotoSansSC-Regular.otf"
```

## 安装后的文件结构
```
vortex_and_firefly/
  game/
    fonts/
      NotoSansSC-Regular.otf  ← 字体文件应该在这里
      README.txt              ← 本文件
```

## 注意事项
1. 字体文件大约 10MB，下载需要一些时间
2. 如果不安装中文字体，游戏仍可运行，但中文字符会显示为方块
3. 字体文件已被添加到 .gitignore，不会被提交到版本控制
4. 许可证：Noto Sans SC 使用 SIL Open Font License，可免费用于商业和非商业用途

## 验证安装
启动游戏后：
- 如果看到 "警告：未找到中文字体"，说明字体文件未正确放置
- 如果中文正常显示，说明安装成功
