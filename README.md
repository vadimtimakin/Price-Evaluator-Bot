# Price-Evaluator-Bot

**Telegram bot that predicts the price of clothing by image [ENG].**

What is Price Evaluator Telegram Bot?
------------------------------------------
Price Evaluator Telegram Bot is the final project for the Hackathon by ODS.

![alt text](https://github.com/t0efL/Price-Evaluator-Bot/blob/main/images/ods.jpg)

The goal was to create a telegram bot which can predict the price of clothing by an image. It was also necessary to deploy the bot to the server, so that the bot could run smoothly and not fall asleep.

The Bot itself: `@PriceEvaluatorBot` (Telegram)

It is possible that you found the bot by tag and found it not working. The reason most likely was that we stopped supporting the bot some time after it was created, so as not to waste the power of the server.

Technology
-------
The bot is based on efficientnetb4. The weigths and the encoder we use in code are [here](https://drive.google.com/drive/folders/1mtsRFAt-K7MCR8En2qmsqSwjtti4RhAH?usp=sharing). You should download this folder and place it in your project repository avoiding changing name to use it. They are too large to place them here. We used the dataset from the [Avito Demand Prediction Challenge](https://www.kaggle.com/c/avito-demand-prediction) Kaggle competition. The simple pipeline for training is [here](https://github.com/t0efL/Price-Evaluator-Bot).
