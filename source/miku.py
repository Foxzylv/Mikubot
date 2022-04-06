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

  if "miku" in message.content.lower():
    await message.channel.send("Hello uwu")

  if "hatsune" in message.content.lower():
    await message.channel.send("Hello (>_<)")

  if "!sing" in message.content.lower():
    await message.channel.send("semai kyoushitsu no katatsumuri shitauchi ga kanaderu merodi ijimekko ijimerarekko dochira mo piiman wa nigai ne daihakken kakkoii ko mo kawaii ko mo kimi no mono dakara uso demo honne de iesu no ankēto itai itai itai no wa iya dakara sakaraenai ja nai…  	“arigatou” mo “ohayou” mo “gomen nasai” mo zenbu natsukashii kotoba ni naru hi ga kuru no jūyonsai mo yonjussai mo odorou rattattatta dareka dareka minna o tasukete iraira poisute guranpuri osanago no kawaii aironii koibito mo shinryakusha mo dochira mo niku no katamari ka daijikken sāroin mo tsubame no su mo kimi no mono dakara supai no tsūshin kiroku wa shiikuretto kowai kowai kowai no wa yada kara nemutte itai ja nai… “ureshii” mo “kanashii” mo “warufuzake” mo zenbu shirokujichū kanshi sareru hi ga kuru no Satou-san mo Suzuki-san mo utaou ranranranran itsuka itsuka namae mo wasurete nakama ni nattara happii endo? nakama hazure wa doko e ikou chimamire ni natta pasupōto sentaku no shunkan wa sugu sugu sugu soba ni “sayonara” mo “oyasumi” mo “mata ashita” mo zenbu tsunagarazu ni togireru hi ga kuru no Tanaka-san mo Takahashi-san mo waraou wahhahhahha dareka dareka dareka dareka dareka “arigatou” mo “ohayou” mo “gomen nasai” mo zenbu natsukashii kotoba ni naru hi ga kuru no inbouron mo gasukonro mo odorou rattattatta dareka dareka minna o tasukete")

    

client.run(os.getenv('Token'))
