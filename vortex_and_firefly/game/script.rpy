## 《漩涡与萤火》- 主脚本文件
## Vortex and Firefly - Main Script

## ============================================
## 角色定义
## ============================================

define geo = Character("Geo Tremor", color="#4A7BA7")
define astral = Character("星图师", color="#8B7AB8")
define narrator = Character(None, kind=nvl)  # 系统叙述者

## ============================================
## 性格系统变量
## ============================================

default acceptance_level = 50      # 接受度：对未知的开放程度
default doubt_intensity = 50       # 怀疑度：科学理性 vs 神秘主义
default martyrdom_tendency = 50    # 殉道倾向：个体牺牲意愿

## ============================================
## 进度追踪变量
## ============================================

default first_playthrough = True
default astral_journal_unlocked = False
default forbidden_experiment_unlocked = False
default endings_achieved = []

## ============================================
## 克拉克硬度指数（可选）
## ============================================

default clarke_index = 50  # 0=神秘主义, 100=硬科幻

## ============================================
## 占位符图片定义
## ============================================

# 背景（当前使用颜色占位符）
image bg mine = "#2B1810"
image bg observatory = "#0F1E2E"
image bg instrument = "#1A1A1A"
image bg vortex = "#4A0E4E"

# 角色（当前使用文本占位符）
image geo neutral = Text("GEO\n[中性]", size=30, color="#4A7BA7")
image geo thinking = Text("GEO\n[思考]", size=30, color="#4A7BA7")
image geo shocked = Text("GEO\n[震惊]", size=30, color="#4A7BA7")
image geo enlightened = Text("GEO\n[顿悟]", size=30, color="#4A7BA7")

image astral calm = Text("ASTRAL\n[冷静]", size=30, color="#8B7AB8")
image astral curious = Text("ASTRAL\n[好奇]", size=30, color="#8B7AB8")

## ============================================
## 性格检测函数
## ============================================

init python:
    def check_personality():
        """返回当前性格倾向的文本描述（调试用）"""
        desc = f"接受度: {acceptance_level} | 怀疑度: {doubt_intensity} | 殉道: {martyrdom_tendency}"
        return desc

    def can_unlock_ending(ending_code):
        """检查是否满足特定结局的解锁条件"""
        if ending_code == "A":
            return acceptance_level >= 60 and doubt_intensity >= 50
        elif ending_code == "B":
            return martyrdom_tendency >= 70
        elif ending_code == "C":
            return doubt_intensity >= 70 and forbidden_experiment_unlocked
        elif ending_code == "D":
            return acceptance_level >= 75 and 40 <= doubt_intensity <= 60
        elif ending_code == "E":
            return martyrdom_tendency <= 30 and acceptance_level <= 40
        elif ending_code == "F":
            return martyrdom_tendency >= 60 and acceptance_level >= 80
        elif ending_code == "G":
            return doubt_intensity <= 40 and acceptance_level >= 55
        return False

## ============================================
## 开始游戏
## ============================================

label start:

    ## 显示性格系统（调试模式）
    # $ quick_menu = False
    # "当前性格: [check_personality()]"

    scene bg mine
    with fade

    play music "audio/mine_ambient.ogg" fadein 3.0

    ## 系统叙述开场
    narrator """
    九个月的孤独。

    八千次数据记录。

    一个不可能的数字。

    这就是真相降临的方式。
    """

    nvl clear

    ## 主角登场
    show geo neutral
    with dissolve

    geo "（盯着屏幕上闪烁的数据）"
    geo "负深度... -247米。"
    geo "这个数字本身就是悖论。"

    show geo thinking

    geo "就像在说'非存在的存在'。"
    geo "但设备不会说谎..."
    geo "除非——"

    ## 分支点0：初始性格塑造（学术回忆闪回）
    menu flashback_academia:
        geo "（脑海中浮现出那场学术会议...）"

        "回忆：教授当众否定你的理论时...":

            ## 子选择
            menu academia_reaction:
                "「我会证明你们都错了」":
                    $ doubt_intensity += 15
                    $ martyrdom_tendency += 10

                    geo "（攥紧拳头）那些自以为是的学者..."
                    geo "他们困在教科书里，看不见真实的宇宙。"

                "「也许他们是对的...」":
                    $ acceptance_level -= 10
                    $ doubt_intensity -= 5

                    geo "（叹气）也许我真的只是在浪费时间。"
                    geo "一个被学术界抛弃的地质学家，在废弃矿井里做梦。"

                "「我只是想找到真相」":
                    geo "（平静地看着数据）"
                    geo "真相不在乎谁相信它。"
                    geo "它只是存在。"

    scene bg mine
    show geo neutral

    geo "但现在... 这个'负深度'就在眼前。"

    jump chapter1_discovery

