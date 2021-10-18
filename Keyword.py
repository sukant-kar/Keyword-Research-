import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()
trends.build_payload(kw_list=["Data Science"])
data = trends.interest_by_region()
print(data.sample(10))
data = trends.trending_searches(pn="india")
print(data.head(10))
keyword = trends.suggestions(keyword="Programming")
data = pd.DataFrame(keyword)
print(data.head())
