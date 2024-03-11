import subprocess,json,time
import requests
import os	
b ="sever"
r = requests.get('https://api.npoint.io/30845589373debc68f8a')
r = json.loads(r.text)
try:
	key = r[b]
	if key == True:
		print("Connected to sever is successfully")
		time.sleep(1)
		print("sever is open")
		time.sleep(1)
		print("Loading...!")
		time.sleep(1)
		print("Sever sẽ đóng vào 12h đêm đến 7h sáng mỗi ngày để bảo trì")
		while True:
			print("""
_________    __           .__   __________
\_   ___ \ _/  |_ _______ |  |  \____    /
/    \  \/ \   __\\_  __ \|  |    /     / 
\     \____ |  |   |  | \/|  |__ /     /_ 
 \_______/ |__|   |__|   |____//_________\
                                       

""")
			exit()
	elif key == False:
		print("""Máy chủ đã đóng để bảo trì vui lòng quay lại sau nếu tool lỗi xin liên hệ
SĐT:0372108501 
FB:https://www.facebook.com/PCTPC57/""")
		time.sleep(10)
except:
	print("""Máy chủ đã đóng để bảo trì vui lòng quay lại sau nếu tool lỗi xin liên hệ
SĐT:0372108501 
FB:https://www.facebook.com/PCTPC57/""")
	time.sleep(10)