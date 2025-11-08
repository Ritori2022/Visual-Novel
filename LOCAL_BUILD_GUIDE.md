# Ren'Py本地打包完整指南

## 🎯 方案一：使用Ren'Py Launcher（最推荐）

### 1. 下载Ren'Py SDK

**Windows/Mac/Linux通用步骤：**

1. 访问官网：https://www.renpy.org/latest.html
2. 下载对应系统的SDK：
   - **Windows**: `renpy-8.x.x-sdk.zip`
   - **Mac**: `renpy-8.x.x-sdk.dmg`
   - **Linux**: `renpy-8.x.x-sdk.tar.bz2`

3. 解压到任意目录（例如 `~/renpy-sdk`）

**推荐SDK版本：Ren'Py 8.1+ （支持Python 3）**

---

### 2. 配置项目

#### 方法A：直接使用当前项目结构

```bash
# 将你的 vortex_and_firefly 目录移动到 Ren'Py SDK 能识别的位置
# 或者在Ren'Py Launcher中设置项目目录
```

#### 方法B：在Launcher中添加项目

1. 启动Ren'Py Launcher
   - **Windows**: 双击 `renpy.exe`
   - **Mac**: 打开 `renpy.app`
   - **Linux**: 运行 `./renpy.sh`

2. 点击 `preferences`（偏好设置）
3. 点击 `Projects Directory`
4. 选择 `/home/user/Visual-Novel` 目录
5. 返回主界面，应该能看到 `vortex_and_firefly` 项目

---

### 3. 开始打包

#### 步骤：

1. **在Ren'Py Launcher中选择你的项目** `vortex_and_firefly`

2. **点击 `Build Distributions`（构建发行版）**

3. **配置打包选项：**
   ```
   勾选你需要的平台：
   ✅ Windows x86_64        # Windows 64位版本（推荐）
   ✅ Linux x86_64          # Linux 64位版本
   ✅ Mac x86_64            # Mac Intel版本
   ✅ Mac ARM64             # Mac Apple Silicon版本
   ⬜ Android               # 需要额外配置
   ⬜ iOS                   # 需要Mac系统+Xcode
   ⬜ Web                   # 就是你之前出问题的这个😅
   ```

4. **点击 `Build` 按钮**

5. **等待构建完成**（首次构建会下载依赖，需要5-15分钟）

6. **查看构建结果：**
   ```
   vortex_and_firefly-dists/
   ├── vortex_and_firefly-1.0-win.zip       # Windows版本
   ├── vortex_and_firefly-1.0-linux.tar.bz2 # Linux版本
   └── vortex_and_firefly-1.0-mac.zip       # Mac版本
   ```

---

## 🚀 方案二：使用命令行打包（适合CI/CD）

如果你想自动化打包流程，可以用命令行方式：

### Linux/Mac:
```bash
# 进入Ren'Py SDK目录
cd ~/renpy-sdk

# 打包所有平台
./renpy.sh launcher distribute /path/to/vortex_and_firefly --dest /path/to/output

# 打包指定平台
./renpy.sh launcher distribute /path/to/vortex_and_firefly \
  --package win --package linux --dest /path/to/output
```

### Windows:
```cmd
# 进入Ren'Py SDK目录
cd C:\renpy-sdk

# 打包
renpy.exe launcher distribute C:\path\to\vortex_and_firefly --dest C:\path\to\output
```

**可用的platform参数：**
- `pc` - Windows
- `linux` - Linux
- `mac` - Mac
- `web` - Web（慎用）
- `android` - Android
- `ios` - iOS

---

## 📦 构建前的检查清单

打包前确保：

### ✅ 必须检查项：

1. **版本信息配置正确** (`game/options.rpy`):
   ```python
   define config.name = "漩涡与萤火"
   define config.version = "1.0"
   define build.name = "vortex_and_firefly"
   ```

2. **图片和音频文件都在正确位置：**
   ```
   game/
   ├── images/
   │   ├── characters/
   │   └── backgrounds/
   └── audio/
       ├── music/
       └── sound/
   ```

