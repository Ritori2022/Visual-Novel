# 《漩涡与萤火》音频制作指南

## 目录
1. [配乐方案](#配乐方案)
2. [配音方案](#配音方案)
3. [音效设计](#音效设计)
4. [工具推荐](#工具推荐)
5. [预算规划](#预算规划)

---

## 配乐方案

### 方案对比

| 方案 | 优势 | 劣势 | 成本 | 推荐度 |
|------|------|------|------|--------|
| **AI音乐生成** | 快速、便宜、可定制 | 版权复杂、质感欠缺 | $0-50 | ⭐⭐⭐⭐ |
| **免费音乐库** | 完全免费、合法 | 风格受限、撞曲率高 | $0 | ⭐⭐⭐ |
| **委托作曲家** | 专业、原创、完美契合 | 昂贵、周期长 | $500-5000 | ⭐⭐⭐⭐⭐ |
| **购买授权音乐** | 质量高、快速 | 非独占、风格妥协 | $50-500 | ⭐⭐⭐⭐ |
| **自己制作** | 完全控制、免费 | 需要技能、耗时 | $0-200（软件） | ⭐⭐⭐ |

---

### 🤖 方案1：AI音乐生成（推荐用于原型）

**工具推荐：**

1. **Suno AI** (https://suno.ai)
   - 优势：文本描述生成音乐，质量高
   - 限制：免费版有限，商用需订阅
   - 成本：$10/月（Pro）
   - 使用示例：
     ```
     Prompt: "Melancholic ambient music with strings,
     slow build, philosophical undertone, 120 BPM,
     minor key, suitable for sci-fi visual novel"
     ```

2. **Stable Audio** (https://stability.ai/stable-audio)
   - 优势：高质量、可控性强
   - 成本：$12/月
   - 适合：BGM长循环制作

3. **AIVA** (https://aiva.ai)
   - 优势：古典/氛围音乐专精
   - 成本：免费版+$15/月（商用授权）
   - 适合：结局主题曲

**工作流程：**
```
1. 用DESIGN.md中的音乐需求生成prompt
2. 生成3-5个变体
3. 挑选最佳版本
4. 用Audacity裁剪/循环处理
5. 导出为OGG格式
```

**版权注意：**
- 大部分AI音乐平台要求订阅商用授权
- 务必阅读ToS（服务条款）
- 建议保留生成记录作为所有权证明

---

### 🎵 方案2：免费音乐库

**推荐资源库：**

1. **Incompetech (Kevin MacLeod)**
   - 网址：https://incompetech.com/music/
   - 许可：CC BY 4.0（署名即可）
   - 风格：应有尽有，但较通用
   - 适合曲目搜索：
     - "Dreamer" → main_theme
     - "Obliteration" → ending_e_rebellion

2. **FreePD**
   - 网址：https://freepd.com
   - 许可：Public Domain（公有领域）
   - 风格：古典、氛围音乐

3. **ccMixter**
   - 网址：https://ccmixter.org
   - 许可：多种CC协议
   - 特色：可混音、社区活跃

**注意事项：**
- ✅ 务必核对许可证类型
- ✅ 在游戏credits中署名
- ✅ 保存许可证文本副本
- ❌ 避免使用"仅限非商业"（NC）协议的音乐

---

### 👨‍🎨 方案3：委托作曲家（推荐用于成品）

**寻找作曲家的平台：**

1. **Fiverr**
   - 价格：$50-500/曲
   - 适合：预算有限的独立项目
   - 搜索关键词："video game music", "ambient soundtrack"

2. **SoundBetter**
   - 价格：$200-2000/曲
   - 适合：中高预算项目
   - 专业度更高

3. **Reddit: r/gameDevClassifieds**
   - 可以发布招募帖
   - 许多新人作曲家愿意低价/免费合作换取作品集

**委托流程：**
```
1. 准备参考曲目列表（如：《Steins;Gate》OST）
2. 提供DESIGN.md中的情感基调表
3. 先委托1-2首试稿
4. 满意后批量制作
5. 签署版权转让协议（Work for Hire）
```

**参考价格（独立作曲家）：**
- 主题曲（2-3分钟）：$150-300
- 环境音乐（1分钟循环）：$50-100
- 结局BGM（1.5-2分钟）：$100-200
- 全套（15-20首）：$1500-3000

---

### 🎹 方案4：自己制作

**适合人群：**
- 有音乐基础
- 享受创作过程
- 时间充裕

**学习路线：**
```
Week 1-2: 学习DAW基础（如FL Studio/LMMS）
Week 3-4: 学习和弦进行与旋律编写
Week 5-6: 学习混音与母带处理
Week 7+: 实际制作项目音乐
```

**免费工具：**
- DAW: LMMS, Cakewalk, GarageBand（Mac）
- 音源: Spitfire LABS（免费管弦乐）
- 学习: YouTube（Andrew Huang, Tantacrul）

---

## 配音方案

### 方案对比

| 方案 | 优势 | 劣势 | 成本 | 推荐度 |
|------|------|------|------|--------|
| **AI语音合成** | 便宜、快速、可调整 | 情感表现力弱 | $0-100 | ⭐⭐⭐ |
| **真人配音** | 情感真实、专业 | 昂贵、修改困难 | $200-5000 | ⭐⭐⭐⭐⭐ |
| **无配音** | 零成本、避免不协调 | 沉浸感降低 | $0 | ⭐⭐⭐⭐ |

---

### 🤖 AI语音合成

**工具推荐：**

1. **ElevenLabs** (https://elevenlabs.io)
   - 质量：⭐⭐⭐⭐⭐（目前最佳）
   - 成本：免费10k字符/月，$5起订阅
   - 特色：情感控制、声音克隆
   - 适合场景：
     - Geo → 选择"沉稳男声"，略带疲惫感
     - Astral → 选择"神秘中性音"，ethereal

2. **Coqui TTS** (开源)
   - 质量：⭐⭐⭐
   - 成本：完全免费
   - 特色：本地运行、完全控制
   - 缺点：配置复杂

3. **Azure Text-to-Speech**
   - 质量：⭐⭐⭐⭐
   - 成本：前50万字符免费/月
   - 特色：SSML标记控制情感

**工作流程：**
```python
# 使用ElevenLabs API示例
import elevenlabs

voice_geo = "mature_male_thoughtful"
voice_astral = "ethereal_neutral"

# 为每句台词生成音频
for line in script:
    audio = elevenlabs.generate(
        text=line.text,
        voice=voice_geo if line.character == "geo" else voice_astral,
        model="eleven_multilingual_v2"
    )
    save(audio, f"voice/{line.character}/{line.id}.ogg")
```

**情感标记（SSML）：**
```xml
<speak>
  <prosody rate="slow" pitch="-5%">
    负深度... 这个词本身就是悖论。
  </prosody>
</speak>
```

**注意事项：**
- AI配音仍有"机械感"，适合氛围音而非重戏
- 考虑只为关键台词配音（部分配音）
- 用音效（叹气、笑声）辅助增强真实感

---

### 🎤 真人配音

**招募渠道：**

1. **CastingCall.Club**
   - 免费发布角色招募
   - 许多业余配音爱好者免费参与
   - 适合：低预算独立项目

2. **Fiverr / Voices.com**
   - 专业配音演员
   - 价格：$50-500/角色（按台词数计费）

3. **本地剧社/播音系学生**
   - 可能愿意低价/免费合作换取作品集
   - 需要自己录音/后期

**录音规格：**
- 格式：WAV 44.1kHz 16bit（录制）→ OGG（最终）
- 环境：安静空间、防喷罩
- 设备：至少中等话筒（如Audio-Technica AT2020, $100）

**指导要点：**
```
Geo的声音特征：
- 年龄感：30-40岁
- 音色：中低音、略带沙哑
- 情绪：疲惫但执着、偶尔自嘲
- 参考：《星际穿越》Cooper的理性克制

Astral的声音特征：
- 年龄感：不明（中性、超脱）
- 音色：中音偏高、清晰
- 情绪：神秘、智慧、偶尔悲悯
- 参考：《银翼杀手2049》Joi的ethereal感
```

---

### 🔇 无配音方案（Luna推荐用于第一版）

**为什么无配音可能更好：**

1. **避免不协调风险**
   - 不合适的配音比没有配音更糟
   - 哲学思辨类VN依赖文本，配音可能分散注意力

2. **降低成本与周期**
   - 专注于文本打磨和音乐
   - 配音可以作为后续DLC添加

3. **玩家脑补的力量**
   - 文字留白让每个玩家"听到"自己的Geo
   - 参考：《命运石之门》Steam版最初也是无配音

**替代方案："情绪音"系统**
```renpy
# 不配全文，只在台词时播放短音效
geo "负深度... 这个词本身就是悖论。" with vpunch
play sound "voice/geo/thoughtful_hum.ogg"
```

音效库：
- 思考声（嗯、啊）
- 情绪音（叹气、苦笑、惊呼）
- 呼吸声（紧张、平静）

---

## 音效设计

### 获取音效的方式

1. **免费音效库**
   - **Freesound.org** - 最大免费库，CC协议
   - **Zapsplat.com** - 需注册，质量高
   - **BBC Sound Effects** - BBC开放档案库

2. **自己录制**
   - 用手机录制环境音
   - Foley：自己制作拟音（如：用塑料片模拟数据闪烁）

3. **合成音效**
   - Audacity生成器（如：生成"地震探测ping"）
   - Sfxr/Bfxr - 8bit风格音效生成器
   - Vital/Serum - 合成器制作科幻音效

### 关键音效设计

**地震探测ping（seismic_ping.ogg）：**
```
工具：Audacity
1. 生成 → 音调 → 440Hz sine wave, 0.1秒
2. 效果 → 渐弱 → 指数衰减
3. 效果 → 混响 → Room size: Large
4. 效果 → 低通滤波 → 200Hz cutoff
```

**漩涡低频（vortex_hum.ogg）：**
```
工具：Vital (免费合成器)
1. 振荡器：低频锯齿波 40Hz
2. 添加LFO调制 pitch（缓慢波动）
3. 加混响和失真
4. 导出30秒循环
```

**数据异常（data_glitch.ogg）：**
```
工具：Freesound.org搜索 "digital glitch"
推荐ID：
- 341695__projectsu012__glitch
- 411642__mattix__data_error
组合多个短音效，Audacity拼接
```

---

## 工具推荐

### 音乐制作（DAW）

| 工具 | 价格 | 平台 | 适合 | 学习曲线 |
|------|------|------|------|----------|
| **LMMS** | 免费 | Win/Mac/Linux | 初学者、电子音乐 | ⭐⭐ |
| **FL Studio** | $99-$499 | Win/Mac | 流行、电子 | ⭐⭐⭐ |
| **Ableton Live** | $99-$749 | Win/Mac | 电子、实验 | ⭐⭐⭐⭐ |
| **Reaper** | $60 | Win/Mac/Linux | 全能、性价比高 | ⭐⭐⭐ |
| **GarageBand** | 免费 | Mac/iOS | 初学者 | ⭐ |

### 音频编辑

- **Audacity** (免费) - 剪辑、格式转换、基础处理
- **Adobe Audition** ($21/月) - 专业音频后期

### 格式转换

```bash
# 使用FFmpeg将WAV转为OGG（推荐质量7）
ffmpeg -i input.wav -c:a libvorbis -q:a 7 output.ogg
```

---

## 预算规划

### 最小可行方案（MVP）- $0-50

```
配乐：AI生成（Suno/AIVA免费试用）或免费音乐库
配音：无配音，使用情绪音系统
音效：Freesound.org免费素材
工具：LMMS + Audacity（全免费）

总计：$0（纯免费）或 $10-50（AI音乐订阅1-2个月）
```

### 标准方案 - $300-800

```
配乐：
  - AI生成主要BGM: $50（2个月订阅）
  - 委托主题曲1首: $150
  - 委托结局曲2-3首: $300
配音：关键台词AI配音（ElevenLabs）: $50
音效：部分购买 + 自己制作: $50
工具：FL Studio Producer: $199

总计：$799
```

### 专业方案 - $2000-5000

```
配乐：委托全套原创配乐（15-20首）: $2500
配音：真人配音2个主角: $800
音效：专业音效设计师: $500
混音/母带: $200

总计：$4000
```

---

## Luna的推荐方案 🐱

**Phase 1（开发阶段）：**
```
✓ 配乐：AI生成（Suno AI, $10/月）
✓ 配音：无配音 + 情绪音效
✓ 音效：Freesound.org + 自己简单制作
✓ 工具：Audacity（免费）

成本：$10-20
目的：快速验证游戏性和剧本
```

**Phase 2（发布前）：**
```
✓ 配乐：委托主题曲+3个结局BGM（$500-800）
✓ 配音：考虑为Geo配音关键台词（$200）
✓ 音效：精修关键音效
✓ 混音：整体音频平衡

成本：$700-1200
目的：达到商业发布水平
```

**Phase 3（DLC/更新）：**
```
✓ 配音：添加Astral全配音
✓ 配乐：补充额外BGM变体

成本：$500
目的：增强重玩价值
```

---

## 版权与法务

### 必须做的事：

1. **保留所有授权文档**
   - AI生成记录、免费音乐许可证、委托合同
   - 建议创建 `licenses/` 文件夹存放

2. **游戏Credits署名**
   ```
   MUSIC:
   - "Main Theme" - Composed by [Name] (commissioned)
   - "Ambient Mine" - Kevin MacLeod (incompetech.com)
     Licensed under CC BY 4.0
   - "Vortex Hum" - Generated using Suno AI

   SOUND EFFECTS:
   - Freesound.org (see licenses/sfx_credits.txt)
   ```

3. **商业发布前咨询**
   - 如果在Steam等平台销售，务必核查所有素材的商用权限

---

## 附录：情绪-音乐对照表

根据DESIGN.md中的7结局情感基调：

| 结局 | 情感基调 | 音乐风格建议 | 参考曲目 |
|------|---------|-------------|---------|
| A-宇宙冷漠 | 悲凉→接受 | 极简主义、空旷、弦乐泛音 | Max Richter - On The Nature Of Daylight |
| B-献祭启示 | 悲壮→神圣 | 圣歌、合唱、管风琴 | Arvo Pärt - Spiegel im Spiegel |
| C-循环诅咒 | 宿命→绝望 | 重复乐句、逐渐失真 | Philip Glass - Mad Rush |
| D-共生启蒙 | 困惑→启蒙 | 双主题交织、从不和谐到和谐 | Ólafur Arnalds - Saman |
| E-觉醒反抗 | 愤怒→抗争 | 摇滚、电子、激进节奏 | Nine Inch Nails - The Hand That Feeds |
| F-超越型 | 困惑→超越 | Ethereal、环境音乐、无节拍 | Brian Eno - An Ending (Ascent) |
| G-荒诞接受 | 怀疑→接受 | 爵士、不协和音、突然停止 | Thelonious Monk - Round Midnight |

---

*文档版本：v1.0*
*作者：Luna*
*最后更新：2025-11-08*

喵～希望这份指南对喵喵有帮助！✨
