import bs4 as bs
import urllib.request
from twilio.rest import Client


#  preset values
#  actual values are crossed out for privacy of course

ACCOUNT_SID = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
AUTH_TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
MY_NUMBER = "+1------4059"
TWILIO_NUMBER= "+1------5207"
WEATHER_PROMPT = "Binghamton is "


#  sends text to my number
def sendText(message):
  twilioCli = Client(ACCOUNT_SID, AUTH_TOKEN)
  twilioCli.messages.create(body=message, from_=TWILIO_NUMBER, to=MY_NUMBER)


def main():
  #  scrapes for weather
  sauce = urllib.request.urlopen('https://weather.com/weather/today/l/42.10,-75.92?temp=f&par=google').read()

  soup = bs.BeautifulSoup(sauce, 'lxml')

  body = soup.body

  bingWeather = body.find('div', class_ = "today_nowcard-temp").text
  bingFeelsLike = body.find('div', class_ = "today_nowcard-feels").text.lower()

  #  sends weather to me
  sendText(WEATHER_PROMPT + bingWeather + " but " + bingFeelsLike)


main()
