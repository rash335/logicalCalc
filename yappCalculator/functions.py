def getNumInRange(num,bits):
    rangeMin = -2**(bits-1)
    rangeMax = 2**(bits-1)-1
    while (num>rangeMax):
        num = num-2**bits;
    while (num<rangeMin):
        num = num+2**bits;
    return num

def formatBinary(binary, bits):
    string=''; string1=''
    for item in binary: string += str(item);  # list to string
    for i in range(0, len(string)):
        string1+=string[i]
        if ((i+1)%4==0) and i<(bits-1):
            string1+=' '
    return string1

def formatHex(Hex, bits):
    string=''; string1=''
    for item in Hex: string += str(item);     # list to string
    for i in range(0, len(string)):
        string1+=string[i]
        if ((i+1)%2==0) and i<(bits-1):
            string1+=' '
    return string1

def remainderHex(num):
    if num==10: return 'A';
    elif num==11: return 'B';
    elif num==12: return "C";
    elif num==13: return 'D';
    elif num==14: return 'E';
    elif num==15: return 'F';
    else: return num;

def alpha2numeric(hexa):
    if hexa=='A': return 10;
    elif hexa=="B": return 11;
    elif hexa=="C": return 12;
    elif hexa=="D": return 13;
    elif hexa=="E": return 14;
    elif hexa=="F": return 15;
    else: return int(hexa);


##############################################################################################################################
################################################################ ALL SIGNED CONVERSIONS FROM ONE BASE TO ANOTHER BASE
##############################################################################################################################
def decimal_binary_signed(num,bits):
    num = getNumInRange(num,bits);
    if num<0: num = num + 2**bits;
    quotient=0; remainder=0; i=0; bin_num=[];
    while i<bits:
        quotient = int(num/2);
        remainder = num - 2*quotient;
        num = quotient;
        i=i+1;
        bin_num.append(remainder);
        binary = formatBinary(bin_num[::-1], bits)
    return binary

def decimal_hexa_signed(num,bits):
    num = getNumInRange(num,bits);
    if num<0: num = num + 2**bits;
    quotient=0; remainder=0; i=0; hexa_num=[];
    while i<bits/4:
        quotient = int(num/16);
        remainder = num - 16*quotient;
        num = quotient;
        i=i+1;
        remainder = remainderHex(remainder);
        hexa_num.append(remainder);
        hexa = formatHex(hexa_num[::-1],bits/4)
    return hexa

def binary_decimal_signed(binary,bits):
    binary = binary.replace(' ','')
    x=''; numlen = len(binary)
    if numlen < bits:
        for i in range(0,bits-numlen): x+='0'
    x=x+binary;    binary=x;
    
    rangeMin = -2**(bits-1);    rangeMax = 2**(bits-1)-1
    num=0; i=0; exp=bits-1;
    while i<bits:
        num = num + 2**exp * int(binary[i]);
        exp = exp-1;
        i=i+1;
        
    while (num>rangeMax):        num = num-2**bits;
    while (num<rangeMin):        num = num+2**bits;
    return num


def hexa_decimal_signed(hexa,bits):
    hexa = hexa.replace(' ','')
    totalpos = int(bits/4)
    hexa = hexa.replace(' ','')
    x=''; numlen = len(hexa)
    if numlen < totalpos:
        for i in range(0,totalpos-numlen): x+='0'
    x=x+hexa;    hexa=x;
    
    rangeMin = -2**(bits-1);    rangeMax = 2**(bits-1)-1
    num=0; i=0; exp = totalpos - 1;
    while i<bits/4:
        hex1 = alpha2numeric(hexa[i].upper())
        num = num + 16**exp * hex1;
        exp = exp-1;
        i+=1;
    while (num>rangeMax):        num = num-2**bits;
    while (num<rangeMin):        num = num+2**bits;
    return num


def binary_hexa_signed(binary,bits):
    binary = binary.replace(' ','')
    deci = binary_decimal_signed(binary,bits)
    return decimal_hexa_signed(deci,bits)

