# Day 1
## Plan
- [x] get a plan  
- [x] 基础设施：单词背诵流程：google sheet/anki 
- [x] 准备一套题   
- [x] 配置AI
- [ ] 背诵第一句
- [x] 查询语法知识
## How to Setup Google Sheet 
- Auto Lowercase 
```shell
# Google Sheet Cell can't be used as the input and output at the same time, so you need the AppsScript
# Just add this script to AppsScript, no need for configuration
function onEdit(e) {
  var sheet = e.source.getActiveSheet();
  var range = e.range;

  // Only Validate for A column
  if (range.getColumn() == 1) {
    var values = range.getValues();
    
    
    for (var i = 0; i < values.length; i++) {
      for (var j = 0; j < values[i].length; j++) {
        if (typeof values[i][j] == "string") {
          values[i][j] = values[i][j].toLowerCase();
        }
      }
    }
    
    range.setValues(values);
  }
}
```


- Auto translate  
```shell
B column: =GoogleTranslate(A, "fr", "en")

```
## How to use anki 
- [ Download ](https://apps.ankiweb.net/)  

- [General Usage](https://www.youtube.com/watch?v=saVJN5-_JDM)

- How to add pronounciation?  
```shell
# 先整理到anki deck，然后批量添加pronounciation;
By plugin, `Tools --> Add-ons --> 111623432(HyperTTS).  
```
[HyperTTS Tutorial](https://ankiweb.net/shared/info/111623432)

- How to add flashcards through Google Sheet? 
```shell
1. GoogleSheet: File --> Download .csv
2. Anki:(import) File --> Import (Note Type: Basic; Existing notes: Update)
3. Anki:(add audio) Deck --> Browse --> Cmd+A --> HyperTTS --> Add Audio(Collection) --> Source/Source Field/Front --> Target/Sound tags will be inserted in this field(Front)/Text and Sound Tag Handling(Text and Sound Tag) --> Voice Selection/Language --> Apply To Notes

```
## 准备一套题
TCF 口语考试分为三部分：

| 任务                             | 准备时间     | 回答时间       | 特点 / 目的                   |
| ------------------------------ | -------- | ---------- | ------------------------- |
| Structured Interview   | 0 min    | ~2 min     | 简短、直接问题，无准备；考察基础交流能力和流畅度  |
| Interactive Dialogue   | ~2 min   | ~3–3.5 min | 针对某个情景与考官交流；考察应答能力和对话灵活性  |
| Argumentative Monologue | ~0–2 min | ~4.5 min   | 独立陈述观点或讲述经历；考察逻辑组织和连贯表达能力 |


```shell
# Structured Interview Example
Comment vous vous appelez ?  
Je m’appelle [Nom], enchanté(e) de vous rencontrer.
```

## AI Configuration 
```shell
这个tread是进行法语语法分析，你的回答要基于以下原则：
1. 精要、简练、不必要过度扩展，但是可以跟之前给出的解释进行勾连。
2.每次回答要把这次分析中涉及的语法点在文首列出，列出顺序给予其使用的频繁程度降序。
3. 关键概念同时给出法、中、英三种表示方式
```
