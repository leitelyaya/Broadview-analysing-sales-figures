# 任务认领与完成情况

Todo list
2018-01-08
1) 群主会加群内每一个人，了解大家擅长的技术、从事的工作、学习的目标、遇到的困难等，请大家积极配合。
大家的反馈非常重要，我会收集起来，以后会针对性地设计技术议题，促进大家共同进步

进度：
2018-01-07
1) 群内讨论了关于分布式计算的可能性，博海提出了"区块链+人工智能"的设想
2) 制定了新的群标签规则，"擅长领域+城市+昵称"
3) 群内有探讨OpenCV在大图内快速识别小图的算法
4) 分配了分析书籍信息的任务给@tc，承诺周二给成果
（另有详细总结，只对贡献者和捐赠者开放）


2018-01-07
1) 群内讨论，以节约计算资源为目标，分布式计算可行性方案，可以预见的困难是本地机器内网穿透的问题，需要测试
具体参考：https://github.com/leitelyaya/Broadview-analysing-sales-figures/blob/master/docs/purchase.md
2) 需要帮手维护Github文档，头疼格式和图床，原图：https://pan.baidu.com/s/1b8aiIi
3) 拉天使投资，设计合理的回报机制，暂时想到针对贡献者和捐赠者提供设计选型分析、BUG处理心得等文档资源。
4) 欢迎扩散和捐赠，谢谢。
5) 分析目标页面的结构，记录链接规则，记录数据格式，分析有可能的困难（Javascript、验证码等）
6) 分布式爬虫任务系统设计，技术选型
7) 阿里云各接口测试
8) 类似Disconf的Python配置管理选型
9) 群内收集，制作调查问卷，例如最近买的技术书籍是什么名字，出版社，什么时候，是否看完，学习难度，交流反馈是否通畅，是否不能坚持等等...

进度：
2018-01-06
我们确定抓取京东、亚马逊、当当出版书籍销售数据和评论数据，放在阿里云中统一管理，服务器资源是自费，可能会有些抠门。昨天我们讨论了几个方面：
1) 数据维度，书籍的介绍、书籍封面颜色、排序情况、评论内容
2) 数据存储方案，使用mongodb或者是mysql
3) 数据抓取方案，Scapy, 正则&PyQuery，八爪鱼等。在谈到抓取数据会被拦截的问题，讨论使用分布式抓取的方案。