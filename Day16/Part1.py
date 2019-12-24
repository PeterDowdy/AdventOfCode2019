import numpy as np
base_pattern = [0,1,0,-1]
inputvalue = np.array([int(x) for x in "59762677844514231707968927042008409969419694517232887554478298452757853493727797530143429199414189647594938168529426160403829916419900898120019486915163598950118118387983556244981478390010010743564233546700525501778401179747909200321695327752871489034092824259484940223162317182126390835917821347817200000199661513570119976546997597685636902767647085231978254788567397815205001371476581059051537484714721063777591837624734411735276719972310946108792993253386343825492200871313132544437143522345753202438698221420628103468831032567529341170616724533679890049900700498413379538865945324121019550366835772552195421407346881595591791012185841146868209045"])

expanded_patterns = np.empty((len(inputvalue),len(inputvalue)), 'int8')
for x in range(0,len(inputvalue)):
    expanded_pattern = np.concatenate((
        np.repeat(base_pattern[0],x+1),
        np.repeat(base_pattern[1],x+1),
        np.repeat(base_pattern[2],x+1),
        np.repeat(base_pattern[3],x+1)
        ))
    expanded_pattern = np.tile(expanded_pattern,1+int(len(inputvalue)/len(expanded_pattern)))
    expanded_patterns[x]= expanded_pattern[1:len(inputvalue)+1]

pattern_matrix = np.stack((expanded_patterns)).astype('int8')
print(pattern_matrix)
def phase(inputvalue, inputpattern):
    outrix = np.multiply(inputpattern,inputvalue)
    return [abs(int(x))%10 for x in np.sum(outrix,axis=1)]

output = inputvalue
for x in range(0,100):
    #print(f'cycle {x}')
    output = phase(np.stack((len(inputvalue)*[output])),pattern_matrix)

print(''.join([str(x) for x in output[0:8]]))
pass