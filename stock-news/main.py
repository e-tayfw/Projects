import os
import requests
import datetime
from twilio.rest import Client
import html

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

account_sid = "AC30247b98e6a49b194a5caddfea8500db"
auth_token = os.environ.get("AUTH_TOKEN")

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": STOCK_API_KEY,
}

news_parameters = {"q": COMPANY_NAME, "apiKey": NEWS_API_KEY}

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
# HINT 2: Work out the value of 5% of yerstday's closing stock price.

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()


date_now = datetime.datetime.now()
yesterday = (date_now - datetime.timedelta(days=1)).date()
day_before_ytd = (date_now - datetime.timedelta(days=2)).date()

closing_ytd_price = float(stock_data["Time Series (Daily)"][str(yesterday)]["4. close"])
closing_day_b4_ytd_price = float(
    stock_data["Time Series (Daily)"][str(day_before_ytd)]["4. close"]
)

diff = closing_ytd_price - closing_day_b4_ytd_price
percentage_diff = round(diff / closing_ytd_price * 100, 0)
if abs(percentage_diff) <= 5.00:
    ## STEP 2: Use https://newsapi.org/docs/endpoints/everything
    # Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
    # HINT 1: Think about using the Python Slice Operator
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    top_3_articles = news_data["articles"][0:3]

    for article in top_3_articles:
        ## STEP 3: Use twilio.com/docs/sms/quickstart/python
        # Send a separate message with each article's title and description to your phone number.
        
        if percentage_diff > 0:
            str_percentage = f"🔺{abs(percentage_diff)}%"
        else:
            str_percentage = f"🔻{abs(percentage_diff)}%"
        message = f"{COMPANY_NAME}: {str_percentage}\nHeadline: {article['title']}\nBrief: {article['description']}"
        formatted_msg = html.unescape(message)
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=formatted_msg,
            from_="+14157669096",
            to="+6591690715",
        )
        print(message.status)


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
