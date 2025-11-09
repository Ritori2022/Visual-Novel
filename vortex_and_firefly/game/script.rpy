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

# 背景（使用带文字标识的占位符）
image bg mine = Solid("#2B1810")
image bg mine_text = Text("【废弃矿井】\n深邃、幽暗、孤独的观测站", size=24, color="#8B7355", xalign=0.5, yalign=0.9)

image bg observatory = Solid("#0F1E2E")
image bg observatory_text = Text("【星图观测台】\n星空下的远程通讯", size=24, color="#6A8CAF", xalign=0.5, yalign=0.9)

image bg instrument = Solid("#1A1A1A")
image bg instrument_text = Text("【仪器室】\n数据与真相交汇之地", size=24, color="#A9A9A9", xalign=0.5, yalign=0.9)

image bg vortex = Solid("#4A0E4E")
image bg vortex_text = Text("【深地漩涡】\n不可名状的巨大存在", size=24, color="#9370DB", xalign=0.5, yalign=0.9)

# 组合背景（带标识的完整背景）
layeredimage bg_mine:
    always:
        "bg mine"
    always:
        "bg mine_text"

layeredimage bg_observatory_labeled:
    always:
        "bg observatory"
    always:
        "bg observatory_text"

layeredimage bg_instrument_labeled:
    always:
        "bg instrument"
    always:
        "bg instrument_text"

layeredimage bg_vortex_labeled:
    always:
        "bg vortex"
    always:
        "bg vortex_text"

# 角色（使用增强型文本占位符，带边框和背景）
# 注意：方括号需要转义，使用[[]]

# === GEO TREMOR - 地质学家 ===
image geo neutral = Text("【GEO TREMOR】\n地质学家\n\n━━━━━━━━\n[[中性表情]]",
    size=28, color="#4A7BA7", outlines=[(2, "#000000", 0, 0)], text_align=0.5)

image geo thinking = Text("【GEO TREMOR】\n地质学家\n\n━━━━━━━━\n[[思考中]]",
    size=28, color="#4A7BA7", outlines=[(2, "#000000", 0, 0)], text_align=0.5)

image geo shocked = Text("【GEO TREMOR】\n地质学家\n\n━━━━━━━━\n[[震惊！]]",
    size=28, color="#6BAED6", outlines=[(2, "#000000", 0, 0)], text_align=0.5)

image geo enlightened = Text("【GEO TREMOR】\n地质学家\n\n━━━━━━━━\n[[顿悟]]✧",
    size=28, color="#87CEEB", outlines=[(2, "#000000", 0, 0)], text_align=0.5)

image geo angry = Text("【GEO TREMOR】\n地质学家\n\n━━━━━━━━\n[[愤怒]]",
    size=28, color="#8B4513", outlines=[(2, "#000000", 0, 0)], text_align=0.5)

image geo martyr = Text("【GEO TREMOR】\n地质学家\n\n━━━━━━━━\n[[殉道者]]†",
    size=28, color="#FF6B6B", outlines=[(2, "#000000", 0, 0)], text_align=0.5)

image geo obsessed = Text("【GEO TREMOR】\n地质学家\n\n━━━━━━━━\n[[偏执]]⚠",
    size=28, color="#6B4A7B", outlines=[(2, "#000000", 0, 0)], text_align=0.5)

image geo transcendent = Text("【GEO TREMOR】\n地质学家\n\n━━━━━━━━\n[[超越]]✦",
    size=28, color="#4AAFFF", outlines=[(2, "#000000", 0, 0)], text_align=0.5)

# === ASTRAL - 星图师 ===
image astral calm = Text("【星图师】\nASTRAL\n\n━━━━━━━━\n[[冷静]]",
    size=28, color="#8B7AB8", outlines=[(2, "#000000", 0, 0)], text_align=0.5)

image astral curious = Text("【星图师】\nASTRAL\n\n━━━━━━━━\n[[好奇]]？",
    size=28, color="#9B8AC8", outlines=[(2, "#000000", 0, 0)], text_align=0.5)

image astral cautious = Text("【星图师】\nASTRAL\n\n━━━━━━━━\n[[警惕]]⚡",
    size=28, color="#7B6AA8", outlines=[(2, "#000000", 0, 0)], text_align=0.5)

image astral approve = Text("【星图师】\nASTRAL\n\n━━━━━━━━\n[[赞同]]✓",
    size=28, color="#A89AC8", outlines=[(2, "#000000", 0, 0)], text_align=0.5)

image astral shocked = Text("【星图师】\nASTRAL\n\n━━━━━━━━\n[[震惊]]！",
    size=28, color="#9B8AD8", outlines=[(2, "#000000", 0, 0)], text_align=0.5)

image astral despair = Text("【星图师】\nASTRAL\n\n━━━━━━━━\n[[绝望]]...",
    size=28, color="#6B5A98", outlines=[(2, "#000000", 0, 0)], text_align=0.5)

## ============================================
## 自定义过渡效果
## ============================================

