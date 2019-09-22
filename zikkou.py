import pygame
from pygame.locals import *
import sys
import random
import csv
import numpy as np
def AI(b_r,b_l,b_u,b_d,b_state):
	data=[]
	data1=[]
	a=0
	#csvデータ読み込み
	with open("gakusyudata1.csv","r") as f:
		reader=csv.reader(f)
		for row in reader:
			data1.append(row)
		for i in range(32):
			data.append([int(n) for n in data1[i]])
	if b_r==0 and b_l==0 and b_u==0 and b_d==0:
		if b_state=="r":
			a=np.random.choice(["r","l","u","d"],p=[data[0][0]/sum(data[0]),data[0][1]/sum(data[0]),data[0][2]/sum(data[0]),data[0][3]/sum(data[0])])
		if b_state=="l":
			a=np.random.choice(["r","l","u","d"],p=[data[1][0]/sum(data[1]),data[1][1]/sum(data[1]),data[1][2]/sum(data[1]),data[1][3]/sum(data[1])])
		if b_state=="u":
			a=np.random.choice(["r","l","u","d"],p=[data[2][0]/sum(data[2]),data[2][1]/sum(data[2]),data[2][2]/sum(data[2]),data[2][3]/sum(data[2])])
		if b_state=="d":
			a=np.random.choice(["r","l","u","d"],p=[data[3][0]/sum(data[3]),data[3][1]/sum(data[3]),data[3][2]/sum(data[3]),data[3][3]/sum(data[3])])
	if b_r==0 and b_l==0 and b_u==0 and b_d==1:
		if b_state=="r":
			a=np.random.choice(["r","l","u"],p=[data[4][0]/sum(data[4]),data[4][1]/sum(data[4]),data[4][2]/sum(data[4])])
		if b_state=="l":
			a=np.random.choice(["r","l","u"],p=[data[5][0]/sum(data[5]),data[5][1]/sum(data[5]),data[5][2]/sum(data[5])])
		if b_state=="d":
			a=np.random.choice(["r","l","u"],p=[data[6][0]/sum(data[6]),data[6][1]/sum(data[6]),data[6][2]/sum(data[6])])
	if b_r==0 and b_l==0 and b_u==1 and b_d==0:
		if b_state=="r":
			a=np.random.choice(["r","l","d"],p=[data[7][0]/sum(data[7]),data[7][1]/sum(data[7]),data[7][2]/sum(data[7])])
		if b_state=="l":
			a=np.random.choice(["r","l","d"],p=[data[8][0]/sum(data[8]),data[8][1]/sum(data[8]),data[8][2]/sum(data[8])])
		if b_state=="u":
			a=np.random.choice(["r","l","d"],p=[data[9][0]/sum(data[9]),data[9][1]/sum(data[9]),data[9][2]/sum(data[9])])
	if b_r==0 and b_l==1 and b_u==0 and b_d==0:
		if b_state=="r":
			a=np.random.choice(["r","u","d"],p=[data[10][0]/sum(data[10]),data[10][1]/sum(data[10]),data[10][2]/sum(data[10])])##初期状態
		if b_state=="l":
			a=np.random.choice(["r","u","d"],p=[data[10][0]/sum(data[10]),data[10][1]/sum(data[10]),data[10][2]/sum(data[10])])
		if b_state=="u":
			a=np.random.choice(["r","u","d"],p=[data[11][0]/sum(data[11]),data[11][1]/sum(data[11]),data[11][2]/sum(data[11])])
		if b_state=="d":
			a=np.random.choice(["r","u","d"],p=[data[12][0]/sum(data[12]),data[12][1]/sum(data[12]),data[12][2]/sum(data[12])])
	if b_r==1 and b_l==0 and b_u==0 and b_d==0:
		if b_state=="r":
			a=np.random.choice(["l","u","d"],p=[data[13][0]/sum(data[13]),data[13][1]/sum(data[13]),data[13][2]/sum(data[13])])
		if b_state=="u":
			a=np.random.choice(["l","u","d"],p=[data[14][0]/sum(data[14]),data[14][1]/sum(data[14]),data[14][2]/sum(data[14])])
		if b_state=="d":
			a=np.random.choice(["l","u","d"],p=[data[15][0]/sum(data[15]),data[15][1]/sum(data[15]),data[15][2]/sum(data[15])])
	if b_r==0 and b_l==0 and b_u==1 and b_d==1:
		if b_state=="r":
			a=np.random.choice(["r","l"],p=[data[16][0]/sum(data[16]),data[16][1]/sum(data[16])])
		if b_state=="l":
			a=np.random.choice(["r","l"],p=[data[17][0]/sum(data[17]),data[17][1]/sum(data[17])])
	if b_r==0 and b_l==1 and b_u==0 and b_d==1:
		if b_state=="r":
			a=np.random.choice(["r","u"],p=[data[18][0]/sum(data[18]),data[18][1]/sum(data[18])])##初期状態
		if b_state=="l":
			a=np.random.choice(["r","u"],p=[data[18][0]/sum(data[18]),data[18][1]/sum(data[18])])
		if b_state=="d":
			a=np.random.choice(["r","u"],p=[data[19][0]/sum(data[19]),data[19][1]/sum(data[19])])
	if b_r==1 and b_l==0 and b_u==0 and b_d==1:
		if b_state=="r":
			a=np.random.choice(["l","u"],p=[data[20][0]/sum(data[20]),data[20][1]/sum(data[20])])
		if b_state=="d":
			a=np.random.choice(["l","u"],p=[data[21][0]/sum(data[21]),data[21][1]/sum(data[21])])
	if b_r==0 and b_l==1 and b_u==1 and b_d==0:
		if b_state=="r":
			a=np.random.choice(["r","d"],p=[data[22][0]/sum(data[22]),data[22][1]/sum(data[22])])##初期状態
		if b_state=="l":
			a=np.random.choice(["r","d"],p=[data[22][0]/sum(data[22]),data[22][1]/sum(data[22])])
		if b_state=="u":
			a=np.random.choice(["r","d"],p=[data[23][0]/sum(data[23]),data[23][1]/sum(data[23])])
	if b_r==1 and b_l==0 and b_u==1 and b_d==0:
		if b_state=="r":
			a=np.random.choice(["l","d"],p=[data[24][0]/sum(data[24]),data[24][1]/sum(data[24])])
		if b_state=="u":
			a=np.random.choice(["l","d"],p=[data[25][0]/sum(data[25]),data[25][1]/sum(data[25])])
	if b_r==1 and b_l==1 and b_u==0 and b_d==0:
		if b_state=="r":
			a=np.random.choice(["u","d"],p=[data[26][0]/sum(data[26]),data[26][1]/sum(data[26])])##初期状態
		if b_state=="u":
			a=np.random.choice(["u","d"],p=[data[26][0]/sum(data[26]),data[26][1]/sum(data[26])])
		if b_state=="d":
			a=np.random.choice(["u","d"],p=[data[27][0]/sum(data[27]),data[27][1]/sum(data[27])])
	if b_r==0 and b_l==1 and b_u==1 and b_d==1:
		if b_state=="r":
			a=np.random.choice(["r"],p=[data[28][0]/sum(data[28])])##初期状態
		if b_state=="l":
			a=np.random.choice(["r"],p=[data[28][0]/sum(data[28])])
	if b_r==1 and b_l==0 and b_u==1 and b_d==1:
		if b_state=="r":
			a=np.random.choice(["l"],p=[data[29][0]/sum(data[29])])
	if b_r==1 and b_l==1 and b_u==0 and b_d==1:
		if b_state=="d":
			a=np.random.choice(["u"],p=[data[30][0]/sum(data[30])])
	if b_r==1 and b_l==1 and b_u==1 and b_d==0:
		if b_state=="u":
			a=np.random.choice(["d"],p=[data[31][0]/sum(data[31])])
	return a
