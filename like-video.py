from Bot import Bot

# your location to chromedriver executable
bot = Bot('chromedriver.exe')

bot.goto_youtube() \
    .login(email='jkogan@mail.ccsf.edu', password='1Sampai5!') \
    .like(videoId='rESdwzBJRtw', watchFullVideo=True) \
    .end()
