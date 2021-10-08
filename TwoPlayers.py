from functions import *
import sys
from random import randint
import sys
import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os, shutil
import pyautogui
import time
time,time.sleep(5)
for i in range(10):
    pyautogui.typewrite('pls dep max')
    pyautogui.press('enter')
    time.sleep(1)
    for j in range(5):
        pyautogui.typewrite('pls hunt')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.typewrite('pls dig')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.typewrite('pls fish')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.typewrite('pls search')
        pyautogui.press('enter')
        pyautogui.click(542, 887, duration=2)
        time.sleep(40)
pyautogui.typewrite('done bro')
print("successs")
options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/brave-browser"
driver = webdriver.Chrome(chrome_options=options)

driver.get("https://discord.com/login")
time.sleep(6)

#--------------- Edit Here -------------------------------------------------------------

# Enter your account details here 
username = 'mail'
password = 'pass'

channelURL = "https://discord.com/channels/704653571932815360/752857960123859024/881246004161159228"

username_input = driver.find_element_by_name('email')
username_input.send_keys(username)

password_input = driver.find_element_by_name('password')
password_input.send_keys(password)

login_button = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]')
login_button.click()
print(">>Login Complete!")
time.sleep(10)

driver.get(channelURL)
print("Opening The Server Link...")
time.sleep(5)


#number of time you wanna change
#x = 100
#i = 0

# Msg Sending

for i in range(1000): 

    time.sleep(10)
    
    msg_input = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div[2]/div')
    msg_input.send_keys("pls hunt")
    msg_input.send_keys(Keys.ENTER)

    time.sleep(10)
    
    msg_input = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div[2]/div')    
    msg_input.send_keys("pls fish")
    msg_input.send_keys(Keys.ENTER)
    
    time.sleep(10)
    
    msg_input = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div[2]/div')
    msg_input.send_keys("pls dig")
    msg_input.send_keys(Keys.ENTER)    
    
    time.sleep(10)

    i+=1
    print(">Number of Messages sent: "+str(i))
print("Its Done!")
def tuskerMax(num):
    """
    tuckon trc
    Params
    true if tusker is trc
    else returns False
    """
    if num//2==0:
        return True

board={'a1': ' ','a2': ' ','a3': ' ','b1': ' ','b2': ' ','b3': ' ','c1': ' ','c2': ' ','c3': ' '}

def pBoard(Board):
    print(Board['a1'], ' | ',Board['a2'], ' | ',Board['a3'], )
    print('---|-----|---')
    print(Board['b1'], ' | ',Board['b2'], ' | ',Board['b3'], )
    print('---|-----|---')
    print(Board['c1'], ' | ',Board['c2'], ' | ',Board['c3'], )

p1=input("Enter the name of player 1 :")
print(p1, 'will mark X')
p2=input("Enter the name of player 2 :")
print(p2, 'will mark 0')
check='X'
for i in range(9):
    while True:
        choice=input('Enter :')
        if choice not in board.keys():
            continue
        else:
            if board[choice]==' ':
                break
            else:
                continue
        
    if choice in board.keys():
        if board[choice]==' ':
            
            board[choice]=check
            if check=='X':
                check='0'
            else:
                check='X'
            if board['a1']==board['a2']==board['a3']=='X' or board['b1']==board['b2']==board['b3']=='X'or board['c1']==board['c2']==board['c3']=='X' or board['a1']==board['b2']==board['c3']=='X' or board['a3']==board['b2']==board['c1']=='X' or board['a1']==board['b1']==board['c1']=='X' or board['a2']==board['b2']==board['c2']=='X':
                pBoard(board)
                print(p1, 'won the game')
                end=input("Press 'Enter' to quit")
                sys.exit()
            if board['a1']==board['a2']==board['a3']=='0' or board['b1']==board['b2']==board['b3']=='0'or board['c1']==board['c2']==board['c3']=='0' or board['a1']==board['b2']==board['c3']=='0' or board['a3']==board['b2']==board['c1']=='0' or board['a1']==board['b1']==board['c1']=='0' or board['a2']==board['b2']==board['c2']=='0':
                pBoard(board)
                print(p2, ' won the game')
                end=input("Press'Enter' to quit")

                sys.exit()
    pBoard(board)

