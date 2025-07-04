import random
import numpy as np
import torch
import sys
import os
import gradio as gr

# Add path to the 'src' directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "chatterbox/src")))
from chatterbox.tts import ChatterboxTTS

# Set device
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print(f"🚀 Running on device: {DEVICE}")

MODEL = None

def get_or_load_model():
    global MODEL
    if MODEL is None:
        print("Model not loaded, initializing...")
        try:
            MODEL = ChatterboxTTS.from_pretrained(DEVICE)
            if hasattr(MODEL, 'to') and str(MODEL.device) != DEVICE:
                MODEL.to(DEVICE)
            print(f"✅ Model loaded on: {getattr(MODEL, 'device', 'N/A')}")
        except Exception as e:
            print(f"❌ Error loading model: {e}")
            raise
    return MODEL

try:
    get_or_load_model()
except Exception as e:
    print(f"CRITICAL: Failed to load model. Error: {e}")

def set_seed(seed: int):
    torch.manual_seed(seed)
    if DEVICE == "cuda":
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
    random.seed(seed)
    np.random.seed(seed)

def generate_tts_audio(
    text_input: str,
    audio_prompt_path_input: str = None,
    exaggeration_input: float = 0.5,
    temperature_input: float = 0.8,
    seed_num_input: int = 0,
    cfgw_input: float = 0.5
) -> tuple[int, np.ndarray]:
    current_model = get_or_load_model()
    if current_model is None:
        raise RuntimeError("TTS model is not loaded.")

    if seed_num_input != 0:
        set_seed(int(seed_num_input))

    torch.cuda.empty_cache()  # Clear GPU cache
    print(f"🎤 Generating audio for: {text_input[:60]}...")

    generate_kwargs = {
        "exaggeration": exaggeration_input,
        "temperature": temperature_input,
        "cfg_weight": cfgw_input,
    }

    if audio_prompt_path_input:
        generate_kwargs["audio_prompt_path"] = audio_prompt_path_input

    text_input = text_input.strip()[:1000]  # limit input length
    wav = current_model.generate(text_input, **generate_kwargs)

    print("✅ Audio generation complete.")
    return (current_model.sr, wav.squeeze(0).numpy())

# --- Gradio UI ---
with gr.Blocks(title="Voice Cloning Studio", css="""
body {
    background-color: #121212;
    color: #FFFFFF;
    font-family: 'Segoe UI', sans-serif;
}
h1, h2 {
    color: #FFA500;
    text-align: center;
}
label {
    color: #F5A623 !important;  /* warm gold */
    font-weight: bold;
    letter-spacing: 0.3px;
}

.gr-button-primary {
    background: linear-gradient(90deg, #FFA500, #FF4500);
    color: white;
    border: none;
    font-weight: bold;
}
.gr-button-primary:hover {
    background: linear-gradient(90deg, #FF6347, #FF8C00);
}
.gr-textbox, .gr-slider, .gr-number, .gr-audio {
    background-color: #1E1E1E;
    border: 1px solid #333;
    color: white;
    border-radius: 8px;
}
.gr-accordion {
    background-color: #1e1e1e;
    color: #ddd;
}
""") as demo:

    gr.Markdown("""
    <h1>🎙️ Voice Cloning Studio</h1>
    <p style="text-align:center; font-size: 1.1rem; color: #ccc;">
        Clone realistic voices using expressive text-to-speech with a single voice sample.
    </p>
    <hr style="border-color: #444;">
    """)

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("## One-Shot Voice Cloning")

            text = gr.Textbox(
                label="💬 Enter Text to Clone Voice",
                placeholder="E.g. Hello, this is a voice clone demo.",
                lines=5,
                max_lines=10
            )

            gr.Markdown("### 🎤 Provide a Single Voice Sample")
            ref_wav = gr.Audio(
                sources=["upload", "microphone"],
                type="filepath",
                label="🎙️ Upload or Record Voice (one-shot)",
                show_label=True
            )

            exaggeration = gr.Slider(
                0.3, 1.2, step=0.05,
                label="🎭 Expressiveness",
                value=0.5
            )

            cfg_weight = gr.Slider(
                0.2, 0.9, step=0.05,
                label="🧭 CFG Weight / Pacing",
                value=0.5
            )

            with gr.Accordion("⚙️ Advanced Settings", open=False):
                temp = gr.Slider(
                    0.05, 1.5, step=0.05,
                    label="🔥 Temperature (variation)",
                    value=0.7
                )
                seed_num = gr.Number(
                    label="🎲 Random Seed (0 = random)",
                    value=0
                )

            run_btn = gr.Button("🚀 Generate Cloned Voice", variant="primary")

        with gr.Column(scale=1):
            gr.Markdown("## Output Panel")
            audio_output = gr.Audio(label="📣 Cloned Voice Output", interactive=False)

            with gr.Accordion("ℹ️ How It Works", open=False):
                gr.Markdown("""
                - Record or upload a **single voice sample**
                - Enter **any text**
                - The model will **clone the voice style** and speak the text
                """)

    run_btn.click(
        fn=generate_tts_audio,
        inputs=[text, ref_wav, exaggeration, temp, seed_num, cfg_weight],
        outputs=[audio_output],
    )

demo.launch()
