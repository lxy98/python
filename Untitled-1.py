import requests
import json
import urllib

def getSogouImag(category,length,path):
    n = length
    cate = category
    imgs = requests.get('http://op.hanhande.net/shtml/op_wz/list_2602_2.shtml/channel/getAllRecomPicByTag.jsp?category='+cate+'&tag=%E5%85%A8%E9%83%A8&start=0&len='+str(n))
    jd = json.loads(imgs.text)
    jd = jd['all_items']
    imgs_url = []
    for j in jd:
        imgs_url.append(j['bthumbUrl'])
    m = 0
    for img_url in imgs_url:
            print('***** '+str(m)+'.jpg *****'+'   Downloading...')
            urllib.request.urlretrieve(img_url,path+str(m)+'.jpg')
            m = m + 1
    print('Download complete!')
    #  d:/download/壁纸/
getSogouImag('壁纸',2000,'E:/picture/')