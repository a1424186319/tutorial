# excel读写
# excel是一种广泛的办公文件格式,表格形式,比csv复杂一些,带一些功能样式,适合普通用户观看,由于带功能样式,所以需要专门负责的包解析.excel后缀 老格式xls,新格式xlsx,新格式兼容老格式.
# 操作excel包选择,XlsxWriter xlrd pyexcel,start数,维护时间都较大同小异,下面以pyexcel讲解

from pyexcel_io import save_data
from pyexcel_io import get_data

data = get_data('2readfile.xlsx')
# print(type(data))
sheet1 = data['Sheet1']
# print(sheet1)
for index,row in enumerate(sheet1):
    if index <= 0:
        continue
    # print('第{}个学生,学生姓名{}'.format(index,row[1]))

# 报错
# 1.不支持格式,请安装插件pyexcel-xls
# 2.没有权限,管理员


# 写示例
# sheet1 = [
# {'name':'小明','age':'13','gender':'男'}
# {'name':'小红','age':'12','gender':'女'}
# ]

sheet2 = [['小明',13],['小李',12]]
save_data(data=sheet2,afile='2writeexcel.xlsx' )