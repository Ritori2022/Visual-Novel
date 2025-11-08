# 🚀 《漩涡与萤火》Web版本部署指南

> 使用一键脚本将你的视觉小说部署到GitHub Pages

---

## 📋 前置条件

在开始之前，你需要：

1. ✅ **Ren'Py SDK 8.2.1+**
   - 下载地址：https://www.renpy.org/latest.html
   - 选择适合你系统的版本（Windows/Mac/Linux）

2. ✅ **Git**
   - Windows: https://git-scm.com/download/win
   - Mac: 通常已预装，或使用 `brew install git`
   - Linux: `sudo apt install git` 或 `sudo yum install git`

3. ✅ **GitHub账号**
   - 确保你有权限推送到仓库

---

## 🎯 快速开始

### Windows用户

1. **下载Ren'Py SDK**
   ```
   解压到：Visual-Novel\renpy-8.2.1-sdk\
   ```

2. **运行部署脚本**
   ```batch
   双击运行: deploy_web.bat
   ```

3. **等待完成**
   - 构建过程需要5-15分钟
   - 脚本会自动完成打包、解压、推送

4. **访问你的游戏**
   ```
   https://ritori2022.github.io/Visual-Novel/
   ```
   ⏰ 需要等待5-10分钟让GitHub Pages生效

---

### Mac/Linux用户

1. **下载Ren'Py SDK**
   ```bash
   # 解压到项目目录
   tar xjf renpy-8.2.1-sdk.tar.bz2
   ```

2. **给脚本执行权限**
   ```bash
   chmod +x deploy_web.sh
   ```

3. **运行部署脚本**
   ```bash
   ./deploy_web.sh
   ```

4. **访问你的游戏**
   ```
   https://ritori2022.github.io/Visual-Novel/
   ```
   ⏰ 需要等待5-10分钟让GitHub Pages生效

---

## 📁 推荐的目录结构

```
Visual-Novel/
├── renpy-8.2.1-sdk/          # Ren'Py SDK (你需要下载)
│   ├── renpy.sh              # Linux/Mac执行文件
│   ├── renpy.exe             # Windows执行文件
│   └── ...
├── vortex_and_firefly/       # 游戏项目
│   ├── game/
│   │   └── script.rpy
│   └── ...
├── deploy_web.sh             # Linux/Mac部署脚本
├── deploy_web.bat            # Windows部署脚本
└── DEPLOY_INSTRUCTIONS.md    # 本文件
```

---

## 🔧 故障排除

### ❌ 找不到Ren'Py SDK

**症状：**
```
错误: 未找到Ren'Py SDK
```

**解决方案：**

1. **检查SDK位置**
   - Windows: 应该在 `Visual-Novel\renpy-8.2.1-sdk\`
   - Mac/Linux: 应该在 `Visual-Novel/renpy-8.2.1-sdk/`

2. **手动指定路径**（高级）

   **Windows** - 编辑 `deploy_web.bat`，在第16行附近修改：
   ```batch
   set RENPY_EXE=C:\你的路径\renpy.exe
   ```

   **Linux/Mac** - 编辑 `deploy_web.sh`，在第24行附近添加：
   ```bash
   RENPY_SH="/你的路径/renpy.sh"
   RENPY_FOUND=true
   ```

---

### ❌ 构建失败

**症状：**
```
构建失败: 找不到 vortex_and_firefly-1.0-web.zip
```

**解决方案：**

1. **检查项目完整性**
   ```bash
   # 确保game/script.rpy存在
   ls vortex_and_firefly/game/script.rpy
   ```

2. **手动构建测试**
   ```bash
   # Linux/Mac
   ./renpy-8.2.1-sdk/renpy.sh launcher

   # Windows
   renpy-8.2.1-sdk\renpy.exe
   ```
   - 在图形界面中选择项目
   - 点击 "Build Distributions"
   - 勾选 "Web"
   - 点击 "Build"

3. **查看错误日志**
   - 构建失败时会显示详细错误
   - 检查是否缺少必需文件

---

### ❌ 推送到GitHub失败

**症状：**
```
Permission denied (publickey)
```

**解决方案：**

1. **配置Git凭据**
   ```bash
   git config --global user.name "你的用户名"
   git config --global user.email "你的邮箱"
   ```

2. **使用SSH密钥（推荐）**

   生成SSH密钥：
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```

   添加到GitHub：
   - 复制公钥：`cat ~/.ssh/id_ed25519.pub`
   - GitHub → Settings → SSH and GPG keys → New SSH key
   - 粘贴公钥

3. **使用HTTPS + Token（备选）**

   修改脚本中的仓库地址：
   ```bash
   # 从
   GITHUB_REPO="https://github.com/Ritori2022/Visual-Novel.git"

   # 改为（使用Personal Access Token）
   GITHUB_REPO="https://ghp_你的token@github.com/Ritori2022/Visual-Novel.git"
   ```

   生成Token：GitHub → Settings → Developer settings → Personal access tokens

