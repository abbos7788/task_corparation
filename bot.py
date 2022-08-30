from config import TOKEN 
import logging
from aiogram import Bot, Dispatcher, executor, types
from button import *
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="nazarov_7788",
  port="3306",
  database="youtube"
)

cursor = db.cursor()
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())





@dp.message_handler(text="✅ Sending")
async def sending(message: types.Message):
    sql = "SELECT * FROM user_data WHERE user_id ='{}'".format(f"{message['chat']['id']}")
    cursor.execute(sql)
    myresult = cursor.fetchall()
    res = f"<b>User name: @{myresult[0][1]}\nName: {myresult[0][2]}\n\nSuggestions: {myresult[0][4]}\n</b>"
    for k in myresult:
        res += f"<b>Comment: {k[3]}</b>\n"
    await message.answer(res, parse_mode="HTML", reply_markup=bosh_sahifa_1)
    await message.answer(f"<b>Thank you for your feedback. This will improve our company overall performance and make to build our strong competitive advantage!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_1)
    sql = f"DELETE FROM user_data WHERE user_id = '{message.chat.id}'"
    cursor.execute(sql)
    db.commit()



@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("""Enter the Menu!""" , parse_mode = 'HTML', reply_markup=bosh_sahifa)

@dp.message_handler(text="🔰 Menu")
async def menu_1(message: types.Message):
    await message.answer("""<b>Welcome to the Menu!</b>\n<i>Choose one of them!</i>""" , parse_mode = 'HTML', reply_markup=bosh_sahifa_1)


@dp.message_handler(text="📑 About Company")
async def menu_1(message: types.Message):
    await message.answer("""<b>Task Corporation- Delivering New Solutions!</b>""" , parse_mode = 'HTML', reply_markup=bosh_sahifa_1)
    await message.answer("""<b>
Provider of modern transportation services since 2014, has offered a full range of transportation and logistic services to meet all the needs of modern businesses.


📍 Location: Aurora, IL
☎️ Contact: 224-704-0004</b>""" , parse_mode = 'HTML', reply_markup=bosh_sahifa_1)


class Auth(StatesGroup):
    name = State()
    text_bot_1 = State()
    text_bot_2 = State()
    text_bot_3 = State()

@dp.message_handler(text="📩 Survey (comments or suggestions)", state="*")
async def on_start_2(message: types.Message, state: FSMContext):
    # await state.reset_state(with_data=True)
    await message.answer(f"""<b>Your responses to this survey will be kept confidential and anonymous. 
Whom do you give feedback to?
Write down the name of employee you want to comment:</b>""", parse_mode="HTML")
    await message.answer(f"""<b>-Name </b>""", parse_mode="HTML", reply_markup=types.ReplyKeyboardRemove())
    await Auth.name.set()

@dp.message_handler(state=Auth.name)
async def name(message: types.Message, state: FSMContext):
    name = message.text
    if name.isdigit():
        await message.answer(f"<b>Can't enter a number!</b>", parse_mode="HTML")

    else:
        await state.update_data(name=name)
        await message.answer(f"<b>Please, Choose min 2 or more comments about him or her</b>", parse_mode="HTML", reply_markup=bosh_sahifa_2_0)
        await Auth.text_bot_1.set()

@dp.message_handler(state=Auth.text_bot_1)
async def text_bot_1(message: types.Message, state: FSMContext):
    text_bot_1 = message.text
    if text_bot_1.isdigit():
        await message.answer(f"<b>Can't enter a number!</b>", parse_mode="HTML")

    else:
        await state.update_data(text_bot_1=text_bot_1)
        await message.answer(f"<b>Tell us what should we fix or improve about this person?</b>",parse_mode="HTML", reply_markup=types.ReplyKeyboardRemove())
        await Auth.text_bot_2.set()

@dp.message_handler(state=Auth.text_bot_2)
async def text_bot_2(message: types.Message, state: FSMContext):
    text_bot_2 = message.text
    if text_bot_2.isdigit():
        await message.answer(f"<b>Can't enter a number!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_bot_2=text_bot_2)
        db.commit()
        global data
        data = await state.get_data()
        sql = "INSERT INTO user_data (user_id, user_name, name, comment, suggestions) VALUES (%s, %s, %s, %s, %s)"
        val = ("5073296253", f"{message.from_user.username}", f"{data.get('name')}", f"{data.get('text_bot_1')}", f"{data.get('text_bot_2')}")
        cursor.execute(sql, val)
        # await message.answer(f"""<b>From whom: {data.get('name')}\nUser name: @{message.from_user.username}\n\nComplaint: {data.get('text_bot_1')}\nSuggestions: {data.get('text_bot_2')}</b>""", parse_mode="HTML", reply_markup=bosh_sahifa_2)                      
        await message.answer(f"<b>Have another suggestion?</b>", parse_mode="HTML", reply_markup=bosh_sahifa_2)
        await state.reset_state(with_data=True)






@dp.message_handler(text="✓ Bad communication skill with drivers")
async def menu_01(message: types.Message):
    sql = "INSERT INTO user_data (user_id, user_name, name, comment, suggestions) VALUES (%s, %s, %s, %s, %s)"
    val = (f"{message.chat.id}", f"{message.from_user.username}", f"{data.get('name')}", f"✓ Bad communication skill with drivers", f"{data.get('text_bot_2')}")
    cursor.execute(sql, val)
    await message.answer("""<b>Joined</b>""" , parse_mode = 'HTML', reply_markup=bosh_sahifa_2)

@dp.message_handler(text="✓ Late response in group, email and phone calls")
async def menu_02(message: types.Message):
    sql = "INSERT INTO user_data (user_id, user_name, name, comment, suggestions) VALUES (%s, %s, %s, %s, %s)"
    val = (f"{message.chat.id}", f"{message.from_user.username}", f"{data.get('name')}", f"✓ Late response in group, email and phone calls", f"{data.get('text_bot_2')}")
    cursor.execute(sql, val)
    await message.answer("""<b>Joined</b>""" , parse_mode = 'HTML', reply_markup=bosh_sahifa_2)

@dp.message_handler(text="✓ Does not follow company rules")
async def menu_03(message: types.Message):
    sql = "INSERT INTO user_data (user_id, user_name, name, comment, suggestions) VALUES (%s, %s, %s, %s, %s)"
    val = (f"{message.chat.id}", f"{message.from_user.username}", f"{data.get('name')}", f"✓ Does not follow company rules", f"{data.get('text_bot_2')}")
    cursor.execute(sql, val)
    await message.answer("""<b>Joined</b>""" , parse_mode = 'HTML', reply_markup=bosh_sahifa_2)

@dp.message_handler(text="✓ Does not leave important notes or comments about issues")
async def menu_04(message: types.Message):
    sql = "INSERT INTO user_data (user_id, user_name, name, comment, suggestions) VALUES (%s, %s, %s, %s, %s)"
    val = (f"{message.chat.id}", f"{message.from_user.username}", f"{data.get('name')}", f"✓ Does not leave important notes or comments about issues", f"{data.get('text_bot_2')}")
    cursor.execute(sql, val)
    await message.answer("""<b>Joined</b>""" , parse_mode = 'HTML', reply_markup=bosh_sahifa_2)



@dp.message_handler(text="✓ Can't communicate with vendors")
async def menu_05(message: types.Message):
    sql = "INSERT INTO user_data (user_id, user_name, name, comment, suggestions) VALUES (%s, %s, %s, %s, %s)"
    val = (f"{message.chat.id}", f"{message.from_user.username}", f"{data.get('name')}", f"✓ Can't communicate with vendors", f"{data.get('text_bot_2')}")
    cursor.execute(sql, val)
    await message.answer("""<b>Joined</b>""" , parse_mode = 'HTML', reply_markup=bosh_sahifa_2)

@dp.message_handler(text="✓ Poor communication with other departments")
async def menu_06(message: types.Message):
    sql = "INSERT INTO user_data (user_id, user_name, name, comment, suggestions) VALUES (%s, %s, %s, %s, %s)"
    val = (f"{message.chat.id}", f"{message.from_user.username}", f"{data.get('name')}", f"✓ Poor communication with other departments", f"{data.get('text_bot_2')}")
    cursor.execute(sql, val)
    await message.answer("""<b>Joined</b>""" , parse_mode = 'HTML', reply_markup=bosh_sahifa_2)

@dp.message_handler(text="✓ Not goal-oriented employee")
async def menu_07(message: types.Message):
    sql = "INSERT INTO user_data (user_id, user_name, name, comment, suggestions) VALUES (%s, %s, %s, %s, %s)"
    val = (f"{message.chat.id}", f"{message.from_user.username}", f"{data.get('name')}", f"✓ Not goal-oriented employee", f"{data.get('text_bot_2')}")
    cursor.execute(sql, val)
    await message.answer("""<b>Joined</b>""" , parse_mode = 'HTML', reply_markup=bosh_sahifa_2)

@dp.message_handler(text="✓ Poor-motivated employee")
async def menu_08(message: types.Message):
    sql = "INSERT INTO user_data (user_id, user_name, name, comment, suggestions) VALUES (%s, %s, %s, %s, %s)"
    val = (f"{message.chat.id}", f"{message.from_user.username}", f"{data.get('name')}", f"✓ Poor-motivated employee", f"{data.get('text_bot_2')}")
    cursor.execute(sql, val)
    await message.answer("""<b>Joined</b>""" , parse_mode = 'HTML', reply_markup=bosh_sahifa_2)



@dp.message_handler(text="✓ Poor negotiation skills")
async def menu_09(message: types.Message):
    sql = "INSERT INTO user_data (user_id, user_name, name, comment, suggestions) VALUES (%s, %s, %s, %s, %s)"
    val = (f"{message.chat.id}", f"{message.from_user.username}", f"{data.get('name')}", f"✓ Poor negotiation skills", f"{data.get('text_bot_2')}")
    cursor.execute(sql, val)
    await message.answer("""<b>Joined</b>""" , parse_mode = 'HTML', reply_markup=bosh_sahifa_2)

@dp.message_handler(text="✓ Does not share his experience with new collegues")
async def menu_10(message: types.Message):
    sql = "INSERT INTO user_data (user_id, user_name, name, comment, suggestions) VALUES (%s, %s, %s, %s, %s)"
    val = (f"{message.chat.id}", f"{message.from_user.username}", f"{data.get('name')}", f"✓ Does not share his experience with new collegues", f"{data.get('text_bot_2')}")
    cursor.execute(sql, val)
    await message.answer("""<b>Joined</b>""" , parse_mode = 'HTML', reply_markup=bosh_sahifa_2)

@dp.message_handler(text="✓ Can't communicate with brokers")
async def menu_11(message: types.Message):
    sql = "INSERT INTO user_data (user_id, user_name, name, comment, suggestions) VALUES (%s, %s, %s, %s, %s)"
    val = (f"{message.chat.id}", f"{message.from_user.username}", f"{data.get('name')}", f"✓ Can't communicate with brokers", f"{data.get('text_bot_2')}")
    cursor.execute(sql, val)
    await message.answer("""<b>Joined</b>""" , parse_mode = 'HTML', reply_markup=bosh_sahifa_2)

@dp.message_handler(text="✓ Bad planing in pick up and delivery")
async def menu_12(message: types.Message):
    sql = "INSERT INTO user_data (user_id, user_name, name, comment, suggestions) VALUES (%s, %s, %s, %s, %s)"
    val = (f"{message.chat.id}", f"{message.from_user.username}", f"{data.get('name')}", f"✓ Bad planing in pick up and delivery", f"{data.get('text_bot_2')}")
    cursor.execute(sql, val)
    await message.answer("""<b>Joined</b>""" , parse_mode = 'HTML', reply_markup=bosh_sahifa_2)




@dp.message_handler(text="✓ Frequent canceling loads")
async def menu_13(message: types.Message):
    sql = "INSERT INTO user_data (user_id, user_name, name, comment, suggestions) VALUES (%s, %s, %s, %s, %s)"
    val = (f"{message.chat.id}", f"{message.from_user.username}", f"{data.get('name')}", f"✓ Frequent canceling loads", f"{data.get('text_bot_2')}")
    cursor.execute(sql, val)
    await message.answer("""<b>Joined</b>""" , parse_mode = 'HTML', reply_markup=bosh_sahifa_2)

@dp.message_handler(text="✓ Does not offer best/ extra/future loads to collegues")
async def menu_14(message: types.Message):
    sql = "INSERT INTO user_data (user_id, user_name, name, comment, suggestions) VALUES (%s, %s, %s, %s, %s)"
    val = (f"{message.chat.id}", f"{message.from_user.username}", f"{data.get('name')}", f"✓ Does not offer best/ extra/future loads to collegues", f"{data.get('text_bot_2')}")
    cursor.execute(sql, val)
    await message.answer("""<b>Joined</b>""" , parse_mode = 'HTML', reply_markup=bosh_sahifa_2)

@dp.message_handler(text="✓ Does not calculate RPM and CPM")
async def menu_15(message: types.Message):
    sql = "INSERT INTO user_data (user_id, user_name, name, comment, suggestions) VALUES (%s, %s, %s, %s, %s)"
    val = (f"{message.chat.id}", f"{message.from_user.username}", f"{data.get('name')}", f"✓ Does not calculate RPM and CPM", f"{data.get('text_bot_2')}")
    cursor.execute(sql, val)
    await message.answer("""<b>Joined</b>""" , parse_mode = 'HTML', reply_markup=bosh_sahifa_2)

@dp.message_handler(text="✓ Does not discuss dedicated loads with management")
async def menu_16(message: types.Message):
    sql = "INSERT INTO user_data (user_id, user_name, name, comment, suggestions) VALUES (%s, %s, %s, %s, %s)"
    val = (f"{message.chat.id}", f"{message.from_user.username}", f"{data.get('name')}", f"✓ Does not discuss dedicated loads with management", f"{data.get('text_bot_2')}")
    cursor.execute(sql, val)
    await message.answer("""<b>Joined</b>""" , parse_mode = 'HTML', reply_markup=bosh_sahifa_2)

@dp.message_handler(text="✓ Negative influencer of our company")
async def menu_17(message: types.Message):
    sql = "INSERT INTO user_data (user_id, user_name, name, comment, suggestions) VALUES (%s, %s, %s, %s, %s)"
    val = (f"{message.chat.id}", f"{message.from_user.username}", f"{data.get('name')}", f"✓ Negative influencer of our company", f"{data.get('text_bot_2')}")
    cursor.execute(sql, val)
    await message.answer("""<b>Joined</b>""" , parse_mode = 'HTML', reply_markup=bosh_sahifa_2)










if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)