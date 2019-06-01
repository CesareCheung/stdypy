import requests
# import Image
def get_demo(url,querystry):
    """
    get方法封装
    :param url: 请求url地址
    :param querystry: get传入参数
    :return:
    """

    r=requests.get(url,params=querystry)
    print(r.text)

def post_demo(url,payload):
    """
    post方法封装
    :param url: 请求地址
    :param payload: 参数
    :return:
    """
    r=requests.post(url,data=payload)
    print(r.json())

if __name__ == '__main__':
    url="http://httpbin.org/get"
    payload = {"name": "Jame"}
    get_demo(url,payload)
    url1="http://httpbin.org/post"
    payload = {"name": "Jame"}
    post_demo(url1,payload)