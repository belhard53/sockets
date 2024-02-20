import asyncio
import time
from aiohttp import ClientSession
import requests

n_step:int = 0

async def aget_weather(city:str, n_city):
    global n_step
    async with ClientSession() as session:
        url = f'http://34.133.51.157/hello'
        params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}

        async with session.get(url=url) as response:
            res = await response.read()       
            
            # принт не асинхронный,  но это конечная точка и выполняется очень быстро            
            n_step += 1 
            print(n_city, res.decode())
    

def get_weather(city):    
        url = f'http://34.133.51.157/hello'
        params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}
        res = requests.get(url)
        with open('err.html', 'w') as f:
            f.write(res.text)
        print(res.text)
    


async def async_main(cities_):
    tasks = []
    for i, city in enumerate(cities_):
        tasks.append(asyncio.create_task(aget_weather(city, i)))

    for task in tasks:
        await task
        

def main(cities_):    
    for city in cities_:
        get_weather(city)

    


cities = ['Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
          'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York']


t = time.time()

asyncio.run(async_main(cities*3))
#main(cities*4)
#get_weather("")
print(time.time() - t)