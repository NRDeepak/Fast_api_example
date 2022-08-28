import uvicorn
from googletrans import Translator

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

translator = Translator()


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("home_page.html", {"request": request})


@app.post(path="/english_text")
async def extract_data_from_images(value=Form(...)):

    translation = translator.translate(value, dest='kn')

    return str(translation.text)

if __name__ == "__main__":
    uvicorn.run("fast_api_example:app", port=18080, log_level="info")
