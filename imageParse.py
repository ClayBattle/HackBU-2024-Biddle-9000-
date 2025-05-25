from openai import OpenAI
import os 
import config
os.environ["OPENAI_API_KEY"] = config.OPENAI_KEY


client = OpenAI()

def parseImage():

    client = OpenAI()

    response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": "The following is a screenshot of a math equation or matrix or similar math object. solve the problem."},
            {
            "type": "image_url",
            "image_url": {
                "url": "file:///C:/Users/clayb/Downloads/Screenshot%202024-02-27%20185932.jpg",#https://miro.medium.com/v2/resize:fit:640/format:webp/1*-PGZIOCgY_qbzeI_yGFO4A.png
            },
            },
        ],
        }
    ],
    )

    print("RESPONSE:"+response.choices[0].message.content)

    # response = client.chat.completions.create(
    # model="gpt-4-1106-preview",
    # messages=[
    #     {
    #     "role": "user",
    #     "content": [
    #         {"type": "text", "text": f" Output this as latex. {response.choices[0].message.content}\n\n ONLY the equation in latex such as \int (u dv). DO NOT output anything other than the latex."}
    #     ],
    #     }
    # ],
    # )
    # print(response.choices[0].message.content)
    # value = response.choices[0].message.content.replace('{{', '{ {').replace('}}', '} }')

parseImage()