3. **测试游戏能正常运行：**
   ```bash
   # 在Launcher中点击 "Launch Project" 测试
   ```

4. **检查build配置** (`game/options.rpy`):
   ```python
   build.classify('**~', None)
   build.classify('**.bak', None)
   build.classify('**/.**', None)
   build.classify('**/#**', None)
   build.classify('**/thumbs.db', None)

   # 排除源代码文件（可选）
   build.classify('**.rpy', None)  # 不打包rpy源文件，只打包rpyc
   ```

### 🔧 可选优化：

5. **压缩图片和音频**（减小包体）
6. **生成rpyc文件**（加快加载速度）
7. **添加应用图标**（`game/gui/window_icon.png`）

---

## 🐛 常见问题解决

### 问题1: "找不到项目"
**解决**：
- 确保项目目录包含 `game` 文件夹
- 确保 `game` 文件夹内有 `.rpy` 文件
- 在Launcher的Preferences中正确设置项目目录

### 问题2: "构建失败 - Python版本错误"
**解决**：
- 使用Ren'Py 8.1+（支持Python 3）
- 删除旧的 `.rpyc` 文件：`find game -name "*.rpyc" -delete`

### 问题3: "Web构建一直出问题"
**解决**：
- Web构建确实是最容易出问题的😅
- **强烈建议**：优先打包PC版本（Windows/Linux/Mac）
- Web版本需要额外配置，且有浏览器兼容性问题

### 问题4: "打包体积太大"
**解决**：
```python
# 在 game/options.rpy 中添加
build.archive("scripts", "all")     # 将所有脚本打包成归档
build.archive("images", "all")      # 将图片打包成归档
build.classify("game/**.png", "images")
build.classify("game/**.jpg", "images")
build.classify("game/**.rpy", "scripts")
```

### 问题5: "Mac版本打包后无法运行"
**解决**：
- Mac需要签名（可以跳过，用户需要允许未签名应用）
- 提供两个版本：Intel (x86_64) 和 Apple Silicon (ARM64)

---

## 📊 打包时间参考

| 平台 | 首次打包 | 后续打包 |
|------|----------|----------|
| Windows | 5-10分钟 | 1-2分钟 |
| Linux | 3-5分钟 | 1分钟 |
| Mac | 8-12分钟 | 2-3分钟 |
| Android | 15-30分钟 | 5-10分钟 |
| Web | 10-20分钟 | 3-5分钟 |

---

## 🎯 推荐工作流

### 开发阶段：
```
1. 用Ren'Py Launcher直接运行测试
2. 不需要打包
```

### 测试阶段：
```
1. 打包Windows版本（最常用）
2. 在真实环境测试
```

### 发布阶段：
```
1. 打包所有目标平台
2. 每个平台独立测试
3. 上传到itch.io/Steam等平台
```

---

## 📝 快速命令参考

```bash
# 方法1: GUI方式（推荐）
1. 启动 Ren'Py Launcher
2. 选择项目
3. 点击 "Build Distributions"
4. 勾选平台
5. 点击 "Build"

# 方法2: 命令行方式
cd /path/to/renpy-sdk
./renpy.sh launcher distribute /home/user/Visual-Novel/vortex_and_firefly

# 方法3: 仅编译脚本（快速测试）
./renpy.sh /home/user/Visual-Novel/vortex_and_firefly compile
```

---

## 💡 小提示

1. **首次打包会很慢**（需要下载依赖），之后就快了
2. **Web版本不推荐初学者**（你已经体验过了😅）
3. **优先打包Windows版本**（玩家最多）
4. **记得备份**：打包前先git commit
5. **测试再发布**：每个平台都要实际运行测试

---

## 🔗 相关资源

- Ren'Py官方文档：https://www.renpy.org/doc/html/
- 构建系统文档：https://www.renpy.org/doc/html/build.html
- 发布指南：https://www.renpy.org/doc/html/distributing.html

---

**祝打包顺利！如果遇到问题随时问我～ 喵！✨**
