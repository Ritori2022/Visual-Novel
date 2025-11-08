# Ren'Py Web 导出指南

## 📦 将视觉小说打包为网页版本（像你的示例）

这份指南将帮助你把《漩涡与萤火》打包成可以在浏览器中运行的网页版本，并部署到GitHub Pages。

---

## 前提条件

1. **下载Ren'Py SDK**
   - 访问：https://www.renpy.org/latest.html
   - 下载适合你操作系统的版本（Windows/Mac/Linux）
   - 解压到你选择的目录

2. **将项目放入Ren'Py**
   - 将`vortex_and_firefly`文件夹复制到Ren'Py SDK的目录下
   - 或在Ren'Py Launcher中设置"Projects Directory"指向项目父目录

---

## 方法一：使用Ren'Py Launcher（推荐）

### 步骤 1：打开项目

1. 启动`renpy.exe`（Windows）或`renpy.sh`（Linux/Mac）
2. 在项目列表中选择"vortex_and_firefly"
3. 确保项目可以正常运行（点击"Launch Project"测试）

### 步骤 2：构建Web版本

1. 点击"Build Distributions"
2. 在平台列表中勾选：
   - ☑️ **Web**
3. 点击"Build"按钮
4. 等待构建完成（可能需要5-15分钟）

### 步骤 3：找到输出文件

构建完成后，Web版本位于：
```
vortex_and_firefly-1.0-web.zip
```

解压这个ZIP文件，你会得到类似这样的结构：
```
vortex_and_firefly-1.0-web/
├── index.html          # 主页面
├── game.js             # 游戏逻辑
├── lib.js              # Ren'Py运行时
├── (其他资源文件)
```

---

## 方法二：使用命令行

### Windows:

```batch
renpy.exe launcher distribute web vortex_and_firefly
```

### Linux/Mac:

```bash
./renpy.sh launcher distribute web vortex_and_firefly
```

---

## 部署到GitHub Pages

### 步骤 1：创建GitHub仓库（如果还没有）

```bash
cd vortex_and_firefly-1.0-web
git init
git add .
git commit -m "Add web build"
```

### 步骤 2：创建GitHub Pages分支

```bash
# 创建orphan分支（无历史记录的新分支）
git checkout --orphan gh-pages

# 添加所有文件
git add .
git commit -m "Deploy web build to GitHub Pages"

# 推送到GitHub
git remote add origin https://github.com/Ritori2022/Visual-Novel.git
git push -u origin gh-pages
```

### 步骤 3：启用GitHub Pages

1. 进入GitHub仓库设置（Settings）
2. 找到"Pages"部分
3. Source选择：`gh-pages` 分支
4. 保存

5-10分钟后，你的游戏将在以下地址可访问：
```
https://ritori2022.github.io/Visual-Novel/
```

---

## 简化部署流程（推荐）

### 创建部署脚本

**deploy.sh**（Linux/Mac）:
```bash
#!/bin/bash

# 构建Web版本
./renpy.sh launcher distribute web vortex_and_firefly

# 解压到临时目录
rm -rf web_deploy
mkdir web_deploy
unzip -q vortex_and_firefly-1.0-web.zip -d web_deploy

# 部署到gh-pages分支
cd web_deploy/vortex_and_firefly-1.0-web
git init
git checkout -b gh-pages
git add .
git commit -m "Deploy $(date)"
git remote add origin https://github.com/Ritori2022/Visual-Novel.git
git push -f origin gh-pages

echo "部署完成！"
echo "访问：https://ritori2022.github.io/Visual-Novel/"
```

**deploy.bat**（Windows）:
```batch
@echo off
REM 构建Web版本
renpy.exe launcher distribute web vortex_and_firefly

REM 解压并部署（需要Git和7zip）
rmdir /s /q web_deploy
mkdir web_deploy
7z x vortex_and_firefly-1.0-web.zip -oweb_deploy

cd web_deploy\vortex_and_firefly-1.0-web
git init
git checkout -b gh-pages
git add .
git commit -m "Deploy %date%"
git remote add origin https://github.com/Ritori2022/Visual-Novel.git
git push -f origin gh-pages

echo 部署完成！
echo 访问：https://ritori2022.github.io/Visual-Novel/
```

---

## 优化Web版本

### 1. 压缩图片

Web版本需要下载所有资源，建议优化图片大小：

```bash
# 使用ImageMagick压缩PNG
find game/images -name "*.png" -exec convert {} -quality 85 {} \;

# 使用pngquant进一步压缩
find game/images -name "*.png" -exec pngquant --force --ext .png {} \;
```

### 2. 压缩音频

```bash
# 转换为更小的OGG格式
find game/audio -name "*.wav" -exec ffmpeg -i {} -c:a libvorbis -q:a 5 {}.ogg \;
```

### 3. 启用渐进加载

在`options.rpy`中添加：

```renpy
## Web构建选项
define config.web_loading_screen = True
define config.web_progressive_downloads = True
```

---

## 常见问题

### Q: Web版本打包失败

**A:** 检查以下几点：
- Ren'Py SDK是否是最新版本（8.2.1+）
- 项目路径是否包含非ASCII字符
- 是否有足够的磁盘空间（至少500MB）

### Q: GitHub Pages显示404

**A:** 确保：
- 推送到了正确的`gh-pages`分支
- GitHub Pages设置中选择了该分支
- 等待5-10分钟让GitHub处理

### Q: 游戏加载很慢

**A:** 优化资源：
- 压缩图片（见上文）
- 减少未使用的资源
- 启用渐进加载（见上文）

### Q: 音频无法播放

**A:** Web版本只支持OGG和OPUS格式：
- 将所有音频转换为OGG
- 检查浏览器控制台错误信息

### Q: 字体显示不正确

**A:** 确保字体文件包含在构建中：
```renpy
# options.rpy
define gui.text_font = "fonts/SourceHanSansCN-Regular.otf"
```

---

## 高级：自定义HTML模板

如果想自定义网页样式，编辑：

```
vortex_and_firefly/web-presplash/
├── index.html         # 主HTML模板
├── style.css          # 自定义CSS
└── background.jpg     # 加载背景图
```

---

## 性能优化建议

### 资源大小限制

| 资源类型 | 推荐大小 | 最大大小 |
|---------|---------|---------|
| 背景图 | < 500KB | < 1MB |
| 角色立绘 | < 300KB | < 500KB |
| BGM | < 3MB | < 5MB |
| 音效 | < 100KB | < 200KB |
| 总体游戏大小 | < 50MB | < 100MB |

### 加载优化

```renpy
## options.rpy

# 预加载关键资源
define config.preload_fonts = True

# 延迟加载音频
define config.automatic_images_strip = True

# 启用Web缓存
define config.web_cache_version = 1
```

---

## 示例：完整工作流程

```bash
# 1. 测试项目
./renpy.sh vortex_and_firefly

# 2. 构建Web版本
./renpy.sh launcher distribute web vortex_and_firefly

# 3. 部署到GitHub Pages
./deploy.sh

# 4. 访问游戏
open https://ritori2022.github.io/Visual-Novel/
```

---

## 参考资源

- **Ren'Py官方文档**：https://www.renpy.org/doc/html/build.html#web
- **GitHub Pages文档**：https://docs.github.com/en/pages
- **Web优化指南**：https://lemmasoft.renai.us/forums/viewtopic.php?t=60888

---

*最后更新：2025-11-08*
*作者：Luna*

喵～希望这份指南对你有帮助！如果遇到问题随时问Luna！✨