def hexa_binary_signed(hexa,bits):
    hexa = hexa.replace(' ','')
    deci = hexa_decimal_signed(hexa,bits)
    return decimal_binary_signed(deci,bits)

### SIGNED CONVERSIONS FUNCTIONS END HERE

##############################################################################################################################
################################################################ UNSIGNED CONVERSIONS
##############################################################################################################################
def getInRange(num,bits):
    rangeMin = 0
    rangeMax = 2**(bits)-1
    while (num>rangeMax):        num = num-2**bits;
    while (num<rangeMin):        num=0;
    return num


def decimal_binary_unsigned(num,bits):
    num = getInRange(num,bits);
    quotient=0; remainder=0; i=0; bin_num=[];
    while i<bits:
        quotient = int(num/2);
        remainder = num - 2*quotient;
        num = quotient;        i=i+1;
        bin_num.append(remainder);
        binary = formatBinary(bin_num[::-1], bits)
    return binary

def decimal_hexa_unsigned(num,bits):
    num = getInRange(num,bits);
    quotient=0; remainder=0; i=0; hexa_num=[];
    while i<bits/4:
        quotient = int(num/16);
        remainder = num - 16*quotient;
        num = quotient;
        i=i+1;
        remainder = remainderHex(remainder);
        hexa_num.append(remainder);
        hexa = formatHex(hexa_num[::-1],bits/4)
    return hexa


def binary_decimal_unsigned(binary,bits):
    binary = binary.replace(' ','')
    x=''; numlen = len(binary)
    if numlen < bits:
        for i in range(0,bits-numlen): x+='0'
    x=x+binary;    binary=x;
    
    rangeMin = 0;    rangeMax = 2**(bits)-1
    num=0; i=0; exp=bits-1;
    while i<bits:
        num = num + 2**exp * int(binary[i]);
        exp = exp-1;
        i=i+1;
        
    while (num>rangeMax):        num = num-2**bits;
    while (num<rangeMin):        num = 0
    return num



def hexa_decimal_unsigned(hexa,bits):
    hexa = hexa.replace(' ','')
    totalpos = int(bits/4)
    hexa = hexa.replace(' ','')
    x=''; numlen = len(hexa)
    if numlen < totalpos:
        for i in range(0,totalpos-numlen): x+='0'
    x=x+hexa;    hexa=x;
    
    rangeMin = 0;    rangeMax = 2**(bits)-1;
    num=0; i=0; exp = totalpos - 1;
    while i<bits/4:
        hex1 = alpha2numeric(hexa[i].upper())
        num = num + 16**exp * hex1;
        exp = exp-1;
        i+=1;
    while (num>rangeMax):        num = num-2**bits;
    while (num<rangeMin):        num = 0
    return num


def binary_hexa_unsigned(binary,bits):
    binary = binary.replace(' ','')
    deci = binary_decimal_unsigned(binary,bits)
    return decimal_hexa_unsigned(deci,bits)

def hexa_binary_unsigned(hexa,bits):
    hexa = hexa.replace(' ','')
    deci = hexa_decimal_unsigned(hexa,bits)
    return decimal_binary_unsigned(deci,bits)

### UNSIGNED CONVERSIONS END HERE




##############################################################################################################################
############################################################### ALL SHIFT OPERATIONS
##############################################################################################################################
def shiftBinaryRight(binary,bits,pos):
    binout=''; binary=binary.replace(' ','')
    x=''; numlen = len(binary)
    if numlen < bits:
        for i in range(0,bits-numlen): x+='0'
    x=x+binary;    binary=x;
    for i in range(0,pos):
        binout+='0'
    for i in range(pos,bits):
        binout+=binary[i-pos]
    binout = formatBinary(binout, bits)
    return binout

