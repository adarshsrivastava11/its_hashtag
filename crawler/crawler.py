import requests
from crawler.models import *

def crawl(graph_url):
    r = requests.get(graph_url)
    response = r.json()
    while 
        for a in response["data"]:
            time = a["created_time"]
            post_id = a["id"]
            url_likes = "graph.facebook.com/%s/likes?key=value&access_token=176565146081574|9f55220446aa4c2d44560f2ebde2430b&summary=true" %post_id
            r = request.get(url_likes)
            response_likes = r.json()
            summary = response["summary"]
            no_of_likes = summary["total_count"]
            data = post_info(message=message,time=time,story=story,id=post_id,no_of_likes = no_of_likes)
            data.save()
        redir_url = response["paging"]["next"]
        r = requests.get(redir_url)
