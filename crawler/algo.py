from crawler.models import *
from datetime import datetime

def nominalize(company_a, company_list):
    model_objects = post_info.objects.get(company=company_a)
    total = 0
    nominalized_likes = {company_a:{:}}
    for a in model_objects:
        total = a.no_of_likes + total
        nominalized_likes[company_a][a.id] = a.no_of_likes
        mean1 = total/float(len(model_objects))
    for b in company_list:
        nominalized_likes[b] = {:}
        model_objects = post_info.objects.get(company=b)
        total_l= 0
        for a in model_objects:
            total_l = a.no_of_likes + total_l
            mean2 = total_l/float(len(model_objects))
        for a in model_objects:
            likes = mean1*a.no_of_likes/mean2
            nominalized_likes[b][a.id] = likes
        return nominalized_likes

def predict(nominalized_likes, hashtag, company_list):
    now = datetime.now()
    total_weight = 0
    sigma_wn = 0
    model_objects = post_info.objects.all()
    days = 0
    for b in model_objects:
        category_list = b.category(',')
        if hastag in category_list:
            sigma_wn = sigma_wn + nominalized_likes[b.company][b.id]
            total_weight = total_weight + 2
            days = days + (2*(now.day - b.time.day))
            days = days + (2*30*(now.month - b.time.month))
            days = days + (2*365*(now.year - b.time.year))
        else:
            sigma_wn = sigma_wn + nominalized_likes[b.company][b.id]
            total_weight = total_weight + 1
            days = days + now.day - b.time.day
            days = days + 30*(now.month - b.time.month)
            days = days + 365*(now.year - b.time.year)
    mean_likes = sigma_wn/float(total_weight)
    mean_days = days/float(total_weight)
    return mean_likes, mean_days