---

### ❌ GitHub Pages显示404

**症状：**
访问 `https://ritori2022.github.io/Visual-Novel/` 显示404

**解决方案：**

1. **启用GitHub Pages**
   - 进入仓库 → Settings → Pages
   - Source: 选择 `gh-pages` 分支
   - 点击 Save

2. **等待部署完成**
   - 首次部署需要5-10分钟
   - 在Actions标签页查看部署状态

3. **检查分支**
   ```bash
   git ls-remote --heads origin
   ```
   - 应该看到 `refs/heads/gh-pages`

---

### ❌ 游戏加载很慢

**症状：**
游戏需要很长时间才能加载完成

**解决方案：**

1. **优化图片**
   ```bash
   # 使用ImageMagick压缩PNG
   find vortex_and_firefly/game/images -name "*.png" -exec convert {} -quality 85 {} \;
   ```

2. **压缩音频**
   ```bash
   # 转换为更小的OGG格式
   find vortex_and_firefly/game/audio -name "*.wav" -exec ffmpeg -i {} -c:a libvorbis -q:a 5 {}.ogg \;
   ```

3. **启用渐进加载**

   在 `vortex_and_firefly/game/options.rpy` 中添加：
   ```renpy
   define config.web_progressive_downloads = True
   ```

---

## 🎨 自定义配置

### 修改版本号

编辑脚本中的版本号：

**deploy_web.sh (第16行):**
```bash
VERSION="1.0"
```

**deploy_web.bat (第12行):**
```batch
set VERSION=1.0
```

版本号会影响输出文件名：`vortex_and_firefly-版本号-web.zip`

---

### 自定义加载页面

在项目中创建自定义预加载页面：

```
vortex_and_firefly/web-presplash/
├── index.html         # 自定义HTML
├── style.css          # 自定义样式
└── background.jpg     # 加载背景
```

---

## 📊 部署流程详解

脚本执行以下5个步骤：

### 1️⃣ 检测Ren'Py SDK
- 在多个常见位置搜索Ren'Py
- 找到后显示路径

### 2️⃣ 验证项目文件
- 检查 `vortex_and_firefly/` 目录是否存在
- 验证必需的game文件

### 3️⃣ 构建Web版本
- 调用 `renpy.sh launcher distribute`
- 生成 `.zip` 压缩包
- 时间：5-15分钟

### 4️⃣ 解压构建结果
- 创建 `web_deploy/` 临时目录
- 解压Web文件

### 5️⃣ 推送到GitHub Pages
- 初始化Git仓库
- 创建 `gh-pages` 分支
- 提交并强制推送

---

## 🔐 安全提示

1. **不要提交敏感信息**
   - 不要在脚本中硬编码密码或Token
   - 使用SSH密钥代替密码

2. **Token管理**
   - 如果使用Personal Access Token，设置最小权限
   - 定期轮换Token

3. **仓库权限**
   - 确保只有信任的人有推送权限
   - 使用Protected Branches保护主分支

---

## 📞 获取帮助

如果遇到问题：

1. **查看日志**
   - 脚本会显示详细的执行过程
   - 记录错误信息

2. **手动调试**
   ```bash
   # 测试Ren'Py是否工作
   ./renpy-8.2.1-sdk/renpy.sh --version

   # 测试Git连接
   git ls-remote https://github.com/Ritori2022/Visual-Novel.git
   ```

3. **参考文档**
   - Ren'Py官方文档：https://www.renpy.org/doc/html/
   - GitHub Pages文档：https://docs.github.com/en/pages

---

## 🎉 成功后的步骤

部署成功后，你可以：

1. **分享游戏链接**
   ```
   https://ritori2022.github.io/Visual-Novel/
   ```

2. **自定义域名**（可选）
   - 在GitHub Pages设置中添加自定义域名
   - 配置CNAME记录

3. **持续更新**
   - 修改游戏内容
   - 再次运行部署脚本即可更新

4. **监控访问量**
   - 使用Google Analytics
   - 在 `web-presplash/index.html` 中添加跟踪代码

---

## 📝 更新游戏

当你修改了游戏内容后：

```bash
# 1. 修改 vortex_and_firefly/game/script.rpy

# 2. 重新运行部署脚本
./deploy_web.sh  # 或 deploy_web.bat

# 3. 等待几分钟，刷新网页查看更新
```

---

## 🌟 最佳实践

1. **版本控制**
   - 每次部署前提交代码到主分支
   - 使用语义化版本号（如1.0, 1.1, 2.0）

2. **测试**
   - 本地测试：在Ren'Py中运行游戏
   - Web测试：部署后在多个浏览器测试

3. **备份**
   - 保留构建产物（.zip文件）
   - 定期备份源代码

4. **优化**
   - 压缩资源文件
   - 使用占位符测试，正式发布时替换高质量资源

---

*最后更新：2025-11-08*
*作者：Luna*

喵～祝你部署顺利！如果有问题随时问Luna！✨
