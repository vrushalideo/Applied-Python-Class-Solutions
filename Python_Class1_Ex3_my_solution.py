import snmp_helper

COMMUNITY_STRING = 'galileo'
IP = '50.242.94.227'

snmp_device = (IP, COMMUNITY_STRING, 8061)

oid_values = []

# oids = (Running Config Last Changed, Running Config Last Saved)

oids = ('1.3.6.1.4.1.9.9.43.1.1.1.0', '1.3.6.1.4.1.9.9.43.1.1.2.0')

sys_Uptime = snmp_helper.snmp_get_oid(snmp_device,oid = '1.3.6.1.2.1.1.3.0')
Output_sys_Uptime = snmp_helper.snmp_extract(sys_Uptime)

Start_Up_Last_Changed = snmp_helper.snmp_get_oid(snmp_device,oid = '1.3.6.1.4.1.9.9.43.1.1.3.0')
Output_Start_Up_Last_Changed = snmp_helper.snmp_extract(Start_Up_Last_Changed)

if int(Output_Start_Up_Last_Changed) == 0:
    print "Start-up Config has not been saved since last boot"

for oid in oids:
    running_config = snmp_helper.snmp_get_oid(snmp_device, oid = oid)
    output_running_config=snmp_helper.snmp_extract(running_config)
    oid_values.append(output_running_config)

print oid_values

if int(oid_values[0]) > int(oid_values[1]):
   print "The running-config has NOT been saved!"
else:
    print "The running-config has been saved at", int(oid_values[1])