## ============================================
## 第一章：发现
## ============================================

label chapter1_discovery:

    scene bg instrument
    show geo shocked
    with fade

    geo "信号强度在增加..."
    geo "它不是噪音。它是... 某种结构。"

    ## 分支点1：面对无法解释的数据
    menu first_anomaly:
        geo "我需要..."

        "「必须找到理性解释」":
            $ doubt_intensity += 10

            geo "检查所有可能的误差来源。"
            geo "设备校准、地质异常、电磁干扰..."
            geo "科学就是排除一切不可能。"

        "「也许世界本就超出理解」":
            $ acceptance_level += 10
            $ doubt_intensity -= 5

            geo "哥德尔不完备定理..."
            geo "也许宇宙本身就包含无法用系统内语言描述的真理。"
            geo "（苦笑）我居然在引用数理逻辑。"

        "「这是改写教科书的机会」":
            geo "如果能证实这一点..."
            geo "不，先别想那些。专注于数据。"

    scene bg mine
    show geo thinking

    geo "我需要... 交叉验证。"
    geo "但谁会相信我？"
    geo "（停顿）"
    geo "等等... 还有一个人。"

    ## 引入星图师
    scene bg observatory
    with fade

    "（三天后，远程通讯）"

    show astral calm
    with dissolve

    astral "Geo Tremor？"
    astral "我以为你已经... 离开学术界了。"

    show geo neutral at left
    show astral calm at right

    geo "我是离开了。但科学没有离开我。"
    geo "我需要你的空间曲率探测器。"

    show astral curious

    astral "（眼神一闪）你发现了什么？"

    geo "一个... 负深度信号。"
    geo "来自地下247米的'不存在的位置'。"

    if clarke_index >= 70:
        astral "时空曲率异常？"
        astral "如果是虫洞或奇点的局部效应..."
    else:
        astral "（低声）深渊的回音..."
        astral "有些东西不该被测量，Geo。"

    show astral calm

    astral "但我会帮你。"
    astral "我们都是... 被放逐者。"

    ## 分支点2：星图师提出联合验证
    menu astral_cooperation:
        astral "两个被学术界抛弃的疯子，联手寻找不存在的真相。"

        "「我们互相需要」":
            $ martyrdom_tendency -= 5
            $ trust_astral = True

            geo "（真诚地）谢谢你，Astral。"
            geo "不是为了帮忙，而是为了... 相信。"

            show astral approve
            astral "信任是稀缺资源。我会珍惜。"

        "「只是互相利用」":
            $ doubt_intensity += 8
            $ trust_astral = False

            geo "我需要你的设备，你需要新发现来证明自己。"
            geo "这是交易，不是友谊。"

            show astral cautious
            astral "（冷笑）至少你诚实。"
            astral "那我们就做诚实的共谋者。"

        "「也许这是命运」":
            $ acceptance_level += 7
            $ trust_astral = True

            geo "两个人，在同一时刻，追寻同一个不可能..."
            geo "也许宇宙在安排什么。"

            show astral curious
            astral "命运论？从一个地质学家口中？"
            astral "（微笑）有趣。"

    scene bg mine
    with fade

    "（两周后）"

    narrator """
    联合观测。

    两台设备。

    同一个信号。

    真相开始具现。
    """

    nvl clear

    jump chapter2_visualization

## ============================================
## 第二章：可视化
## ============================================

label chapter2_visualization:

    scene bg instrument
    show geo thinking at left
    show astral curious at right
    with fade

    astral "交叉验证完成。"
    astral "你的地震数据... 和我的空间曲率读数完全吻合。"

    show geo shocked

    geo "这意味着..."

    astral "它是真的。某种东西确实存在于'负深度'。"

    ## 准备进入可视化实验
    geo "我改造了成像算法。"
    geo "如果能把信号转化为影像..."

    show astral cautious

    astral "Geo，有些真相..."
    astral "也许不该被看见。"

    menu proceed_visualization:
        "是否继续可视化实验？"

        "「继续。我必须知道」":
            $ acceptance_level += 5
            jump vortex_revelation

        "「也许... 你说得对」":
            $ acceptance_level -= 10
            jump ending_G_early  # 早期荒诞接受结局分支

