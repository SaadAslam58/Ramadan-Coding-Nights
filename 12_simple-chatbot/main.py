import chainlit as cl

# Its an decorator
@cl.on_message

# Define an async function that takes a message parameter
async def main(message: cl.Message):

        # Create a response string using the message content
    responce = f"You said: {message.content}"

        # Send the response message back to the user
    await cl.Message(content=responce).send()