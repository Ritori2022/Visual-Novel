# 🚀 一键部署到GitHub Pages

## 快速开始（3步完成）

### Windows用户：

```batch
1. 下载Ren'Py SDK到此目录
2. 双击运行: deploy_web.bat
3. 访问: https://ritori2022.github.io/Visual-Novel/
```

### Mac/Linux用户：

```bash
1. 下载Ren'Py SDK到此目录
2. ./deploy_web.sh
3. 访问: https://ritori2022.github.io/Visual-Novel/
```

---

## 📦 你需要下载的东西

### Ren'Py SDK
- **下载地址**: https://www.renpy.org/latest.html
- **版本**: 8.2.1 或更高
- **大小**: ~200MB

**放置位置：**
```
Visual-Novel/
├── renpy-8.2.1-sdk/    ← 解压到这里
│   ├── renpy.sh        (Linux/Mac)
│   └── renpy.exe       (Windows)
├── vortex_and_firefly/
├── deploy_web.sh       ← 部署脚本
└── deploy_web.bat      ← Windows部署脚本
```

---

## ⚡ 脚本功能

这些脚本会自动：

1. ✅ 检测Ren'Py SDK
2. ✅ 构建Web版本（5-15分钟）
3. ✅ 解压构建结果
4. ✅ 推送到GitHub Pages
5. ✅ 清理临时文件

**完全自动化，无需手动操作！**

---

## 🎯 部署后访问

```
主站: https://ritori2022.github.io/Visual-Novel/
```

⏰ **首次部署需要5-10分钟生效**

---

## 📖 详细文档

遇到问题？查看完整指南：
- **[DEPLOY_INSTRUCTIONS.md](DEPLOY_INSTRUCTIONS.md)** - 详细部署指南
- **[WEB_EXPORT_GUIDE.md](vortex_and_firefly/WEB_EXPORT_GUIDE.md)** - 手动打包教程

---

## 🔧 常见问题

### Q: 找不到Ren'Py SDK
**A:** 确保下载并解压到项目目录，文件夹名应为 `renpy-8.2.1-sdk`

### Q: 推送失败 (Permission denied)
**A:** 配置Git SSH密钥或使用Personal Access Token

### Q: GitHub Pages显示404
**A:** 到仓库Settings → Pages，选择gh-pages分支

更多问题见 [DEPLOY_INSTRUCTIONS.md](DEPLOY_INSTRUCTIONS.md)

---

## 🎨 更新游戏

修改游戏后重新部署：

```bash
# 修改代码
vim vortex_and_firefly/game/script.rpy

# 重新部署
./deploy_web.sh  # 或 deploy_web.bat

# 等待几分钟查看更新
```

---

*Luna创建 © 2025*