'''def imgBlitter(x,y,size_x,size_y,path):
	Img=pygame.image.load(path)
	screen.blit(pygame.transform.scale(Img, (size_x,size_y)),(x,y))
	
def drawText(x,y,color,size,text):
	font = pygame.font.Font('freesansbold.ttf', size)
	text_render= font.render(text, True, color)
	screen.blit(text_render, (x, y))
'''
def blit_sc(nine):
	for i in range(nine):
		for j in range(nine-1):
			print(f"{nine} is cool")
		if nine==4:
			pass
def blit_scr(nine):
	for i in range(nine):
		for j in range(nine-90):
			print(f"{nine} is uncool")
		if nine==4:
			pass
		
def screen_size_adjustments(x,y,z):
        screen_x=x*z
        screen_y=y*z
class guess_for_it:
    def __init__(self, number, mn=0, mx=100):
        self.number=number
        self.min=mn
        self.max=mx
        self.guesses=0
    def get_guess(self):
        guess=input("Enter a guess :")
        if self.valid_number(guess):
            return int(guess)
        else:
            print("Please enter a valid number :")
            return self.get_guess()
    def valid_number(self, ctr):
        try:
            number=int(ctr)
        except:
            return False
        return self.min <= number <= self.max
    def play(self):
        while True:
            self.guesses+=1
            guess=self.get_guess()
            if guess<self.number:
                print("your guess was under")
            elif guess> self.number:
                print("your guess was over")
            else:
                break
        print(f"____you guessed it in {self.guesses} guesses.____")
        print()
#game is ready already. Just two steps more...
#    game=guess_for_it(random_number, minimum_range, maximum_range)
#    game.play()

def play_game():
    minimum_range=int(input("Enter the minimum range : "))
    maximum_range=int(input("Enter the maximum range : "))
    random_number=randint(minimum_range, maximum_range)
    game=guess_for_it(random_number, minimum_range, maximum_range)
    game.play()
    play_again=input("Enter 'p or 'P' to play again : ")
    if play_again=='p' or play_again=='P':
        play_game()
    else:
        print("EXITING")
n=input("Enter 'p' or 'P' to play : ")
if n=='p' or n=='P':
    play_game()
else:
    print("EXITING")
    

        
