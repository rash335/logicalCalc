from django.shortcuts import render
from django.http import JsonResponse
from json import dumps
from django.views.decorators.csrf import csrf_exempt
from . import functions

# Create your views here.
def homepage(res):
    return render(res, 'homepage.html')

def bitArithmetic(res):
    return render(res, 'bitArithmetic.html')

def bitShiftRotate(res):
    return render(res,'bitShiftRotate.html')

def baseConversions(res):
    return render(res, 'baseConversions.html')    

def bitShift(res):
    return render(res,'bitShift.html')

def bitRotate(res):
    return render(res, 'bitRotate.html')

def logicalOperations(res):
    return render(res,'logicalOperations.html')

def calculation(req):
    num1 = int( req.POST.get('num1') );
    num2 = int( req.POST.get('num2') );
    num3 = int( req.POST.get('num3') );
    data = {
        "num1": num1, "num2":num2, "num3":num3, "num4":num1+num2-num3,
    }
    return JsonResponse(data)



def changeBinary(req):
    binary = req.POST.get('stringVal');
    bits = int(req.POST.get('bits'));
    operand = (req.POST.get('operand'));
    deci = functions.binary_decimal_signed(binary,bits)
    if operand=='Add': deci+=1;
    elif operand=='Sub': deci-=1;
    binary = functions.decimal_binary_signed(deci,bits)
    data = {'changedValue':binary}
    return JsonResponse(data)

def changeHexa(req):
    hexa = req.POST.get('stringVal');
    bits = int(req.POST.get('bits'));
    operand = (req.POST.get('operand'));
    deci = functions.hexa_decimal_signed(hexa,bits)
    if operand=='Add': deci+=1;
    elif operand=='Sub': deci-=1;
    hexa = functions.decimal_hexa_signed(deci,bits)
    data = {'changedValue':hexa}
    return JsonResponse(data)


def allconversions(req):
    dec = int(req.POST.get('decstr'));
    binstr = req.POST.get('binstr');
    hexstr = req.POST.get('hexstr');
    bits = int(req.POST.get('bits'));
    decbinS = functions.decimal_binary_signed(dec,bits)
    dechexS = functions.decimal_hexa_signed(dec,bits)
    bindecS = functions.binary_decimal_signed(binstr,bits)
    binhexS = functions.binary_hexa_signed(binstr,bits)
    hexdecS = functions.hexa_decimal_signed(hexstr,bits)
    hexbinS = functions.hexa_binary_signed(hexstr,bits)
    decbinUS = functions.decimal_binary_unsigned(dec,bits)
    dechexUS = functions.decimal_hexa_unsigned(dec,bits)
    bindecUS = functions.binary_decimal_unsigned(binstr,bits)
    binhexUS = functions.binary_hexa_unsigned(binstr,bits)
    hexdecUS = functions.hexa_decimal_unsigned(hexstr,bits)
    hexbinUS = functions.hexa_binary_unsigned(hexstr,bits)
    data={'decbinS':decbinS,'dechexS':dechexS,'bindecS':bindecS,'binhexS':binhexS,'hexdecS':hexdecS,'hexbinS':hexbinS,
            'decbinUS':decbinUS,'dechexUS':dechexUS,'bindecUS':bindecUS,'binhexUS':binhexUS,'hexdecUS':hexdecUS,'hexbinUS':hexbinUS}
    return JsonResponse(data);

def allShiftings(req):
    decstr = int(req.POST.get('decstr'));
    binstr = req.POST.get('binstr');
    hexstr = req.POST.get('hexstr');
    bits = int(req.POST.get('bits'));

    decshift = (req.POST.get('decshift'));
    binshift = (req.POST.get('binshift'));
    hexshift = (req.POST.get('hexshift'));

    decpos = int(req.POST.get('decpos'));
    binpos = int(req.POST.get('binpos'));
    hexpos = int(req.POST.get('hexpos'));

    print('data received: ', decstr, binstr, hexstr, bits)
    print('shifting are: ', decshift, binshift, hexshift)
    print('positions are: ', decpos, binpos, hexpos)
    print('the num in range is: ',functions.getNumInRange(decstr,bits))

    if decshift=="Right":        bin1 = functions.shiftDecimalRight(decstr,bits,decpos)
    elif decshift=="Left":        bin1 = functions.shiftDecimalLeft(decstr,bits,decpos)
    ShftDecDec = functions.binary_decimal_unsigned(bin1,bits)
    ShftDecBin = bin1
    ShftDecHex = functions.binary_hexa_unsigned(bin1,bits)
    
    if binshift=="Right":        bin1 = functions.shiftBinaryRight(binstr,bits,binpos)
    elif binshift=="Left":        bin1 = functions.shiftBinaryLeft(binstr,bits,binpos)
    ShftBinDec = functions.binary_decimal_unsigned(bin1,bits)
    ShftBinBin = bin1
    ShftBinHex = functions.binary_hexa_unsigned(bin1,bits)
    
    if hexshift=="Right":        bin1 = functions.shiftHexaRight(hexstr,bits,hexpos)
    elif hexshift=="Left":        bin1 = functions.shiftHexaLeft(hexstr,bits,hexpos)
    ShftHexDec = functions.binary_decimal_unsigned(bin1,bits)
    ShftHexBin = bin1
    ShftHexHex = functions.binary_hexa_unsigned(bin1,bits)

    # print('decimal input is: ',decstr,' and to be shifted ', decshift,' by ',decpos,' bits')
    # print( ShftDecDec, ShftDecBin, ShftDecHex )
    # print('binary input is: ',binstr,' and to be shifted ', binshift,' by ',binpos,' bits')
    # print(ShftBinDec, ShftBinBin, ShftBinHex)
    # print('hexa input is: ',hexstr,' and to be shifted ', hexshift,' by ',hexpos,' bits')
    # print( ShftHexDec,ShftHexBin, ShftHexHex )


    data={'ShftDecDec':ShftDecDec,'ShftDecBin':ShftDecBin, 'ShftDecHex':ShftDecHex,
        'ShftBinDec':ShftBinDec,'ShftBinBin':ShftBinBin, 'ShftBinHex':ShftBinHex,
        'ShftHexDec':ShftHexDec,'ShftHexBin':ShftHexBin, 'ShftHexHex':ShftHexHex,}
    return JsonResponse(data)

