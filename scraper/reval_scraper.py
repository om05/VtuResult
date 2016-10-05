import csv
import pdb
import requests 
from bs4 import BeautifulSoup
import os
import boto3
import time 
#dynamodb = boto3.resource('dynamodb', region_name='us-east-1',aws_access_key_id='',aws_secret_access_key='')
#table=dynamodb.Table('results')
college_code =['1ay', '1ap', '1aa', '1ao', '1ah', '1aj', '1ak', '1ac', '1am', '1as', '1ar', '1at', 
	'1au', '1bg', '1bt', '1bc', '1bi', '1bh', '1bs', '1bm', '1by', '1bo', '1ck', '1cr', '1cd', '1cg', 
	'1ce', '1dt', '1ds', '1db', '1da', '1cc', '1gv', '1ec', '1ep', '1ew', '1gs', '1gc', '1ga', '1gd', 
	'1sk', '1gg', '1hk', '1hm', '1ic', '1ii', '1jv', '1js', '1jt', '1ks', '1ki', '1kn', '1me', '1mj', 
	'1nj', '1nc', '1nh', '1ox', '1pn', '1pe', '1ri', '1rl', '1rr', '1rg', '1re', '1rn', '1sj', '1va', 
	'1st', '1sz', '1sg', '1sc', '1sp', '1hs', '1sb', '1sv', '1mv', '1jb', '1sw', '1bn', '1kt', '1kh', 
	'1rc', '1ve', '1tj', '1vi', '1vj', '1vk', '1yd', '4ad', '4ai', '4al', '4bw', '4bb', '4bd', '4bp', 
	'4cb', '4ci', '4dm', '4ek', '4mg', '4gm', '4ge', '4gh', '4gl', '4gk', '4gw', '4jn', '4kv', '4km', 
	'4mh', '4mt', '4mk', '4nn', '4pa', '4pm', '4pr', '4ra', '4sf', '4sh', '4mw', '4sm', '4su', '4sn',
	 '4es', '4so', '4ub', '4vv', '4vm', '4vp', '4yg', '2av', '2ag', '2ab', '2ae', '2bv', '2bl', '2gp', 
	 '4go', '2gb', '2hn', '2ji', '2kd', '2ke', '2kl', '2gi', '2mb', '2mm', '2rh', '2bu', '2sr', '2sa', 
	 '2ha', '2ka', '2tg', '2vs', '2vd', '3ae', '3bk', '3br', '3gf', '3gu', '3gn', '3kc', '3kb', '3la', 
	 '3na', '3pg', '3vc', '3rb', '3sl', '3vn']

def get_usn(prefix):
	#pdb.set_trace()
	usns=[]
	#os.system('mkdir '+prefix)
	try:
		with open('new_sem/'+prefix+'.csv', 'rb') as csvfile:
			usn_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
			for row in usn_reader:
				usn=row[0]
				try:
					usns.append(usn)
				except ValueError:
					pass
	except :
		pass
	return usns

def main():
	for prefix in college_code:
		college_cources=get_usn(prefix)
		if college_cources:
			for usn in college_cources:
				threshold=0
				
				pdb.set_trace()
				marks_dict = {}
				site="http://result.vtu.ac.in/cbcs_results2016Arrears.aspx?usn="+usn+"&sem=1"
				req=requests.post(site)
				soup=BeautifulSoup(req.text,'lxml')
				#input=soup.findAll("input")
				try:
					marks_list= {}
					name=soup.findAll(attrs={"name":"txtName"})[0]['value']
					
					for i in range(1,9):
						#pdb.set_trace()
						num=str(i)
						try:
							subject=soup.findAll(attrs={"name":"txtSub"+num})[0]['value'].upper().strip().replace(',','')
							code= soup.findAll(attrs={"name":"txtCode"+num})[0]['value'].upper().strip()
							credits=soup.findAll(attrs={"name":"txtCredits"+num})[0]['value'].upper().strip()
							credits_earned=soup.findAll(attrs={"name":"txtCreditEarned"+num})[0]['value'].upper().strip()
							grade_letter=soup.findAll(attrs={"name":"txtGardeLetter"+num})[0]['value'].upper().strip()
							grade_points=soup.findAll(attrs={"name":"txtGP"+num})[0]['value'].upper().strip()
							credits_points=soup.findAll(attrs={"name":"txtCP"+num})[0]['value'].upper().strip()
							remarks=soup.findAll(attrs={"name":"txtRemarks"+num})[0]['value'].upper().strip()
							if not remarks:
								remarks="noremarks"
							marks_dict[subject]=code+"_"+credits+"_"+credits_earned+"_"+grade_letter+"_"+grade_points+"_"+credits_points+"_"+remarks+"_1_arr"
							
							"""if marks:
								marks_list.append(marks)
							threshold=0
							"""
						except KeyError:
							break
					#pdb.set_trace()
					if marks_dict:
						#pdb.set_trace()
						"""table.put_item(Item={
						"usn_sem":usn+"_1",
						"arrear_1":marks_dict
						})"""
						print marks_dict
						time.sleep(1)
						
				except IndexError:
					pass
						
						
						



if __name__ == '__main__':
	main()
	