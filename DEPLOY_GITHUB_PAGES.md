# GitHub Pages 部署指南

## ✅ Web打包已完成！

所有web文件已成功推送到 `docs/` 目录：
- ✅ RenPyWeb 8.4 运行环境 (~15MB)
- ✅ 《漩涡与萤火》游戏内容 (5.4MB)
- ✅ 中文标题配置
- ✅ 7结局多线程叙事

---

## 📋 GitHub Pages 部署步骤

### 1. 访问仓库设置
```
https://github.com/Ritori2022/Visual-Novel/settings/pages
```

### 2. 配置GitHub Pages

在 "Build and deployment" 部分：

**Source（来源）：**
选择 `Deploy from a branch`

**Branch（分支）：**
- 分支：`claude/text-to-image-models-011CUw5He1JECp6GXyfK4cW4`
- 文件夹：`/docs`
- 点击 **Save** 保存

### 3. 等待部署

- GitHub会自动构建并部署（约1-2分钟）
- 在 Settings → Pages 页面顶部会显示部署状态
- 成功后会显示：**"Your site is live at https://ritori2022.github.io/Visual-Novel/"**

### 4. 访问游戏

部署成功后，访问：
```
https://ritori2022.github.io/Visual-Novel/
```

---

## 🎮 游戏信息

**标题：** 漩涡与萤火 (Vortex and Firefly)

**特性：**
- 7个哲学结局（A-G）
- 隐藏人格系统（接受度、怀疑度、殉道倾向）
- 渐进式结局解锁
- 3章主线剧情
- 多重选择影响走向

**技术规格：**
- 引擎：Ren'Py 8.4 + RenPyWeb
- 总大小：约20MB
- 浏览器兼容：Chrome, Firefox, Edge, Safari（需要WebAssembly支持）

---

## ⚠️ 可能的问题与解决

### 问题1：404 Not Found
**原因：** 部署尚未完成或配置错误
**解决：**
1. 检查Settings → Pages中是否显示"Your site is live"
2. 确认分支和文件夹配置正确
3. 等待3-5分钟后刷新

### 问题2：加载缓慢
**原因：** 首次加载需要下载20MB文件
**解决：** 这是正常的，WebAssembly引擎较大，后续访问会使用浏览器缓存

### 问题3：无法运行
**原因：** 浏览器不支持WebAssembly
**解决：** 使用现代浏览器（Chrome 90+, Firefox 90+, Edge 90+）

---

## 🔧 高级配置（可选）

### 自定义域名
如果有自己的域名，可以在Settings → Pages中配置Custom domain

### HTTPS
GitHub Pages自动提供HTTPS，无需额外配置

### 游戏更新
如果需要更新游戏内容：
1. 修改 `vortex_and_firefly/game/script.rpy`
2. 重新打包：运行 `build_web.py`
3. 替换 `docs/game.zip`
4. 提交并推送更改
5. GitHub Pages会自动重新部署

---

## 📊 文件结构

```
docs/
├── index.html          # 游戏入口页面（已配置中文标题）
├── index.js            # JavaScript加载器
├── index.wasm          # WebAssembly引擎核心
├── game.zip            # 游戏内容（脚本、资源等）
├── pyapp.data          # Python应用数据
├── pyapp-data.js       # Python应用元数据
├── pythonhome.data     # Python环境
├── pythonhome-data.js  # Python环境元数据
├── htaccess.txt        # Apache配置（可选）
└── renpyweb-version.txt # 版本信息
```

---

## 🎉 部署完成后

你可以：
1. 分享游戏链接给朋友
2. 在社交媒体上宣传
3. 嵌入到个人网站
4. 继续开发新章节或结局

---

*生成时间：2025-11-08*
*如有问题，可以继续在对话中咨询Luna～喵*