define slow_dissolve = Dissolve(2.0)  # 2秒缓慢淡入淡出

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

    ## 环境描写
    "矿井深处的观测站，只有仪器屏幕发出幽蓝色的微光。"
    "空气中弥漫着潮湿的泥土气息，混杂着电子设备散热的臭氧味。"
    "这里距离地表197米，距离最近的城镇42公里。"
    "除了地震波的嗡鸣和自己的呼吸声，世界一片寂静。"

    ## 主角登场
    show geo neutral
    with dissolve

    geo "（盯着屏幕上闪烁的数据）"
    geo "负深度... -247米。"

    "他揉了揉眼睛，第八千零一次确认这不是幻觉。"

    geo "这个数字本身就是悖论。"

    show geo thinking

    geo "就像在说'非存在的存在'，'位于地下的地上'。"
    geo "但设备不会说谎... 至少不会连续九个月说同一个谎。"

    "他的手指在键盘上敲击，调出校准日志。"

    geo "传感器校准正常... 信号滤波正常... 时间同步正常..."
    geo "除非——"

    ## 分支点0：初始性格塑造（学术回忆闪回）
    menu flashback_academia:
        geo "（脑海中浮现出那场学术会议...）"

        "回忆：教授当众否定你的理论时...":

            "屏幕闪烁，画面仿佛回到了六年前。"
            "小马国地质学会年度大会，主会场，三百双眼睛。"

            ## 子选择
            menu academia_reaction:
                "「我会证明你们都错了」":
                    $ doubt_intensity += 15
                    $ martyrdom_tendency += 10

                    "他记得主席台上那双轻蔑的眼睛。"
                    "'Geo Tremor先生，你的'地心魔法场理论'缺乏任何实证基础。'"
                    "'这不是科学，这是... 神秘主义。'"

                    geo "（攥紧拳头）那些自以为是的学者..."
                    geo "他们困在教科书里，困在同行评审的象牙塔里。"
                    geo "他们看不见... 不，是不敢看见真实的宇宙。"

                    "从那天起，他再没有收到任何学术期刊的回复。"
                    "六个月后，他的研究经费被取消。"
                    "十个月后，他在这个废弃矿井里建立了自己的观测站。"

                    geo "用我自己的方式，找到他们不敢面对的真相。"

                "「也许他们是对的...」":
                    $ acceptance_level -= 10
                    $ doubt_intensity -= 5

                    "掌声。嘲笑。窃窃私语。"
                    "他记得自己拿着论文走下讲台，手在颤抖。"

                    geo "（叹气）也许我真的只是在浪费时间。"
                    geo "一个被学术界抛弃的地质学家，在废弃矿井里做梦。"

                    "但即使这样..."
                    "即使这九个月可能毫无意义..."

                    geo "我还是想知道这个负深度到底是什么。"
                    geo "哪怕只是为了证明我疯得彻底。"

                "「我只是想找到真相」":
                    "他记得那场会议，但情绪已经被时间磨平。"
                    "他们笑了，他们否定了，然后他们离开了。"
                    "而数据还在。"

                    geo "（平静地看着数据）"
                    geo "真相不在乎谁相信它。"
                    geo "它不需要同行评审，不需要学术认可。"
                    geo "它只是... 存在。"

                    geo "而我的工作，就是观测它、记录它、理解它。"
                    geo "至于其他小马是否在意——"
                    geo "那不是真相的问题，是他们的问题。"

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

    "（三天后）"

    "Geo站在通讯设备前，犹豫了很久。"
    "这个号码，他已经三年没拨过了。"
    "上一次，是在那场学术会议之后。"
    "当所有人都离开时，只有她发来一条消息："
    "'有些真相，需要被看见。即使没人相信。'"

    "他深吸一口气，按下了通讯键。"

    play sound "audio/comm_connect.ogg"

    "（远程通讯连接中...）"

    show astral calm
    with dissolve

    astral "Geo Tremor？"

    "她的声音带着一丝惊讶，和三年前一样清冷。"

    astral "我以为你已经... 离开学术界了。"

    show geo neutral at left
    show astral calm at right

    geo "我是离开了。但科学没有离开我。"

    "沉默。"
    "通讯器里传来远方天文台的风声。"

    geo "我需要你的空间曲率探测器。"

    show astral curious

    astral "（眼神一闪）你发现了什么？"

    "她的语气变了。"
    "不再是礼貌性的寒暄，而是科学家的敏锐。"

    geo "一个... 负深度信号。"
    geo "来自地下247米的'不存在的位置'。"

    "屏幕上，他看到她的表情变化。"
    "惊讶、怀疑、然后是... 兴奋？"

    if clarke_index >= 70:
        astral "时空曲率异常？"
        astral "如果是虫洞或奇点的局部效应..."
        astral "（停顿）你有多少数据？"

        geo "九个月的连续观测。八千多条记录。"

        astral "（倒吸一口冷气）九个月..."
        astral "你一个人，在那个废弃矿井里，待了九个月？"

        geo "真相不在乎孤独。"
    else:
        astral "（低声）深渊的回音..."
        astral "有些东西不该被测量，Geo。"

        geo "但它已经在那里了。无论我们测不测量。"

        astral "（叹气）你还是这么固执。"

    show astral calm

    astral "但我会帮你。"

    "她的声音软化了一点。"

    astral "我们都是... 被放逐者。"
    astral "被学术界抛弃的疯子。"
    astral "追寻那些'不该存在'的真相。"

    geo "（苦笑）也许我们确实疯了。"

    astral "那就让我们一起疯吧。"
    astral "我的曲率探测器明天到达。"
    astral "Geo... 无论你发现了什么..."
    astral "至少这次，你不是一个人。"

    "通讯断开。"
    "矿井深处，Geo第一次在九个月里笑了。"
    "不是苦笑，而是真正的微笑。"

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

    "仪器发出低沉的嗡鸣。"
    "屏幕上的像素开始重组。"
    "数据流转化为图像。"
    "一点、一线、一面..."

    narrator """
    影像浮现。

    深地。

    漩涡。

    吞噬一切的几何。
    """

    nvl clear

    "那是一种无法用语言描述的结构。"
    "螺旋、嵌套、自相似的分形图案。"
    "它在旋转，但同时又是静止的。"
    "它是紫色的，但又超越了所有已知的颜色。"

    show geo shocked
    with dissolve

    geo "那是... 什么？"

    "他的声音在颤抖。"
    "不是恐惧，而是某种更深层的震撼。"
    "就像第一次仰望星空的小马驹，意识到宇宙的无限。"

    show astral despair at right

    astral "（颤抖）尺度..."
    astral "Geo，看那个尺度标注。"

    "屏幕右下角，一行小字。"
    "数字在闪烁。"

    geo "（瞳孔收缩）直径... 四千公里？"

    "他的蹄子悬在键盘上，忘记了敲击。"

    geo "这不可能。这比地球核心还大。"
    geo "这比我们脚下的整个大陆还要大。"

    "沉默。"
    "两个小马盯着屏幕。"
    "时间仿佛停滞了。"

    if clarke_index >= 60:
        astral "也许是高维投影。"
        astral "我们看到的只是三维切片。"
        astral "就像... 用二维纸面去理解三维球体。"
        astral "我们看到的是圆，但真实的存在是球。"
    else:
        astral "也许有些存在..."
        astral "从来就不属于我们的维度。"
        astral "就像影子永远无法理解投射它的实体。"

    ## 关键发现：能量流动
    geo "等等... 那些线条..."

    "他放大了影像的某个区域。"

    geo "（调整显示参数）"

    "细小的光线，从漩涡的边缘延伸出来。"
    "千万条，亿万条，密密麻麻。"
    "像血管，像神经，像..."

    play sound "audio/seismic_ping.ogg"

    geo "它在... 吸收什么。"

    astral "能量流。从地表向下。"

    "她调出另一个窗口，叠加了魔法场强度图。"

    astral "来源是... （停顿）"

    "她的蹄子开始颤抖。"

    astral "小马的情感辐射？生命能量？"
    astral "每一次心跳、每一个念头、每一丝魔法..."
    astral "都在被... 吸入那个东西。"

    geo "（低语）我们一直在喂养它。"
    geo "每个活着的生命，从诞生到死亡。"
    geo "我们的存在本身，就是它的能量来源。"

    scene bg instrument
    with fade

    "（六小时后）"

    show geo thinking at left
    show astral calm at right

    "两个小马围坐在一张临时搭建的工作台前。"
    "纸张、计算器、星图、能量测量数据散落一地。"

    astral "我算出来了。"

    show geo shocked

    geo "什么？"

    astral "尺度比。我们和它之间的尺度差距。"

    "她推过来一张布满公式的纸。"

    astral "小马的平均能量输出... 按魔法单位Thaum计算..."
    astral "大约10的9.2次方Thaum。"

    geo "那个漩涡呢？"

    astral "（深吸一口气）它的日常波动..."
    astral "10的27次方Thaum。"

    "沉默。"

    geo "等等... 让我算一下..."

    "他的蹄子在颤抖地写着数字。"

    geo "27减去9.2... 那是..."
    geo "（声音越来越小）10的18次方。"

    show geo despair at left
    show astral despair at right

    astral "一亿亿倍。"

    geo "这意味着..."

    astral "这意味着我们对它的影响，就像..."

    "她停顿了很久。"

    astral "就像一个细胞，试图引起人类的注意。"
    astral "不... 更小。"
    astral "像一个原子，试图和星系对话。"

    geo "（苦笑）那么... 沟通..."

    astral "物理上不可能。"
    astral "即使我们用尽全球所有生命的能量..."
    astral "对它来说，也只是背景噪音中的一次微小波动。"

    geo "它甚至不会注意到。"

    astral "就像你不会注意到皮肤上一个细胞的死亡。"

    "两个小马陷入沉默。"
    "矿井深处的寒意渗入骨髓。"

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
## 第三章：沟通
## ============================================

