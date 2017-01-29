from PIL import Image
#import random
from rdrand import RdRandom
random = RdRandom()
import math
import ipdb

myresolution = 32
resolutionx = myresolution
resolutiony = myresolution

def makepicture(resolutionx, resolutiony):
    #data = [random.randint(0, 255) for _ in xrange(resolutionx*resolutiony)]
    #data[:] = [data[i : i+(resolutionx + resolutiony) / 2] for i in xrange(0, resolutionx*resolutiony, (resolutionx + resolutiony) / 2)]
    #print data
    return data

data = []
for x in xrange(resolutionx):
    yline = []
    for y in xrange(resolutiony):
        yline.append((random.randint(0,255), random.randint(0,255),random.randint(0,255)))
    data.append(yline)

scale = 64
img = Image.new('RGB', (resolutionx*scale, resolutiony*scale), 'black')
pixels = img.load()

#print img

lastr, lastg, lastb = 255,255,255

for x in xrange(resolutionx*scale):
    #print "Line",x, "rgb", data[x/scale]
    for y in xrange(resolutiony*scale):
        pixels[x, y] = data[x/scale][y/scale]
        #print data[x][y]

def test():
        r, g, b  = random.randint(0,lastr),random.randint(0,lastg), random.randint(0,lastb)
        pixels[x,y] = r,g,b
        lastr = int(math.sin(y*y+r)*100000)
        lastg = int(math.sin(x*y+g)*100000)
        lastb = int(math.sin(x*y+b)*100000)
        if lastr < 1:
            lastr = int(random.getrandbytes(1).encode('hex'),16)
        if lastg < 1:
            lastg = int(random.getrandbytes(1).encode('hex'),16)
        if lastb < 1:
            lastb = int(random.getrandbytes(1).encode('hex'),16)

#ipdb.set_trace()

img.show()
img.save('/tmp/image.bmp')
