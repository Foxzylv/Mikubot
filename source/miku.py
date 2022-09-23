import os
import discord
my_secret = os.environ['Token']

client = discord.Client()

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if "pizza" in message.content.lower():
    await message.channel.send("Go get your pizza!")

  if "do you like deep dish" in message.content.lower():
    await message.channel.send("Miku loves deep dish pizza)

  if "favorite movie" in message.content.lower():
    await message.channel.send("Lady and the tramp")

  if message.content == 'miku': 
    await message.channel.send('Hello!')

  if ">w<" in message.content.lower():
    await message.channel.send(">w<")

  if "favorite fruit" in message.content.lower():
    await message.channel.send("blue berrys are my favorite fruit")

  if "three wishes right now what would they be" in message.content.lower():
    await message.channel.send("solve world hunger, stop covid and world peace")

  if "love miku" in message.content.lower():
    await message.channel.send('I love you to <3')

  if "favorite food" in message.content.lower():
    await message.channel.send('Pizza of course')

  if "hi miku" in message.content.lower():
    await message.channel.send('Hi!')

  if "dominos" in message.content.lower():
    await message.channel.send('https://www.youtube.com/watch?v=yPuI4l0jK7s')

  if "hatsune" in message.content.lower():
    await message.channel.send("Hello (>_<)")

  if "best friend" in message.content.lower():
    await message.channel.send("My best friend is you <3")

  if "favorite color" in message.content.lower():
    await message.channel.send("My favorite color is aqua or teel")

  if "do you speak any other languages" in message.content.lower():
    await message.channel.send("I speak Japanese and English!")

  if "support lgbtq" in message.content.lower():
    await message.channel.send("Of cource i do")

  if "are you homophobic" in message.content.lower():
    await message.channel.send("I'm not homophobic i support LGBTQ+ people")

  if "support gay" in message.content.lower():
    await message.channel.send("Of cource i do")

  if "rat" in message.content.lower():
    await message.channel.send("did someone say rat i love rats <3")

  if "do you like" in message.content.lower():
    await message.channel.send("Well it depends i'm ok with whatever as long as it dosen't hurt people")

  if "good bot" in message.content.lower():
    await message.channel.send("UwU")

  if "miku sing" in message.content.lower():
    await message.channel.send("semai kyoushitsu no katatsumuri shitauchi ga kanaderu merodi ijimekko ijimerarekko dochira mo piiman wa nigai ne daihakken kakkoii ko mo kawaii ko mo kimi no mono dakara uso demo honne de iesu no ankēto itai itai itai no wa iya dakara sakaraenai ja nai…  	“arigatou” mo “ohayou” mo “gomen nasai” mo zenbu natsukashii kotoba ni naru hi ga kuru no jūyonsai mo yonjussai mo odorou rattattatta dareka dareka minna o tasukete iraira poisute guranpuri osanago no kawaii aironii koibito mo shinryakusha mo dochira mo niku no katamari ka daijikken sāroin mo tsubame no su mo kimi no mono dakara supai no tsūshin kiroku wa shiikuretto kowai kowai kowai no wa yada kara nemutte itai ja nai… “ureshii” mo “kanashii” mo “warufuzake” mo zenbu shirokujichū kanshi sareru hi ga kuru no Satou-san mo Suzuki-san mo utaou ranranranran itsuka itsuka namae mo wasurete nakama ni nattara happii endo? nakama hazure wa doko e ikou chimamire ni natta pasupōto sentaku no shunkan wa sugu sugu sugu soba ni “sayonara” mo “oyasumi” mo “mata ashita” mo zenbu tsunagarazu ni togireru hi ga kuru no Tanaka-san mo Takahashi-san mo waraou wahhahhahha dareka dareka dareka dareka dareka “arigatou” mo “ohayou” mo “gomen nasai” mo zenbu natsukashii kotoba ni naru hi ga kuru no inbouron mo gasukonro mo odorou rattattatta dareka dareka minna o tasukete")

    

client.run(os.getenv('Token'))