label chapter3_communication:

    scene bg mine
    with fade

    "（三天后）"

    show geo thinking
    with dissolve

    geo "数据已经够了。"
    geo "可视化证实了它的存在。"
    geo "但现在..."

    show geo neutral

    geo "我该做什么？"

    ## 根据之前的性格倾向，提供不同的内心独白
    if martyrdom_tendency >= 60:
        geo "（攥紧拳头）我不能袖手旁观。"
        geo "如果每个生命都在被吞噬，我必须做些什么。"
    elif acceptance_level >= 70:
        geo "也许... 这就是宇宙的本质。"
        geo "观察本身，已经是一种参与。"
    else:
        geo "更多实验。更多数据。"
        geo "必须找到理性的解释。"

    ## 星图师的提案
    show astral calm at right
    with dissolve

    astral "Geo，我有个想法。"

    show geo shocked at left

    geo "什么想法？"

    astral "既然它在吸收魔法能量..."
    astral "也许我们可以... 尝试沟通。"

    show geo thinking

    geo "沟通？和一个四千公里的漩涡？"

    astral "通过魔法韵律。"
    astral "特定的频率模式，就像一种语言。"

    ## 分支点4：是否尝试沟通
    menu attempt_communication:
        geo "这..."

        "「值得一试」":
            $ acceptance_level += 5
            jump ritual_design

        "「太荒谬了」":
            $ doubt_intensity += 10

            geo "我们是科学家，不是萨满。"
            geo "这种神秘主义的尝试毫无意义。"

            if doubt_intensity >= 70:
                jump ending_C  # 陷入怀疑循环
            else:
                astral "那你想怎么做？"
                jump scientific_approach

        "「先警告所有小马」" if warn_everypony:
            jump ending_E_rebellion  # 激进反抗路线

