from aiohttp import web

routes = web.RouteTableDef()


@routes.route("*", "/")
async def hello(request: web.Request):
    return web.Response(text="Hello, world!")


app = web.Application()
app.add_routes(routes)
web.run_app(app)