def shiftBinaryLeft(binary,bits,pos):
    binout='';    binary=binary.replace(' ','')
    x=''; numlen = len(binary)
    if numlen < bits:
        for i in range(0,bits-numlen): x+='0'
    x=x+binary;    binary=x;
    for i in range(0,bits-pos):
        binout+=binary[i+pos]
    for i in range(bits-pos,bits):
        binout+='0'
    binout = formatBinary(binout, bits)
    return binout

def shiftDecimalRight(num, bits, pos):
    binary = decimal_binary_signed(num,bits);
    return shiftBinaryRight(binary,bits,pos)
def shiftDecimalLeft(num, bits, pos):
    binary = decimal_binary_signed(num,bits);
    return shiftBinaryLeft(binary,bits,pos)
def shiftHexaRight(hexa,bits,pos):
    binary = hexa_binary_unsigned(hexa,bits)
    return shiftBinaryRight(binary,bits,pos)
def shiftHexaLeft(hexa,bits,pos):
    binary = hexa_binary_unsigned(hexa,bits)
    return shiftBinaryLeft(binary,bits,pos)
##############################################################################################################################
############################################################### ALL ROTATE OPERATIONS
##############################################################################################################################
def rotateBinaryRight(binary,bits,pos):
    binout='';    binary=binary.replace(' ','')
    x=''; numlen = len(binary)
    if numlen < bits:
        for i in range(0,bits-numlen): x+='0'
    x=x+binary;    binary=x;    
    for i in range(0,pos):
        binout+=binary[bits-pos+i]
    for i in range(pos,bits):
        binout+=binary[i-pos]
    binout = formatBinary(binout, bits)
    return binout

def rotateBinaryLeft(binary,bits,pos):
    binout='';    binary=binary.replace(' ','')
    x=''; numlen = len(binary)
    if numlen < bits:
        for i in range(0,bits-numlen): x+='0'
    x=x+binary;    binary=x;    
    for i in range(0,bits-pos):
        binout+=binary[i+pos]
    for i in range(bits-pos,bits):
        binout+=binary[i-(bits-pos)]
    binout = formatBinary(binout, bits)
    return binout

def rotateDecimalRight(num, bits, pos):
    binary = decimal_binary_signed(num,bits);
    return rotateBinaryRight(binary,bits,pos)
def rotateDecimalLeft(num, bits, pos):
    binary = decimal_binary_signed(num,bits);
    return rotateBinaryLeft(binary,bits,pos)
def rotateHexaRight(hexa,bits,pos):
    binary = hexa_binary_unsigned(hexa,bits)
    return rotateBinaryRight(binary,bits,pos)
def rotateHexaLeft(hexa,bits,pos):
    binary = hexa_binary_unsigned(hexa,bits)
    return rotateBinaryLeft(binary,bits,pos)
### SHIFT AND ROTATE OPERATIONS END HERE



####################################################################################################################
################################################## ALL ARITHMETIC OPERATIONS START HERE
####################################################################################################################
def decimalAdd(dec1,dec2,bits):
    return getNumInRange(dec1+dec2,bits)
def decimalSubtract(dec1,dec2,bits):
    return getNumInRange(dec1-dec2,bits)
def decimalmultiply(dec1,dec2,bits):
    return getNumInRange(dec1*dec2,bits)
def decimalDivide(dec1,dec2,bits):
    return getNumInRange(int(dec1/dec2),bits)


def binaryAdd(bin1, bin2, bits):
    dec1 = binary_decimal_signed(bin1,bits)
    dec2 = binary_decimal_signed(bin2,bits)
    out = getNumInRange(dec1+dec2,bits)
    return out

def binarySubtract(bin1, bin2, bits):
    dec1 = binary_decimal_signed(bin1,bits)
    dec2 = binary_decimal_signed(bin2,bits)
    out = getNumInRange(dec1-dec2,bits)
    return out

def binaryMultiply(bin1, bin2, bits):
    dec1 = binary_decimal_signed(bin1,bits)
    dec2 = binary_decimal_signed(bin2,bits)
    out = getNumInRange(dec1*dec2,bits)
    return out

