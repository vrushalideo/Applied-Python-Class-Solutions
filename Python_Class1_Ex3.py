import snmp_helper
 
 
community_string = 'xxxxxx'
 
snmp_port = 7961
 
ip = 'x.x.x.x'
 
some_device = (ip, community_string, snmp_port)
 
#System Up Time
sysUptime = '1.3.6.1.2.1.1.3.0'
 
# Uptime when running config last changed
ccmHistoryRunningLastChanged = '1.3.6.1.4.1.9.9.43.1.1.1.0'
 
# Uptime when running config last saved (note any 'write' constitutes a save)
ccmHistoryRunningLastSaved = '1.3.6.1.4.1.9.9.43.1.1.2.0'
 
# Uptime when startup config last saved
ccmHistoryStartupLastChanged = '1.3.6.1.4.1.9.9.43.1.1.3.0'
 
snmp_sysUptime = snmp_helper.snmp_get_oid(some_device, oid=sysUptime)
snmp_run_change = snmp_helper.snmp_get_oid(some_device, oid=ccmHistoryRunningLastChanged)
snmp_run_save = snmp_helper.snmp_get_oid(some_device, oid=ccmHistoryRunningLastSaved)
snmp_start_save = snmp_helper.snmp_get_oid(some_device, oid=ccmHistoryStartupLastChanged)
 
output_sysUptime = snmp_helper.snmp_extract(snmp_sysUptime)
output_run_change = snmp_helper.snmp_extract(snmp_run_change)
output_run_save = snmp_helper.snmp_extract(snmp_run_save)
output_start_save = snmp_helper.snmp_extract(snmp_start_save)
 
 
print 'This is System Uptime'
print '============================================='
print output_sysUptime
print '\n \n'
print 'This is Run Last Changed'
print '============================================='
print output_run_change
print '\n \n'
print 'This is Run Last Saved'
print '============================================='
print output_run_save
print '\n \n'
print 'This is Start Last Saved'
print '============================================='
print output_start_save
print '\n \n'
 
if int(output_start_save) == 0:
print "The startup-config has not been saved since the last boot!"
if int(output_run_change) > int(output_run_save):
print "The running-config has NOT been saved!"
else:
print "The running-config has been saved at", int(output_run_save) 
