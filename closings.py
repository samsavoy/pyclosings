import urllib.request
from bs4 import BeautifulSoup

def main():
	content = urllib.request.urlopen('http://local.wnep.com/transfers/school.html')
	content = content.read()
	soup = BeautifulSoup(content)
	schools = soup.find_all("font",class_="orgname")
	statuses = soup.find_all("font",class_="status")
	time = soup.find("td",class_="timestamp")
	list = []
	counter = 0
	for school in schools:
		list.append((school.string, statuses[counter].string))
		counter = counter + 1
	print(time.string)
	printList(list)

def printList(list):
	if (len(list) > 0):
		for updates in list:
			print(updates[0],":",updates[1])

	else:
		print("No closings or delays found.")

main()
