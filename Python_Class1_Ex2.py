from snmp_helper import snmp_get_oid, snmp_extract

COMMUNITY_STRING = 'galileo'
IP = '50.242.94.227'

a_device = (IP, COMMUNITY_STRING, 7961)
b_device = (IP, COMMUNITY_STRING, 8061)

OID= ('1.3.6.1.2.1.1.1.0','1.3.6.1.2.1.1.5.0')

for device in (a_device, b_device):
    for oid in OID:
        snmp_data_rtr = snmp_get_oid(device, oid)
        output_rtr = snmp_extract(snmp_data_rtr)
        print output_rtr
