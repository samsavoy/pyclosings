import urllib.request
from bs4 import BeautifulSoup

def main():
	content = urllib.request.urlopen('http://local.wnep.com/transfers/school.html')
	content = content.read()
	soup = BeautifulSoup(content)
	schools = soup.find_all("font", class_="orgname")
	statuses = soup.find_all("font",class_="status")
	list = []
	counter = 0
	for school in schools:
		list.append((school.string, statuses[counter].string))
		counter = counter + 1
	printList(list)

def printList(list):
	schools = []
	statuses = []
	for updates in list:
		schools.append(updates[0])
		statuses.append(updates[1])
		print(schools[-1],":", statuses[-1])

main()
