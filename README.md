# Lichess Blindfold Client

A python program that allows the user to play a lichess game while only being able to see the chess notation and no board. Useful for when the user wants to play alone, wants no board at all to be seen, and can't touch type SAN move notation (e.g. Nf3, e6, axb3)

---

## About this application:

Python version required is 3.9.2+

In order to check if you have a new enough version, open Command Prompt or Terminal and type `python3 --version`

---

## Setup

Immediately after cloning the repository, install dependencies by typing `cd LichessBlindfoldClient` and then `pip3 install -r requirements.txt`

Then, you must give the program your lichess username and a valid API token for lichess.org

To generate a lichess.org API Token, open a web browser and navigate to `lichess.org`, then click on your username in the top right corner, and then click `Preferences`. On the left side-bar, towards the bottom, you'll find a section labeled `API Access Tokens`. Click on this section and then you'll find a blue button in the top right corner that you can press to generate a new token. Flip all of the switches so that this token can fully access your account, then press `Submit`. The random string you see is your API token. Keep this page open for later.

In order to give the program your details, if you are already in the `LichessBlindfoldClient` directory, type `cd source`, then `cd secrets`, and then `python3 setup.py`. You will then be prompted to type in your lichess username and copy in your lichess API token. 

If you've done everything above, you're all set!

Navigate to the `source` directory and type `python3 main.py` and enjoy the program!

