import pygame
import math
from random import randint
pygame.init()
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption('space')
running=True
left_button_touched=False
right_button_touched=False
fire_button_pressed=False
speed=15
enemy_down_speed=200
num_of_enemies=6
gameoverScore=False
rect=pygame.Rect((0,1500),(1080,2))
score_value=0
collision=False
#background=pygame.image.load('vBG.jpg')

#buttons
buttonImg = pygame.image.load('contrast.png')
fireButtonImg=pygame.image.load('record.png')

def movementButton(x,y):
	screen.blit(pygame.transform.scale(buttonImg,(128,128)),(x,y))
	
def fireButton(x,y):
	screen.blit(pygame.transform.scale(fireButtonImg,(180,180)),(x,y))


#isOver function
def isOver(buttonType, pos):
	if buttonType=='left':
		if pos[0]<228 and pos[0]>120 and pos[1]<1878 and pos[1]>1750:
			return True
	elif buttonType=='right':
		if pos[0]<960 and pos[0]>832 and pos[1]<1878 and pos[1]>1750:
			return True
	elif buttonType=='fire':
		if pos[0]<595 and pos[0]>467 and pos[1]<1878 and pos[1]>1750:
			return True
	else:
		False

#score
font = pygame.font.Font('freesansbold.ttf', 64)
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def isCollision(enemyX,bulletX,enemyY,bulletY):
		if math.sqrt(math.pow(enemyX+62-bulletX, 2)+math.pow(enemyY+62-bulletY, 2))<60:
			return True

#GameOver
gameover_font=pygame.font.Font('freesansbold.ttf',112)
def gameover():
	global gameoverScore
	gameoverScore=True
	text=gameover_font.render("Game Over", True, (255,255,255))
	screen.blit(text,(240,900))
	show_score(400,1150)

#player
playerImg=pygame.image.load("player.png")
playerX=476
playerY=1550
playerXChange=0
def player(x,y):
	screen.blit(pygame.transform.scale(playerImg,(124,124)),(x,y))

	
#bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 1550
bulletX_change = 0
bulletY_change = 20
bullet_state = "ready"
def bullet(x,y):
	global bullet_state
	bullet_state="fire"
	screen.blit(pygame.transform.scale(bulletImg,(32,32)),(x,y))

#enemy
enemyImg=[]
enemyX=[]
enemyY=[]
enemyXChange=[]
enemyYChange=[]

for i in range(num_of_enemies):
	enemyImg.append(pygame.image.load("enemy.png"))
	enemyX.append(randint(0,956))
	enemyY.append(randint(10,400))
	enemy_speed=randint(3,10)
	enemyXChange.append(enemy_speed)
	enemyYChange.append(enemy_down_speed)
def enemy(x,y,i):
	screen.blit(pygame.transform.scale(enemyImg[i],(124,124)),(x,y))
	
	
while running:
	screen.fill((0,0,0))
	#screen.blit(pygame.transform.scale(background, (2300,2300)),(-500,0))
	pos=pygame.mouse.get_pos()
	
	for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False
				
				
			elif event.type==pygame.MOUSEBUTTONDOWN:
				if isOver('left', pos):
					#playerX+=10
					left_button_touched=True
				elif isOver('right', pos):
					right_button_touched=True
				elif isOver('fire', pos):
					      if bullet_state is "ready":
					      	if not gameoverScore:
					      		bulletX=playerX+45
					      		bullet(bulletX, bulletY)
					      		fire_button_pressed=True
			elif event.type==pygame.MOUSEBUTTONUP:
				left_button_touched=False
				right_button_touched=False
				fire_button_pressed=False
				playerXChange=0
	if left_button_touched:
		if playerX>0:
			playerXChange=-speed
			playerX+=playerXChange
		else:
			playerX=0
	if right_button_touched:
		if playerX<956:
			playerXChange=speed
			playerX+=playerXChange
		else:
			playerX=956
	for i in range(num_of_enemies):
		enemyX[i] += enemyXChange[i]
		if enemyX[i]>956:
			enemyXChange[i]=-enemyXChange[i]
			enemyY[i]+=enemyYChange[i]
		elif enemyX[i]<0:
			enemyXChange[i]=-enemyXChange[i]
			enemyY[i]+=enemyYChange[i]
		enemy(enemyX[i], enemyY[i], i)
		if isCollision(enemyX[i],bulletX,enemyY[i],bulletY):
			score_value+=1
			randint(10,900)
			enemyY[i]=randint(10,150)
			bulletY=1550
			bullet_state='ready'
		enemy(enemyX[i], enemyY[i], i)
		if enemyY[i]>1400:
			for i in range(num_of_enemies):
				enemyY[i]=3000
			gameover()
	if bulletY <= 0:
		bulletY=1550
		bullet_state="ready"
	if bullet_state is "fire":
		bullet(bulletX, bulletY)
		bulletY -= bulletY_change
	if not gameoverScore:
		player(playerX, playerY)
		movementButton(120,1750)
		movementButton(832,1750)
		fireButton(450, 1750)
		show_score(10,10)
		screen.fill((255,255,255),rect)
	pygame.display.update()	