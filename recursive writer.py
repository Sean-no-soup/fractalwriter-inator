#recursively writes until desired size or the python crashes
#made by: Sean, no soup#///////////////////////////////////////////////////

ch1 = ' :3' #solid
ch2 = '   ' #background


#start on line 10 so easier to translate from gimp, rectangular mask
mask = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0],
        [0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],
        [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
        [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
        [0,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
        [0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0],
        [1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,0,0],
        [1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
        [0,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0],
        
        ]

userNum = int(input('number of iterations?:'))
if userNum == 0:
    print(ch1)
    quit
maskRows = len(mask)
maskCols = len(mask[0])

def check_mask(row,col):
    if mask[row][col]: return True
    return False

textFile = open('recursive_output.txt','w')

for row in range(0, maskRows**userNum):         #vertical position
    for col in range(0, maskCols**userNum):     #horizontal position      
        for layer in range(userNum-1,-1, -1):   #masks to check, starts at 1-iteration-number and counts down to 0. largest to smallest

            #find position on mask
            #ex: 3x3 mask, 3 iterations, 27x27 total. pos(0-26) -> maskpos (0-2)
            #layer 2:27x27  mask^layer = 27        maskpos= (pos/(maskMax**layer))%mask = (pos/9)%3    0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2
            #layer 1:9x9    mask^layer = 9         maskpos= (pos/(maskMax**layer))%mask = (pos/3)%3    0 0 0 1 1 1 2 2 2 0 0 0 1 1 1 2 2 2 0 0 0 1 1 1 2 2 2
            #layer 0:3x3    mask^layer = 3         maskpos= (pos/(maskMax**layer))%mask = (pos/1)%3    0 1 2 0 1 2 0 1 2 0 1 2 0 1 2 0 1 2 0 1 2 0 1 2 0 1 2

            maskRow = int(  (row/(maskRows**layer))   %   maskRows)
            maskCol = int(  (col/(maskCols**layer))   %   maskCols)

            if not check_mask(maskRow,maskCol): #if blocked by a mask write to file and skip to the next position
                textFile.write(ch2)
                break
        else:textFile.write(ch1)                #if all masks pass write to file and move to the next position
    textFile.write('\n')                        #each new row write a new line

textFile.close()
