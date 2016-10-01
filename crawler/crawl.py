import requests
from crawler.models import *

def crawl(graph_url):
    r = requests.get(graph_url)
    response = r.json()
    while response["data"]!=[]: 
        for a in response["data"]:
            time = a["created_time"]
            post_id = a["id"]
            message = a["message"]
            url_likes = "https://graph.facebook.com/%s/likes?key=value&access_token=176565146081574|9f55220446aa4c2d44560f2ebde2430b&summary=true" %post_id
            print url_likes
            r = requests.get(url_likes)
            response_likes = r.json()
            summary = response_likes["summary"]
            no_of_likes = summary["total_count"]
            data = post_info(message=message,time=time,id=post_id,no_of_likes = no_of_likes)
            data.save()
        redir_url = response["paging"]["next"]
        r = requests.get(redir_url)

