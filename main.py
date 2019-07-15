from aiohttp import web


async def hello(request: web.Request):
    data = request.query
    print(data)
    return web.Response(text=f"key = {data.get('key', 'default value')}, key1 = {data.get('key1', 'default data 1')}")


app = web.Application()
app.add_routes([web.get('/', hello)])

web.run_app(app, port=5002)