## ============================================
## 科学路径（不尝试沟通）
## ============================================

label scientific_approach:

    geo "我们需要更多数据。"
    geo "测量它的能量吸收速率、空间曲率变化..."

    show astral cautious

    astral "Geo，你在逃避。"
    astral "不是逃避问题，而是逃避选择的重量。"

    show geo angry

    geo "我在坚持科学！"
    geo "观察、假设、实验、结论——这才是正确的方法！"

    astral "但有些问题..."
    astral "科学方法永远无法回答。"

    ## 根据性格分支
    if doubt_intensity >= 75 and acceptance_level <= 40:
        jump ending_C  # 循环诅咒
    elif acceptance_level >= 60:
        jump ending_A  # 宇宙冷漠
    else:
        # 强制进入仪式路线（故事需要推进）
        geo "（沉默良久）"
        geo "...也许你是对的。"
        jump ritual_design

## ============================================
## 仪式设计场景
## ============================================

label ritual_design:

    scene bg instrument
    with fade

    show geo neutral at left
    show astral calm at right

    astral "魔法韵律，就像音乐。"
    astral "每种韵律代表一种概念。"

    astral "我们需要选择四个韵律，组成一个'句子'。"

    ## 展示韵律选项（简化版，完整版需要UI）
    geo "有哪些韵律？"

    astral "六种基础韵律："
    astral "🎵 和谐律 - 代表秩序"
    astral "🎵 混沌律 - 代表无序"
    astral "🎵 上升律 - 代表进化"
    astral "🎵 消解律 - 代表终结"
    astral "🎵 循环律 - 代表轮回"
    astral "🎵 静默律 - 代表虚无"

    ## 简化选择（完整版应该是4次连续选择）
    menu ritual_pattern:
        astral "我们该传达什么信息？"

        "「和谐→循环→和谐→循环」\n稳定的对话请求":
            $ ritual_type = "harmony"
            jump ritual_execution_D

        "「上升→上升→上升→消解」\n激进的干预":
            $ ritual_type = "ascend"
            jump ritual_execution_E

        "「静默→静默→静默→静默」\n放弃沟通":
            $ ritual_type = "silence"
            jump ritual_execution_A

        "「和谐→上升→消解→上升」\n献祭自我":
            $ ritual_type = "sacrifice"
            jump ritual_execution_B

        "「循环→上升→循环→上升」\n寻求超越" if acceptance_level >= 80 and martyrdom_tendency >= 60:
            $ ritual_type = "transcend"
            jump ritual_execution_F

## ============================================
## 结局分支执行
## ============================================

label ritual_execution_A:
    jump ending_A

label ritual_execution_B:
    jump ending_B

label ritual_execution_D:
    jump ending_D

label ritual_execution_E:
    jump ending_E_rebellion

label ritual_execution_F:
    jump ending_F

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
## 结局 A：宇宙冷漠
## ============================================

