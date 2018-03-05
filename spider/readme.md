# 功能

1) 爬去当当网计算机类目所有图书
2) 支持代理随机选择
3) 支持代理ip随机选择

# 如何运行

window 安装scrapy时需要安装编译工具 cl:
https://www.visualstudio.com/53d997bd-3c36-48fb-a592-ee2eb51a09a5

1) pip install scrapy
2) cd bookinfo
3) scrapy crawl dangdangbook
4) chrome插件Xpath Helper，能快速提取xpath表达式，加速编码过程
http://bj.ddooo.com:8081/uuauth/xpathhp_109412.rar?f8c2ce1891356808d605255747d92dd1.rar


运行完毕后项目根目录出现/bookdata/data.json 为目标数据

# 目标数据格式解释
```
[
{
    "coverImage": "/h/t/t/p://img3m8.ddimg.cn/71/36/23520788-1_w_2.jpg",
    "classify": "['\u8ba1\u7b97\u673a/\u7f51\u7edc', '\u7a0b\u5e8f\u8bbe\u8ba1', '\u5176\u4ed6']",
    "index": 0, 
    "pageNo": 2,
    'content':'"html doc"',
},
{},
{},100
]
```
目标数据为一个符合Python list 数据格式的字典list最后一个数字代表图书的总数


# todo list
1) 获取所有的评论数据