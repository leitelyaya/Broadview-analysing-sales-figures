# 爬虫实践

1) 从远端etcd服务，监听任务队列，获得"任务"
> 任务格式如下：
```
{
    "type": "dangdang-list|dangdang-book|...",
    "url": "链接",
    "coverImage": "cover.jpg",
    "classify": "分类",
    "index": "列表页中的排名",
    "pageNo": "列表中的第几页"
}
```

2) 任务type说明：

名称 | 说明
---|---
dangdang-list | 当当网列表页面处理程序
dangdang-book | 当当网书籍页面处理程序
jd-list | 京东列表页面分析处理程序
jd-book | 京东书籍页面处理程序
amazon-list | 亚马逊列表页面处理程序
amazon-book | 亚马逊书籍页面处理程序

3) 分析网页，如果是列表页，需要把"任务"(要抓的书籍页)回传到远端etcd任务列表里
4) 抓取的网页结果，使用[Callback方式上传](https://help.aliyun.com/document_detail/31989.html)
> Callback的回调地址是"分析程序"(即etcd服务)
5) 存储目录格式
> "/<网站名>/<书名>.json"
> 内容格式如下：

```
{
    "coverImage": "cover.jpg",
    "classify": "分类",
    "index": "列表页中的排名",
    "pageNo": "列表中的第几页",
    "content": "html内容"
}
```

