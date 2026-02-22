# Tools
## Interactive IPA for French
- [French Phonetic Chart](https://ceciestlafrance.com/french-phonetic-alphabet/?utm_source=chatgpt.com)
- [International Phonetic Alphabet for French — IPA Chart](https://easypronunciation.com/en/french-letters-pronunciation-ipa-chart)

- [Interactive IPA Chart](https://www.ipachart.com/)

## 冠词articles

| 类别                           | 阳性单数 | 阴性单数  | 元音前   | 复数  | 英文对应          | 用法核心     |
| ---------------------------- | ---- | ----- | ----- | --- | ------------- | -------- |
| **定冠词**<br>Article défini    | {{fr('le')}}   | {{fr('la')}}    | l’    | {{fr('les')}} | the           | 特指、已知    |
| **不定冠词**<br>Article indéfini | {{fr('un')}}   | {{fr('une')}}   | —     | {{fr('des')}} | a / an / some | 第一次提到    |
| **部分冠词**<br>Article partitif | {{fr('du')}}   | {{fr('de la')}}  | de l’ | {{fr('des')}} | some          | 不可数 / 抽象 |



## 动词变位规则 
先去掉`er`然后按照如下规则：

| 人称代词 (Subject) | 词尾 (Ending) | 示例：Parler (Speak) |
| :--- | :--- | :--- |
| {{fr('Je')}} | **-e** | Je parle |
| {{fr('Tu')}} | **-es** | Tu parles |
| {{fr('Il')}} / {{fr('Elle')}} / {{fr('On')}} | **-e** | Il parle |
| {{fr('Nous')}} | **-ons** | Nous parlons |
| {{fr('Vous')}} | **-ez** | Vous parlez |
| {{fr('Ils')}} / {{fr('Elles')}} | **-ent** | Ils parlent |

## 反身代词列表

| 主语代词 (Subject Pronoun) | 反身代词 (Reflexive Pronoun) | 英文意思                                         |
| ---------------------- | ------------------------ | -------------------------------------------- |
| {{fr('je')}}                     | me → m’                  | myself                                       |
| {{fr('tu')}}                     | te → t’                  | yourself (singular/informal)                 |
| {{fr('il')}}                     | se → s’                  | himself                                      |
| {{fr('elle')}}                   | se → s’                  | herself                                      |
| {{fr('on')}}                     | se → s’                  | oneself / we / people (depending on context) |
| {{fr('nous')}}                   | nous                     | ourselves                                    |
| {{fr('vous')}}                   | vous                     | yourself (formal) / yourselves               |
| {{fr('ils')}}                    | se → s’                  | themselves                                   |
| {{fr('elles')}}                  | se → s’                  | themselves                                   |

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
请帮我分析以下法语句子，严格按以下要求执行：
1️⃣ 语法点
列出所有涉及的语法点（动词变位、倒装、疑问词、代词、形容词性物主代词等）
按使用频率及重要性降序排列
每个语法点标注：法语术语 / 中文 / 英文

2️⃣ 单词原型表（合并版）
列出句子中每个单词的原型（动词 → 不定式，名词 → 单数原型，形容词 → 阳性单数原型，代词/疑问词/介词 → 原型）
表格列顺序：
| 单词 | 原型 | 中文意思 | IPA | 变形原理（说明从原型到实际形式的变化过程，包括性、数、人称、时态、倒装、省音、连读等） |

3️⃣ 句型分析
句型名称（法语术语 / 中文 / 英文）
法语中实用占比（高/中/低）
句子公式 / 结构
句子中文翻译

4️⃣ 分析顺序
语法点列表
单词原型表（合并版 + IPA + 变形原理）
句型分析

5️⃣ 注意事项
分析精要、简洁，但可与前面概念勾连
强调法语特有规则：性数一致、动词倒装、省音、连读等
保持统一格式，方便对比不同句子
```
