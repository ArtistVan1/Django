from django.shortcuts import render
from django.http import HttpResponse
#处理http请求的代码
# Create your views here.
def listorders(request):
    return HttpResponse("下面是系统的所有订单")

def listorders1(request):
    return HttpResponse("下面是系统的所有订单111")


def listorders2(request):
    return HttpResponse("下面是系统的所有订单222")

def listorders3(request):
    return HttpResponse("下面是系统的所有订单333")

from common.models import Customer

# 先定义好HTML模板
html_template = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
table {
    border-collapse: collapse;
}
th, td {
    padding: 8px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}
</style>
</head>
    <body>
        <table>
        <tr>
        <th>id</th>
        <th>姓名</th>
        <th>电话号码</th>
        <th>地址</th>
        </tr>

        %s


        </table>
    </body>
</html>
'''


def listcustomers(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Customer.objects.values()

    # 检查url中是否有参数phonenumber
    ph = request.GET.get('phonenumber', None)

    # 如果有，添加过滤条件
    if ph:
        qs = qs.filter(phonenumber=ph)

    # 生成html模板中要插入的html片段内容
    tableContent = ''
    for customer in qs:
        tableContent += '<tr>'

        for name, value in customer.items():
            tableContent += f'<td>{value}</td>'

        tableContent += '</tr>'

    return HttpResponse(html_template % tableContent)