def binaryDivide(bin1, bin2, bits):
    dec1 = binary_decimal_signed(bin1,bits)
    dec2 = binary_decimal_signed(bin2,bits)
    out = getNumInRange(int(dec1/dec2),bits)
    return out



def hexAdd(hex1,hex2,bits):
    dec1 = hexa_decimal_signed(hex1,bits)
    dec2 = hexa_decimal_signed(hex2,bits)
    dec = getNumInRange(dec1 + dec2,bits)
    return dec

def hexSubtract(hex1,hex2,bits):
    dec1 = hexa_decimal_signed(hex1,bits)
    dec2 = hexa_decimal_signed(hex2,bits)
    dec = getNumInRange(dec1 - dec2,bits)
    return dec

def hexMultiply(hex1,hex2,bits):
    dec1 = hexa_decimal_signed(hex1,bits)
    dec2 = hexa_decimal_signed(hex2,bits)
    dec = getNumInRange(dec1 * dec2,bits)
    return dec

def hexDivide(hex1,hex2,bits):
    dec1 = hexa_decimal_signed(hex1,bits)
    dec2 = hexa_decimal_signed(hex2,bits)
    dec = getNumInRange(int(dec1 / dec2),bits)
    return dec
####################################################################################################################
################################################## ALL ARITHMETIC OPERATIONS END HERE
####################################################################################################################


####################################################################################################################
################################################## ALL LOGICAL OPERATIONS START HERE
####################################################################################################################
def decimalORR(dec1,dec2,bits):
    dec1 = getNumInRange(dec1,bits);
    dec2 = getNumInRange(dec2,bits);
    res = dec1 | dec2;
    return res

def decimalAND(dec1,dec2,bits):
    dec1 = getNumInRange(dec1,bits);
    dec2 = getNumInRange(dec2,bits);
    res = dec1 & dec2;
    return res 

def decimalXOR(dec1,dec2,bits):
    dec1 = getNumInRange(dec1,bits);
    dec2 = getNumInRange(dec2,bits);
    res = dec1 ^ dec2;
    return res

def decimalNOT(dec1,bits):
    dec1 = -1*dec1 - 1;
    return dec1
########################################################
def binaryORR(bin1,bin2,bits):
    dec1 = binary_decimal_signed(bin1,bits);
    dec2 = binary_decimal_signed(bin2,bits);
    return decimal_binary_signed(dec1 | dec2,bits)

def binaryAND(bin1,bin2,bits):
    dec1 = binary_decimal_signed(bin1,bits);
    dec2 = binary_decimal_signed(bin2,bits);
    return decimal_binary_signed(dec1 & dec2,bits)

def binaryXOR(bin1,bin2,bits):
    dec1 = binary_decimal_signed(bin1,bits);
    dec2 = binary_decimal_signed(bin2,bits);
    return decimal_binary_signed(dec1 ^ dec2,bits)

def binaryNOT(bin1,bits):
    dec1 = binary_decimal_signed(bin1,bits);
    dec1 = -1 * dec1 - 1;
    return decimal_binary_signed(dec1,bits)
########################################################
def hexaORR(bin1,bin2,bits):
    dec1 = hexa_decimal_signed(bin1,bits);
    dec2 = hexa_decimal_signed(bin2,bits);
    return decimal_hexa_signed(dec1 | dec2,bits)

def hexaAND(bin1,bin2,bits):
    dec1 = hexa_decimal_signed(bin1,bits);
    dec2 = hexa_decimal_signed(bin2,bits);
    return decimal_hexa_signed(dec1 & dec2,bits)

def hexaXOR(bin1,bin2,bits):
    dec1 = hexa_decimal_signed(bin1,bits);
    dec2 = hexa_decimal_signed(bin2,bits);
    return decimal_hexa_signed(dec1 ^ dec2,bits)

def hexaNOT(bin1,bits):
    dec1 = hexa_decimal_signed(bin1,bits);
    dec1 = -1 * dec1 - 1;
    return decimal_hexa_signed(dec1,bits)
