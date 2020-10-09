# Deep Learning
from tensorflow import keras
import numpy as np

# Telegram-bot's base
from aiogram import Bot, Dispatcher, executor, types
import logging

# Image preprocessing
import cv2
from PIL import Image

# Clearing the RAM
import gc

# Getting the encoder
import pickle
with open(u"model/encoder", "rb") as f:
    OH = pickle.load(f)

# Set API_TOKEN. You must have your own.
API_TOKEN = ''

# Configure logging.
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher.
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Initialize the net.
model = keras.models.load_model('model/mobilenet/')

IMG_SIZE = 244  # const

"""Processing functions."""


def im_open(path):
    """Image open function."""
    img = np.asarray(Image.open(path))
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    return img


def pred_cost(tfmodel, im1, oh):
    """Inference function."""
    pred = tfmodel.predict(im1.reshape((-1, IMG_SIZE, IMG_SIZE, 3)))
    pred_oh = np.zeros(24)
    pred_oh[pred.argmax()] = 1
    cost = oh.inverse_transform(pred_oh.reshape(1, -1))[0][0]
    gc.collect()  # Clear the RAM.
    return cost


"""The bot's interface functions."""


@dp.message_handler(commands=['test'])
async def test(message: types.Message):
    """Test function."""
    await message.answer(text='It works!')


@dp.message_handler(commands=['tech'])
async def test(message: types.Message):
    """Describes the techology."""
    await message.answer(text="I'm based on efficientnetb4.")


@dp.message_handler(commands=['help'])
async def help_message(message: types.Message):
    """
    Outputs a small instruction when the corresponding command is received.
    """
    await message.answer(text="Hi, "
                              "I'm here to help you estimate the price of your"
                              "clothes. All you need to do is send me an image "
                              "of the clothes you want to estimate. Then I'll "
                              "tell you the price. It might take a little bit"
                              " of time.")


@dp.message_handler(commands=['creators'])
async def creator(message: types.Message):
    """Displays information about the bot's Creators."""
    link = 'https://github.com/t0efL/Price-Evaluator-Bot'
    await message.answer(text="I've been created as the project "
                              "for hackaton by ODS." 
                              f"\nMy code is here: {link}."
                              "\nMy creators:"
                              "\n - Vadim Timakin,"
                              "\n - Maksim Zhdanov,"
                              "\n - Fyodor Dobryansky, "
                              "\n - Yevhen Kravchenko,"
                              "\n - Vladislav Lebyodkin, "
                              "\n - Vyacheslav Chuev")

 
@dp.message_handler(commands=['fun'])
async def fun(message: types.Message):
    """Bonus."""
    with open('bonus.jpg', 'rb') as file:
        await message.answer_photo(file, caption='Done!')


@dp.message_handler(content_types=['photo'])
async def photo_processing(message):
    """
    Triggered when the user sends an image and starts its proccessing.
    """
    await message.photo[-1].download('image.jpg')
    im = im_open("image.jpg")
    price = pred_cost(model, im, OH)
    await message.answer(text="Estimated price is " + str(price) + " RUB.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
