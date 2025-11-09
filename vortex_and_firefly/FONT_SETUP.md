# 中文字体配置指南

## 问题
当前项目使用DejaVuSans字体，不支持中文字符。游戏中的中文内容（角色名"星图师"、占位符文字等）会显示为方块。

## 解决方案

### 方案1：添加思源黑体（推荐）

1. 下载思源黑体（Noto Sans SC）
   - 项目地址：https://github.com/googlefonts/noto-cjk
   - 直接下载：https://github.com/googlefonts/noto-cjk/raw/main/Sans/OTF/SimplifiedChinese/NotoSansSC-Regular.otf

2. 将字体文件放置到：
   ```
   vortex_and_firefly/game/fonts/NotoSansSC-Regular.otf
   ```

3. 在 `script.rpy` 开头添加字体定义：
   ```renpy
   ## 中文字体支持
   define gui.text_font = "fonts/NotoSansSC-Regular.otf"
   define gui.name_text_font = "fonts/NotoSansSC-Regular.otf"
   define gui.interface_text_font = "fonts/NotoSansSC-Regular.otf"
   ```

### 方案2：使用Web字体（适用于网页版）

在 `script.rpy` 中添加：
```renpy
init python:
    # 使用Google Fonts的思源黑体
    config.font_replacement_map["DejaVuSans.ttf", False, True] = ("fonts/NotoSansSC-Regular.otf", False, False)
```

### 方案3：字体子集化（减小文件大小）

如果担心字体文件过大（Noto Sans SC约10MB），可以使用字体子集化工具只保留需要的汉字：

```bash
# 使用 fonttools 创建字体子集
pip install fonttools
pyftsubset NotoSansSC-Regular.otf \
  --text-file=characters.txt \
  --output-file=NotoSansSC-Subset.otf
```

其中 `characters.txt` 包含游戏中所有使用的中文字符。

## 当前状态
- ❌ 未配置中文字体
- ✅ 脚本已包含中文内容
- ⚠️ 需要添加中文字体支持才能正常显示

## 文件大小参考
- NotoSansSC-Regular.otf: ~10MB
- DejaVuSans.ttf: ~739KB
- 子集化后的字体: ~1-2MB（取决于字符数量）
