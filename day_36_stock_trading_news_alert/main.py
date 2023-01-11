import config
import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"
# COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": config.alpha_api_key,
}
response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]

stock_prices = [value for (key, value) in stock_data.items()]
yesterday_price = stock_prices[0]["4. close"]


# TODO 2. - Get the day before yesterday's closing stock price

day_before_yesterday_price = stock_prices[1]["4. close"]


# test values 👇🏾
# yesterday_price = 120
# day_before_yesterday_price = 200


# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
yesterday_price = int(float(yesterday_price))
day_before_yesterday_price = int(float(day_before_yesterday_price))


print(yesterday_price - day_before_yesterday_price)


def price_increased():
    return yesterday_price - day_before_yesterday_price > 0


# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
def percentage():
    return int(
        abs(yesterday_price - day_before_yesterday_price)
        / ((yesterday_price + day_before_yesterday_price) / 2)
        * 100
    )


print(percentage())


# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


news_params = {"q": COMPANY_NAME, "apiKey": config.news_api_key}

news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
news_response.raise_for_status()
news_articles = news_response.json()["articles"]

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
articles = [news_articles[article] for article in range(3)]
# article_title = articles[0]["title"]
# article_desc = articles[0]["description"]
# print(articles)


account_sid = config.twilio_account_sid
auth_token = config.twilio_auth_token

percent = percentage()

if percentage() >= 5 and price_increased():

    for article in range(len(articles)):
        article_title = articles[article]["title"]
        article_desc = articles[article]["description"]
        # body = f"{STOCK_NAME}: 🔺{int(percent)}%\nHeadline: {article_title}.\nBrief: {article_desc}"
        # print(body)

        # TODO 9. - Send each article as a separate message via Twilio. s

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"{STOCK_NAME}: 🔺{int(percent)}%\nHeadline: {article_title}.\nBrief: {article_desc}",
            from_=config.twilio_phone_num,
            to=config.my_phone_num,
        )
        print(message.status)
elif percentage() > 5 and not price_increased():
    for article in range(len(articles)):
        article_title = articles[article]["title"]
        article_desc = articles[article]["description"]
        # body = f"{STOCK_NAME}: 🔻{int(percent)}%\nHeadline: {article_title}.\nBrief: {article_desc}"
        # print(body)

        # TODO 9. - Send each article as a separate message via Twilio. s

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"{STOCK_NAME}: 🔻{int(percent)}%\nHeadline: {article_title}.\nBrief: {article_desc}",
            from_=config.twilio_phone_num,
            to=config.my_phone_num,
        )
        print(message.status)


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
