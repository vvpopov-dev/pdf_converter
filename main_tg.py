'''БОТ ПРЕДЛОЖКА'''


from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# from db import Database


token = '5433300427:AAHv91cBjfhh1aDNFa1YUXKmN9GKKbffW50'
chat = '@testbotlt123'
chat_ban = '@bantestbotlt123'
bot = Bot(token=token)
dp = Dispatcher(bot)
admin = ('254520309', '1824608884')
# db = Database('database.db')
dict = {}
blacklist = []


'''АДМИН-ПАНЕЛЬ'''


@dp.message_handler(commands=['ban'])
async def ban(message: types.Message):
    mes = str(message.from_user.id)
    if mes in admin:
        try:
            abuser_id = int(message.get_args())
        except(ValueError, TypeError):
            return await message.answer('Неверно введен ид')

        blacklist.append(abuser_id)
        await message.reply(f"Пользователь {abuser_id} заблокирован.")
    else:
        await message.reply('Данная команда только для администрации!')


@dp.message_handler(commands=['unban'])
async def unban(message: types.Message):
    mes = str(message.from_user.id)
    if mes in admin:
        try:
            abuser_id = int(message.get_args())
        except(ValueError, TypeError):
            return await message.answer('Неверно введен ид')

        blacklist.remove(abuser_id)
        await message.reply(f"Пользователь {abuser_id} разблокирован.")
    else:
        await message.reply('Данная команда только для администрации!')


@dp.message_handler(commands=['sendall'])
async def start(message: types.Message):
    mes = str(message.from_user.id)
    if mes in admin:
        text = message.text[9:]
        # users = db.get_users()
        # for row in users:
            # try:
            #     await bot.send_message(row[0], text)
            #     if int(row[1]) != 1:
            #         db.set_active(row[0], 1)
            # except:
            #     db.set_active(row[0], 0)

        await message.answer('Рассылка завершена.')


'''ПОЛЬЗОВАТЕЛЬСКАЯ ПАНЕЛЬ'''


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    btn_ru = KeyboardButton('🇷🇺Русский🇷🇺')
    btn_en = KeyboardButton('🇬🇧English🇬🇧')
    btn_es = KeyboardButton('🇪🇸Español🇪🇸')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(btn_ru).insert(btn_en).add(btn_es)
    # if not db.user_exists(message.from_user.id):
    #     db.add_user(message.from_user.id)
    await message.answer('Выберите язык:\nChoose language:\nElige lengua:', reply_markup=keyboard)


@dp.message_handler()
async def language(message: types.Message):
    btn_ru = KeyboardButton('🇷🇺Русский🇷🇺')
    btn_en = KeyboardButton('🇬🇧English🇬🇧')
    btn_es = KeyboardButton('🇪🇸Español🇪🇸')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(btn_ru).insert(btn_en).add(btn_es)
    lang = message.text
    user = int(message.from_user.id)
    dict[user] = lang
    if user in blacklist:
        if lang == '🇷🇺Русский🇷🇺':
            await message.answer('Привет!! я бот для предложки. Если ты отправишь мне контент для нашего канала, то в скором времени я выложу твои файлы в наш канал. мы благодарны каждому подписчику за каждый файл.\n\nпожалуйста отправляй мне только хентай контент и ничего кроме хентай контента. \nлоли, милфы, трап и так далее.')
        elif lang == '🇬🇧English🇬🇧':
            await message.answer('Hi!! I\'m a suggestion bot. If you send me content for our channel, then soon I will upload your files to our channel. we are grateful to every subscriber for every file.\n\nplease only send me hentai content and nothing but hentai content.\nloli, milf, trap and so on.')
        elif lang == '🇪🇸Español🇪🇸':
            await message.answer('¡¡Hola!! Soy un robot de sugerencias. Si me envía contenido para nuestro canal, pronto subiré sus archivos a nuestro canal. estamos agradecidos a cada suscriptor por cada archivo.\n\npor favor solo envíeme contenido hentai y nada más que contenido hentai.\nloli, milf, trampa, etc.')
    else:
        if lang == '🇷🇺Русский🇷🇺':
            await message.answer(
                'Привет!! я бот для предложки. Если ты отправишь мне контент для нашего канала, то в скором времени я выложу твои файлы в наш канал. мы благодарны каждому подписчику за каждый файл.\n\nпожалуйста отправляй мне только хентай контент и ничего кроме хентай контента. \nлоли, милфы, трап и так далее.')
        elif lang == '🇬🇧English🇬🇧':
            await message.answer(
                'Hi!! I\'m a suggestion bot. If you send me content for our channel, then soon I will upload your files to our channel. we are grateful to every subscriber for every file.\n\nplease only send me hentai content and nothing but hentai content.\nloli, milf, trap and so on.')
        elif lang == '🇪🇸Español🇪🇸':
            await message.answer(
                '¡¡Hola!! Soy un robot de sugerencias. Si me envía contenido para nuestro canal, pronto subiré sus archivos a nuestro canal. estamos agradecidos a cada suscriptor por cada archivo.\n\npor favor solo envíeme contenido hentai y nada más que contenido hentai.\nloli, milf, trampa, etc.')