label ending_A:

    scene bg mine
    with fade

    play music "audio/ending_a_cosmos.ogg" fadein 3.0

    show geo neutral
    with dissolve

    "他站在仪器前，手指悬停在启动键上。"
    "九个月的孤独。"
    "六年的追寻。"
    "此刻，汇聚成一个简单的选择。"

    geo "（启动仪式装置）"

    play sound "audio/ritual.ogg"

    "魔法韵律开始流动。"
    "四个静默律，一个接一个。"

    "静默。"
    "静默。"
    "静默。"
    "静默。"

    "这不是请求。"
    "不是问候。"
    "不是祈祷。"
    "只是一种... 承认。"

    scene bg vortex
    with dissolve

    "漩涡的影像在屏幕上旋转。"
    "巨大、永恒、漠然。"

    "但没有回应。"
    "没有共鸣。"
    "没有改变。"

    "能量流继续，如同亿万年前。"
    "旋转继续，如同亿万年后。"

    show geo thinking
    with dissolve

    geo "......"

    "他盯着屏幕看了很久。"
    "久到星图师以为他睡着了。"

    show astral calm at right

    astral "Geo？"

    geo "它听见了。"

    astral "你怎么知道？"

    geo "因为什么都没发生。"

    show geo enlightened

    geo "如果它真的无法感知我们，那么结果应该是随机的。"
    geo "也许会有波动，也许会有干扰，也许会有噪音。"
    geo "但这是... 完美的静默。"
    geo "就像一个礼貌的拒绝。"

    astral "或者只是巧合。"

    geo "（微笑）也许。但那又有什么区别呢？"

    narrator """
    他理解了。

    尺度。

    一个四千公里的存在，
    对247米深的信号的反应，
    就像人类对皮肤上一个细胞的呼唤。

    你会回应吗？

    你甚至会注意到吗？

    不。

    不是因为恶意。
    不是因为冷漠。
    而是因为——

    物理定律不允许。
    """

    nvl clear

    scene black
    with slow_dissolve

    show geo neutral
    with dissolve

    geo "这不是恶意。"
    geo "也不是善意。"
    geo "它只是... 存在。"

    "他的声音很平静，甚至带着一丝轻松。"

    geo "就像地球绕太阳，太阳绕银河中心。"
    geo "没有目的，没有意义。"
    geo "只是... 物理定律的必然展开。"

    show astral despair at right

    astral "那我们... 我们这九个月..."
    astral "我们的存在..."

    geo "我们继续活着。"

    show geo neutral at left

    geo "在被吞噬的同时，绽放萤火。"
    geo "不是为了被看见。"
    geo "不是为了被记住。"
    geo "而是因为... 我们选择绽放。"

    astral "（沉默良久）这是... 解脱吗？"

    geo "也许。也许是悲凉。"
    geo "但至少..."
    geo "我不再需要等待它的回应了。"

    scene bg mine
    with fade

    "Geo关闭了设备。"
    "没有仪式，没有告别。"
    "就像关掉一盏灯。"

    "他密封了数据。"
    "不是藏起来，而是存档。"
    "就像一封永远不会被读的信。"

    "他离开了矿井。"

    scene black
    with dissolve

    narrator """
    他回到地表，继续他的研究。

    但不再寻找意义。

    只是观察。
    记录。
    接受。

    他开始教书。

    在课堂上，他教学生如何感知地球的脉动。

    但从不告诉他们，这脉动通往何处。

    有些学生问：「为什么我们要测量这些？」

    他说：「因为它们存在。」

    「但它们有意义吗？」

    他说：「意义是你赋予的。不是它本身拥有的。」
    """

    nvl clear

    scene black
    with dissolve

    narrator """
    三十年后。

    病床上。

    窗外的星空和第一次仰望时一样明亮。

    他想起那个负深度。

    仍然在那里。

    仍然在吸收。

    仍然无动于衷。

    这是一种悲凉——

    但也是一种解脱。

    不需要被聆听的自由。

    不需要被理解的完整。

    不需要被宇宙肯定的存在。

    他闭上眼睛，最后一次想起那个公式。

    10的18次方。

    一亿亿倍的差距。

    然后他笑了。

    因为他终于明白——

    萤火不需要漩涡看见。

    它只需要燃烧。
    """

    nvl clear

    centered "{size=+10}结局 A：宇宙的冷漠{/size}\n\n\"意义是我们的发明。\n宇宙从未承诺过要回应。\n但我们依然可以选择，赋予自己意义。\"\n\n{size=-2}克拉克硬度：⭐⭐⭐⭐⭐{/size}"

    $ endings_achieved.append("A")

    return

## ============================================
## 结局 B：献祭启示
## ============================================