def main():
	(rand_ta,rand_yo)=([],[])
	(w,h) = (600,600)   # 画面サイズ
	(x,y) = (20, h//2)
	(ta,yo) = (w//15,h//15)
	(ta_g,yo_g)=(random.randint(0,14),random.randint(0,14))
	(log_x,log_y)=([20],[h//2])
	bl_j=[]
	bl_j_g=0
	cl_key=0
	k=0
	bl_l=0
	bl_r=0
	bl_u=0
	bl_d=0
	bl_l_g=0
	bl_r_g=0
	bl_u_g=0
	bl_d_g=0
	data1=[]
	data=[]
	state_bl=[]
	b_state="r"
	f_name="gamedata1.csv"
	
	for i in range(50):
		bl_j.append(0)
	pygame.init()       # pygame初期化
	pygame.display.set_mode((w, h), 0, 32)  # 画面設定
	screen = pygame.display.get_surface()
	jud=0
	#ランダムブロックの位置決め
	for i in range(50):
		rand_ta.append(random.randint(0,14))
		rand_yo.append(random.randint(0,14))
		if rand_ta[i]==0 and rand_yo[i]==7:
			rand_ta[i]=random.randint(0,14)
			rand_yo[i]=random.randint(0,14)
		if rand_ta[i]==ta_g and rand_yo[i]==yo_g:
			rand_ta[i]=random.randint(0,14)
			rand_yo[i]=random.randint(0,14)
	while (1):
		pygame.display.update()     # 画面更新
		pygame.time.wait(30)        # 更新時間間隔
		screen.fill((0, 0, 0, 0))  # 画面の背景色
		# 円の中心座標が画面の範囲外にある場合
		if x <= 20:
			x = 20
			bl_l=1
		if x >= w-20:
			x = w-20
			bl_r=1
		if y <= 20:
			y = 20
			bl_u=1
		if y >= h-20:
			y = h-20
			bl_d=1
		# ブロック生成 サーチ
		for i in range(50):
			if bl_j[i]==0:
				pygame.draw.rect(screen,(0,0,0),Rect(ta*rand_ta[i],yo*rand_yo[i],40,40))
			#左サーチ
			if x>ta*rand_ta[i] and y<yo*rand_yo[i]+40 and x<ta*rand_ta[i]+80 and y>yo*rand_yo[i]:
				bl_j[i]=1
				bl_l=1
			#右サーチ
			if x>ta*rand_ta[i]-40 and y<yo*rand_yo[i]+40 and x<ta*rand_ta[i]+40 and y>yo*rand_yo[i]:
				bl_j[i]=1
				bl_r=1
			#下サーチ
			if x>ta*rand_ta[i] and y<yo*rand_yo[i]+40 and x<ta*rand_ta[i]+40 and y>yo*rand_yo[i]-40:
				bl_j[i]=1
				bl_d=1
			#上サーチ
			if x>ta*rand_ta[i] and y<yo*rand_yo[i]+80 and x<ta*rand_ta[i]+40 and y>yo*rand_yo[i]:
				bl_j[i]=1
				bl_u=1
			#見つけたブロック
			if bl_j[i]==1:
				pygame.draw.rect(screen,(255,0,0),Rect(ta*rand_ta[i],yo*rand_yo[i],40,40))
			
			if x>ta*rand_ta[i] and y<yo*rand_yo[i]+40 and x<ta*rand_ta[i]+40 and y>yo*rand_yo[i]:
				pygame.draw.rect(screen,(255,255,255),Rect(ta*rand_ta[i],yo*rand_yo[i],40,40))
	# 通ったルート
		for i in range(k):
			pygame.draw.rect(screen,(100,150,150),Rect(log_x[i]-20,log_y[i]-20,40,40))
	# 正解ブロック サーチ
		if bl_j_g==0:
			pygame.draw.rect(screen,(0,0,0),Rect(ta*ta_g,yo*yo_g,40,40))
		if bl_j_g==1:
			pygame.draw.rect(screen,(0,200,200),Rect(ta*ta_g,yo*yo_g,40,40))
		#左サーチ
		if x>ta*ta_g and y<yo*yo_g+40 and x<ta*ta_g+80 and y>yo*yo_g:
			bl_l_g=1
			bl_j_g=1
		#右サーチ
		if x>ta*ta_g-40 and y<yo*yo_g+40 and x<ta*ta_g+40 and y>yo*yo_g:
			bl_r_g=1
			bl_j_g=1
		#下サーチ
		if x>ta*ta_g and y<yo*yo_g+40 and x<ta*ta_g+40 and y>yo*yo_g-40:
			bl_d_g=1
			bl_j_g=1
		#上サーチ
		if x>ta*ta_g and y<yo*yo_g+80 and x<ta*ta_g+40 and y>yo*yo_g:
			bl_u_g=1
			bl_j_g=1
		#ゴール
		if x>ta*ta_g and y<yo*yo_g+40 and x<ta*ta_g+40 and y>yo*yo_g:
			pygame.draw.rect(screen,(255,255,255),Rect(ta*ta_g,yo*yo_g,40,40))
			print("ゴールまでの移動回数:",cl_key)
			pygame.quit()
			sys.exit()
	# 円を描画
		pygame.draw.circle(screen, (0, 200, 0), (x, y), 20)
	# 罫線
		for i in range(15):
			for j in range(15):
				pygame.draw.rect(screen,(255,255,255),Rect(ta*i,yo*j,40,40),2)
        # イベント処理
		for event in pygame.event.get():
            # 画面の閉じるボタンを押したとき
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
            # キーを押したとき
			if event.type == KEYDOWN:
                # ESCキーなら終了
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
				#スペースキーを押したとき
				if event.key == K_SPACE:
					state=AI(bl_r,bl_l,bl_u,bl_d,b_state)
					#ゴールを見つけた場合
					if bl_r_g==1:
						x += 40
						cl_key+=1
						log_x.append(x)
						log_y.append(y)
						k+=1
						state_bl.append([bl_r,bl_l,bl_u,bl_d,"r",b_state])
						b_state="r"
					if bl_l_g==1:
						x -= 40
						cl_key+=1
						log_x.append(x)
						log_y.append(y)
						k+=1
						state_bl.append([bl_r,bl_l,bl_u,bl_d,"l",b_state])
						b_state="l"
					if bl_u_g==1:
						y -= 40
						cl_key+=1
						log_x.append(x)
						log_y.append(y)
						k+=1
						state_bl.append([bl_r,bl_l,bl_u,bl_d,"u",b_state])
						b_state="u"
					if bl_d_g==1:
						y += 40
						cl_key+=1
						log_x.append(x)
						log_y.append(y)
						k+=1
						state_bl.append([bl_r,bl_l,bl_u,bl_d,"d",b_state])
						b_state="d"
					#AI関数から受け取って移動
					if state=="r" and bl_j_g==0:
						x += 40
						cl_key+=1
						log_x.append(x)
						log_y.append(y)
						k+=1
						state_bl.append([bl_r,bl_l,bl_u,bl_d,"r",b_state])
						b_state="r"
					if state=="l" and bl_j_g==0:
						x -= 40
						cl_key+=1
						log_x.append(x)
						log_y.append(y)
						k+=1
						state_bl.append([bl_r,bl_l,bl_u,bl_d,"l",b_state])
						b_state="l"
					if state=="u" and bl_j_g==0:
						y -= 40
						cl_key+=1
						log_x.append(x)
						log_y.append(y)
						k+=1
						state_bl.append([bl_r,bl_l,bl_u,bl_d,"u",b_state])
						b_state="u"
					if state=="d" and bl_j_g==0:
						y += 40
						cl_key+=1
						log_x.append(x)
						log_y.append(y)
						k+=1
						state_bl.append([bl_r,bl_l,bl_u,bl_d,"d",b_state])
						b_state="d"
				#ブロックの位置の初期化
				bl_l=0
				bl_r=0
				bl_u=0
				bl_d=0
	
						
if __name__ == "__main__":
	main()
