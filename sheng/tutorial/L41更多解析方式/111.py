from lxml import etree
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re

# url = 'http://example.python-scraping.com/places/default/view/United-States-234'
# headers = {
#     'User-Agent': UserAgent().random
# }
# response = requests.get(url=url,headers=headers)
# if not response.status_code==200:
#     raise Exception(f"请求失败,{response.status_code}")
# html_content = response.text
html_content="""
<!--[if HTML5]><![endif]-->
<!DOCTYPE html>
<!-- paulirish.com/2008/conditional-stylesheets-vs-css-hacks-answer-neither/ -->
<!--[if lt IE 7]><html class="ie ie6 ie-lte9 ie-lte8 ie-lte7 no-js" lang="en"> <![endif]-->
<!--[if IE 7]><html class="ie ie7 ie-lte9 ie-lte8 ie-lte7 no-js" lang="en"> <![endif]-->
<!--[if IE 8]><html class="ie ie8 ie-lte9 ie-lte8 no-js" lang="en"> <![endif]-->
<!--[if IE 9]><html class="ie9 ie-lte9 no-js" lang="en"> <![endif]-->
<!--[if (gt IE 9)|!(IE)]><!--> <html class="no-js" lang="en"> <!--<![endif]-->
<head>
<title>Example web scraping website</title>
  <!--[if !HTML5]>
      <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <![endif]-->
  <!-- www.phpied.com/conditional-comments-block-downloads/ -->
  <!-- Always force latest IE rendering engine
       (even in intranet) & Chrome Frame
       Remove this if you use the .htaccess -->
	   
  <meta charset="utf-8" />

  <!-- http://dev.w3.org/html5/markup/meta.name.html -->
  <meta name="application-name" content="places" />

  <!--  Mobile Viewport Fix
        j.mp/mobileviewport & davidbcalhoun.com/2010/viewport-metatag
        device-width: Occupy full width of the screen in its current orientation
        initial-scale = 1.0 retains dimensions instead of zooming out if page height > device height
        user-scalable = yes allows the user to zoom in -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <link rel="shortcut icon" href="/places/static/images/favicon.ico" type="image/x-icon">
  <link rel="apple-touch-icon" href="/places/static/images/favicon.png">

  <!-- All JavaScript at the bottom, except for Modernizr which enables
       HTML5 elements & feature detects -->
  <script src="/places/static/js/modernizr.custom.js"></script>

  <!-- include stylesheets -->
  

  <script type="text/javascript"><!--
    // These variables are used by the web2py_ajax_init function in web2py_ajax.js (which is loaded below).
    var w2p_ajax_confirm_message = "Are you sure you want to delete this object?";
    var w2p_ajax_disable_with_message = "Working...";
    var w2p_ajax_date_format = "%Y-%m-%d";
    var w2p_ajax_datetime_format = "%Y-%m-%d %H:%M:%S";
    var ajax_error_500 = 'An error occured, please <a href="/places/default/view/United-States-234">reload</a> the page'
    //--></script>

<meta name="keywords" content="web2py, python, web scraping" />
<meta name="generator" content="Web2py Web Framework" />
<meta name="author" content="Web Scraping with Python" />
<script src="/places/static/js/jquery.js" type="text/javascript"></script><link href="/places/static/css/calendar.css" rel="stylesheet" type="text/css" /><script src="/places/static/js/calendar.js" type="text/javascript"></script><script src="/places/static/js/web2py.js" type="text/javascript"></script><link href="/places/static/css/web2py.css" rel="stylesheet" type="text/css" /><link href="/places/static/css/bootstrap.min.css" rel="stylesheet" type="text/css" /><link href="/places/static/css/bootstrap-responsive.min.css" rel="stylesheet" type="text/css" /><link href="/places/static/css/style.css" rel="stylesheet" type="text/css" /><link href="/places/static/css/web2py_bootstrap.css" rel="stylesheet" type="text/css" />


  

  <!-- uncomment here to load jquery-ui
       <link rel="stylesheet" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.3/themes/ui-lightness/jquery-ui.css" type="text/css" media="all" />
       <script src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.3/jquery-ui.min.js" type="text/javascript"></script>
       uncomment to load jquery-ui //-->
  <noscript><link href="/places/static/css/web2py_bootstrap_nojs.css" rel="stylesheet" type="text/css" /></noscript>
  
</head>

<body>
  <!-- Navbar ================================================== -->
  <div class="navbar navbar-inverse">
    <div class="flash"></div>
    <div class="navbar-inner">
      <div class="container">
        
        <!-- the next tag is necessary for bootstrap menus, do not remove -->
        <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse" style="display:none;">
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        
        <ul id="navbar" class="nav pull-right"><li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" href="#" rel="nofollow">Log In</a><ul class="dropdown-menu"><li><a href="/places/default/user/register?_next=/places/default/view/United-States-234" rel="nofollow"><i class="icon icon-user glyphicon glyphicon-user"></i> Sign Up</a></li><li class="divider"></li><li><a href="/places/default/user/login?_next=/places/default/view/United-States-234" rel="nofollow"><i class="icon icon-off glyphicon glyphicon-off"></i> Log In</a></li></ul></li></ul>
        <div class="nav">
          
          <ul class="nav"><li class="web2py-menu-first"><a href="/places/default/index">Home</a></li><li class="web2py-menu-last"><a href="/places/default/search">Search</a></li></ul>
          
        </div><!--/.nav-collapse -->
      </div>
    </div>
  </div><!--/top navbar -->

  <div class="container">
    <!-- Masthead ================================================== -->
      
    <header class="mastheader row" id="header">
        <div class="span12">
            <div class="page-header">
                <h1>
                    Example web scraping website
                    <small></small>
                </h1>
            </div>
        </div>
    </header>
	

    <section id="main" class="main row">
        

        <div class="span12">
            
            

<form action="#" enctype="multipart/form-data" method="post"><table><tr id="places_flag_img__row"><td class="w2p_fl"><label class="readonly" for="places_flag_img" id="places_flag_img__label">Flag: </label></td><td class="w2p_fw"><img src="/places/static/images/flags/us.png" /></td><td class="w2p_fc"></td></tr><tr id="places_area__row"><td class="w2p_fl"><label class="readonly" for="places_area" id="places_area__label">Area: </label></td><td class="w2p_fw">9,629,091 square kilometres</td><td class="w2p_fc"></td></tr><tr id="places_population__row"><td class="w2p_fl"><label class="readonly" for="places_population" id="places_population__label">Population: </label></td><td class="w2p_fw">310,232,863</td><td class="w2p_fc"></td></tr><tr id="places_iso__row"><td class="w2p_fl"><label class="readonly" for="places_iso" id="places_iso__label">Iso: </label></td><td class="w2p_fw">US</td><td class="w2p_fc"></td></tr><tr id="places_country_or_district__row"><td class="w2p_fl"><label class="readonly" for="places_country_or_district" id="places_country_or_district__label">Country (District): </label></td><td class="w2p_fw">United States</td><td class="w2p_fc"></td></tr><tr id="places_capital__row"><td class="w2p_fl"><label class="readonly" for="places_capital" id="places_capital__label">Capital: </label></td><td class="w2p_fw">Washington</td><td class="w2p_fc"></td></tr><tr id="places_continent__row"><td class="w2p_fl"><label class="readonly" for="places_continent" id="places_continent__label">Continent: </label></td><td class="w2p_fw"><a href="/places/default/continent/NA">NA</a></td><td class="w2p_fc"></td></tr><tr id="places_tld__row"><td class="w2p_fl"><label class="readonly" for="places_tld" id="places_tld__label">Tld: </label></td><td class="w2p_fw">.us</td><td class="w2p_fc"></td></tr><tr id="places_currency_code__row"><td class="w2p_fl"><label class="readonly" for="places_currency_code" id="places_currency_code__label">Currency Code: </label></td><td class="w2p_fw">USD</td><td class="w2p_fc"></td></tr><tr id="places_currency_name__row"><td class="w2p_fl"><label class="readonly" for="places_currency_name" id="places_currency_name__label">Currency Name: </label></td><td class="w2p_fw">Dollar</td><td class="w2p_fc"></td></tr><tr id="places_phone__row"><td class="w2p_fl"><label class="readonly" for="places_phone" id="places_phone__label">Phone: </label></td><td class="w2p_fw">1</td><td class="w2p_fc"></td></tr><tr id="places_postal_code_format__row"><td class="w2p_fl"><label class="readonly" for="places_postal_code_format" id="places_postal_code_format__label">Postal Code Format: </label></td><td class="w2p_fw">#####-####</td><td class="w2p_fc"></td></tr><tr id="places_postal_code_regex__row"><td class="w2p_fl"><label class="readonly" for="places_postal_code_regex" id="places_postal_code_regex__label">Postal Code Regex: </label></td><td class="w2p_fw">^\d{5}(-\d{4})?$</td><td class="w2p_fc"></td></tr><tr id="places_languages__row"><td class="w2p_fl"><label class="readonly" for="places_languages" id="places_languages__label">Languages: </label></td><td class="w2p_fw">en-US,es-US,haw,fr</td><td class="w2p_fc"></td></tr><tr id="places_neighbours__row"><td class="w2p_fl"><label class="readonly" for="places_neighbours" id="places_neighbours__label">Neighbours: </label></td><td class="w2p_fw"><div><a href="/places/default/iso/CA">CA </a><a href="/places/default/iso/MX">MX </a><a href="/places/default/iso/CU">CU </a></div></td><td class="w2p_fc"></td></tr></table><div style="display:none;"><input name="id" type="hidden" value="743646" /></div></form>

<a href="/places/default/edit/United-States-234">Edit</a>

            
        </div>

        
    </section><!--/main-->

    <!-- Footer ================================================== -->
    <div class="row">
        <footer class="footer span12" id="footer">
        </footer>
    </div>

  </div> <!-- /container -->

  <!-- The javascript =============================================
       (Placed at the end of the document so the pages load faster) -->
  <script src="/places/static/js/bootstrap.min.js"></script>
  <script src="/places/static/js/web2py_bootstrap.js"></script>
  <!--[if lt IE 7 ]>
      <script src="/places/static/js/dd_belatedpng.js"></script>
      <script> DD_belatedPNG.fix('img, .png_bg'); //fix any <img> or .png_bg background-images </script>
      <![endif]-->
</body>
</html>

"""
# init
tree = etree.HTML(html_content)
bs = BeautifulSoup(html_content,'lxml')

# pattern

# <tr id="places_country_or_district__row">
# <td class="w2p_fl"><label class="readonly" for="places_country_or_district" id="places_country_or_district__label">
# Country (District): </label>
# </td>
# <td class="w2p_fw">
# United States</td>
# <td class="w2p_fc">
# </td>
# </tr>

# 正则
pattern_re  =re.compile(r'<tr id="places_country_or_district__row">.*?<td class="w2p_fl">.*?<td class="w2p_fw">(.*?)</td>',re.S)
re_result = pattern_re.findall(html_content)
print(re_result[0])

# xpath

print(tree.xpath('//tr[@id="places_country_or_district__row"]/td[@class="w2p_fw"]/text()')[0])

# bs
tr = bs.find(id="places_country_or_district__row")
td = tr.find('td',{'class':"w2p_fw"})
print(td)
print(td.string)




