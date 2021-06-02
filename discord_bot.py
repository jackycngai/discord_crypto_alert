import discord
import asyncio
import yfinance as yf
import moving_average

class discord_test(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.my_background_task())

    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self))

    async def on_message(self,message):
        if message.author == self.user:
            return

        if message.content.startswith('$BTC'):
            btc_time, btc_close, btc_status = moving_average.moving_average('BTC-USD').get_trend(True, True)
            await message.channel.send('Time: {} Price: {} Status: {}.'.format(btc_time, btc_close, btc_status))
            with open("BTC-USD.jpg", "rb") as fh:
                btc = discord.File(fh, filename="BTC-USD.jpg")
            await message.channel.send(file=btc)

        if message.content.startswith('$ETH'):
            eth_time, eth_close, eth_status = moving_average.moving_average('ETH-USD').get_trend(True, True)
            await message.channel.send('Time: {} Price: {} Status: {}.'.format(eth_time, eth_close, eth_status))
            with open("ETH-USD.jpg", "rb") as fh:
                eth = discord.File(fh, filename="ETH-USD.jpg")
            await message.channel.send(file=eth)

        if message.content.startswith('$DOGE'):
            doge_time, doge_close, doge_status = moving_average.moving_average('DOGE-USD').get_trend(True, True)
            await message.channel.send('Time: {} Price: {} Status: {}.'.format(doge_time, doge_close, doge_status))
            with open("DOGE-USD.jpg", "rb") as fh:
                doge = discord.File(fh, filename="DOGE-USD.jpg")
            await message.channel.send(file=doge)

    async def my_background_task(self):
        await self.wait_until_ready()
        counter = 0
        channel = self.get_channel(CHANNEL_ID_HERE!!!)
        timedate_b = None
        timedate_e = None
        timedate_d = None
        status_b = None
        status_e = None
        status_d = None
        while not self.is_closed():
            btc_time, btc_close, btc_status = moving_average.moving_average('BTC-USD').get_trend(False, False)
            eth_time, eth_close, eth_status = moving_average.moving_average('ETH-USD').get_trend(False, False)
            doge_time, doge_close, doge_status = moving_average.moving_average('DOGE-USD').get_trend(False, False)
            if timedate_b != btc_time and status_b != btc_status:
                moving_average.moving_average('BTC-USD').get_trend(True, True)
                with open("BTC-USD.jpg", "rb") as fh:
                    btc = discord.File(fh, filename="BTC-USD.jpg")
                await channel.send(file=btc)
                print('Time: {} Price: {} Status: {}.'.format(btc_time, btc_close, btc_status))
                btc_str = ('{}: Price of BTC-USD is at {}, you should {}'.format(btc_time, btc_close, btc_status))
                await channel.send(btc_str)
                timedate_b = btc_time
                status_b = btc_status
            if timedate_e != eth_time and status_e != eth_status:
                moving_average.moving_average('ETH-USD').get_trend(True, True)
                with open("ETH-USD.jpg", "rb") as fh:
                    eth = discord.File(fh, filename="ETH-USD.jpg")
                await channel.send(file=eth)
                print('Time: {} Price: {} Status: {}.'.format(eth_time, eth_close, eth_status))
                eth_str = ('{}: Price of ETH-USD is at {}, you should {}'.format(eth_time, eth_close, eth_status))
                await channel.send(eth_str)
                timedate_e = eth_time
                status_e = eth_status
            if timedate_d != doge_time and status_d != doge_status:
                moving_average.moving_average('DOGE-USD').get_trend(True, True)
                with open("DOGE-USD.jpg", "rb") as fh:
                    doge = discord.File(fh, filename="DOGE-USD.jpg")
                await channel.send(file=doge)
                print('Time: {} Price: {} Status: {}.'.format(doge_time, doge_close, doge_status))
                doge_str = ('{}: Price of DOGE-USD is at {}, you should {}'.format(doge_time, doge_close, doge_status))
                await channel.send(doge_str)
                timedate_d = doge_time
                status_d = doge_status
            await asyncio.sleep(60) # task runs every 60 seconds

if __name__ == '__main__':
    client = discord_test()
    client.run("PLACE_TOKEN_HERE!!!")
