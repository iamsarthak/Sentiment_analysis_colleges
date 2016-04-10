import requests
from bs4 import BeautifulSoup
def get_link(query):
	search_query=query.replace(' ' , '+')
	i=requests.get("https://www.youtube.com/results?sp=CAM%253D&q="+search_query)
	soup=BeautifulSoup(i.text)
	youtubelinks=soup.find_all("a")
	count=0;
	super_count=0;
	listofhref=[];	
	for links in youtubelinks:
		youtubehref=links.get('href')
		youtubehrefstring=str(youtubehref)
		if "/watch?v=" in youtubehrefstring:
			if youtubehrefstring not in listofhref:		
				listofhref.append(youtubehrefstring)
				super_count=super_count+1
				if(super_count<=3):
					print("the link to the  video is "+"www.youtube.com"+youtubehrefstring)
					print(embed_code(youtubehrefstring))	
						#for s in youtubehrefstring:
						#count=count+1;
						#if s=="=":
						
						#embedlink="https://www.youtube.com/embed/"+youtubehrefstring[count:]
						#print('<iframe width="420" height="315" src="'+embedlink+'"frameborder="0" allowfullscreen></iframe>')
		
	return result_link

def embed_code(youtubehrefstring)
	count=0
	for s in youtubehrefstring:
		count=count+1;
		if s=="=":
			embedlink="https://www.youtube.com/embed/"+youtubehrefstring[count:]
			code='<iframe width="420" height="315" src="'+embedlink+'"frameborder="0" allowfullscreen></iframe>'
			break
	return code
#"&sp=CAM%253D"
