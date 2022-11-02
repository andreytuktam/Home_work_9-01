import emoji
from random import randint


pole = [["   ", "   ", "   "], ["   ", "   ", "   "], ["   ", "   ", "   "]]
print((emoji.emojize(":white_square_button:")).join(pole[0]))
print(emoji.emojize(":white_square_button:") * 6)
print((emoji.emojize(":white_square_button:")).join(pole[1]))
print(emoji.emojize(":white_square_button:") * 6)
print((emoji.emojize(":white_square_button:")).join(pole[2]))
s = 1
p = 0
k = randint(0, 1)
print(s)
flag = True
while flag == True:
    if k == 0:
        x = (int(input(f'игрок {emoji.emojize(":yawning_face:")} введи номер строки 1-3: ')) - 1)
        y = (int(input(f'игрок {emoji.emojize(":yawning_face:")} введи номер столбца 1-3: ')) - 1)
        if pole[x][y] != emoji.emojize(":woozy_face:"):
            pole[x][y] = emoji.emojize(":yawning_face:") 
        else:
            print("эта ячейка занята, перезапусти программу!")
            flag = False
        print((emoji.emojize(":white_square_button:")).join(pole[0]))
        print(emoji.emojize(":white_square_button:") * 6)
        print((emoji.emojize(":white_square_button:")).join(pole[1]))
        print(emoji.emojize(":white_square_button:") * 6)
        print((emoji.emojize(":white_square_button:")).join(pole[2]))
        k = k + 1
        s += 1
        print(s)
        if pole[0][0] == pole[1][0] == pole[2][0] == emoji.emojize(":yawning_face:") or pole[0][1] == pole[1][1] == pole[2][1] == emoji.emojize(":yawning_face:") or\
            pole[0][2] == pole[1][2] == pole[2][2] == emoji.emojize(":yawning_face:") or pole[0][0] == pole[0][1] == pole[0][2] == emoji.emojize(":yawning_face:") or\
            pole[1][0] == pole[1][1] == pole[1][2] == emoji.emojize(":yawning_face:") or pole[2][0] == pole[2][1] == pole[2][2] == emoji.emojize(":yawning_face:") or\
            pole[0][0] == pole[1][1] == pole[2][2] == emoji.emojize(":yawning_face:") or pole[0][2] == pole[1][1] == pole[2][0] == emoji.emojize(":yawning_face:"):
            print(f'игрок {emoji.emojize(":yawning_face:")} победил')
            p += 1
            if p == 2:
                flag = False
        
        if s == 10:
            flag = False
    if k == 1 and flag != False:
        x1 = (int(input(f'игрок {emoji.emojize(":woozy_face:")} введи номер строки 1-3: ')) - 1)
        y1 = (int(input(f'игрок {emoji.emojize(":woozy_face:")} введи номер столбца 1-3: ')) - 1)
        if pole[x1][y1] != emoji.emojize(":yawning_face:"):
            pole[x1][y1] = emoji.emojize(":woozy_face:")
        else:
            print("эта ячейка занята, перезапусти программу!")
            flag = False  
        print((emoji.emojize(":white_square_button:")).join(pole[0]))
        print(emoji.emojize(":white_square_button:") * 6)
        print((emoji.emojize(":white_square_button:")).join(pole[1]))
        print(emoji.emojize(":white_square_button:") * 6)
        print((emoji.emojize(":white_square_button:")).join(pole[2]))
        k = k - 1
        s += 1
        print(s)
        if pole[0][0] == pole[1][0] == pole[2][0] == emoji.emojize(":woozy_face:") or pole[0][1] == pole[1][1] == pole[2][1] == emoji.emojize(":woozy_face:") or\
            pole[0][2] == pole[1][2] == pole[2][2] == emoji.emojize(":woozy_face:") or pole[0][0] == pole[0][1] == pole[0][2] == emoji.emojize(":woozy_face:") or\
            pole[1][0] == pole[1][1] == pole[1][2] == emoji.emojize(":woozy_face:") or pole[2][0] == pole[2][1] == pole[2][2] == emoji.emojize(":woozy_face:") or\
            pole[0][0] == pole[1][1] == pole[2][2] == emoji.emojize(":woozy_face:") or pole[0][2] == pole[1][1] == pole[2][0] == emoji.emojize(":woozy_face:"):
            print(f'игрок {emoji.emojize(":woozy_face:")} победил')
            p += 1
            if p == 2:
                flag = False 
            
        if s == 10:
            flag = False  
if p == 2:
    print("ничья!")