import os
import requests
from bs4 import BeautifulSoup
from colorama import Fore,Back,Style,init
import urllib.request
import time

init(convert=True)
print(Fore.GREEN)
print(Style.BRIGHT)

print("PLEASE REMOVE THE (img,css,js) FOLDER FROM THE CURRENT DIRECTORY OTHERWISE IT WILL CAUSE ERROR \n")

os.mkdir('shivam_cracker')
os.chdir('shivam_cracker')
directory  = os.getcwd()

def main():
	try:
		url = str(input("Enter the url of the website add https of https also \n"))
		os.mkdir('img')

		print(Fore.RED + "Started encoding\n")




		time.sleep(2)
		print("########## ==> 25% \n")
		time.sleep(2)
		print("################## ==> 55% \n")
		time.sleep(2)
		print("############################# ==> 100% \n")

		print("Start Cracking \n")

		r = requests.get(url)
		soup =BeautifulSoup(r.content,'html.parser')
		# print(soup.prettify())

		

		all_the_css_links = []

		with open('index.html','w') as op:
			op.write(str(r.text))

		for i in soup.find_all("link"):
			print(i)
			try:
				all_the_css_links.append(i['href'])
				
			except Exception as e:
				pass



		all_the_js_links = []


		for i in soup.find_all("script"):
			# print(i.contents)
			# print(i.get_text() + "\n\n\n\n\n")
			# print(i.text)
			print(i)

			try:
				all_the_js_links.append(i['src'])
			except Exception as e:
				pass


		print(all_the_css_links)
		print(all_the_js_links)


		all_the_image_links = []

		for i in soup.find_all("img"):
			try:
				all_the_image_links.append(i['src'])
			except Exception as e:
				pass



		# def dl_jpg(url,file_path,file_name):
		#     full_path = file_path + file_name + '.jpg'
		#     urllib.request.urlretrieve(url,full_path)


		# url = input("Enter img url to download")
		# file_name = input("Enter the name of file")    

		# dl_jpg(url,'img/',file_name)

		def image_downloader(a):
			for item in a:
				if ("https" in item) or ("http" in item):
					pass
				else:
					img_extension_split = item.split('.') 
					img_extension = img_extension_split[len(img_extension_split)-1]

					try:
					    img_name_split = item.split('/')    		
					except Exception as e:
					    img_name_split = item.split('//')		
					
					img_name = 	img_name_split[len(img_name_split)-1].split('.')[0]

					full_path = 'img/' + img_name + f".{img_extension}"
					print(Fore.MAGENTA + "Downloading image\n")
					print(f"{full_path}\n")
					try:
					    urllib.request.urlretrieve(url + '/' + item,full_path)
						
					except Exception as e:
						pass

		image_downloader(all_the_image_links)

		os.mkdir('css')
		def saving_to_css_folder(a):
			os.chdir("css")
			for item in a:
				
				
				split_item = item.split('.') 
				last_item = split_item[len(split_item)-1]

				if ("https" in item) or ("http" in item):
					pass

				elif last_item == 'css':
					 try:
					 	name_item_list = item.split('/')
					 except Exception as e:
					 	name_item_list = item.split('//')
					 
					 name_item =  url + '/' + name_item_list[len(name_item_list)-1]	
					 
					   
					 text = requests.get(url + '/' + item).text
					 print(Fore.CYAN + "downloading css file ")
					 print(f"{url + '/' + item} downloaded Successfully \n")
					 # print(text)
					 file_name =str(name_item_list[len(name_item_list)-1])
					 with open (file_name,'w') as op:
					 	op.write(str(text))
				else:
					pass	 	

			os.chdir(directory)		 	
			print(os.getcwd())

		saving_to_css_folder(all_the_css_links)

		os.mkdir('js')

		def saving_to_js_folder(a):
			os.chdir("js")
			for item in a:
				split_item = item.split('.') 
				last_item = split_item[len(split_item)-1]

				if ("https" in item) or ("http" in item):
					pass	
				elif last_item =='js':

					try:
					 	name_item_list = item.split('/')

					except Exception as e:
					 	name_item_list = item.split('//')



					name_of_the_file = name_item_list[len(name_item_list)-1]	 	
					
					text = requests.get(url + '/' + item).text		
					print(Fore.YELLOW + "Downloading js files\n")
					print(f"{url + '/' + item} donwloaded \n")
					with open(str(name_of_the_file),'w') as op:
						op.write(text)
				else:
					pass	

			os.chdir(directory)		


		saving_to_js_folder(all_the_js_links)




		all_the_anchor_tags = []


		for item in soup.find_all('a'):
			print(item)
			try:
				print(item['href'])
				all_the_anchor_tags.append(str(item['href']))
			except Exception as e:
				print("Not found")
			# all_the_anchor_tags.append(item['href'])


		print(all_the_anchor_tags)

		def check_for_on_page_anchor(string):
			a = string.split()
			first_letter = a[0]
			if first_letter=='#':
				return False
			elif "https" in string:
				return False	
			elif "http" in string:
				return False	
			elif string[0]=='#':
				return False	
			elif first_letter == '/':
				return False	
			else:
				return True	

		def anchor_tag_finder(all_the_anchor_tags):		
			for item in all_the_anchor_tags:
			    if check_for_on_page_anchor(item):
				    split_item = item.split('/')
				    name_of_the_page = split_item[len(split_item)-1]
				    text_main = requests.get(url + name_of_the_page)
				    print(f"\n\n {url + '/' + name_of_the_page} \n\n\n")
				    text = text_main.text
				    soup = BeautifulSoup(text_main.content,'html.parser')
				    all_the_css_links = []
				    for i in soup.find_all("link"):
					    # print(i)
					    try:
						    all_the_css_links.append(i['href'])
				
					    except Exception as e:
						    pass

				    saving_to_css_folder(all_the_css_links)	     

				    all_the_js_links = []


				    for i in soup.find_all("script"):
					    print(i)

					    try:
						    all_the_js_links.append(i['src'])
					    except Exception as e:
						    pass

				    saving_to_js_folder(all_the_js_links)		

				    all_the_image_links = []

				    for i in soup.find_all('img'):
				    	all_the_image_links.append(i['src'])
				    image_downloader(all_the_image_links)	

				    try:
					    with open(f"{name_of_the_page}.html",'w') as op:
					 	    op.write(text) 
				    except Exception as e:
					    with open(name_of_the_page,'w') as op:
					 	    op.write(text)


		anchor_tag_finder(all_the_anchor_tags)
	except Exception as q:
		pass	


main()