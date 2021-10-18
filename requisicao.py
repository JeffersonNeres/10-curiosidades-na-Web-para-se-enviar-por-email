from asyncio import ensure_future, gather, get_event_loop
from aiohttp import ClientSession
from funcao import *

# devido algumas urls exigirem User-Agent foinecessario utilizar if para indetificar cadaurl e se necessario User-Agent

async def buscar(session, url):
    async with session.get(url) as response:
        return await response.text()

async def buscar_com_agent(session, url, agent=0):
    async with session.get(url, headers=agent) as response:
        return await response.text()

async def run():
    tasks = []
    contador_agent = 0
    headers = ""
    async with ClientSession() as session:
        for url in url_lista:
            if contador_agent < 3:
                if url == url_lista[contador_agent]:
                    headers = headers_lista[contador_agent]
                    task = ensure_future(buscar_com_agent(session, url, headers))
            if contador_agent == 3:
                del(headers)
            contador_agent += 1
            task = ensure_future(buscar(session, url))
            tasks.append(task)
        responses = await gather(*tasks)
        return responses

loop = get_event_loop()
future = ensure_future(run())
requisicao = loop.run_until_complete(future)
registra_requisicao = requisicao