@dp.message_handler(content_types=['photo'])
async def photo(message: types.Message):
    name = message.from_user.username
    ph = message.photo[-1].file_id
    user = int(message.from_user.id)
    lang = dict[message.from_user.id]
    if user in blacklist:
        if lang == '🇷🇺Русский🇷🇺':
            await message.answer('Большое спасибо за материал!')
        elif lang == '🇬🇧English🇬🇧':
            await message.answer('Thank you very much for the material!')
        elif lang == '🇪🇸Español🇪🇸':
            await message.answer('¡Muchas gracias por el material!')
        await bot.send_photo(chat_ban, ph, caption=f'Фотография от {name}, {user}')
    else:
        if lang == '🇷🇺Русский🇷🇺':
            await message.answer('Большое спасибо за материал!')
        elif lang == '🇬🇧English🇬🇧':
            await message.answer('Thank you very much for the material!')
        elif lang == '🇪🇸Español🇪🇸':
            await message.answer('¡Muchas gracias por el material!')
        await bot.send_photo(chat, ph, caption=f'Фотография от {name}, {user}')


@dp.message_handler(content_types=['video'])
async def video(message: types.Message):
    name = message.from_user.username
    
    vi = message.video.file_id
    lang = dict[message.from_user.id]
    user = int(message.from_user.id)
    if user in blacklist:
        if lang == '🇷🇺Русский🇷🇺':
            await message.answer('Большое спасибо за материал!')
        elif lang == '🇬🇧English🇬🇧':
            await message.answer('Thank you very much for the material!')
        elif lang == '🇪🇸Español🇪🇸':
            await message.answer('¡Muchas gracias por el material!')
        await bot.send_photo(chat_ban, vi, caption=f'Видеозапись от {name}, {user}')
    else:
        if lang == '🇷🇺Русский🇷🇺':
            await message.answer('Большое спасибо за материал!')
        elif lang == '🇬🇧English🇬🇧':
            await message.answer('Thank you very much for the material!')
        elif lang == '🇪🇸Español🇪🇸':
            await message.answer('¡Muchas gracias por el material!')
        await bot.send_video(chat, vi, caption=f'Видеозапись от {name}')


@dp.message_handler(content_types=['document'])
async def doc(message: types.Message):
    name = message.from_user.username
    doc = message.document.file_id
    lang = dict[message.from_user.id]
    user = int(message.from_user.id)
    if user in blacklist:
        if lang == '🇷🇺Русский🇷🇺':
            await message.answer('Большое спасибо за материал!')
        elif lang == '🇬🇧English🇬🇧':
            await message.answer('Thank you very much for the material!')
        elif lang == '🇪🇸Español🇪🇸':
            await message.answer('¡Muchas gracias por el material!')
        await bot.send_photo(chat_ban, doc, caption=f'Документ от {name}, {user}')
    else:
        if lang == '🇷🇺Русский🇷🇺':
            await message.answer('Большое спасибо за материал!')
        elif lang == '🇬🇧English🇬🇧':
            await message.answer('Thank you very much for the material!')
        elif lang == '🇪🇸Español🇪🇸':
            await message.answer('¡Muchas gracias por el material!')
        await bot.send_video(chat, doc, caption=f'Документ от {name}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)