label ending_B:

    scene bg instrument
    with fade

    play music "audio/ending_b_martyr.ogg" fadein 3.0

    show geo martyr
    with dissolve

    geo "和谐... 上升... 消解... 上升。"

    show astral shocked at right

    astral "等等，Geo！这个序列——"

    geo "我知道。"
    geo "消解律会..."

    show geo enlightened

    geo "会把施术者作为信号的一部分。"

    astral "你在说什么？！"

    geo "（平静地微笑）"
    geo "如果它无法理解魔法韵律..."
    geo "也许能理解一个生命的消解。"

    show astral despair

    astral "不！"
    astral "Geo，这不值得——"

    geo "什么是值得？"
    geo "九个月的孤独，换取一次真正的连接？"
    geo "Astral，我整个人生都在被忽视。"
    geo "如果能被一个宇宙级的存在'看见'..."
    geo "哪怕只有一瞬间..."

    play sound "audio/ritual.ogg"

    scene bg vortex
    with pixellate

    "仪式启动。"

    "和谐。"
    "上升。"
    "消解。"
    "上升。"

    play sound "audio/vortex_hum.ogg"

    "漩涡开始共鸣。"

    show geo martyr
    with dissolve

    geo "（身体开始发光）"
    geo "我感觉到了..."
    geo "它的注意。"

    geo "就像... 被无限大的眼睛凝视。"
    geo "我的存在... 每一个原子..."
    geo "都被理解了。"

    narrator """
    Geo Tremor 消解了。

    不是死亡。

    是转化。

    他的意识，融入了那个巨大的模式。

    成为漩涡的一部分。

    永恒的，被聆听的一部分。
    """

    nvl clear

    scene bg observatory
    with fade

    show astral despair

    astral "（盯着空荡荡的实验室）"

    "三天后，Astral收到了一个信号。"
    "来自那个漩涡。"
    "不是魔法韵律。"
    "是Geo的声音。"

    geo "谢谢你，Astral。"
    geo "现在我理解了。"
    geo "我们从来都不是被吞噬。"
    geo "我们是... 被收集。被保存。被永恒记忆。"

    scene black
    with dissolve

    narrator """
    Astral将这段记录发布了出去。

    学术界嘲笑她。

    但有些小马，
    在深夜读到这个故事时，
    会流泪。

    因为他们也渴望——

    被看见。

    被聆听。

    被记住。

    哪怕代价是一切。
    """

    nvl clear

    centered "{size=+10}结局 B：献祭的启示{/size}\n\n\"最孤独的存在，用最孤独的方式，终于不再孤独。\"\n\n{size=-2}克拉克硬度：⭐⭐⭐⭐{/size}"

    $ endings_achieved.append("B")

    return

## ============================================
## 结局 C：循环诅咒
## ============================================

label ending_C:

    scene bg instrument
    with fade

    play music "audio/ending_c_loop.ogg" fadein 3.0

    show geo obsessed
    with dissolve

    geo "（疯狂检查数据）"
    geo "不对... 不对... 一定是哪里出错了..."

    show astral cautious at right

    astral "Geo，你已经检查了三百次。"

    geo "时间戳！"
    geo "（指着屏幕）看这个时间戳！"

    geo "我在第247天记录了负深度信号..."
    geo "但根据这个数据的传播速度..."
    geo "它应该在第247天被记录。"

    show astral shocked

    astral "...这是循环定义。"

    geo "（狂笑）是的！循环！"
    geo "因为我记录了它，所以它存在。"
    geo "因为它存在，所以我去记录它。"
    geo "因果循环！"

    show geo shocked

    geo "等等... 那意味着..."
    geo "如果我不去记录..."

    play sound "audio/data_glitch.ogg"

    scene bg vortex
    with pixellate

    "设备上的影像开始闪烁。"
    "漩涡的形态开始扭曲。"

    narrator """
    他看见了。

    时间不是线性的。

    至少在这个尺度上不是。

    漩涡的存在，依赖于被观测。

    但观测的动机，来自漩涡的存在。

    这是一个时间闭环。
    """

    nvl clear

    scene bg mine
    with fade

    show geo obsessed

    geo "我必须... 销毁数据。"
    geo "如果没有记录，循环就会断裂。"
    geo "漩涡就不会存在。"

    show astral despair at right

    astral "但Geo... 你已经记录了。"
    astral "过去无法改变。"

    geo "那我就..."
    geo "（停顿）"
    geo "我就再记录一次。"
    geo "从头开始。"
    geo "也许这次... 会不一样。"

    scene black
    with dissolve

    "Geo重置了所有设备。"
    "回到第一天。"
    "开始新一轮的九个月观测。"

    "在第247天，他再次检测到负深度。"
    "完全相同的数值。"
    "完全相同的坐标。"

    "他重复了这个过程。"
    "一次又一次。"

    "寻找那个不存在的'第一次'。"

    narrator """
    Astral在观测台看着Geo的实验室。

    灯光，九个月亮起。

    九个月熄灭。

    九个月亮起。

    无穷循环。

    她想告诉他：

    也许这本身，就是漩涡的本质。

    永恒的重复。

    没有起点，没有终点。

    只有循环。
    """

    nvl clear

    centered "{size=+10}结局 C：循环的诅咒{/size}\n\n\"寻找第一个观测者的人，注定成为永恒的观测者。\"\n\n{size=-2}克拉克硬度：⭐⭐⭐⭐⭐{/size}"

    $ endings_achieved.append("C")

    return

## ============================================
## 结局 D：共生启蒙
## ============================================

