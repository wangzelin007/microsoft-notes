网页结构
[html](https://www.w3school.com.cn/tags/html_ref_byfunc.asp)  
```html
<!DOCTYPE html> HTML5
<html> </html> 网页根标签  
    <head> </head> 网页头部
        <meta charset="UTF-8"> 网页元数据：字符集
        <meta name="keywords" content="HTML5,CSS3"> 用于搜索
        <meta name="description" content="一个好网站"> 搜索结果显示
        <meta http-qeuiv="refresh" content="3;url=xxx"> 重定向 
        <title> </title> 浏览器标题栏 也会作为搜索结果超链接上的文字
    <body> 
      <header></header> 头部
      <main></main> 主要内容
      <footer></footer> 底部
      <nav></nav> 导航
      <aside></aside> 和主体相关的其他内容（侧边栏）
      <article></article> 独立的文章
      <section></section> 独立的区块
      <div></div> 无语义，用来分区block。
      <span></span> 无语义，用来分区inline
    </body> 网页主体

block element 独占一行 布局
<h1> to <h6> headline 搜索引擎也会通过 <h></h> 判断网页
<hgroup> </hgroup> 标题分组
<p> </p> paragraph 定义段落。 p元素中不能放任何的块元素 lorem自动生成文字
<br>	定义简单的折行。
<hr> 	定义水平线。
<blockquto></blockquto> 长引用

inline element 不会独占一行 包裹文字
<em></em> 语音语调的加重
<strong></strong> 强调重要的内容
<q></q> 短引用
<a href=""></a> 可以嵌套除了自身的任何元素
  
替换元素
<img src="" alt="">
  
HTML注释
<!--...-->

```

```html
<a href="" target=""></a> 超链接或锚点 anchor:  
target:
  - _blank 新开页面
  - _self self 当前页面
  - _parent 父层
  - _top 顶层
  - download 下载  
href:
  - www.http://xxx 跳转网页
  - # 回到顶部 or 占位符
  - #id id是元素的唯一标识
  - javascript:; 占位符
```
form 表单  
input 输入  
button 按钮

列表
```html
列表可以互相嵌套
<ul></ul> unordered-list  
<ol></ol> ordered-list  
<li></li> list item
<dl></dl> description list 定义列表
<dt></dt> Description Term element
<dd></dd> Description Details element  
```

small
kbd keyboard  

```html
<video src="" controls autoplay></video> 视频  
<audio src="" controls autoplay></audio> 音频
controls 播放控制组件
autoplay 但是浏览器为了用户体验，不允许自动播放
loop 循环
<audio controls>
  请升级浏览器！
  <source src="">
</audio>
```

```html
<iframe src="" frameborder="0"></iframe> 内联框架：引入其他页面
freamborder: 0 去掉边框

```

table  
  - border  
  - colgroup  
    - col width  
  - th head  
  - tb body  
  - tf foot  
    - tr row  
      - td data  
section 章节
nav navigation bar
      
---

```
<img src="#" alt="logo"/>
alt = alternative 二选一的：图片无法加载时显示，而且会被搜索引擎收录。
src:
  - 路径：相对 or 绝对
  - 网站路径：删除或者版权问题
  - base64 编码内容
width 
height
  - 单位：px 像素
  - 指定一个时会等比例缩放
格式：
  - jpeg(jpg) 颜色丰富，不支持动图、透明 -> 照片
  - gif 颜色少，支持动图、透明 -> 动图
  - png 颜色丰富，支持复杂透明，不支持动图 -> 网页
  - webp 具备所有优点，同时很小，谷歌网页图片格式，兼容性差。
  - base64 和网页一起加载的图片，加载速度快。
```

---

- 除了 div 和 span，其他标签都有默认样式
- MDN： div mdn

---

html 中不能直接书写一些特殊符号，需要使用html实体(转义字符)
语法：&name;
- nbsp 空格
- gt 大于
- lt 小于
- copy 版权保护
[html 实体](https://www.w3school.com.cn/html/html_entities.asp)
