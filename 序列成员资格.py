database = [ 
 	['hx' ,  '192'],
 	['yh' ,  '111'],
 	['lyn',  '321']
]
username = raw_input('User name: ')
pin = raw_input("PIN code: ")

if [username,pin] in database: print 'Access granted'