def allRotatings(req):
    decstr = int(req.POST.get('decstr'));
    binstr = req.POST.get('binstr');
    hexstr = req.POST.get('hexstr');
    bits = int(req.POST.get('bits'));

    decrotate = (req.POST.get('decRotate'));
    binrotate = (req.POST.get('binRotate'));
    hexrotate = (req.POST.get('hexRotate'));

    decpos = int(req.POST.get('decpos'));
    binpos = int(req.POST.get('binpos'));
    hexpos = int(req.POST.get('hexpos'));

    # print('DATA RECEIVED: ', decstr, binstr, hexstr, bits)
    # print('ROTATINGS ARE: ', decrotate, binrotate, hexrotate)
    # print('POSITIONS ARE: ', decpos, binpos, hexpos)

    if decrotate=="Right":        bin1 = functions.rotateDecimalRight(decstr,bits,decpos)
    elif decrotate=="Left":        bin1 = functions.rotateDecimalLeft(decstr,bits,decpos)
    RotDecDec = functions.binary_decimal_unsigned(bin1,bits)
    RotDecBin = bin1
    RotDecHex = functions.binary_hexa_unsigned(bin1,bits)
    
    if binrotate=="Right":        bin1 = functions.rotateBinaryRight(binstr,bits,binpos)
    elif binrotate=="Left":        bin1 = functions.rotateBinaryLeft(binstr,bits,binpos)
    RotBinDec = functions.binary_decimal_unsigned(bin1,bits)
    RotBinBin = bin1
    RotBinHex = functions.binary_hexa_unsigned(bin1,bits)
    
    if hexrotate=="Right":        bin1 = functions.rotateHexaRight(hexstr,bits,hexpos)
    elif hexrotate=="Left":        bin1 = functions.rotateHexaLeft(hexstr,bits,hexpos)
    RotHexDec = functions.binary_decimal_unsigned(bin1,bits)
    RotHexBin = bin1
    RotHexHex = functions.binary_hexa_unsigned(bin1,bits)


    data={'RotDecDec':RotDecDec,'RotDecBin':RotDecBin, 'RotDecHex':RotDecHex,
        'RotBinDec':RotBinDec,'RotBinBin':RotBinBin, 'RotBinHex':RotBinHex,
        'RotHexDec':RotHexDec,'RotHexBin':RotHexBin, 'RotHexHex':RotHexHex,}
    return JsonResponse(data)


def allArithmetic(req):
    dec1 = int(req.POST.get('dec1'));
    bin1 = req.POST.get('bin1');
    hex1 = req.POST.get('hex1');
    dec2 = int(req.POST.get('dec2'));
    bin2 = req.POST.get('bin2');
    hex2 = req.POST.get('hex2');
    bits = int(req.POST.get('bits'));

    decArth = (req.POST.get('decArth'));
    binArth = (req.POST.get('binArth'));
    hexArth = (req.POST.get('hexArth'));

    if decArth == '+':  dec = functions.decimalAdd(dec1,dec2,bits)
    if decArth == '-':  dec = functions.decimalSubtract(dec1,dec2,bits)
    if decArth == '*':  dec = functions.decimalmultiply(dec1,dec2,bits)
    if decArth == '/':  dec = functions.decimalDivide(dec1,dec2,bits)
    ArthDecDec = dec;
    ArthDecBin = functions.decimal_binary_signed(dec,bits)
    ArthDecHex = functions.decimal_hexa_signed(dec,bits)

    if binArth == '+':  dec = functions.binaryAdd(bin1,bin2,bits)
    if binArth == '-':  dec = functions.binarySubtract(bin1,bin2,bits)
    if binArth == '*':  dec = functions.binarymultiply(bin1,bin2,bits)
    if binArth == '/':  dec = functions.binaryDivide(bin1,bin2,bits)
    ArthBinDec = dec;
    ArthBinBin = functions.decimal_binary_signed(dec,bits)
    ArthBinHex = functions.decimal_hexa_signed(dec,bits)

    if hexArth == '+':  dec = functions.hexAdd(hex1,hex2,bits)
    if hexArth == '-':  dec = functions.hexSubtract(hex1,hex2,bits)
    if hexArth == '*':  dec = functions.hexmultiply(hex1,hex2,bits)
    if hexArth == '/':  dec = functions.hexDivide(hex1,hex2,bits)
    ArthHexDec = dec;
    ArthHexBin = functions.decimal_binary_signed(dec,bits)
    ArthHexHex = functions.decimal_hexa_signed(dec,bits)

    data={'ArthDecDec':ArthDecDec,'ArthDecBin':ArthDecBin, 'ArthDecHex':ArthDecHex,
        'ArthBinDec':ArthBinDec,'ArthBinBin':ArthBinBin, 'ArthBinHex':ArthBinHex,
        'ArthHexDec':ArthHexDec,'ArthHexBin':ArthHexBin, 'ArthHexHex':ArthHexHex,}
    return JsonResponse(data)