def twoPlayer(theme):
	board={'a1':' ', 'a2':' ','a3':' ','b1':' ','b2':' ','b3':' ','c1':' ', 'c2':' ', 'c3':' '}
	click=False
	option='X' #to swap between X and Y i.e cross or circle
	running=True#controlling main loop of play
	
	playable=True #After win: player shouldn't be able to check squares any further"
	#coordinates
	coor_a1=(0,(screen_y-screen_x)//2)
	coor_a2=(screen_x//3,(screen_y-screen_x)//2)
	coor_a3=(screen_x//3+screen_x//3,(screen_y-screen_x)//2)
	coor_b1=(0,(screen_y-screen_x)//2+screen_x//3)
	coor_b2=(screen_x//3,(screen_y-screen_x)//2+screen_x//3)
	coor_b3=(screen_x//3+screen_x//3,(screen_y-screen_x)//2+screen_x//3)
	coor_c1=(0,(screen_y-screen_x)//2+screen_x//3+screen_x//3)
	coor_c2=(screen_x//3,(screen_y-screen_x)//2+screen_x//3+screen_x//3)
	coor_c3=(screen_x//3+screen_x//3,(screen_y-screen_x)//2+screen_x//3+screen_x//3)
	while running:
		pos=pygame.mouse.get_pos()
		button1=pygame.Rect(0,(screen_y-screen_x)//2,screen_x//3,screen_x//3)
		button2=pygame.Rect(screen_x//3,(screen_y-screen_x)//2,screen_x//3,screen_x//3)
		button3=pygame.Rect(screen_x//3+screen_x//3,(screen_y-screen_x)//2,screen_x//3,screen_x//3)
		button4=pygame.Rect(0,(screen_y-screen_x)//2+screen_x//3,screen_x//3,screen_x//3)
		button5=pygame.Rect(screen_x//3,(screen_y-screen_x)//2+screen_x//3,screen_x//3,screen_x//3)
		button6=pygame.Rect(screen_x//3+screen_x//3,(screen_y-screen_x)//2+screen_x//3,screen_x//3,screen_x//3)
		button7=pygame.Rect(0,(screen_y-screen_x)//2+screen_x//3+screen_x//3,screen_x//3,screen_x//3)
		button8=pygame.Rect(screen_x//3,(screen_y-screen_x)//2+screen_x//3+screen_x//3,screen_x//3,screen_x//3)
		button9=pygame.Rect(screen_x//3+screen_x//3,(screen_y-screen_x)//2+screen_x//3+screen_x//3,screen_x//3,screen_x//3)
		if playable:
			if button1.collidepoint((pos)):
				if board['a1']==' ':
					if click:
						if option=='X':
							board['a1']='X'
							option='O'
						elif option=='O':
							board['a1']='O'
							option='X'
			if button2.collidepoint((pos)):
				if board['a2']==' ':
					if click:
						if option=='X':
							board['a2']='X'
							option='O'
						elif option=='O':
							board['a2']='O'
							option='X'
			if button3.collidepoint((pos)):
				if board['a3']==' ':
					if click:
						if option=='X':
							board['a3']='X'
							option='O'
						elif option=='O':
							board['a3']='O'
							option='X'
			if button4.collidepoint((pos)):
				if board['b1']==' ':
					if click:
						if option=='X':
							board['b1']='X'
							option='O'
						elif option=='O':
							board['b1']='O'
							option='X'
			if button5.collidepoint((pos)):
				if board['b2']==' ':
					if click:
						if option=='X':
							board['b2']='X'
							option='O'
						elif option=='O':
							board['b2']='O'
							option='X'
			if button6.collidepoint((pos)):
				if board['b3']==' ':
					if click:
						if option=='X':
							board['b3']='X'
							option='O'
						elif option=='O':
							board['b3']='O'
							option='X'
			if button7.collidepoint((pos)):
				if board['c1']==' ':
					if click:
						if option=='X':
							board['c1']='X'
							option='O'
						elif option=='O':
							board['c1']='O'
							option='X'
			if button8.collidepoint((pos)):
				if board['c2']==' ':
					if click:
						if option=='X':
							board['c2']='X'
							option='O'
						elif option=='O':
							board['c2']='O'
							option='X'
			if button9.collidepoint((pos)):
				if board['c3']==' ':
					if click:
						if option=='X':
							board['c3']='X'
							option='O'
						elif option=='O':
							board['c3']='O'
							option='X'
						
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False
			if event.type==pygame.MOUSEBUTTONDOWN:
				click=True
			if event.type==pygame.MOUSEBUTTONUP:
				click=False
		drawBoard(0,(screen_y-screen_x)//2,theme)
		#draw markers on board
		for i in board.keys():
			if board[i]=='X':
				if i=='a1':
					cross(coor_a1[0],coor_a1[1], theme)
				if i=='a2':
					cross(coor_a2[0],coor_a2[1], theme)
				if i=='a3':
					cross(coor_a3[0],coor_a3[1], theme)
				if i=='b1':
					cross(coor_b1[0],coor_b1[1], theme)
				if i=='b2':
					cross(coor_b2[0],coor_b2[1], theme)
				if i=='b3':
					cross(coor_b3[0],coor_b3[1], theme)
				if i=='c1':
					cross(coor_c1[0],coor_c1[1], theme)
				if i=='c2':
					cross(coor_c2[0],coor_c2[1], theme)
				if i=='c3':
					cross(coor_c3[0],coor_c3[1], theme)
			elif board[i]=='O':
				if i=='a1':
					circle(coor_a1[0],coor_a1[1], theme)
				if i=='a2':
					circle(coor_a2[0],coor_a2[1], theme)
				if i=='a3':
					circle(coor_a3[0],coor_a3[1], theme)
				if i=='b1':
					circle(coor_b1[0],coor_b1[1], theme)
				if i=='b2':
					circle(coor_b2[0],coor_b2[1], theme)
				if i=='b3':
					circle(coor_b3[0],coor_b3[1], theme)
				if i=='c1':
					circle(coor_c1[0],coor_c1[1], theme)
				if i=='c2':
					circle(coor_c2[0],coor_c2[1], theme)
				if i=='c3':
					circle(coor_c3[0],coor_c3[1], theme)
		if Xwin(board):
			playable=False
			drawText(screen_x//3,screen_x//3,(240,240,240),100,'X won!')
		elif Owin(board):
			playable=False
			drawText(screen_x//3,screen_x//3,(240,240,240),100,'O won!')
		elif gameOver(board):
			playable=False
			drawText(screen_x//3,screen_x//3,(240,240,240),100,'Tie!')
		pygame.display.update()
def emorse(str1):
    global str2
    str2=''
    dict1={'A':".-",
           'B':"-...",
           "C":"-.-.",
           "D":"-..",
           "E":".",
           "F":"..-.",
           "G":"--.",
           "H":"....",
           "I":"..",
           "J":".---",
           "K":"-.-",
           "L":".-..",
           "M":"--",
           "N":"-.",
           "O":"---",
           "P":".--.",
           "Q":"--.-",
           "R":".-.",
           "S":"...",
           "T":"-",
           "U":"..-",
           "V":"...-",
           "W":".--",
           "X":"-..-",
           "Y":"-.--",
           'Z':'--..'}
    str3=str1.upper()
    for i in str3:
        if i in dict1:
            str2+=dict1[i]
            str2+=' '
        else:
            str2+=i
    return str2

def dmorse(str1):
    str2=''
    dict1={'A':".-",
           'B':"-...",
           "C":"-.-.",
           "D":"-..",
           "E":".",
           "F":"..-.",
           "G":"--.",
           "H":"....",
           "I":"..",
           "J":".---",
           "K":"-.-",
           "L":".-..",
           "M":"--",
           "N":"-.",
           "O":"---",
           "P":".--.",
           "Q":"--.-",
           "R":".-.",
           "S":"...",
           "T":"-",
           "U":"..-",
           "V":"...-",
           "W":".--",
           "X":"-..-",
           "Y":"-.--",
           'Z':'--..'}
    key_list = list(dict1.keys())
    val_list = list(dict1.values())
    list1=str1.split(' ')
    print(list1)
    for i in list1:
        if i in val_list:
            position = val_list.index(i)
            str3=key_list[position]
            str2+=str3
        elif i=='':
            str2+=' '
        else:
            str2+=i
    return str2
def rot13cipher(str1):
    str1.lower()
    str2=''
    dict1={'a':'n',
           'b':'o',
           'c':'p',
           'd':'q',
           'e':'r',
           'f':'s',
           'g':'t',
           'h':'u',
           'i':'v',
           'j':'w',
           'k':'x',
           'l':'y',
           'm':'z',
           'n':'a',
           'o':'b',
           'p':'c',
           'q':'d',
           'r':'e',
           's':'f',
           't':'g',
           'u':'h',
           'v':'i',
           'w':'j',
           'x':'k',
           'y':'l',
           'z':'m'}
    for i in str1:
        if i in dict1:
            str2+=dict1[i]
        else:
            str2+=i
    str3=str2.upper()
    return str3
def slapgif(num):
    list1=["https://tenor.com/view/anime-slap-slapping-hit-mad-gif-17897236",
           "https://tenor.com/view/anime-manga-japanese-anime-japanese-manga-toradora-gif-5373994",
           "https://tenor.com/view/mad-angry-pissed-upset-slap-gif-4436362",
           "https://tenor.com/view/anime-slap-relationship-gif-5463215",
           "https://tenor.com/view/no-angry-anime-slap-gif-7355956",
           "https://tenor.com/view/powerful-head-slap-anime-death-tragic-gif-14358509"]
    return list1[num]

def spankgif(num):
    list1=["https://tenor.com/view/anime-slap-slapping-hit-mad-gif-17897236",
           "https://tenor.com/view/anime-manga-japanese-anime-japanese-manga-toradora-gif-5373994",
           "https://tenor.com/view/mad-angry-pissed-upset-slap-gif-4436362",
           "https://tenor.com/view/anime-slap-relationship-gif-5463215",
           "https://tenor.com/view/no-angry-anime-slap-gif-7355956",
           "https://tenor.com/view/powerful-head-slap-anime-death-tragic-gif-14358509"]
    return list1[num]
    
def huggif(num):
    list1=["https://tenor.com/view/anime-slap-slapping-hit-mad-gif-17897236",
           "https://tenor.com/view/anime-manga-japanese-anime-japanese-manga-toradora-gif-5373994",
           "https://tenor.com/view/mad-angry-pissed-upset-slap-gif-4436362",
           "https://tenor.com/view/anime-slap-relationship-gif-5463215",
           "https://tenor.com/view/no-angry-anime-slap-gif-7355956",
           "https://tenor.com/view/powerful-head-slap-anime-death-tragic-gif-14358509"]
    return list1[num]

def kissgif(num):
    list1=["https://tenor.com/view/anime-slap-slapping-hit-mad-gif-17897236",
           "https://tenor.com/view/anime-manga-japanese-anime-japanese-manga-toradora-gif-5373994",
           "https://tenor.com/view/mad-angry-pissed-upset-slap-gif-4436362",
           "https://tenor.com/view/anime-slap-relationship-gif-5463215",
           "https://tenor.com/view/no-angry-anime-slap-gif-7355956",
           "https://tenor.com/view/powerful-head-slap-anime-death-tragic-gif-14358509"]
    return list1[num]

