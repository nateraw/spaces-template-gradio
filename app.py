import gradio as gr


def main(text):
    # A gradio function that lowercases text and returns it
    return text.lower()


# A simple gradio app for text
app = gr.Interface(
    main,
    inputs="text",
    outputs="text",
    title="Spaces Template Gradio",
    description="A template app for Hugging Face Spaces",
)
app.launch(debug=True)

