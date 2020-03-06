#!/usr/bin/env python3
#coding=utf-8

import cgi, cgitb
import json

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalidns.request.v20150109.DescribeDomainRecordsRequest import DescribeDomainRecordsRequest
from aliyunsdkalidns.request.v20150109.UpdateDomainRecordRequest import UpdateDomainRecordRequest

form = cgi.FieldStorage()

access_key_id = form.getvalue('access_key_id')
access_secret = form.getvalue('access_secret')
dns_domain_name = form.getvalue('dns_domain_name')
dns_rr = form.getvalue('dns_rr')
dns_type = form.getvalue('dns_type')
dns_value = form.getvalue('dns_value')

client = AcsClient(access_key_id, access_secret, 'cn-hangzhou')

request = DescribeDomainRecordsRequest()
request.set_accept_format('json')
request.set_DomainName(dns_domain_name)
request.set_RRKeyWord(dns_rr)
response = client.do_action_with_exception(request)

data2 = json.loads(str(response, encoding='utf-8'))

dns_record_id = data2['DomainRecords']["Record"][0]["RecordId"]
old_value = data2['DomainRecords']["Record"][0]["Value"]

if old_value != dns_value:

    request2 = UpdateDomainRecordRequest()
    request2.set_accept_format('json')
    request2.set_Value(dns_value)
    request2.set_Type(dns_type)
    request2.set_RR(dns_rr)
    request2.set_RecordId(dns_record_id)
    response2 = client.do_action_with_exception(request2)
    # python2:  print(response)
    print(str(response2, encoding='utf-8'))
    print('Content-type:text/html')
    print('')
    print('<html>')
    print('<head>')
    print('<meta charset="utf-8">')
    print('<title>aliddns</title>')
    print('</head>')
    print('<body>')
    print('<h2>success, old_ip is %s ,new ip is %s</h2>' % (old_value, dns_value))
    print('</body>')
    print('</html>')    
else:
    print('Content-type:text/html')
    print('')
    print('<html>')
    print('<head>')
    print('<meta charset="utf-8">')
    print('<title>aliddns</title>')
    print('</head>')
    print('<body>')
    print('<h2>need not update, old_ip is %s ,new ip is %s</h2>' % (old_value, dns_value))   
    print('</body>')
    print('</html>')
