from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from openai import OpenAI

app = FastAPI()
@app.get("/", response_class=HTMLResponse)
def instant():
    client = OpenAI()
    message = """
    You are on a website that has just been deployed to production for the first time. You are a helpful assistant that is here to greet the user and let them know that their deployment was successful.
    
    Please respond with a friendly message that welcomes the user to their new website and congratulates them on their successful deployment.
        """
    messages = [{"role": "user", "content": message}]
    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=messages,
    )
    reply = response.choices[0].message.content.replace("/n", "<br>")
    html = {
        f"<html><head><title>Welcome to Your New Website!</title></head><body><h1>{reply}</h1></body></html>"
    }
    return html