label vortex_revelation:

    play sound "audio/data_glitch.ogg"

    scene bg vortex
    with pixellate

    play music "audio/vortex_hum.ogg"

    narrator """
    影像浮现。

    深地。

    漩涡。

    吞噬一切的几何。
    """

    nvl clear

    show geo shocked
    with dissolve

    geo "那是... 什么？"

    show astral despair at right

    astral "（颤抖）尺度..."
    astral "Geo，看那个尺度标注。"

    geo "（瞳孔收缩）直径... 四千公里？"
    geo "这不可能。这比地球核心还大。"

    if clarke_index >= 60:
        astral "也许是高维投影。"
        astral "我们看到的只是三维切片。"
    else:
        astral "也许有些存在..."
        astral "从来就不属于我们的维度。"

    ## 关键发现：能量流动
    geo "等等... 那些线条..."
    geo "（调整显示参数）"

    play sound "audio/seismic_ping.ogg"

    geo "它在... 吸收什么。"

    astral "能量流。从地表向下。"
    astral "来源是... （停顿）"
    astral "小马的情感辐射？生命能量？"

    ## 分支点3：看到真相后的反应
    menu truth_reaction:
        geo "我们所有的情感、生命、意识... 都在被..."

        "「必须警告所有小马」":
            $ martyrdom_tendency += 15
            $ warn_everypony = True

            geo "（站起身）这太重要了！"
            geo "每个生命都在被某种... 巨物寄生！"
            geo "我要发布这一切——数据、图像、全部！"

            show astral cautious
            astral "他们会说你疯了。"
            astral "就像上次一样。"

            if trust_astral:
                geo "但这次你在我身边。"
                geo "两个人的疯狂，就是证据的开始。"
            else:
                geo "那就让他们说。真相不需要被相信。"

        "「需要更多数据证实」":
            $ doubt_intensity += 10
            $ warn_everypony = False

            geo "（冷静下来）不... 还不够。"
            geo "一个影像不是证据。"
            geo "我需要可重复的观测、能量测量、时间序列..."

            show astral calm
            astral "理性的选择。"
            astral "但Geo... 有些问题，数据永远无法回答。"

        "「这超出我的理解范畴」":
            $ acceptance_level += 12
            $ warn_everypony = False

            geo "（瘫坐）我只是个地质学家..."
            geo "这... 这是哲学、神学、形而上学的领域。"

            show astral calm
            astral "理解的边界。"
            astral "也许到达这里，本身就是一种成就。"

        "「也许这只是数据幻觉」" if doubt_intensity >= 60:
            $ doubt_intensity += 15
            $ data_skeptic = True

            geo "（疯狂检查代码）"
            geo "算法错误、传感器漂移、信号混叠..."
            geo "一定是哪里出错了。"
            geo "不可能。这一切都不可能。"

            show astral despair
            astral "否认也是一种回应。"

            # 这个分支通向C循环诅咒结局

    jump chapter3_communication

## ============================================
## 第三章：沟通（占位符）
## ============================================

label chapter3_communication:

    scene bg mine
    with fade

    "（占位符：仪式设计章节）"
    "（此处将实现仪式韵律组合交互）"

    # 这里将根据之前的选择分支到不同结局

    "【开发中：后续章节】"
    "当前性格状态："
    "接受度: [acceptance_level]"
    "怀疑度: [doubt_intensity]"
    "殉道倾向: [martyrdom_tendency]"

    return

## ============================================
## 结局：G-荒诞接受（早期分支）
## ============================================

label ending_G_early:

    scene bg mine
    with fade

    show geo thinking

    geo "也许... 有些问题不该被问。"
    geo "有些真相不该被寻找。"

    show astral calm at right

    astral "（点头）智慧的选择。"
    astral "回到表面吧，Geo。"
    astral "阳光、草地、可理解的世界。"

    scene black
    with dissolve

    narrator """
    他关闭了设备。

    密封了矿井。

    那个'负深度'仍在某处闪烁。

    但不再有人注视。

    这是一种接受——

    接受无知，也是一种智慧。
    """

    nvl clear

    centered "{size=+10}结局 G: 荒诞的接受{/size}\n\n\"有些问题，不回答也是答案。\""

    $ endings_achieved.append("G")

    return

## ============================================
## 占位符：其他结局
## ============================================

label ending_A:
    "【结局A：宇宙冷漠】- 开发中"
    return

label ending_B:
    "【结局B：献祭启示】- 开发中"
    return

label ending_C:
    "【结局C：循环诅咒】- 开发中"
    return

label ending_D:
    "【结局D：共生启蒙】- 开发中"
    return

label ending_E:
    "【结局E：觉醒反抗】- 开发中"
    return

label ending_F:
    "【结局F：超越型】- 开发中"
    return
