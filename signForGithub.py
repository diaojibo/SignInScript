f = open('signChange')
state = f.readline()
f.close()
fo = open('signChange','w')
if state == 'true':
    new_state = 'false'
else:
    new_state = 'true'
fo.write(new_state)
fo.close()
