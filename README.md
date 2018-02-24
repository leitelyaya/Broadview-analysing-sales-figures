# 博文视角销售数据分析

1) 目标  
> 如果从出版社的销售量和营业额来分析的话，这实际上是个策略优化问题，也就是说采用什么样的策略（或者调整其销售策略）才能使得出版社的利润最大化，我们都知道：利润 = 收入 - 成本，一本书的收入就是它的销售价格（不适定价哦，销售价格需要建立一个定价模型，需要预测一本书的市场欢迎度，受欢迎的书多生产多宣传，关注少的书少生产），一本书的成本怎么计算得咨询博文军啦。所以这个利润应该就是我们的目标函数。

2) 数据源的获取  
> 无外乎两种方式：博文军帮忙提供一些博文视点图书的数据；大家自行到各大平台进行爬去（需要说明的是爬去的动作是必须有的，因为可以爬取到读者的评论信息，这个评论信息是很重要的，而且不光是博文视点出版的图书，其它朋友出版社出版的IT类图书信息我们也要爬取到，每一个书各方面的特征都要爬到，比如是否附带光盘，图书的封面颜色等等弱信息），然后我们获取到的图书数据都是作为机器学习的训练数据，还有一个问题就是用什么信息作为机器学习的标签数据呢，这个大家得一起讨论讨论，比如销售量等等。

3) 行业数据与读者特征  
> 博文视点是出版IT相关的图书，所以原则上来讲，卖书的群体主要是以程序员和计算机类专业的学生为主，程序员主要分布在北上广，其它地方零散分布，这个可以爬去一些招聘网站的招聘数据作为数据源来分析行业和读者特征。

4) 这个应该是个预测类问题，卷积网络或者机器学习模型都可以做。

5) 图书在前端展示时候的排序问题，怎样排获益最大，也需要设计一个算法。  
> 现有方案为流量计费方案

> [任务认领与完成情况](docs/todolist.md)
> [采购分析](docs/purchase.md)

## 博文寻踪组织

![image](docs/博文寻踪群.jpg)

> 服务器实践资源有限，所有捐赠款项将用于研究工作。承诺对支持者回馈==一份特别的礼物==，一份精心准备的一手资料，内容包括但不限于所有实践过程的设计思路和踩过的坑。

![image](docs/微信收款.jpg)

