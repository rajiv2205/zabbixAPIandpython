from pyzabbix import ZabbixAPI

# The hostname at which the Zabbix web interface is available
ZABBIX_SERVER = 'http://10.0.132.171:8080/zabbix'

zapi = ZabbixAPI(ZABBIX_SERVER)

# Disable SSL certificate verification
zapi.session.verify = False

# Login to the Zabbix API
zapi.login('Admin', 'zabbix')

# Loop through all hosts interfaces, getting only "main" interfaces of type "agent"
for h in zapi.hostinterface.get(output=["dns","ip","useip","hostid"],selectHosts=["host"],filter={"main":1,"type":1}):
    print('Server %s has IP %s has ID %s' % (h['hosts'][0]['host'], h['ip'], h['hostid']))
