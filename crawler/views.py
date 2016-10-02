from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import redirect



from datetime import datetime 
from crawler.algo import * 
from crawler.crawl import * 

def main_page(request):
	projected_likes = 0
	projected_days = 0
	mean_like=0
	mean_days=0
	print "LLL"
	# company_url = "https://graph.facebook.com/antaragni.iitk/posts/?key=value&access_token=176565146081574|9f55220446aa4c2d44560f2ebde2430b"
	# crawl(company_url)
	list_companies = ["antaragni","ritambhara"]
	company_a = request.POST.get('company',False)
	hashtag = request.POST.get('hashtag',False)
	if company_a != False:
		print "post successful"
		nominalized_likes = nominalize(company_a,list_companies)
		mean_like,mean_days = predict(nominalized_likes,hashtag,list_companies)

	projected_likes = int(mean_like)
	projected_days = int(mean_days)





	return render(request,'index.html',{'projected_likes':projected_likes})
