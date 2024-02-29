import gradio as gr
import random as rd
import string


def generate_passwords(length, count):
    passwords = []
    for _ in range(count):
        aplhanumeric = string.ascii_letters + string.digits
        password = ''.join(rd.choice(aplhanumeric) for _ in range(length))
        passwords.append(password)
    return ", ".join(passwords)


iface = gr.Interface(
    fn=generate_passwords,
    inputs=[
        gr.Slider(minimum=4, maximum=50, step=1, label="Password Length"),
        gr.Slider(minimum=1, maximum=10, step=1, label="Number of Passwords")
    ],

    outputs=gr.Textbox(label="Generated Passwords"),
    
    title="Random Password Generator",
    description="Enter the length of password and number of passwords you want to generate."
)

iface.launch()
