# 获取RenPyWeb模板文件指南

## 问题说明

Web打包已完成第一步，生成了 `game.zip`（5.6MB），但缺少RenPyWeb运行环境文件。

需要的文件结构：
```
web-dist/
├── game.zip          ✅ 已生成
├── index.html        ❌ 缺少
├── renpy.wasm        ❌ 缺少
├── renpy.js          ❌ 缺少
├── renpy.data        ❌ 缺少
├── web-icon.png      ❌ 缺少
├── web-presplash.jpg ❌ 缺少
└── [其他支持文件]     ❌ 缺少
```

---

## 解决方案

### 方法1: 从本地Ren'Py Launcher获取（推荐）

**步骤：**

1. **打开Ren'Py Launcher**
   - 运行本地的 Ren'Py SDK（如果没有，从 https://www.renpy.org/ 下载）

2. **下载Web支持**
   - 在Launcher主界面，点击 "Android / Web / iOS"
   - 选择 "Install Web Support" 或 "Web"
   - 点击下载按钮，等待下载完成（约10-20MB）

3. **定位web文件夹**
   ```
   # Windows:
   C:\renpy-8.4.1-sdk\web\

   # macOS/Linux:
   ~/renpy-8.4.1-sdk/web/
   ```

4. **压缩并上传**
   ```bash
   # 进入SDK目录
   cd renpy-8.4.1-sdk/

   # 压缩web文件夹
   zip -r web.zip web/

   # 或者使用tar
   tar -czf web.tar.gz web/
   ```

5. **上传到GitHub**
   - 将 `web.zip` 或 `web.tar.gz` 上传到 `renpy-sdk-split-files` 分支
   - 如果文件过大（>100MB），使用文件分割：
     ```bash
     split -b 20M web.zip web.zip.part
     ```

---

### 方法2: 复用之前的Tutorial打包结果

如果你之前成功打包过Tutorial项目的web版本：

1. **找到之前的web打包目录**
   ```
   # 可能的位置：
   ~/renpy-8.4.1-sdk/tutorial-8.4-web/
   ~/Desktop/tutorial-web/
   [你的自定义路径]/
   ```

2. **复制关键文件**
   需要的文件（除了game.zip）：
   - `index.html`
   - `renpy.wasm`
   - `renpy.js`
   - `renpy.data`
   - `renpy.js.symbols`（可选）
   - `renpy-sw.js`（Service Worker，可选）
   - `web-icon.png`
   - `web-presplash.jpg`
   - `progressive_download.txt`

3. **上传到仓库**
   - 创建 `web-template/` 文件夹
   - 将上述文件放入并提交

---

### 方法3: 从GitHub上的RenPyWeb项目获取

**仓库地址：** https://github.com/renpy/renpyweb

1. **下载预编译的web资源**
   - 访问 https://github.com/renpy/renpyweb/releases
   - 下载最新版本的 `renpyweb-8.4.x.tar.bz2`

2. **解压并上传**
   ```bash
   tar -xjf renpyweb-8.4.x.tar.bz2
   # 上传解压后的文件
   ```

---

## 下一步操作

完成上述任意一种方法后，告诉我文件已上传，我将：

1. 解压/提取web模板文件
2. 复制到 `web-dist/` 目录
3. 调整 `index.html` 中的游戏名称
4. 创建gh-pages分支
5. 部署到GitHub Pages

---

## 预期最终结果

部署成功后，访问地址：
```
https://ritori2022.github.io/Visual-Novel/
```

即可在浏览器中玩《漩涡与萤火》！🎮✨

---

*生成时间: 2025-11-08*
*需要帮助？在对话中告诉Luna～*
