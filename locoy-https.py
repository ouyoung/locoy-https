from http.server import BaseHTTPRequestHandler, HTTPServer  # 导入HTTP处理相关模块
import requests
import webbrowser as web


# 自定义http服务器配置
class HTTPHandler(BaseHTTPRequestHandler):
    # 处理GET请求
    def do_GET(self):
        uri = self.path  # 获取地址参数，入参格式：http://127.0.0.1:8000/?url=https://httpbin.org/ip
        try:
            url = uri.split("?url=")[-1]
            try:
                source = get_html(url)
            except:
                source = "获取html代码出错"
        except:
            source = "网址解析错误：{}".format(uri)

        self.protocal_version = 'HTTP/1.1'  # 设置协议版本
        self.send_response(200)  # 设置响应状态码
        self.send_header("", "")  # 设置响应头
        self.end_headers()
        self.wfile.write(bytes(source, "utf-8"))  # 输出响应内容


# 对实际网址进行requests请求源码
def get_html(url):
    # 自定请求头
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "cookie": "",
        "accept-encoding": "gzip, deflate"
    }
    try:
        r = requests.get(url, headers=headers, timeout=10)
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "请求失败：{}，请输入正确的请求网址!".format(url)


# http服务启动配置
def start_server(port):
    http_server = HTTPServer(('', int(port)), HTTPHandler)
    print("------------------------------------------------------------")
    print("[ https代理请求脚本 ]")
    print("请求前缀：{}{}{}".format("http://127.0.0.1:", port, "?url="))
    print("访问示例：{}{}{}".format("http://127.0.0.1:", port, "?url=https://httpbin.org/ip"))
    doc = ""  # 教程地址
    print("火车头免费规则QQ群：836864369")
    print("使用教程：{}".format(doc))
    print("-------------------------------------------------------------")
    # web.open(doc)
    http_server.serve_forever()  # 设置一直监听并接收请求


if __name__ == '__main__':
    start_server(8000)
