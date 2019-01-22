import urllib.request
import re
import requests
from fake_useragent import UserAgent

url = 'https://book.douban.com/latest?icn=index-latestbook-all'
base_url = url + '1' + '/'
print(base_url)
ua = UserAgent()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
}
req = urllib.request.Request(base_url, headers=headers)
resp = urllib.request.urlopen(req)
html_content = resp.read().decode('utf-8')
print(html_content)


html_content ="""
<!DOCTYPE html>
<html lang="zh-cmn-Hans" class="ua-windows ua-webkit book-new-nav">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>新书速递</title>
  
<script>!function(e){var o=function(o,n,t){var c,i,r=new Date;n=n||30,t=t||"/",r.setTime(r.getTime()+24*n*60*60*1e3),c="; expires="+r.toGMTString();for(i in o)e.cookie=i+"="+o[i]+c+"; path="+t},n=function(o){var n,t,c,i=o+"=",r=e.cookie.split(";");for(t=0,c=r.length;t<c;t++)if(n=r[t].replace(/^\s+|\s+$/g,""),0==n.indexOf(i))return n.substring(i.length,n.length).replace(/\"/g,"");return null},t=e.write,c={"douban.com":1,"douban.fm":1,"google.com":1,"google.cn":1,"googleapis.com":1,"gmaptiles.co.kr":1,"gstatic.com":1,"gstatic.cn":1,"google-analytics.com":1,"googleadservices.com":1},i=function(e,o){var n=new Image;n.onload=function(){},n.src="https://www.douban.com/j/except_report?kind=ra022&reason="+encodeURIComponent(e)+"&environment="+encodeURIComponent(o)},r=function(o){try{t.call(e,o)}catch(e){t(o)}},a=/<script.*?src\=["']?([^"'\s>]+)/gi,g=/http:\/\/(.+?)\.([^\/]+).+/i;e.writeln=e.write=function(e){var t,l=a.exec(e);return l&&(t=g.exec(l[1]))?c[t[2]]?void r(e):void("tqs"!==n("hj")&&(i(l[1],location.href),o({hj:"tqs"},1),setTimeout(function(){location.replace(location.href)},50))):void r(e)}}(document);
</script>

  
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="Sun, 6 Mar 2005 01:00:00 GMT">
  
  <script>var _head_start = new Date();</script>
  
  <link href="https://img3.doubanio.com/f/book/e7612a013a5e76c7c680323c74748d21cd703ba0/css/book/master.css" rel="stylesheet" type="text/css">

  <link href="https://img3.doubanio.com/f/book/222a5c61e041638af8defc87cf97f4a863a77922/css/book/base/init.css" rel="stylesheet">
  <style type="text/css"></style>
  <script src="https://img3.doubanio.com/f/book/0495cb173e298c28593766009c7b0a953246c5b5/js/book/lib/jquery/jquery.js"></script>
  <script src="https://img3.doubanio.com/f/book/7d36c07b1b7a7a386c3bff538ae46d9d0f0990a0/js/book/master.js"></script>
  

  
    <link href="https://img3.doubanio.com/f/book/4471ade48d89ae0783c90521b6659dc8fda29f55/css/book/express-more.css" rel="stylesheet"/>

  <script> 
    $(function(){
        var $win = $(window),
        t = $('.article h2').offset().top;
        isShowFixTop();
        $win.on('scroll', function() {
            isShowFixTop();
        });
        function isShowFixTop() {
            if ($win.scrollTop() > t) {
                $('.fixTop').show()
            }else{
                $('.fixTop').hide()
            }
        }
    })
 </script>
  <!-- COLLECTED CSS -->

  <link rel="shortcut icon" href="https://img3.doubanio.com/favicon.ico" type="image/x-icon">
</head>
<body>
  
    <script>var _body_start = new Date();</script>
    
  



    <link href="//img3.doubanio.com/dae/accounts/resources/984c231/shire/bundle.css" rel="stylesheet" type="text/css">



<div id="db-global-nav" class="global-nav">
  <div class="bd">
    
<div class="top-nav-info">
  <a href="https://www.douban.com/accounts/login?source=book" class="nav-login" rel="nofollow">登录</a>
  <a href="https://www.douban.com/accounts/register?source=book" class="nav-register" rel="nofollow">注册</a>
</div>


    <div class="top-nav-doubanapp">
  <a href="https://www.douban.com/doubanapp/app?channel=top-nav" class="lnk-doubanapp">下载豆瓣客户端</a>
  <div id="doubanapp-tip">
    <a href="https://www.douban.com/doubanapp/app?channel=qipao" class="tip-link">豆瓣 <span class="version">6.0</span> 全新发布</a>
    <a href="javascript: void 0;" class="tip-close">×</a>
  </div>
  <div id="top-nav-appintro" class="more-items">
    <p class="appintro-title">豆瓣</p>
    <p class="qrcode">扫码直接下载</p>
    <div class="download">
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=iOS">iPhone</a>
      <span>·</span>
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=Android" class="download-android">Android</a>
    </div>
  </div>
</div>

    


<div class="global-nav-items">
  <ul>
    <li class="">
      <a href="https://www.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-main&quot;,&quot;uid&quot;:&quot;0&quot;}">豆瓣</a>
    </li>
    <li class="on">
      <a href="https://book.douban.com"  data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-book&quot;,&quot;uid&quot;:&quot;0&quot;}">读书</a>
    </li>
    <li class="">
      <a href="https://movie.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-movie&quot;,&quot;uid&quot;:&quot;0&quot;}">电影</a>
    </li>
    <li class="">
      <a href="https://music.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-music&quot;,&quot;uid&quot;:&quot;0&quot;}">音乐</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/location" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-location&quot;,&quot;uid&quot;:&quot;0&quot;}">同城</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/group" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-group&quot;,&quot;uid&quot;:&quot;0&quot;}">小组</a>
    </li>
    <li class="">
      <a href="https://read.douban.com&#47;?dcs=top-nav&amp;dcm=douban" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-read&quot;,&quot;uid&quot;:&quot;0&quot;}">阅读</a>
    </li>
    <li class="">
      <a href="https://douban.fm&#47;?from_=shire_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-fm&quot;,&quot;uid&quot;:&quot;0&quot;}">FM</a>
    </li>
    <li class="">
      <a href="https://time.douban.com&#47;?dt_time_source=douban-web_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-time&quot;,&quot;uid&quot;:&quot;0&quot;}">时间</a>
    </li>
    <li class="">
      <a href="https://market.douban.com&#47;?utm_campaign=douban_top_nav&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-market&quot;,&quot;uid&quot;:&quot;0&quot;}">豆品</a>
    </li>
    <li>
      <a href="#more" class="bn-more"><span>更多</span></a>
      <div class="more-items">
        <table cellpadding="0" cellspacing="0">
          <tbody>
            <tr>
              <td>
                <a href="https://ypy.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-ypy&quot;,&quot;uid&quot;:&quot;0&quot;}">豆瓣摄影</a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </li>
  </ul>
</div>

  </div>
</div>
<script>
  ;window._GLOBAL_NAV = {
    DOUBAN_URL: "https://www.douban.com",
    N_NEW_NOTIS: 0,
    N_NEW_DOUMAIL: 0
  };
</script>



    <script src="//img3.doubanio.com/dae/accounts/resources/984c231/shire/bundle.js" defer="defer"></script>




  



    <link href="//img3.doubanio.com/dae/accounts/resources/19507ad/book/bundle.css" rel="stylesheet" type="text/css">




<div id="db-nav-book" class="nav">
  <div class="nav-wrap">
  <div class="nav-primary">
    <div class="nav-logo">
      <a href="https:&#47;&#47;book.douban.com">豆瓣读书</a>
    </div>
    <div class="nav-search">
      <form action="https:&#47;&#47;book.douban.com/subject_search" method="get">
        <fieldset>
          <legend>搜索：</legend>
          <label for="inp-query">
          </label>
          <div class="inp"><input id="inp-query" name="search_text" size="22" maxlength="60" placeholder="书名、作者、ISBN" value=""></div>
          <div class="inp-btn"><input type="submit" value="搜索"></div>
          <input type="hidden" name="cat" value="1001" />
        </fieldset>
      </form>
    </div>
  </div>
  </div>
  <div class="nav-secondary">
    

<div class="nav-items">
  <ul>
    <li    ><a href="https://book.douban.com/cart/"
     >购书单</a>
    </li>
    <li    ><a href="https://read.douban.com/ebooks/?dcs=book-nav&dcm=douban"
            target="_blank"
     >电子图书</a>
    </li>
    <li    ><a href="https://market.douban.com/book?utm_campaign=book_nav_freyr&utm_source=douban&utm_medium=pc_web"
     >豆瓣书店</a>
    </li>
    <li    ><a href="https://book.douban.com/annual/2017?source=navigation"
            target="_blank"
     >2017年度榜单</a>
    </li>
    <li    ><a href="https://book.douban.com/standbyme/2017?source=navigation"
            target="_blank"
     >2017读书报告</a>
    </li>
    <li          class=" book-cart"
    ><a href="https://market.douban.com/cart/?biz_type=book&utm_campaign=book_nav_cart&utm_source=douban&utm_medium=pc_web"
            target="_blank"
     >购物车</a>
    </li>
  </ul>
</div>

  </div>
</div>

<script id="suggResult" type="text/x-jquery-tmpl">
  <li data-link="{{= url}}">
            <a href="{{= url}}" onclick="moreurl(this, {from:'book_search_sugg', query:'{{= keyword }}', subject_id:'{{= id}}', i: '{{= index}}', type: '{{= type}}'})">
            <img src="{{= pic}}" width="40" />
            <div>
                <em>{{= title}}</em>
                {{if year}}
                    <span>{{= year}}</span>
                {{/if}}
                <p>
                {{if type == "b"}}
                    {{= author_name}}
                {{else type == "a" }}
                    {{if en_name}}
                        {{= en_name}}
                    {{/if}}
                {{/if}}
                 </p>
            </div>
        </a>
        </li>
  </script>




    <script src="//img3.doubanio.com/dae/accounts/resources/19507ad/book/bundle.js" defer="defer"></script>





    <div id="wrapper">
        
        
    <div id="content">
        <h1>新书速递</h1>
        <div class="grid-12-12 clearfix">
            

    <div class="fixTop">
        <h2 class="fleft">虚构类  · · · · · · </h2>
        <h2 class="fright">非虚构类  · · · · · · </h2>
    </div>
    <div class="article">
    <h2>虚构类  · · · · · · </h2>
    <ul class="cover-col-4 clearfix">
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30366534/"><img src="https://img3.doubanio.com/view/subject/m/public/s29917601.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30366534/">熊镇</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small  color-lightgray">
                                
                        </span>
                    </p>
                    <p class="color-gray">
                        [瑞典] 弗雷德里克·巴克曼 / 四川文艺出版社 / 2018-12
                    </p>
                    <p class="detail">
                        一个女孩遭遇性侵，整个小镇都在袒护罪犯。《一个叫欧维的男人决定去死》《外婆的道歉信》《清单人生》作者新作。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30382687/"><img src="https://img3.doubanio.com/view/subject/m/public/s29927081.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30382687/">度外</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small  color-lightgray">
                                
                        </span>
                    </p>
                    <p class="color-gray">
                        黄国峻 / 后浪丨四川人民出版社 / 2018-12
                    </p>
                    <p class="detail">
                        黄国峻的短篇小说集。运用实验性的文字，探寻小说艺术的新可能。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30285035/"><img src="https://img3.doubanio.com/view/subject/m/public/s29928015.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30285035/">蜜蜂与远雷</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small  color-lightgray">
                                
                        </span>
                    </p>
                    <p class="color-gray">
                        [日]恩田陆 / 中国友谊出版公司 / 2018-12
                    </p>
                    <p class="detail">
                        三年一度的芳江钢琴比赛开幕，具备不同身份和天赋的参赛者们在此邂逅。直木奖＋书店大奖“双冠王”作品。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30364975/"><img src="https://img3.doubanio.com/view/subject/m/public/s29921692.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30364975/">吃麻雀的少女</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small  color-lightgray">
                                
                        </span>
                    </p>
                    <p class="color-gray">
                        朱一叶 / 北京出版集团北京十月文艺出版社 / 2018-12
                    </p>
                    <p class="detail">
                        家里又来了客人，爸爸照例端上了一盘油炸小麻雀。可我并不想吃麻雀，因为我的小伙伴东东告诉我，他死去的爸爸变成了麻雀。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30276249/"><img src="https://img3.doubanio.com/view/subject/m/public/s29922145.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30276249/">长路</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar45"></span> 
                        <span class="font-small  color-lightgray">
                                9.0
                        </span>
                    </p>
                    <p class="color-gray">
                        [美] 科马克·麦卡锡 / 理想国丨九州出版社 / 2018-11
                    </p>
                    <p class="detail">
                        不知名的灾难让世界成了废墟。一对父子推着装满食物与生存装备的手推车前行，往南方海岸寻找一线生路。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30338153/"><img src="https://img3.doubanio.com/view/subject/m/public/s29938524.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30338153/">景恒街</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small  color-lightgray">
                                
                        </span>
                    </p>
                    <p class="color-gray">
                        笛安 / 北京十月文艺出版社 / 2019-1
                    </p>
                    <p class="detail">
                        景恒街是北京CBD附近的一条街道，也是主人公关景恒的名字。笛安新作。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30368773/"><img src="https://img3.doubanio.com/view/subject/m/public/s29923201.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30368773/">神奇动物：格林德沃之罪</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar40"></span> 
                        <span class="font-small  color-lightgray">
                                8.0
                        </span>
                    </p>
                    <p class="color-gray">
                        [英] J·K·罗琳 / 人民文学出版社 / 2018-11-16
                    </p>
                    <p class="detail">
                        J.K.罗琳创作的“神奇动物”系列电影第二部剧本。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30283373/"><img src="https://img3.doubanio.com/view/subject/m/public/s29910765.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30283373/">I窃星</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar40"></span> 
                        <span class="font-small  color-lightgray">
                                8.1
                        </span>
                    </p>
                    <p class="color-gray">
                        [英] 阿瑟·克拉克 / 安·范德米尔 / 杰夫·范德米尔 / 北京联合出版公司 / 2018-11
                    </p>
                    <p class="detail">
                        收录了20世纪初到20世纪50年代之间的25篇科幻作品，作者包括艾萨克•阿西莫夫、阿瑟•克拉克、菲利普•迪克等。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30344739/"><img src="https://img3.doubanio.com/view/subject/m/public/s29908761.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30344739/">她跟我聊到枫树、水的微笑以及永恒</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar45"></span> 
                        <span class="font-small  color-lightgray">
                                9.0
                        </span>
                    </p>
                    <p class="color-gray">
                        [法] 安东尼·帕耶 / 北京联合出版公司 / 2018-11
                    </p>
                    <p class="detail">
                        在大多数人看来，26岁的亚历山大·克劳诺斯无疑过着令人羡慕的生活。他却觉得自己从没有真正存在过。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30385318/"><img src="https://img1.doubanio.com/view/subject/m/public/s29929579.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30385318/">鲤·时间胶囊</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small  color-lightgray">
                                评价人数不足
                        </span>
                    </p>
                    <p class="color-gray">
                        张悦然 主编 / 理想国 | 九州出版社 / 2018-11
                    </p>
                    <p class="detail">
                        内容包括：24位作家和文化人预言他们眼中的文学的未来。“匿名作家计划”第二辑。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/27614658/"><img src="https://img3.doubanio.com/view/subject/m/public/s29895376.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/27614658/">当代俄罗斯小说集</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small  color-lightgray">
                                评价人数不足
                        </span>
                    </p>
                    <p class="color-gray">
                        [俄]麦列霍夫等 / 上海译文出版社 / 2018-11
                    </p>
                    <p class="detail">
                         汇集当代俄罗斯文学优秀作品。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30357179/"><img src="https://img1.doubanio.com/view/subject/m/public/s29906087.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30357179/">310上海异人故事</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small  color-lightgray">
                                
                        </span>
                    </p>
                    <p class="color-gray">
                        王莫之 / 上海文艺出版社 / 2018-11
                    </p>
                    <p class="detail">
                        小说描写的对象是身份证前三位数字为“310”的人，也就是上海人。十三篇关于上海遗梦的短篇小说。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30314829/"><img src="https://img1.doubanio.com/view/subject/m/public/s29940587.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30314829/">爱你，西蒙</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small  color-lightgray">
                                评价人数不足
                        </span>
                    </p>
                    <p class="color-gray">
                        [美]贝奇·艾伯特利 / 上海三联书店 / 2018-12
                    </p>
                    <p class="detail">
                        如果世界不喜欢你本来的样子，你是否依旧敢于做自己？同名热门电影《爱你，西蒙》原著小说。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30331243/"><img src="https://img3.doubanio.com/view/subject/m/public/s29910472.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30331243/">镖人</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar45"></span> 
                        <span class="font-small  color-lightgray">
                                8.6
                        </span>
                    </p>
                    <p class="color-gray">
                        许先哲 / 北京联合出版公司 / 2018-11
                    </p>
                    <p class="detail">
                        一部重现隋唐江湖的热血漫画！
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30384152/"><img src="https://img3.doubanio.com/view/subject/m/public/s29934015.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30384152/">夜里老鼠们要睡觉</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small  color-lightgray">
                                评价人数不足
                        </span>
                    </p>
                    <p class="color-gray">
                        [德]沃尔夫冈·博歇尔特 / 人民文学出版社 / 2018-11
                    </p>
                    <p class="detail">
                        沃尔夫冈·博歇尔特是二战后德国“废墟文学”的代表作家。本书收入作者的短篇小说代表作《面包》等，反映了战争对人的摧残，灾难中人性的温暖。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30365850/"><img src="https://img3.doubanio.com/view/subject/m/public/s29924104.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30365850/">喜欢就买单</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar45"></span> 
                        <span class="font-small  color-lightgray">
                                9.0
                        </span>
                    </p>
                    <p class="color-gray">
                        闻珺里 / 江苏文艺出版社 / 2018-11-15
                    </p>
                    <p class="detail">
                        两个六零后男人，他们既是这个时代的利益既得者，又都在各自的泥淖中挣扎求生。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30317421/"><img src="https://img1.doubanio.com/view/subject/m/public/s29910689.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30317421/">禁断的魔术</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small  color-lightgray">
                                
                        </span>
                    </p>
                    <p class="color-gray">
                        [日]东野圭吾 / 南海出版公司 / 2018-12
                    </p>
                    <p class="detail">
                        东野圭吾“神探伽利略”汤川学系列最新长篇小说。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30297167/"><img src="https://img1.doubanio.com/view/subject/m/public/s29852158.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30297167/">沉睡的记忆</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small  color-lightgray">
                                评价人数不足
                        </span>
                    </p>
                    <p class="color-gray">
                        [法]帕特里克·莫迪亚诺 / 人民文学出版社 / 2018-11
                    </p>
                    <p class="detail">
                        《沉睡的记忆》出版于2017年，是莫迪亚诺荣获诺贝尔文学奖之后首部作品。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30345429/"><img src="https://img3.doubanio.com/view/subject/m/public/s29924140.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30345429/">被弃养的女孩</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar45"></span> 
                        <span class="font-small  color-lightgray">
                                8.6
                        </span>
                    </p>
                    <p class="color-gray">
                        [意]多娜泰拉·迪皮耶特兰托尼奥 / 外语教学与研究出版社 / 2018-10
                    </p>
                    <p class="detail">
                        十三岁时，拥有一个温馨家庭的她突然被告知自己是个养女，必须回到亲生父母身边。她不得不告别好朋友和“家人”，开始一段别样的生活。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/28355275/"><img src="https://img1.doubanio.com/view/subject/m/public/s29879117.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/28355275/">摇摆时光</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small  color-lightgray">
                                评价人数不足
                        </span>
                    </p>
                    <p class="color-gray">
                        [英]扎迪·史密斯 / 上海译文出版社 / 2018-10
                    </p>
                    <p class="detail">
                        童年时代的好友，是否注定要渐行渐远？2017年布克奖长名单入围作品。
                    </p>
                </div>
            </li>
    </ul>
    </div>

            

    <div class="aside">
    <h2 class="pl20">非虚构类  · · · · · · </h2>
    <ul class="cover-col-4 pl20 clearfix">
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30258589/"><img src="https://img3.doubanio.com/view/subject/m/public/s29942481.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30258589/">成为母亲</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small color-lightgray">
                                评价人数不足
                        </span>
                    </p>
                    <p class="color-gray">
                        [英]蕾切尔·卡斯克(Rachel Cusk) / 上海人民出版社 / 2019-1
                    </p>
                    <p>
                        怀孕生子不仅区分了男人和女人，也区分了女人和女人。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30297160/"><img src="https://img3.doubanio.com/view/subject/m/public/s29923220.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30297160/">死于昨日世界</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small color-lightgray">
                                
                        </span>
                    </p>
                    <p class="color-gray">
                        李静睿 / 上海三联书店 / 2019-1
                    </p>
                    <p>
                        李静睿继《愿你的道路漫长》之后推出的第二本非虚构作品，记录了自己近些年的阅读心得和思想历程。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30365536/"><img src="https://img3.doubanio.com/view/subject/m/public/s29909471.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30365536/">清单</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small color-lightgray">
                                
                        </span>
                    </p>
                    <p class="color-gray">
                        [英] 肖恩•厄舍 / 广西师范大学出版社 / 2018-12
                    </p>
                    <p>
                        124张清单跨越古今，涵盖了许多历史事件，以及名人们经历的奇闻趣事。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30326080/"><img src="https://img3.doubanio.com/view/subject/m/public/s29928386.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30326080/">历史写作简明指南</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small color-lightgray">
                                评价人数不足
                        </span>
                    </p>
                    <p class="color-gray">
                        [美] 理查德·马里厄斯（RICHARD MARIUS） / [美］梅尔文·E.佩吉（MELVIN E. PAGE） / 后浪丨四川人民出版社 / 2018-12
                    </p>
                    <p>
                        本书旨在教会读者如何像历史学家一样思考和写作。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30312155/"><img src="https://img3.doubanio.com/view/subject/m/public/s29927165.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30312155/">尼安德特人</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small color-lightgray">
                                评价人数不足
                        </span>
                    </p>
                    <p class="color-gray">
                        [瑞典] 斯万特·帕博（Svante Pääbo） / 浙江教育出版社 / 2018-12
                    </p>
                    <p>
                        以现代分子手段，重探人类演化路径。在“走出非洲”与“多地起源”的学说争论之间，持续追问“人之为人”的起源、演化与未来。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30348025/"><img src="https://img3.doubanio.com/view/subject/m/public/s29918274.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30348025/">文化理论与大众文化导论</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small color-lightgray">
                                
                        </span>
                    </p>
                    <p class="color-gray">
                        [英] 约翰·斯道雷 / 北京大学出版社 / 2019-1-1
                    </p>
                    <p>
                        国际知名文化研究学者约翰斯•道雷所著之经典教材，在西方学界产生的影响经久不衰，是公认的媒介与文化研究领域最为权威的综述性著作之一。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30366602/"><img src="https://img3.doubanio.com/view/subject/m/public/s29938326.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30366602/">认知迭代</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small color-lightgray">
                                
                        </span>
                    </p>
                    <p class="color-gray">
                        【英】卡罗琳•威廉姆斯 著 / 北京日报出版社/阳光博客 / 2018-12
                    </p>
                    <p>
                        保持专注的方式就是要“拥抱波动”，学会让大脑在专注和走神这两种状态中自由切换。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/27112574/"><img src="https://img1.doubanio.com/view/subject/m/public/s29792238.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/27112574/">作家和出版人</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar45"></span> 
                        <span class="font-small color-lightgray">
                                9.1
                        </span>
                    </p>
                    <p class="color-gray">
                        [德] 西格弗里德·温塞德 / 人民文学出版社 / 2018-11
                    </p>
                    <p>
                        文学对时代的意义何为？文学出版人的职责何为？
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30223227/"><img src="https://img3.doubanio.com/view/subject/m/public/s29920471.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30223227/">莎士比亚植物志</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small color-lightgray">
                                评价人数不足
                        </span>
                    </p>
                    <p class="color-gray">
                        [英] 玛格丽特·威尔斯 / 人民文学出版社 / 2019-1-1
                    </p>
                    <p>
                        精选莎翁剧作中49种植物，从文学、历史、园艺、烹饪、医学、民俗、语言等多角度写小传，描绘出一幅生动的莎士比亚式花园图景。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30377493/"><img src="https://img1.doubanio.com/view/subject/m/public/s29923199.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30377493/">周迅·自在人间</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar45"></span> 
                        <span class="font-small color-lightgray">
                                8.8
                        </span>
                    </p>
                    <p class="color-gray">
                        周迅 x Lens / 世纪文景/上海人民出版社 / 2018-11-27
                    </p>
                    <p>
                        20多位圈内师友一起为周迅写下的“小传”，近300张摄影师私藏照片首次曝光。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30379527/"><img src="https://img3.doubanio.com/view/subject/m/public/s29923715.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30379527/">世界观（原书第2版）</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar50"></span> 
                        <span class="font-small color-lightgray">
                                9.7
                        </span>
                    </p>
                    <p class="color-gray">
                        [美]理查德·德威特 / 机械工业出版社 / 2018-11-15
                    </p>
                    <p>
                        纵论西方科学两千年，探索科学的起源和思维的本质。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30335756/"><img src="https://img3.doubanio.com/view/subject/m/public/s29946093.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30335756/">我是个怪圈</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small color-lightgray">
                                评价人数不足
                        </span>
                    </p>
                    <p class="color-gray">
                        [美]侯世达 / 中信出版集团 / 2019-1-1
                    </p>
                    <p>
                        《哥德尔、艾舍尔、巴赫》出版30年后，侯世达回到了他最有发言权的领域回答：我是什么？
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30387994/"><img src="https://img3.doubanio.com/view/subject/m/public/s29934995.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30387994/">剑桥中国经济史</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small color-lightgray">
                                评价人数不足
                        </span>
                    </p>
                    <p class="color-gray">
                        万志英 / 中国人民大学出版社 / 2018-11-30
                    </p>
                    <p>
                        作者从青铜时代写到20世纪初、视野横跨近3000年历史，他吸收现有硏究的精华，并在此基础上创作一本关于中国经济长期发展的详尽之作。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30368506/"><img src="https://img3.doubanio.com/view/subject/m/public/s29912465.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30368506/">东南园墅</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar45"></span> 
                        <span class="font-small color-lightgray">
                                9.1
                        </span>
                    </p>
                    <p class="color-gray">
                        童寯 / 浦睿文化·湖南美术出版社 / 2018-11
                    </p>
                    <p>
                        建筑界一代宗师童寯，向世界介绍中国古典园林之美的经典著作。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30376180/"><img src="https://img1.doubanio.com/view/subject/m/public/s29920478.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30376180/">激昂的幻梦</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small color-lightgray">
                                评价人数不足
                        </span>
                    </p>
                    <p class="color-gray">
                        [美] 李·斯特拉斯伯格 著 / [美] 伊万杰琳·墨菲斯 编辑整理 / 后浪丨台海出版社 / 2018-12
                    </p>
                    <p>
                        奠定方法派表演理论的开山之作。完整呈现了对当代表演艺术有着巨大影响力的方法派的训练方法与贡献。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30318643/"><img src="https://img1.doubanio.com/view/subject/m/public/s29888258.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30318643/">酗酒、猫与赞美诗</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar40"></span> 
                        <span class="font-small color-lightgray">
                                7.7
                        </span>
                    </p>
                    <p class="color-gray">
                        [美]托马斯·林奇 / 新星出版社 / 2018-10
                    </p>
                    <p>
                        作者从一位殡葬师的角度来观察人事，双重身份和幽默的冷嘲与饱含深情的叙述笔调常令人欲罢不能。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30380222/"><img src="https://img3.doubanio.com/view/subject/m/public/s29935900.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30380222/">欲望与尊严</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar40"></span> 
                        <span class="font-small color-lightgray">
                                8.4
                        </span>
                    </p>
                    <p class="color-gray">
                        肖索未 / 社会科学文献出版社 / 2018-10
                    </p>
                    <p>
                        本书以婚外包养关系为棱镜，考察市场转型期中国社会的亲密关系及其背后的情感逻辑与伦理实践。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30279065/"><img src="https://img3.doubanio.com/view/subject/m/public/s29927893.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30279065/">考古的故事</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar45"></span> 
                        <span class="font-small color-lightgray">
                                9.2
                        </span>
                    </p>
                    <p class="color-gray">
                        [美] 埃里克·H.克莱因 / 中信出版集团·新思文化 / 2018-10-20
                    </p>
                    <p>
                        真实的考古故事，比探险电影更精彩。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30359547/"><img src="https://img1.doubanio.com/view/subject/m/public/s29926878.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30359547/">写小说最重要的十件事</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small color-lightgray">
                                评价人数不足
                        </span>
                    </p>
                    <p class="color-gray">
                        [美] 厄休拉·勒古恩 / 后浪丨江西人民出版社 / 2019-1
                    </p>
                    <p>
                        本书是厄休拉•勒古恩主持“写作工作坊”时的课堂讲义，也是她多年创作及阅读经验的浓缩。
                    </p>
                </div>
            </li>
        
            <li>
                <a class="cover" href="https://book.douban.com/subject/30373807/"><img src="https://img1.doubanio.com/view/subject/m/public/s29917729.jpg"/></a>
                <div class="detail-frame">
                    <h2>
                        <a href="https://book.douban.com/subject/30373807/">有滋有味：我的厨艺人生</a>
                    </h2>
                    <p class="rating">
                        <span class="allstar00"></span> 
                        <span class="font-small color-lightgray">
                                
                        </span>
                    </p>
                    <p class="color-gray">
                        [美] 露西·尼斯利 / 后浪丨北京联合出版公司 / 2019-1
                    </p>
                    <p>
                        尼斯利用她娴熟的绘图技艺和全面的烹饪知识，将只有专业厨师才懂的烹饪技巧逐一画在纸上，就算是料理新人也可以轻松掌握！
                    </p>
                </div>
            </li>
    </ul>
    </div>

        </div>
    </div>

        
  <div id="footer">
    
<span id="icp" class="fleft gray-link">
    &copy; 2005－2018 douban.com, all rights reserved 北京豆网科技有限公司
</span>

<a href="https://www.douban.com/hnypt/variformcyst.py" style="display: none;"></a>

<span class="fright">
    <a href="https://www.douban.com/about">关于豆瓣</a>
    · <a href="https://www.douban.com/jobs">在豆瓣工作</a>
    · <a href="https://www.douban.com/about?topic=contactus">联系我们</a>
    · <a href="https://www.douban.com/about?policy=disclaimer">免责声明</a>
    
    · <a href="https://help.douban.com/?app=book" target="_blank">帮助中心</a>
    · <a href="https://book.douban.com/library_invitation">图书馆合作</a>
    · <a href="https://www.douban.com/doubanapp/">移动应用</a>
    · <a href="https://www.douban.com/partner/">豆瓣广告</a>
</span>

  </div>

    </div>
      
  

    <!-- COLLECTED JS -->
    <!-- mako -->
    
    
  

<script type="text/javascript">
  var _paq = _paq || [];
  _paq.push(['trackPageView']);
  _paq.push(['enableLinkTracking']);
  (function() {
    var p=(('https:' == document.location.protocol) ? 'https' : 'http'), u=p+'://fundin.douban.com/';
    _paq.push(['setTrackerUrl', u+'piwik']);
    _paq.push(['setSiteId', '100001']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0]; 
    g.type='text/javascript';
    g.defer=true; 
    g.async=true; 
    g.src=p+'://s.doubanio.com/dae/fundin/piwik.js';
    s.parentNode.insertBefore(g,s);
  })();
</script>

<script type="text/javascript">
var setMethodWithNs = function(namespace) {
  var ns = namespace ? namespace + '.' : ''
    , fn = function(string) {
        if(!ns) {return string}
        return ns + string
      }
  return fn
}

var gaWithNamespace = function(fn, namespace) {
  var method = setMethodWithNs(namespace)
  fn.call(this, method)
}

var _gaq = _gaq || []
  , accounts = [
      { id: 'UA-7019765-1', namespace: 'douban' }
    , { id: 'UA-7019765-16', namespace: '' }
    ]
  , gaInit = function(account) {
      gaWithNamespace(function(method) {
        gaInitFn.call(this, method, account)
      }, account.namespace)
    }
  , gaInitFn = function(method, account) {
      _gaq.push([method('_setAccount'), account.id])

      
  _gaq.push([method('_addOrganic'), 'google', 'q'])
  _gaq.push([method('_addOrganic'), 'baidu', 'wd'])
  _gaq.push([method('_addOrganic'), 'soso', 'w'])
  _gaq.push([method('_addOrganic'), 'youdao', 'q'])
  _gaq.push([method('_addOrganic'), 'so.360.cn', 'q'])
  _gaq.push([method('_addOrganic'), 'sogou', 'query'])
  if (account.namespace) {
    _gaq.push([method('_addIgnoredOrganic'), '豆瓣'])
    _gaq.push([method('_addIgnoredOrganic'), 'douban'])
    _gaq.push([method('_addIgnoredOrganic'), '豆瓣网'])
    _gaq.push([method('_addIgnoredOrganic'), 'www.douban.com'])
  }

      if (account.namespace === 'douban') {
        _gaq.push([method('_setDomainName'), '.douban.com'])
      }

        _gaq.push([method('_setCustomVar'), 1, 'responsive_view_mode', 'desktop', 3])

        _gaq.push([method('_setCustomVar'), 2, 'login_status', '0', 2]);

      _gaq.push([method('_trackPageview')])
    }

for(var i = 0, l = accounts.length; i < l; i++) {
  var account = accounts[i]
  gaInit(account)
}


;(function() {
    var ga = document.createElement('script');
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    ga.setAttribute('async', 'true');
    document.documentElement.firstChild.appendChild(ga);
})()
</script>








    <!-- anson42-docker-->

</body>
</html>































"""
pattern = re.compile(r'<div class="detail-frame">.*?<a href=".*?">.*?(.*?)</a>.*?<p class="color-gray">(.*?)</p>', re.S)
results = re.findall(pattern,html_content)
for i in results:
    book = re.sub('[\n ]', '', i[0])
    author = re.sub('[\n ]', '', i[1])
    print(f'书籍：{book}\t作者：{author}')

