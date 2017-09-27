import xmltodict
import json
import requests 
from collections import OrderedDict 

r = requests.get('http://www.gatikwe.com/webservices/GatiKWEDktTrack.jsp?p1=169280845&p2=EE19F2E45374D26A')
print "hello"
data = xmltodict.parse(r.text)
length = (len(data['Gatiresponse']['dktinfo']['TRANSIT_DTLS']['ROW']))
jsondata=OrderedDict()
lst = []

tagdict = {
    'DKTAD': 'InTransit',
    'ECPS': 'InTransit',
    'EOUS': 'InTransit',
    'TCADO': 'InTransit',
    'TCSOU': 'InTransit',
    'TCSEO': 'InTransit',
    'TCAER': 'InTransit',
    'DKTRED': 'InTransit',

    'DPDCC': 'OutForDelivery',
    'DUNDL': 'AttemptFail',
    'DDLVD': 'Delivered',

    'ACP': 'Returned',
    'PAC': 'Returned',
    'REJ': 'Returned',
    'RPOP': 'Returned',
    'POP': 'Returned',
    'RCN': 'Returned',
    'CAN': 'Returned',

    'DDITS': 'Exeception',
    'DSITS': 'Exeception',
    'DPITS': 'Exeception',
    'DLITS': 'Exeception',
   
}





for i in range(length):
    
    jsondata = {

    "message":data['Gatiresponse']['dktinfo']['TRANSIT_DTLS']['ROW'][i]['INTRANSIT_STATUS'],
    "courier_slug": "gati-kwe",
    "location": data['Gatiresponse']['dktinfo']['TRANSIT_DTLS']['ROW'][i]['INTRANSIT_LOCATION'],
    "trackingNumber": data['Gatiresponse']['dktinfo']['DOCKET_NUMBER'],
    "tag":  data['Gatiresponse']['dktinfo']['TRANSIT_DTLS']['ROW'][i]['INTRANSIT_STATUS_CODE'] ,
    "checkpoint_time":data['Gatiresponse']['dktinfo']['TRANSIT_DTLS']['ROW'][i]['INTRANSIT_DATE'] + "  "+ data['Gatiresponse']['dktinfo']['TRANSIT_DTLS']['ROW'][i]['INTRANSIT_TIME'],
                         
    
} 

    
    for i, j in tagdict.items():      
     if i == jsondata["tag"]:
    	jsondata["tag"]=j
    lst.append(jsondata) 
    
with open('data1.json', 'a') as f:
  jsondata=json.dumps(lst, f, indent=4)
  f.write(jsondata + '\n')
   

