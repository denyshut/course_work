import telebot #Імпорт A Python implementation
import requests #impor библиотеки request
from config import token #import токена з BotFather


def telegram_bot():  # Функція виклику бота
    bot = telebot.TeleBot(token) # Присвоєння змінній bot token з BotFathe

    # При введенні команди '/start' привітаємося з користувачем.
    @bot.message_handler(commands=["start"]) #Дана функція відповідає  на команду /start
    def start_message(message):
        bot.send_message(message.chat.id, "Привіт, я LolBot.\nЩоб побачити що я вмію напиши: /help")

    # При введенні команди '/help' відкривається список доступних команд.
    @bot.message_handler(commands=["help"]) # Дана функція відповідає  на команду /help
    def help_message(message):
        bot.send_message(message.chat.id, "Список команд:\n/geo - визначення геолокації"
                                          "\n запитай мене:"
                                          "\n що ти хочеш робити сьогодні,"
                                          "\n який фільм переглянути")
    # При написанні команди '/geo' бот видає іформацію геолокації
    @bot.message_handler(commands=["geo"]) #Дана функція відповідає  на команду /geo
    def geo_message(message):
        rq = requests.get("https://freegeoip.app/json/")  # Link до API
        response = rq.json() # Список у форматі JSON
        ip_geo = response["ip"]  # Витягуєм інформацію з JSON
        country_geo = response["country_name"]
        zip_geo = response["zip_code"]
        city_geo = response["city"]
        bot.send_message(message.chat.id,
                         f"IP💻 :{ip_geo}\n"
                         f"Країна🗺: {country_geo}\n"
                         f"Код міста📄: {zip_geo}\n"
                         f"Місто🏘: {city_geo}")  # Відповідаєм на команду користувача

    @bot.message_handler(content_types=["text"]) # Даний message_handler після отримання повідомлення відповідає користувачеві
    def random_activity(message):
        if message.text.lower() == "що робити сьогодні":
            req = requests.get("http://www.boredapi.com/api/activity/")  # Link до API
            response = req.json() # Список у форматі JSON
            activity = response["activity"]
            type = response["type"]
            bot.send_message(message.chat.id,
                             f"You can🎭: {activity},\nIt is🗿: {type}")

        if message.text.lower() == "який фільм переглянути":
            url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/tt1375666"  # Link до API

            headers = {
                'x-rapidapi-key': "ce9a7ad3camsha86857eaf9a15b4p1bab97jsn7662ec455913",
                'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com"
            } # Ключі за допомогою яких ми авторизовуємся в API

            response = requests.request("GET", url, headers=headers)
            req = response.json() # Список у форматі JSON
            title = req["title"]
            year = req["year"]
            length = req["length"]
            rating = req["rating"]
            bot.send_message(message.chat.id,
                             f"Назва🎥: {title},\n"
                             f"Рік🔥: {year},\n"
                             f"Тривалість⏱: {length} \n"
                             f"Рейтинг💣: {rating}")

    bot.polling()


if __name__ == '__main__':
    telegram_bot() # Виклик бота
