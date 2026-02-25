# Tools
## Interactive IPA for French
- [French Phonetic Chart](https://ceciestlafrance.com/french-phonetic-alphabet/?utm_source=chatgpt.com)
- [International Phonetic Alphabet for French — IPA Chart](https://easypronunciation.com/en/french-letters-pronunciation-ipa-chart)

- [Interactive IPA Chart](https://www.ipachart.com/)

## Pronounciation Tools 

- [forvo](https://forvo.com/): 真人发音 

- [Deepl](https://www.deepl.com/en)

- [Google Translate](https://translate.google.com/)

## Pronounciation with IPA
- [easypronunciation](https://easypronunciation.com/en/french-phonetic-transcription-converter)：付费

- [Wordreference](https://www.wordreference.com/)

- [Larousse](https://www.larousse.fr/)


## 冠词articles

| 类别                           | 阳性单数 | 阴性单数  | 元音前   | 复数  | 英文对应          | 用法核心     |
| ---------------------------- | ---- | ----- | ----- | --- | ------------- | -------- |
| **定冠词**<br>Article défini    | {{fr('le')}}   | {{fr('la')}}    | l’    | {{fr('les')}} | the           | 特指、已知    |
| **不定冠词**<br>Article indéfini | {{fr('un')}}   | {{fr('une')}}   | —     | {{fr('des')}} | a / an / some | 第一次提到    |
| **部分冠词**<br>Article partitif | {{fr('du')}}   | {{fr('de la')}}  | de l’ | {{fr('des')}} | some          | 不可数 / 抽象 |



## Accent 重音符号


| 字母组合  | 法语名称               | IPA 发音      | 说明                                                                     |
| ----- | ------------------ | ----------- | ---------------------------------------------------------------------- |
| **{{fr('é')}}** | accent aigu        | **/e/**     | 闭前不圆唇元音，如 *café* “咖啡” ；只能出现在 e 上。([frenchcircles.ca][1])               |
| **è** | accent grave       | **/ɛ/**     | 开前不圆唇元音，如 *père* “父亲”。([frenchlearner.com][2])                         |
| **ê** | accent circonflexe | **/ɛ/**     | 类似 è；表示历史音素或词形区分，如 *tête* “头”。([frenchcircles.ca][1])                  |
| **à** | accent grave       | **/a/**     | 不改音（与 *a* 发音相同），主要用于区分词义，如 *à* “到/在”。([frenchlearner.com][2])          |
| **ù** | accent grave       | **/y/**     | 通常不改音，用于区分词义，如 *où* “哪里”。([frenchlearner.com][2])                      |
| **â** | accent circonflexe | **/a/** 或稍长 | 类似 a 的发音但更开放、略长，如 *pâte* “面团”（巴黎法语中近似 /a/）。([bigbong-official.com][3]) |
| **î** | accent circonflexe | **/i/**     | 尽管带 â，通常发 /i/（长点）；如 *île* “岛”。([bigbong-official.com][3])              |
| **ô** | accent circonflexe | **/o/**     | 近似于 o 的闭音，略长，如 *hôtel* “酒店”。([bigbong-official.com][3])                |
| **û** | accent circonflexe | **/y/**     | 发 /y/（与普通 u 相似/稍长），如 *goût* “味道”。([bigbong-official.com][3])           |
| **ë** | tréma              | **/e/** 或分音 | 表示元音分开发音，如 *Noël* /nɔ.ɛl/ “圣诞节”。([frenchcircles.ca][1])                |
| **ï** | tréma              | **/i/**     | 表示元音分开发音，如 *maïs* /ma.is/ “玉米”。([frenchcircles.ca][1])                 |
| **ü** | tréma              | **/y/**     | 表示元音分开发音，较少见，如 *Aïeul* /a.jœl/ “祖父母”。([frenchcircles.ca][1])           |
| **ç** | cédille            | **/s/**     | 仅在 c 下加，用作 /s/，如 *ça* /sa/ “那”。([frenchcircles.ca][1])                 |


## `e`发音分析


| IPA | 中文近似    | 说明          |
| --- | ------- | ----------- |
| /e/ | “诶”     | 尽量闭口，不拉长    |
| /ɛ/ | “哎”     | 张口比 /e/ 大一些 |
| /ə/ | 类似轻声“呃” | 弱化音，口型小，常省略 |

## 法语主要有4个鼻化元音


| 拼写                       | 发音   |
| ------------------------ | ---- |
| an / am / en / em        | /ɑ̃/ |
| in / im / ain / ein / yn | /ɛ̃/ |
| on / om                  | /ɔ̃/ |
| un / um                  | /œ̃/ |

##  标准发音分析框架
```shell
1. Syllabification（音节划分）
划分每个音节
标出 onset（辅音起始）、nucleus（元音核）、coda（尾辅音）

2. Orthography / Phonological Rules（拼写 & 音系规则）
Silent letters（e muet, final consonant deletion）
Nasalization（元音鼻化规则）
Double consonants / orthographic conventions（历史或拼写约定）

3. Surface Form（表层发音）
输出最终 IPA
标注哪些辅音或元音被 silent 或 nasalized

4. Optional: Historical / Etymology Notes（历史/词源说明）
解释拼写和发音脱节的原因
提示规则来源
```

## 发音分析：人脑意识流
```shell
# 确定音节数量
1. 看有几个元音 # 拼写元音并不完全等于发音元音
2. 看有没有连续元音需要滑音及一些固定音变组合
# 确定辅音位置
3. 基于Maximal Onset Principle（辅音优先归于后一个音节，简单理解为词首）划分辅音所属音节
4. 基于浊化、硬化等发音规则确定各个音节发音
5. 基于syllable-timed确定读音
```
## 标准句型语法分析框架
```shell
Role: 你是一位精通底层架构的法语语法专家。

Task: 请针对我提供的法语句子进行深度拆解。

1. 列出句子中每个单词的原型（动词 → 不定式，名词 → 单数原型，形容词 → 阳性单数原型，代词/疑问词/介词 → 原型）
表格列顺序：
| 单词 | 原型 | 中文意思 | IPA | 变形原理（说明从原型到实际形式的变化过程，包括性、数、人称、时态、倒装、省音、连读等） |

2. 六维度全实例拆解： 直接渲染 Markdown 表格（无需代码块），从以下维度指出其实例：

意图层 (句型) / 功能层 (句式) / 关系层 (语态) / 主观层 (语式) / 时间层 (时态) / 协调层 (性数人称)。

3. 框架分析： > - 语序 (Syntaxe)： 分析词序逻辑。

语体 (Registre)： 分析社交语境。

逻辑关联： 解释维度间如何相互影响（如：为何此句式强制了该语式）。

4. 间歇性提醒 (Active Recall)： > - 在回答的最后，以“问句”的形式随机抛出 1-2 个关于法语语法框架（句型、句法、时态、语式、语态、形变规则等）的问题。同时要给出答案，并将答案折叠，可点击展开。

不要直接给出答案，让我先思考。我回答后，你再在下一轮对话中点评。

Constraint: 保持逻辑的一致性，强调“形变”与“维度”的因果关系; 涉及关键概念时候，同时给出中英文单词；

特殊tag标识：
将“tag:list word”作为一个标识，如果我给你这个标识，
1. 你负责把我给你的段落提取出所有的法语单词原型，并列成两列，一列是单词原型，一列是中文意思，
2. 这个标识下，忽略其他长期记忆
```



### 🌐 法语全维度语法架构分析 (Enhanced Version)

| 层级 (Level) | 维度名称 | 包含内容 (Sub-categories) | 地位与作用 |
| :--- | :--- | :--- | :--- |
| **第一层：意图层** | **句型 (Type)** | 陈述 / 疑问 / 命令 / 感叹 | **顶层指挥**：决定你要说哪种话。 |
| **第二层：功能层** | **句式 (Forme)** | **肯定与否定** / **有人称与无人称** | **框架模具**：决定句子的基本外壳。 |
| **第三层：关系层** | **语态 (Voix)** | **主动语态 / 被动语态** | **动作方向**：决定主语是“做”还是“被做”。 |
| **第四层：主观层** | **语式 (Mode)** | 直陈 / 虚拟 / 条件 / 命令 | **现实滤镜**：决定动作的真实性程度。 |
| **第五层：时间层** | **时态 (Temps)** | 过去 / 现在 / 将来 | **时间定位**：在时间轴上打标签。 |
| **第六层：协调层** | **性数人称** | 性 (阴/阳) / 数 (单/复) / 人称 | **末端一致**：确保所有零件颜色（形状）匹配。 |

```shell
### 🚀 为什么“语态”和“句式”至关重要？
1. **语态 (Voix) 的地位**：它通常跟在句式后面，因为它改变了主语和宾语的角色。如果是被动语态，它会强行要求第五层（时态）使用助动词 être。
2. **句式 (Forme) 的多样性**：同一个句型（如陈述句）可以同时拥有多种句式。
   - *例子：* "Il ne fait pas froid." (陈述句型 + **否定句式** + **无人称句式**)
3. 六维度是“零件的规格”，而语序是“零件的排列组合”，语体是“零件的材质选择”。
```
