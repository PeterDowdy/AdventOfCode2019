import numpy as np

base_pattern = [0, 1, 0, -1]
inputvalue = 10000 * [
    int(x)
    for x in "59762677844514231707968927042008409969419694517232887554478298452757853493727797530143429199414189647594938168529426160403829916419900898120019486915163598950118118387983556244981478390010010743564233546700525501778401179747909200321695327752871489034092824259484940223162317182126390835917821347817200000199661513570119976546997597685636902767647085231978254788567397815205001371476581059051537484714721063777591837624734411735276719972310946108792993253386343825492200871313132544437143522345753202438698221420628103468831032567529341170616724533679890049900700498413379538865945324121019550366835772552195421407346881595591791012185841146868209045"
]
inputlength = len(inputvalue)
targetoffset = int("".join([str(x) for x in inputvalue[0:7]]))

restricted_subset = inputvalue[targetoffset:]
restricted_subset_length = inputlength - targetoffset


# def get_pattern(sequence, inputlength):
#    segment = np.concatenate(
#        (
#            np.repeat(base_pattern[0], sequence + 1),
#            np.repeat(base_pattern[1], sequence + 1),
#            np.repeat(base_pattern[2], sequence + 1),
#            np.repeat(base_pattern[3], sequence + 1),
#        )
#    )
#    return np.tile(segment, 1 + int(inputlength / len(segment)))[(1 + sequence) : (inputlength + 1)]


# def phase(signalvalue, inputpattern):
#    return sum(signalvalue * inputpattern)


output = np.array(restricted_subset)
print("Starting", flush=True)
for x in range(0, 100):
    next = np.empty((restricted_subset_length), "int16")
    buf = 0

    for z in range(inputlength - 1, targetoffset - 1, -1):
        # this only works because I know we're so far along in the sequence that it's all ones
        buf += output[z - targetoffset]
        next[z - targetoffset] = buf % 10
    output = next
    print(f"cycle {x} completed", flush=True)
print("".join([str(x) for x in output[:8]]), flush=True)
pass
