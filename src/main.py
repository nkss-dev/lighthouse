import json
from aiohttp import web
from aiohttp.web import json_response, Request, Response

from utils.papers import fetch_papers

routes = web.RouteTableDef()


@routes.route("*", "/")
async def hello(request: Request):
    return Response(text="Hello, world!")


@routes.route("*", "/papers/{course_code}")
async def question_paper(request: Request):
    content_type = request.headers.get("Content-Type", "")
    assert content_type == "application/json"

    course_code = request.match_info["course_code"]
    papers = await fetch_papers()
    for paper in papers:
        print(paper)
        print()
        print()
    return json_response({})


@routes.route("*", "/papers")
async def question_papers(request: Request):
    content_type = request.headers.get("Content-Type", "")
    assert content_type == "application/json"

    data = json.loads((await request.read()).decode())
    return json_response(data)


app = web.Application()
app.add_routes(routes)
web.run_app(app)
