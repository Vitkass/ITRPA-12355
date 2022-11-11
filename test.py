import pyautogui as pq
from mss.darwin import MSS as mss
from PIL import Image



needle = 'mail.png'
haystack = 'new.png' 


position = pq.locate(needle, haystack)
print(position)

screen = Image.open(needle)
main = Image.open(haystack)

screen_width, screen_hieght = screen.size
main_width, main_hieght = main.size


print(screen_width, screen_hieght)
print(main_width, main_hieght)

if not position:
    y = 0
    sum_hieght = screen_hieght + 40
    fal = False
    
    while 1:
        x = 0
        sum_width = screen_width + 40
        print(sum_width)

        if  main_hieght/(y+1) < 1.5 :
            sum_hieght += abs(y - main_hieght)
            y -= screen_hieght
            fal = True

        
        while 1:
            if main_width/(x+1) > 1.5:
                position = pq.locate(needle, haystack, region=[x, y, sum_width, sum_hieght])
                if position:
                    print('find position')
                    break
            else:
                sum_width += abs(x - main_width)
                x -= screen_width
                print(x, y, sum_width, sum_hieght)
                position = pq.locate(needle, haystack, region=[x, y, sum_width, sum_hieght])
                if position:
                    print('find position')
                    break
                break
            
            x += screen_width

        y +=screen_hieght

        if fal:
            print('That is all, folks')
            break


print(position)

            




print(pq.position())

if position:
    img = Image.open('monitor.png')
    cut = [position[0],position[1], position[0]+position[2], position[1]+position[3]]
    print(cut)
    crop = img.crop(cut)
    crop.save('skr.png')
    

t = dict(
    t= 'lsa'
)
