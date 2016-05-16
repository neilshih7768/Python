import requests
import shutil
rs = requests.session()
res = rs.get('https://fbfh.trade.gov.tw/rich/text/common/code_98/CheckImageCode.aspx', stream=True, verify=False)
f = open('check.png', 'wb')
shutil.copyfileobj(res.raw, f)
f.close()



from IPython.display import Image
Image('check.png')



import requests

payload = {
    'queryType':'C',
    'basic_select':'2',
    'chinese_name':'台北',
    'ccc_select':'1',
    'pname_select':'1',
    'txtCheckCode':'87zgx5'
}

res = requests.post('https://fbfh.trade.gov.tw/rich/text/indexfbOL.asp', data=payload, verify=False)
res.encode = 'utf-8'
print res.text