# 🎮 快速开始：添加中文字体支持

## ⚠️ 重要提示

游戏脚本包含大量中文内容（931个独立汉字），但当前**未包含中文字体文件**（避免仓库体积过大）。

**没有中文字体时的表现：**
- 游戏启动时会显示：`警告：未找到中文字体，中文可能无法正常显示`
- 中文字符会显示为方块 ▢▢▢
- 游戏不会崩溃，但阅读体验很差

## 📥 快速安装字体（3步完成）

### 方式1：自动下载（Linux/Mac - 推荐）

```bash
cd Visual-Novel
chmod +x download_font.sh
./download_font.sh
```

如果自动下载失败，请使用方式2。

### 方式2：手动下载（所有系统）

#### 步骤1：下载字体文件

访问 **Google Fonts** 下载思源黑体：
1. 打开 https://fonts.google.com/noto/specimen/Noto+Sans+SC
2. 点击右上角 **"Get font"** 按钮
3. 点击右上角购物车图标，然后点击 **"Download all"**
4. 解压下载的 `Noto_Sans_SC.zip` 文件

#### 步骤2：复制字体文件

找到解压后的字体文件：
- 文件名：`NotoSansSC-Regular.ttf` 或 `NotoSansSC-Regular.otf`
- 大小：约 10MB

复制到项目目录：
```
Visual-Novel/
  vortex_and_firefly/
    game/
      fonts/
        NotoSansSC-Regular.otf  ← 复制到这里（重命名为.otf）
```

#### 步骤3：验证安装

运行游戏，如果没有看到"未找到中文字体"警告，说明安装成功！

## 🔍 使用的中文字符统计

- **独立汉字数量：** 931个
- **主要内容：** 角色名、场景描述、对话文本、结局文字
- **示例：** 星图师、废弃矿井、深地漩涡、宇宙的冷漠...

## 💡 其他选项

### 选项A：使用其他中文字体

如果你有其他中文字体（.ttf 或 .otf格式），可以：
1. 重命名为 `NotoSansSC-Regular.otf`
2. 复制到 `vortex_and_firefly/game/fonts/` 目录

### 选项B：创建字体子集（高级用户）

如果想减小字体文件大小，可以创建只包含游戏所需931个汉字的子集：

```bash
# 安装 fonttools
pip install fonttools

# 创建字体子集（需要先有完整字体）
pyftsubset NotoSansSC-Regular.otf \
  --text-file=/tmp/game_chinese_chars.txt \
  --output-file=vortex_and_firefly/game/fonts/NotoSansSC-Regular.otf
```

这可以将字体文件从10MB减小到约1-2MB。

## 📝 许可证信息

**Noto Sans SC (思源黑体)**
- 许可证：SIL Open Font License 1.1
- 可用于：商业和非商业项目
- 无需支付费用
- 项目地址：https://github.com/googlefonts/noto-cjk

## ❓ 常见问题

### Q: 为什么不直接包含字体文件？
A: 字体文件约10MB，会显著增加Git仓库大小和克隆时间。

### Q: 可以使用其他字体吗？
A: 可以！任何支持中文的.ttf或.otf字体都可以，只需重命名为`NotoSansSC-Regular.otf`。

### Q: 我下载了字体但游戏还是显示方块？
A: 检查：
1. 文件名是否正确：`NotoSansSC-Regular.otf`
2. 文件路径是否正确：`vortex_and_firefly/game/fonts/`
3. 文件格式是否正确：.ttf 或 .otf（不是.zip或.html）

### Q: 有更小的替代字体吗？
A: 可以尝试：
- 文泉驿微米黑（约4MB）
- 文泉驿正黑（约7MB）
- 思源黑体 Light版（约8MB）

## 🎉 完成！

字体安装后，你就可以享受完整的《漩涡与萤火》视觉小说体验了！

游戏特色：
- ✨ 多重分支剧情
- 🌌 7个不同结局
- 🎭 深度哲学主题
- 💫 性格系统影响走向

祝你游戏愉快！
