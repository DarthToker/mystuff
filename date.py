import time
x =(time.strftime("%m/%d/%Y"))
a,b,c = x.split('/')

if a == '01':
    a = 'January'

if a == '02':
    a = 'February'
    
if a == '03':
    a = 'March'
     
if a == '04':
    a = 'April'
     
if a == '05':
    a = 'May'
     
if a == '06':
    a = 'June'
     
if a == '07':
    a = 'July'
 
if a == '08':
    a = 'August'
       
if a == '09':
    a = 'September'
    
if a == '10':
    a = 'October'
    
if a == '11':
    a = 'November'
    
if a == '12':
    a = 'December'
 

print ("today's date is %s %s %s" %(a,b,c))

print "today's date is " +a +b
d,e = b

print d
print e
if d == '0':
    print e
else:
    print b
    





