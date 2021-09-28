1. mac 上如何查看帮助文档：
    tldr sed
2. 部分例子：
    sed 's/foo/bar/' test.txt # 在一行中只替换一次（首次出现
    sed -e 's/foo/bar/g' myfile.txt #替换每行中所有出现的
    sed -e '1,10s/enchantment/entrapment/g' myfile2.txt #用短语 'entrapment' 替换所有出现的短语 'enchantment'，但是只在第一到第十行（包括这两行）上这样做。
    sed -e '/^$/,/^END/s/hills/mountains/g' myfile3.txt #用 'mountains' 替换 'hills'，但是，只从空行开始，到以三个字符 'END' 开始的行结束（包括这两行）的文本块上这样做
3. 好文章：
    https://www.huaweicloud.com/articles/12e14b083723b9d9ad084f6042f68073.html
    