import gradio as gr
from a_cnk_a_nk_peraluminous_classifier import classify, plot_diagram

def compute(al2o3, cao, na2o, k2o):
    try:
        al2o3 = float(al2o3)
        cao = float(cao)
        na2o = float(na2o)
        k2o = float(k2o)
    except (ValueError, TypeError):
        return 0.0, 0.0, "Invalid input: enter numeric values.", None
    a_cnk, a_nk, label = classify(al2o3, cao, na2o, k2o)
    fig = plot_diagram(a_cnk, a_nk)
    return a_cnk, a_nk, label, fig

with gr.Blocks(title="A/CNK A/NK Peraluminous Classifier") as demo:
    gr.Markdown("## A/CNK A/NK Peraluminous Classifier")
    with gr.Row():
        al2o3_in = gr.Number(label="Al₂O₃ (wt%)", value=15.0, step=0.1)
        cao_in = gr.Number(label="CaO (wt%)", value=10.0, step=0.1)
        na2o_in = gr.Number(label="Na₂O (wt%)", value=3.0, step=0.1)
        k2o_in = gr.Number(label="K₂O (wt%)", value=2.0, step=0.1)
    calc_btn = gr.Button("Calculate")
    with gr.Row():
        with gr.Column():
            a_cnk_out = gr.Number(label="A/CNK", interactive=False)
            a_nk_out = gr.Number(label="A/NK", interactive=False)
            class_out = gr.Textbox(label="Classification", interactive=False)
        with gr.Column():
            plot_out = gr.Plot(label="A/CNK vs A/NK Diagram")

    calc_btn.click(
        fn=compute,
        inputs=[al2o3_in, cao_in, na2o_in, k2o_in],
        outputs=[a_cnk_out, a_nk_out, class_out, plot_out],
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
