网页表现
CSS 层叠样式表

引入方式：
```html
1. 内联样式 p[style=""]
<p style="color:red; font-size: 60px;">aaa</p>
2. 内部样式表 html>head>style
<html><head><style></style></head></html>
3. 外部样式表
<link rel="stylesheet" href="">
``` 

CSS 注释： /* */

选择器关系
1. 父元素：直接包含子元素的
2. 子元素：直接被父元素包含的
3. 祖先元素：直接或间接包含后代元素的，父元素也是祖先元素
4. 后代元素：直接或间接被祖先元素包含的，子元素也是后代元素
5. 兄弟元素：拥有相同父元素的

CSS 选择器
[css selectors](https://github.com/flukeout/css-diner)
1. 直接选取所有指定元素
2. id 选择器 `#id{}` 唯一
3. class 选择器 `.class{}` 可以重复, 多个 class 使用空格分隔
4. 通配选择器 `*{}`
5. 交集选择器 `选择器1选择器2选择器3{}` eg: `div.red{} a.b.c{}`
6. 并集选择器 `选择器1,选择器2{}`
7. 父子选择器 `父 > 子`
8. 后代选择器 `祖先 后代`
9. 兄弟元素选择器：只能后顾 无法前瞻
  - 下一个兄弟：`兄 + 弟` eg: `p + span{}`
  - 选择所有兄弟： `兄 ~ 弟` 
10. 属性选择器：
  - `[attr]`
  - `[attr=value]`
  - `[attr^=value]` 选择属性值以value开头的
  - `[attr$=value]` 结尾
  - `[attr*=value]` 包含
11. 伪类选择器：
伪类即某个特殊状态的类，比如：第一个、被点击的、偶数的、鼠标移入的元素  
伪类是根据所有子元素进行排序的
  - :xxx 伪类
    - 不同类型
      - :only-child select any element that is the only element inside if another one.
      - :first-child
      - :last-child
      - :nth-last-child() like nth-child, but counting from the back!
      - :nth-child()
        - :nth-child(\d) 选中第n个
        - :nth-child(n) 全选
        - :nth-child(2n) or :nth-child(even) 偶数
        - :nth-child(2n+1) or :nth-child(odd) 奇数
    - 同类型中
      - :only-of-type select the only element of its type within another element.
      - :first-of-type 
      - :last-of-type 
      - :nth-of-type()
        - plate:nth-of-type(2n+3) select every 2nd plate, starting from the 3rd.
    - :not() 否定伪类
      - ul > li:not(:nth-child(3)){} : ul 子元素中除了第三个的所有 li
    - :link 没访问过的链接
    - :visited 访问过的链接，**由于隐私原因，visited 只支持改链接颜色**
    - :hover 鼠标移入
    - :active 鼠标点击
    - :focus 获得焦点的元素
    - :empty select elements that don't have any other elements inside of them.
12. 伪元素选择器：
伪元素即页面中特殊位置的元素
  - ::xxx
  - ::first-letter 第一个字母
  - ::first-line 第一行
  - ::selection 鼠标选中的内容
  - ::before 元素的开始 ::after 元素的结束
    - 必须结合content使用
    - 实际案例： <q></q> 加上的引号 
13. 选择器的权重 high -> low
    - !important 获取到最高优先级！
    - 内联样式
    - id选择器
    - 类和伪类选择器
    - 元素选择器
    - 通配选择器
    - 继承样式

样式继承
1. 为一个元素设置的样式会应用到它的后代元素上。
2. 把统一样式设置到共同的祖先上。
3. 背景相关，布局相关不会继承。 eg: background-color

单位
1. px：像素点，同样的200px在高清屏下会自动放大，所以显示效果不一样。
2. %：百分比，默认相对父元素的百分比。
3. em: 根据字体大小计算，1em = 1font-size, 默认16px。
4. rem：根据root元素的字体大小计算。
5. RGB：red/green/blue 浓度调配，取值 0-255 或 0%-100%。rgb(r,g,b,x)
   x 代表透明度, 0 全透明 1 不透明。
6. RGB 16 进制 #ff0000 -> 255,0,0 -> 简写：#f00
7. HSL: HSLA hsl(0, saturation, lightness);
   - H色相 0-360度，代表颜色 
   - S饱和度 颜色浓度 0-100 **%**
   - L亮度 0-100 **%** 