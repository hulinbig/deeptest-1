# coding=utf-8

'''
json是javascript object notation的简写，是一种轻量级的数据交换格式，易于阅读和编写，是目前前后端最常用的数据交互格式之一。


标准库

在Python中，提供了标准的json库来对json串进行解码和编码解析。

常用的函数如下

json.dumps
将python对象编码成json字符串, 返回json串

json.loads
将已编码的json串解码为python对象，返回python对应的数据类型

下面我们看下python对象和json类型的转化对照表:

Python类型	         Json
字典dict	             object
list列表、tuple元组	 array
str字符串	             string
int、long、float	     number
True	             true
False	             false
None	             null
'''

import json

if __name__ == "__main__":
    print("字典和json互转示例")
    json_str = '{"name":"开源优测","url":"testingunion.com","id":"DeepTest"}'
    # 类型
    print("原类型:", type(json_str))

    # 转换为 json
    json_dict = json.loads(json_str)
    print("转换后的类型为 :", type(json_dict))
    for k, v in json_dict.items():
        print(k, ":", v)
    print("------json转换为字典示例-------")

    json_dict = {"name": "开源优测", "url": "testingunion.com", "id": "DeepTest"}
    print("原类型:", type(json_dict))
    json_str = json.dumps(json_dict)
    print("转换后的类型为 :", type(json_str))
    print(json_str)

    # 高级实例
    print("-------->>>>json串解析高级实例")
    json_demo = """
          {
              "weixin": [
                  {
                      "name": "开源优测",
                      "uid": "DeepTest",
                      "desc": "分享开源测试技术"
                  },
                  {
                      "name": "开源优测_demo",
                      "uid": "DeepTest_demo",
                      "desc": "分享开源测试技术_demo"
                  }
              ],
              "web": [
                  {
                      "url": "www.testingunion.com",
                      "name": "开源优测社区",
                      "desc": "分享各类开源测试技巧"
                  },
                  {
                      "url": "www.testingunion.com_demo",
                      "name": "开源优测社区_demo",
                      "desc": "分享各类开源测试技巧_demo"
                  }
              ]
          }
      """
    # json字符串转换为json
    json_dict = json.loads(json_demo)

    # 遍历字典
    for (k, v) in json_dict.items():
        # 输出第一层级, k 为 weixin、 web;  v 为 其对应的列表即 [] 中的数据
        print(k, " : ", v)
        for data in v:
            # 遍历列表
            # v 为 []
            for (data_k, data_v) in data.items():
                # 每个data为[]中的一个字典
                # 遍历列表中的字典
                print("    ", data_k, " : ", data_v)