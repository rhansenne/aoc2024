# I'm sure there is a much cleaner/simpler solution to this problem, but I approached this as follows:
# Binary addition makes use of full and half adders as explained here:
# https://bjc.edc.org/bjc-r/cur/programming/6-computers/optional-projects/2-adder.html
# So each output wire represents either a (half or full adder) sum, a (half or full adder) carry or an 
# intermediate carry (which together with the half adder carry serves as input for the full adder carry calculation).
# By recursively checking the logic (starting with the z-wire outputs) we can identify which
# input wires or gates are not consistent with the expected logic. This indicates where swaps have
# taken place.
inp,logic=open('input.txt', 'r').read().split('\n\n')
rules={}
swapped=set()

for l in logic.split('\n'):
    s=l.split(' ')
    in1,op,in2,out=s[0],s[1],s[2],s[4]
    rules[out]=[in1,op,in2]

def isXY(wire):
    return wire[1:].isdigit()

def checktype(output,expected):
    rule=rules[output]
    in1,op,in2=rule[0],rule[1],rule[2]    
    match(expected):
        case 'ha_sum':
            if not (isXY(in1) and op=='XOR' and isXY(in2)):
                return False            
        case 'ha_carry':
            if not (isXY(in1) and op=='AND' and isXY(in2)):
                return False
        case 'fa_carry':
            if not (not isXY(in1) and op=='OR' and not isXY(in2)):
                return False
        case 'interm_carry':
            if not (not isXY(in1) and op=='AND' and not isXY(in2)):
                return False
        case 'fa_sum':
            if not (not isXY(in1) and op=='XOR' and not isXY(in2)):
                return False
    return True

def validate_inputs(in1,in2,exp1,exp2): #boolean logic is commutative, so check both variations 
    if checktype(in1,exp1) and checktype(in2,exp2):
        validate(in1,exp1)
        validate(in2,exp2)
    elif checktype(in1,exp2) and checktype(in2,exp1):                
        validate(in1,exp2)
        validate(in2,exp1)
    elif checktype(in1,exp1): #input 2 is inconsistent with expected input
        validate(in1,exp1)
        swapped.add(in2)
    elif checktype(in1,exp2): #input 2 is inconsistent with expected input
        validate(in1,exp2)
        swapped.add(in2)
    elif checktype(in2,exp1): #input 1 is inconsistent with expected input
        validate(in2,exp1)
        swapped.add(in1)
    elif checktype(in2,exp2): #input 1 is inconsistent with expected input
        validate(in2,exp2)
        swapped.add(in1)
    else: #both inputs are inconsistent with expected input
        swapped.add(in1)
        swapped.add(in2)  

def validate(output,expected):
    rule=rules[output]
    in1,op,in2=rule[0],rule[1],rule[2]    
    match(expected):
        case 'ha_sum':
            if not checktype(output,'ha_sum'):
                swapped.add(output)            
        case 'ha_carry':
            if not checktype(output,'ha_carry'):
                swapped.add(output)            
        case 'fa_carry':
            if not checktype(output,'fa_carry'):
                swapped.add(output)            
            else:
                validate_inputs(in1,in2,'interm_carry','ha_carry')
        case 'interm_carry':
            if not checktype(output,'interm_carry'):
                swapped.add(output)            
            else:
                if rules[in1][0][1:]=='00' or rules[in1][1][1:]=='00':
                    validate_inputs(in1,in2,'ha_carry','ha_sum') #interim carry for second to last bit takes half adder instead of full adder carry        
                else:
                    validate_inputs(in1,in2,'fa_carry','ha_sum')        
        case 'fa_sum':
            if not checktype(output,'fa_sum'):
                swapped.add(output)            
            else:
                if rules[in1][0][1:]=='00' or rules[in1][1][1:]=='00':
                    validate_inputs(in1,in2,'ha_carry','ha_sum') #full adder sum for second to last bit takes half adder instead of full adder carry
                else:
                    validate_inputs(in1,in2,'fa_carry','ha_sum')
                    
for k in sorted(rules.keys()):    
    if k[0]=='z':
        if (k[1:]=='00'):
            validate('z00','ha_sum') #last result bit does not depend on previous carry
        elif (k[1:]=='45'):
            validate('z45','fa_carry') #first result bit only depends on previous full adder carry
        else:
            validate(k,'fa_sum') #intermediate bits are the full adder sum

print(','.join(swapped))