# В разработке...
import requests
from flask import Flask
from flask import request
from flask import jsonify
# import bitcoinrpc
# import pyTelegramBotAPI
# import json
import telebot
from telebot import types
from flask_sslify import SSLify
# import random
import MySQLdb
# import mysqlclient
import pymysql.cursors
from blockchain.wallet import Wallet
import os



token = '377736641:AAHm8BrhKN_nS7bNs1LqAsPus4ts5V-DsSc'
URL = 'https://api.telegram.org/bot' + token + '/'
# https://api.telegram.org/bot377736641:AAHm8BrhKN_nS7bNs1LqAsPus4ts5V-DsSc/setWebhook?url=https://netr153.pythonanywhere.com/
app = Flask(__name__)
sslify = SSLify(app)
bot = telebot.TeleBot(token)


def button(chat_id):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Обмен', 'Кошелёк']])
    bot.send_message(chat_id, "Бот в разработке.", reply_markup=keyboard)


def send_message(chat_id, text):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


def walletbuttons(chat_id, bal):
    keyboard = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Пополнение баланса", callback_data="send")
    keyboard.add(callback_button)
    button2 = telebot.types.InlineKeyboardButton(text="Вывод", callback_data="sendback")
    keyboard.add(button2)
    bot.send_message(chat_id, "Ваш баланс: "+str(bal), reply_markup=keyboard)


def tradebuttons(chat_id):
    keyboard = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Создать обмен", callback_data="create_trade")
    keyboard.add(callback_button)
    button2 = telebot.types.InlineKeyboardButton(text="Найти обмен", callback_data="find_trade")
    keyboard.add(button2)
    bot.send_message(chat_id, str("Функция пока не работает"), reply_markup=keyboard)


# Listing addresses (важная функция)
def answer(chat_id, message):   # функция,обрабатывающая сообщение.
    if message == "test":
        send_message(chat_id, "test_answer")
    elif message == "/start":
        send_message(chat_id, "Здравствуйте.")
        button(chat_id)
    elif message == "Обмен":
        # send_message(chat_id, "Эта функция в разработке")
        tradebuttons(chat_id)
        
    elif message == "Кошелёк":
        send_message(chat_id, "Функция в разработке")
        UserInfo = databasefuncSelect(chat_id)
        if UserInfo == "нет информации":
            wallet = Wallet('d636749b-77ea-400d-b46c-a4c3a73961c1', 'TvIsT666', 'http://127.0.0.1:3000', '0947a1c1-69aa-4e00-a74b-01bc5d05df07')
            # send_message(chat_id, "wallet test")             
            send_message(chat_id, wallet)
            try:                            # a tyt net))
                newaddr = wallet.new_address(chat_id)
                # newaddr = newaddr['address']
                send_message(chat_id, newaddr)
                # databasefunc(chat_id, newaddr, 0, 0)
            except:
                send_message(chat_id, "create_address problem")
        walletbuttons(chat_id, 0)  # заместо 0 поставить balance, который будет получаться из б.д.
    elif message == "send":
        send_message(chat_id,"Эта функция пока не работает")
    elif message == "sendback":
        send_message(chat_id, "Эта функция пока не работает")
    elif message == "find_trade":
        send_message(chat_id, "Эта функция пока не работает")
    elif message == "create_trade":
        send_message(chat_id, "Эта функция пока не работает")
        # получение переменной balance из базы данных.
        #
    elif message == "select db_info":
        databasefuncSelect(chat_id)
    elif message == "my_chat_id":
        send_message(chat_id,"your chat_id: " + str(chat_id))
    # elif message == "createdb":
        # databasecreate(chat_id)
    # elif message == "dropdb":
        # droptable(chat_id)
    else:
        send_message(chat_id,"Неизвестная команда:" + message)
        # создание адресов (new address)
        # walletbuttons(chat_id, 0)
    return