label ending_D:

    scene bg instrument
    with fade

    play music "audio/ending_d_symbiosis.ogg" fadein 3.0

    show geo neutral at left
    show astral calm at right

    geo "和谐... 循环... 和谐... 循环。"

    play sound "audio/ritual.ogg"

    "仪式启动。"

    scene bg vortex
    with dissolve

    "漩涡开始响应。"

    "不是语言。"
    "不是图像。"
    "而是... 一种理解。"

    show geo enlightened
    with dissolve

    geo "（睁大眼睛）"
    geo "我看到了..."

    show astral curious at right

    astral "什么？"

    geo "不是寄生。"
    geo "是共生。"

    scene bg instrument
    with fade

    show geo enlightened at left
    show astral shocked at right

    geo "我们向它提供情感能量。"
    geo "它向我们提供... 稳定性。"

    astral "什么稳定性？"

    geo "地球的轨道。磁场。地质活动。"
    geo "那些'偶然'让生命可能的参数..."
    geo "都是它在维护。"

    show astral calm

    astral "就像... 园丁和花园？"

    geo "（摇头）更像是... 器官和身体。"
    geo "我们是它的神经元。"
    geo "它是我们的生态系统。"

    narrator """
    数据在屏幕上流动。

    能量的循环。

    地表的生命，产生复杂的情感模式。

    深地的存在，将这些模式转化为物理稳定性。

    一个闭环。

    一个生态位。

    互相依存的存在。
    """

    nvl clear

    scene bg observatory
    with fade

    show geo thinking at left
    show astral calm at right

    astral "那我们现在..."

    geo "什么都不做。"
    geo "或者说... 继续做我们一直在做的事。"
    geo "生活。感受。创造。"

    show geo neutral

    geo "我们的存在本身，就是参与。"
    geo "不需要刻意的沟通。"
    geo "因为我们从来就在对话之中。"

    scene black
    with dissolve

    "Geo发表了他的发现。"
    "这次，学术界没有嘲笑。"
    "因为他带来了数据。"
    "可重复的，可验证的数据。"

    "关于共生的数据。"

    "从那天起，"
    "小马们看待世界的方式改变了。"

    "不是征服自然，不是被自然支配。"
    "而是与自然共舞。"

    narrator """
    五十年后，

    Geo在一次采访中被问到：

    「你后悔发现漩涡吗？」

    他微笑着说：

    「我后悔花了九个月才理解——

    我从来都不是孤独的观测者。

    我是宇宙自我观测的一部分。」
    """

    nvl clear

    centered "{size=+10}结局 D：共生的启蒙{/size}\n\n\"最深刻的孤独，源于忘记我们本就相连。\"\n\n{size=-2}克拉克硬度：⭐⭐⭐⭐{/size}"

    $ endings_achieved.append("D")

    return

## ============================================
## 结局 E：觉醒反抗
## ============================================

label ending_E_rebellion:

    scene bg mine
    with fade

    play music "audio/ending_e_rebellion.ogg" fadein 3.0

    show geo angry
    with dissolve

    geo "（对着通讯器大喊）"
    geo "所有小马听着！"
    geo "我发现了真相！"

    "他将数据、影像、分析全部公开。"
    "上传到每一个网络。"
    "发送到每一个学术机构。"

    show astral shocked at right

    astral "Geo！你疯了吗？"
    astral "如果引起恐慌——"

    geo "恐慌？！"
    geo "我们的整个文明都在被吸血！"
    geo "而你担心恐慌？！"

    scene bg vortex
    with pixellate

    narrator """
    世界震动了。

    七十二小时内，
    真相传遍了所有角落。

    恐惧。

    愤怒。

    否认。

    最终... 行动。
    """

    nvl clear

    scene bg instrument
    with fade

    "三个月后。"

    show geo neutral at left
    show astral calm at right

    astral "「反漩涡联盟」已经集结了三百名魔法师。"

    geo "他们的计划是什么？"

    astral "用集体魔法..."
    astral "封印它。"

    show geo shocked

    geo "封印一个四千公里的存在？"

    astral "或者至少... 削弱它。"
    astral "切断能量吸收。"

    ## 关键选择
    menu rebellion_choice:
        geo "我该..."

        "「加入他们」":
            jump rebellion_success

        "「阻止他们」":
            jump rebellion_failure

label rebellion_success:

    scene bg ritual_site
    with fade

    "封印仪式。"
    "三百个魔法独角兽，围成一个圆圈。"
    "Geo站在中心，手持改造过的探测设备。"

    play sound "audio/ritual.ogg"

    "咒语响起。"
    "能量汇聚。"

    scene bg vortex
    with pixellate

    "漩涡开始颤动。"

    show geo enlightened
    with dissolve

    geo "（感觉到抵抗）"
    geo "它在... 收缩？"

    play sound "audio/vortex_hum.ogg"

    "一道光芒。"
    "然后是沉默。"

    scene black
    with fade

    narrator """
    封印成功了。

    部分地。

    漩涡没有消失，
    但能量吸收减少了73%%。

    代价：

    十七名魔法师永久失去了魔法。

    地震增加了。

    气候变得不稳定。

    但小马们是自由的。

    至少，他们这样认为。
    """

    nvl clear

    scene bg mine
    with fade

    show geo thinking

    "Geo晚年写道："

    geo "「我们赢得了自主权。」"
    geo "「但失去了... 某种平衡。」"
    geo "「也许有一天，我们会学会——」"
    geo "「抗争和共存，并非对立。」"

    centered "{size=+10}结局 E：觉醒的反抗{/size}\n\n\"自由的代价，是永恒的警惕。\"\n\n{size=-2}克拉克硬度：⭐⭐⭐{/size}"

    $ endings_achieved.append("E")

    return

