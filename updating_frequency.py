import datetime
import advertools as adv
import pandas as pd

br_sitemap = adv.sitemap_to_df('https://www.bankrate.com/sitemap/sitemap-index.xml')

br_sitemap['lastmod']= pd.to_datetime(br_sitemap['lastmod'])
br_sitemap['month'] = br_sitemap['lastmod'].dt.month
br_sitemap['month'] = br_sitemap['month'].apply(lambda x: pd.to_datetime(str(x), format='%m').strftime('%B'))
br_sitemap=br_sitemap.assign(month=br_sitemap['month'])

br_sitemap.groupby('month')['loc'].count().plot(legend=True)