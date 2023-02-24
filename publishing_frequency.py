import advertools as adv
import pandas as pd

adv.crawl('https://www.bankrate.com/', 'bankrate.jl', follow_links=True,
          xpath_selectors ={'published_date': "//span[@class='type-body-two text-slate text-crop-none']/text()"}, # change this variable based on the XPath of the date's element
          custom_settings={'CLOSESPIDER_PAGECOUNT': 200}) #delete this variable since it was used to limit the number of pages to crawl

bankratet=pd.read_json('bankrate.jl', lines=True)
bankratet.to_csv('bankrate.csv')

bankratet=pd.read_csv('bankrate.csv')
cols=['published_date','url']
data=bankratet[cols]
data.to_csv('data.csv')

bankrate_dates=pd.read_csv('data.csv')
bankrate_dates=bankrate_dates.dropna()
bankrate_dates['published_date']=pd.to_datetime(bankrate_dates['published_date'])
bankrate_dates=bankrate_dates.sort_values(by='published_date')

bankrate_dates['month'] = bankrate_dates['published_date'].dt.month
bankrate_dates['month'] = bankrate_dates['month'].apply(lambda x: pd.to_datetime(str(x), format='%m').strftime('%B'))
bankrate_dates=bankrate_dates.assign(month=bankrate_dates['month'])

bankrate_dates.groupby('month')['url'].count().plot(legend=True)