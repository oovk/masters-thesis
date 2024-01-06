import vertexai
from vertexai import language_models

project_id = "modular-glider-408308"
location = "us-central1"

def streaming_prediction(project_id: str, location: str) -> str:
    """Streaming Chat Example with a Large Language Model."""

    vertexai.init(project=project_id, location=location)

    chat_model = language_models.ChatModel.from_pretrained("chat-bison")

    parameters = {
        "temperature": 0.8,
        "max_output_tokens": 2048,
        "top_p": 0.95,
        "top_k": 40,
    }

    chat = chat_model.start_chat(
        context=system_prompt,#add our system_prompt
        examples=[
            language_models.InputOutputTextPair(
                input_text=input_prompt,#add input data example
                output_text=output_prompt,#add output we expect
            ),
        ],
    )

    responses = chat.send_message_streaming(
        message=data_csv,#provide our own data
        **parameters,
    )

    for response in responses:
        print(response.candidates[0].text)


if __name__ == "__main__":
    streaming_prediction(project_id, location)