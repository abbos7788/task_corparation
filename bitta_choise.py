# from config import TOKEN 
# import logging
# from aiogram import Bot, Dispatcher, executor, types
# from button import *
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.dispatcher import FSMContext
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.types import Message,CallbackQuery


# logging.basicConfig(level=logging.INFO)

# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot, storage=MemoryStorage())




# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     await message.answer("""Enter the Menu!""" , parse_mode = 'HTML', reply_markup=bosh_sahifa)

# @dp.message_handler(text="🔰 Menu")
# async def menu_1(message: types.Message):
#     await message.answer("""<b>Welcome to the Menu!</b>\n<i>Choose one of them!</i>""" , parse_mode = 'HTML', reply_markup=bosh_sahifa_1)


# @dp.message_handler(text="📑 About Company")
# async def menu_1(message: types.Message):
#     await message.answer("""<b>Task Corporation- Delivering New Solutions!</b>""" , parse_mode = 'HTML', reply_markup=bosh_sahifa_1)
#     await message.answer("""<b>
# Provider of modern transportation services since 2014, has offered a full range of transportation and logistic services to meet all the needs of modern businesses.


# 📍 Location: Aurora, IL
# ☎️ Contact: 224-704-0004</b>""" , parse_mode = 'HTML', reply_markup=bosh_sahifa_1)


# class Auth(StatesGroup):
#     name = State()
#     text_bot_1 = State()
#     text_bot_2 = State()
#     text_bot_3 = State()

# @dp.message_handler(text="📩 Survey (comments or suggestions)", state="*")
# async def on_start_2(message: types.Message, state: FSMContext):
#     # await state.reset_state(with_data=True)
#     await message.answer(f"""<b>Your responses to this survey will be kept confidential and anonymous. 
# Whom do you give feedback to?
# Write down the name of employee you want to comment:</b>""", parse_mode="HTML")
#     await message.answer(f"""<b>-Name </b>""", parse_mode="HTML", reply_markup=types.ReplyKeyboardRemove())
#     await Auth.name.set()

# @dp.message_handler(state=Auth.name)
# async def name(message: types.Message, state: FSMContext):
#     name = message.text
#     if name.isdigit():
#         await message.answer(f"<b>Can't enter a number!</b>", parse_mode="HTML")

#     else:
#         await state.update_data(name=name)
#         await message.answer(f"<b>Please, Choose min 2 or more comments about him or her</b>", parse_mode="HTML", reply_markup=bosh_sahifa_2)
#         await Auth.text_bot_1.set()

# @dp.message_handler(state=Auth.text_bot_1)
# async def text_bot_1(message: types.Message, state: FSMContext):
#     text_bot_1 = message.text
#     if text_bot_1.isdigit():
#         await message.answer(f"<b>Can't enter a number!</b>", parse_mode="HTML")

#     else:
#         await state.update_data(text_bot_1=text_bot_1)
#         await message.answer(f"<b>Tell us what should we fix or improve about this person?</b>",parse_mode="HTML", reply_markup=types.ReplyKeyboardRemove())
#         await Auth.text_bot_2.set()

# @dp.message_handler(state=Auth.text_bot_2)
# async def text_bot_2(message: types.Message, state: FSMContext):
#     text_bot_2 = message.text
#     if text_bot_2.isdigit():
#         await message.answer(f"<b>Can't enter a number!</b>", parse_mode="HTML")
#     else:
#         await state.update_data(text_bot_2=text_bot_2)
#         data = await state.get_data()
#         await message.answer(f"""<b>From whom: {data.get('name')}\nUser name: @{message.from_user.username}\n\nComplaint: {data.get('text_bot_1')}\nSuggestions: {data.get('text_bot_2')}</b>""", parse_mode="HTML", reply_markup=bosh_sahifa_1)                      
#         await message.answer(f"<b>Thank you for your feedback. This will improve our company overall performance and make to build our strong competitive advantage!</b>", parse_mode="HTML")
#         await state.reset_state(with_data=True)





# # @dp.message_handler(state=Auth.text_bot_2)
# # async def text_bot_2(message: types.Message, state: FSMContext):
# #     text_bot_2 = message.text
# #     if text_bot_2.isdigit():
# #         await message.answer(f"<b>Can't enter a number!</b>", parse_mode="HTML")
# #     else:
# #         await state.update_data(text_bot_2=text_bot_2)
# #         data = await state.get_data()
# #         await message.answer(f"""<b>From whom: {data.get('name')}\nUser name: @{message.from_user.username}\n\nTo whom: {data.get('text_bot_1')}\nComplaint: {data.get('text_bot_2')}</b>""", parse_mode="HTML", reply_markup=bosh_sahifa_1)                      
# #         await state.reset_state(with_data=True)


# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)