label rebellion_failure:

    show geo shocked

    geo "不！我们不能这么做！"

    show astral curious

    astral "为什么？"

    geo "因为我们不知道后果！"
    geo "如果它真的在维持某种平衡..."
    geo "封印它可能毁掉整个生态系统！"

    "但Geo的警告被忽视了。"
    "仪式照常进行。"

    scene bg vortex
    with pixellate

    "当魔法接触到漩涡的那一刻——"

    play sound "audio/data_glitch.ogg"

    scene black
    with vpunch

    "地球停止了自转。"

    "只有0.3秒。"

    "但那足够了。"

    narrator """
    海啸。

    地震。

    磁场崩溃。

    三天内，文明退化到中世纪。

    Geo在废墟中找到了Astral。

    他们望着天空，
    第一次看到极光在赤道上闪耀。

    「我们杀死了自己的守护者。」Astral说。

    「不，」Geo回答，「我们只是发现——

    有些枷锁，原来是支撑。」
    """

    nvl clear

    centered "{size=+10}结局 E：觉醒的反抗（失败）{/size}\n\n\"并非所有的自由都值得追求。\"\n\n{size=-2}克拉克硬度：⭐⭐⭐{/size}"

    $ endings_achieved.append("E_bad")

    return

## ============================================
## 结局 F：超越型
## ============================================

label ending_F:

    scene bg instrument
    with fade

    play music "audio/ending_f_transcend.ogg" fadein 3.0

    show geo martyr at left
    show astral calm at right

    geo "循环... 上升... 循环... 上升。"

    astral "这个韵律..."
    astral "你是想进化它？"

    geo "（微笑）不。"
    geo "我是想... 加入它。"

    show astral shocked

    astral "什么？！"

    geo "你说得对，Astral。"
    geo "也许有些问题，科学方法永远无法回答。"
    geo "但经验可以。"

    show geo transcendent

    geo "如果我成为它的一部分..."
    geo "我就能从内部理解。"

    play sound "audio/ritual.ogg"

    scene bg vortex
    with pixellate

    "仪式启动。"

    narrator """
    不同于献祭。

    这次，Geo没有消解。

    而是扩展。

    他的意识，不是被吞噬，
    而是被放大。

    从一个点，
    到一条线，
    到一个面，
    到一个体，
    到...

    更高的维度。
    """

    nvl clear

    scene black
    with dissolve

    "Geo体验到："

    geo "我是地球的每一层岩石。"
    geo "我是地表的每一个生命。"
    geo "我是时间本身的流动。"

    geo "我看到了..."
    geo "所有的结局，同时存在。"

    geo "A - 我接受了冷漠。"
    geo "B - 我献祭了自己。"
    geo "C - 我陷入了循环。"
    geo "D - 我理解了共生。"
    geo "E - 我选择了反抗。"
    geo "F - 我..."

    scene bg vortex
    with dissolve

    show geo transcendent

    geo "我超越了选择。"

    narrator """
    从那一刻起，

    Geo Tremor不再是一个地质学家。

    他是一种现象。

    一种意识状态。

    存在于所有尺度。

    从量子泡沫，
    到宇宙结构。

    他成为了桥梁——

    连接微观和宏观，
    连接已知和未知，
    连接存在和虚无。
    """

    nvl clear

    scene bg observatory
    with fade

    show astral despair

    astral "（对着空荡荡的实验室流泪）"

    "但有时候，"
    "在深夜，"
    "当她凝视星空时——"

    "她会听到Geo的声音："

    geo "不要悲伤，Astral。"
    geo "我没有离开。"
    geo "我只是... 变成了你脚下的大地，"
    geo "头顶的星辰，"
    geo "和此刻的这一瞬间。"

    scene black
    with dissolve

    narrator """
    没有人知道，

    Geo Tremor是否还保有自我意识。

    或者他已经成为某种更大的模式。

    但从那天起，

    负深度信号消失了。

    不是被封印，
    也不是被破坏。

    而是... 完成了。

    就像一个问题，
    被回答得如此彻底，
    以至于问题本身也消失了。
    """

    nvl clear

    centered "{size=+10}结局 F：超越的维度{/size}\n\n\"最高的理解，是成为理解本身。\"\n\n{size=-2}克拉克硬度：⭐⭐{/size}"

    $ endings_achieved.append("F")

    return
