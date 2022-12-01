import openai

def generate_image(prompt: str) -> str:
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="256x256"
    )
    return response['data'][0]['url']