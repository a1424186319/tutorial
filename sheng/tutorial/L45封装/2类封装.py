# 练习

# 函数封装和类封装并没有孰优孰劣,函数封装思维自然,类封装封装程度更高,django框架函数封装,odoo框架类封装.
import requests
from lxml import etree

class Github(object):
    def __init__(self):
        # 属性公共变量 配置项 全局需要访问
        self.login_url = 'https://github.com/login'
        self.do_login_url = 'https://github.com/session'
        self.profile_url = 'https://github.com/settings/profile'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    'Host': 'github.com',
    'Referer': 'https://github.com/login'

        }
        self.s = requests.Session()


    def get_csrf_token(self):
        """
        请求表单页,获取authenticity_token(csrf token)
        :return: {str}
        """
        resp = self.s.get(self.login_url,headers=self.headers)
        html_content = resp.text
        pattern = '//input[@name="authenticity_token"]/@value'
        dom = etree.HTML(html_content)
        authenticity_token = dom.xpath(pattern)[0]
        return authenticity_token

    def dologin(self,authenticity_token):
        """
        去登陆
        :param authenticity_token: 组装请求参数所需
        :return: True
        """
        params = {
            'authenticity_token': authenticity_token,
            'login': '1424186319@qq.com',
            'password': 'Dnfwaspy15',
            'commit': 'Sign in',
            'utf8': '✓ '
        }
        resp = self.s.post(self.do_login_url,headers=self.headers, data=params)
        if resp.status_code != 200:
            print('登录成功')
        return True


    def request_profile(self):
        """
        请求个人设置页
        :return:{str}<html></html>
        """
        profile_resp = self.s.get(self.profile_url,headers=self.headers)
        if profile_resp.status_code != requests.codes.ok:
            raise Exception("请求个人设置页失败")
        return profile_resp.text

    def get_user_email(self,html_content):

        pattern_profile_email = '//select[@id="user_profile_email"]/id=[2]/text()'
        profile_dom = etree.HTML(html_content)

        profile_email = profile_dom.xpath(pattern_profile_email)[0]
        print(profile_email)

    # def get_user_name(self,html_content):
    #     # pattern_profile_email = '//select[@id="user_profile_email"]/option[2]/text()'
    #     # profile_dom = etree.HTML(html_content)
    #     #
    #     # profile_email = profile_dom.xpath(pattern_profile_email)[0]
    #     # print(profile_email)
    #
    #
    #
    #     print()





if __name__ == '__main__':
    github = Github()
    authenticity_token = github.get_csrf_token()
    github.dologin(authenticity_token)

    profile_html_content = github.request_profile()

    github.get_user_email(profile_html_content)

    github.get_user_name