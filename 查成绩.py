#encoding: utf-8
import urllib,urllib2,cookielib,webbrowser


#配置信息
class uestc:
    print 'input your student ID'
    ID = raw_input()
    print 'input your password'
    password = raw_input()
    login_path = "https://uis.uestc.edu.cn/amserver/UI/Login?goto=http%3A%2F%2Fportal.uestc.edu.cn%2Flogin.portal"
    def __init__(self):
        self.cj = cookielib.LWPCookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)
        self.opener.addheaders = [('User-agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36')]

    #模拟登陆
    def login(self):
        post_data = urllib.urlencode({
            'IDToken1':self.ID,
            'IDToken2':self.password,
            })
        #发起HTTP请求
        #print post_data
        request = urllib2.Request(self.login_path,post_data)
        html = self.opener.open(request).read()
        get_url = self.opener.open(request).geturl()
        if get_url == 'http://portal.uestc.edu.cn/index.portal':
            #print get_url
            #self.cj.save('uestc.cookie')
            print 'Login success !'
            
            path='http://eams.uestc.edu.cn/eams/teach/grade/course/person.action'
            webbrowser.open(path)

test=uestc()
test.login()