def databasefunc(chat_id, wallet_id, balance, adressbal):
    connection = pymysql.connect(host="us-cdbr-iron-east-04.cleardb.net", user="b955e96665f0be", password="9078e623", db="heroku_4bf54ea004008da", charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    # send_message(chat_id, "TEST")
    # connection.commit()
    cursor = connection.cursor()
    sql = "Insert into USER_INFO(id, wallet, balance, adressbal) values(%s, %s, %s, %s)"
    try:
        cursor.execute(sql, (chat_id, wallet_id, balance, adressbal))
        connection.commit()
    except(SyntaxError):
        send_message(chat_id, "SyntaxError")
    connection.close()
'''


def databasecreatetable(chat_id):
    connection = pymysql.connect(host="us-cdbr-iron-east-04.cleardb.net", user="b955e96665f0be", password="9078e623", db="heroku_4bf54ea004008da", charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    sql = "CREATE TABLE USER_INFO ( user_id VARCHAR(20), wallet_id VARCHAR(25), balance VARCHAR(30), address_balance VARCHAR(30))"
    try:
        cursor.execute(sql)
        connection.commit
        send_message(chat_id, "Таблица создана")
    except():
        send_message(chat_id, "syntaxError")
    connection.close
  
    
def droptable(chat_id):
    connection = pymysql.connect(host="us-cdbr-iron-east-04.cleardb.net", user="b955e96665f0be", password="9078e623", db="heroku_4bf54ea004008da", charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    sql = "DROP TABLE USER_INFO"  
    try:
        cursor.execute(sql)
        connection.commit
        send_message(chat_id, "Таблица удалена")
    except():
        send_message(chat_id, "syntaxError")
    connection.close
'''


def databasefuncSelect(chat_id):         #  получение строки из б.д  с chat_id
    connection = pymysql.connect(host="us-cdbr-iron-east-04.cleardb.net", user="b955e96665f0be", password="9078e623", db="heroku_4bf54ea004008da", charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    # sql = "Select * from TEST;"
    sql = "Select * from USER_INFO;"
    try:
        cursor.execute(sql)
        rowdata = cursor.fetchall()
        for record in rowdata:
            # id = record['USER_ID']
            id = record['id']
            if str(chat_id) == str(id) :
                send_message(chat_id, record)
                connection.close
                return record
            # else:
                # message = str(chat_id) + " != " + str(id)
                # send_message(chat_id, message)
                # send_message(chat_id, "wait")
            # send_message(chat_id, record)
    except(SyntaxError):
        send_message(chat_id, "SyntaxError")
    connection.close
    none = "нет информации"
    return none


def database_updatefunc(balance, chat_id):
    connection = pymysql.connect(host="us-cdbr-iron-east-04.cleardb.net", user="b955e96665f0be", password="9078e623", db="heroku_4bf54ea004008da", charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    sql = "Update USER_INFO set balance = %s where id = %s;"
    cursor.execute(sql, (balance, chat_id))  # код останавливается на этой строке
    # send_message(chat_id, "test123_update")
    connection.commit()
    connection.close()

    
def database_updatefunc2(balance, chat_id):
    connection = pymysql.connect(host="us-cdbr-iron-east-04.cleardb.net", user="b955e96665f0be", password="9078e623", db="heroku_4bf54ea004008da", charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    sql = "Update USER_INFO set adress_balance = %s where id = %s;"
    cursor.execute(sql, (balance, chat_id))
    # send_message(chat_id, "test123_update")
    connection.commit()
    connection.close()    


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        try:
            chat_id = r['message']['chat']['id']
            message = r['message']['text']
            i = 1
        except(KeyError):
            try:
                chat_id = r['callback_query']['from']['id']
                message = r['callback_query']['data']
                i = 0
            except:
                i = 3
        if i != 3:
            answer(chat_id, message)
            if i == 1:
                # database_updatefunc(message, chat_id)
                pass
                # databasefunc(chat_id, message)
            return jsonify(r)
    else:
        return '<h1>hello from bot</h1>'


def main():
    pass


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)


# setaccount
# getnewaddress
