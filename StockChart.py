import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
import yfinance as yf
import plotly.express as px

###########################
#### the following is the side bar

st.sidebar.header('Simple Stock Chart :chart:')

symbol = st.sidebar.text_input('Enter Symbol', 'AAPL')
start_date = st.sidebar.date_input('Start Date', dt.date(2020, 1, 1))
end_date = st.sidebar.date_input('End Date')
# sub_button = st.sidebar.button ('Click to get stock price')

#################   main pannel 
st.subheader (f"{symbol} :wave:")

if True :
	# data =yf.download (symbol, start=start_date, end= end_date)
	ticker = yf.Ticker (symbol)
	data = ticker.history( start=start_date, end= end_date )
	# st.dataframe (data)
	fig = px.line (data, x=data.index, y=data['Close'], title = symbol)
	st.plotly_chart(fig)
	# st.dataframe (data)

	pricing_date, fundamental, news = st.tabs(['Pricing', 'Fundamental','News'])

	with pricing_date:
		st.header ('price movements')
		data2 = data
		data2['% Change'] =data['Close']/data['Close'].shift(1) -1
		data2.dropna(inplace = True)
		# st.write (data2)
		annual_return = data2['% Change'].mean()*252*100
		stdev = np.std (data2['% Change']) *np.sqrt(252)*100
		st.write('Annualized Return is:', annual_return, '%')
		st.write('Annualized Standard Deviation is:', stdev, '%')
		st.dataframe (data2)

	with fundamental:
		# ticker = yf.Ticker (symbol)
		income_stmt = ticker.get_income_stmt()
		st.write (income_stmt)
		st.write (ticker.balance_sheet)

	with news:
		try:
			news_one = ticker.news[0]
		except Exception as e:
			print(f"Failed to fetch news: {e}")
			news_one = 'can not find news'

		# for i in range (5):
		# 	news_one = ticker.news[i]
		# 	# st.subheader (news_one ['title'])
		# 	# st.write (news_one ['link'])
		# 	st.write (news_one)
		
		st.write (news_one)
		# st.write (type(ticker.news[0]))