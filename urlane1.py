from PIL import Image, ImageDraw
#img = Image.open('Sharvan Sharma.jpg').convert('L')
#img.save('output_file.jpg')
#height and width generator
def patterndraw( wnew, hnew, wslot, hslot, img ,fac):
    x1 = wnew + int(fac*(wslot));y1 = hnew + int(fac*(hslot))
    x2 = wnew + int((1-fac)*(wslot));y2 = hnew + int((1-fac)*(hslot))
    f1 = linedrawalgo(x1,y1,x2,y1,img)#line upper -
    f2 = linedrawalgo(x1,y1,x1,y2,img)#line left |
    f3 = linedrawalgo(x1,y1,x2,y2,img)#diagonal \
    f4 = linedrawalgo(x1,y2,x2,y1,img)#diagonal /
    f5 = linedrawalgo(x1,y2,x2,y2,img)#line lower -
    f6 = linedrawalgo(x2,y1,x2,y2,img)#line right |
    arr = [f1,f2,f3,f4,f5,f6]
    return arr
#breshanhams lines algo but this function generate the factor which detect how the image pixels are changing
"""arr is transfered from pattern draw and through naive bayes
we predict answer in the form of 0,1.(0 for object not present and 1 for object present)"""
def predictor(arr):
    s = sum(arr)
    if s  > 0:#means if 4 line have the changed values than there is a object
        return 1
    else:
        return 0
def linedrawalgo(x1,y1,x2,y2,img):
    xn=x1;yn=y1;c=0;t=0
    if (y2-y1)<(x2-x1):#m<1
        pk = 2*(y2 - y1) - (x2 - x1)
        while(xn <= x2):
            if pk >= 0 :
                xn = xn + 1
                yn = yn + 1
                pk = pk + (y2-y1) - (x2-x1)
            else:
                xn = xn + 1
                yn = yn
                pk = pk + (y2-y1)
            v = checkerpoint(xn,yn,img)
            c = c + v # number of changed pixels
            t = t + 1 #total number of pixels
    elif (y2-y1)>(x2-x1):#m<1
        pk = 2*(x2 - x1) - (y2 - y1)
        while(yn <= y2):
            if pk >= 0 :
                xn = xn + 1
                yn = yn + 1
                pk = pk + (x2-x1) - (y2-y1)
            else:
                xn = xn
                yn = yn + 1
                pk = pk + (x2-x1)
            v = checkerpoint(xn,yn,img)
            c = c + v # number of changed pixels
            t = t + 1 #total number of pixels
    else:
        while(yn <= y2):
            xn = xn + 1
            yn = yn + 1
        v = checkerpoint(xn,yn,img)
        c = c + v # number of changed pixels
        t = t + 1 #total number of pixels
    if float(c/t) >= 0.5:
        return 1
    else:
        return 0
def checkerpoint(x,y,img):
    initial = 255
    pixvalue = img.getpixel((x,y))
    if (initial - pixvalue) > 25:
        return 1
    else:
        return 0
def arrgen(wnew,hnew,wslot,hslot,img):
    fac = [0.1,0.2,0.3,0.4];i=0;ans = 0
    while(i<len(fac)):
        arr = patterndraw(wnew,hnew,wslot,hslot,img ,fac[i])
        ans = ans + predictor(arr)
        i=i+1
    if ans <= 1:
        return 0
    else:
        return 1
#patterngen
def patterngen(divfactor):
    hnew=0;wnew=0;arr2=[]
    #hwtuple = hwtuple + ( int(width) , int(height) )
    #img = Image.new('RGB',hwtuple, color=(255, 255, 255)).convert('L')
    img = Image.open('sp6.png').convert('L')
    height = img.size[1]
    width = img.size[0]
    #pixv = img.load()
    wslot=int(width/divfactor[0]);hslot=int(height/divfactor[1]);
    draw = ImageDraw.Draw(img)
    for i in range(divfactor[1]):
        hnew = int(i*hslot)
        for j in range(divfactor[0]):
            wnew = int(j*wslot)
            ans = arrgen(wnew,hnew,wslot,hslot,img)
            if j==0:
                draw.line((0,hnew,width,hnew),fill=128)
            if i==0:
                draw.line((wnew,0,wnew,height),fill=128)
                arr2.append(ans)
            else:
                arr2[j] = arr2[j] + ans
    #pixv[j,i] = tpl
    #image closing and saving part
    #img.show()
    del draw
    img.save('sp6n.png')
    img.close()
    return arr2 
#input values
"""print("width:")
width = int(input())
print("height:")
height = int(input())"""
print("Enter the number of slot in which you want to divide width ")
widthdivisionfactor = int(input())
print("Enter the number of slot in which you want to divide height ")
heightdivisionfactor = int(input())
"""print("enter the name for image and extension like img.jpg")
imname = input()"""
#output
divfactor = [ widthdivisionfactor , heightdivisionfactor ]
arr = patterngen(divfactor)
print(arr)
