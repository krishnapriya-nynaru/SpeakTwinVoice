# SpeakTwin – One-Shot Voice Cloning App
Clone a voice. Speak like it. Instantly.

SpeakTwin is a lightweight, powerful voice cloning tool that transforms any short voice sample into a fully expressive speech generator. Just upload a clip or record directly, type your message, and hear it spoken back in the cloned voice — all in a single shot.

- 🔹 Powered by Resemble AI & Chatterbox TTS
- 🔸 Supports one-shot voice cloning
- 🎙️ Upload or record a reference voice
- 💬 Type text to synthesize
- 🚀 Generate lifelike, emotional speech in seconds

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Results & User Interface](#results)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## Installation
1. Create conda enviroenment 
    ```bash
    conda create -n env_name python=3.10
    ```
2. Activate conda enviroenment
    ```bash
    conda activate env_name
    ```
3. Clone this repository:
   ```bash
   git clone https://github.com/krishnapriya-nynaru/SpeakTwinVoice.git
   ```
4. Change to Project directory
    ```bash
    cd SpeakTwinVoice
    ```
5. Install required packages :
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the Voice Cloning App
```bash
python app.py
```
2. Open your browser and go to:
```bash
http://127.0.0.1:7860/
```
3. Use the SpeakTwin Interface:
    - 🎙️ Upload or record a voice sample (optional, for cloning).
    - 💬 Enter the text you want the cloned voice to speak.
    - 🎭 Adjust settings like expressiveness, pacing (CFG), and randomness (temperature).
    - ⚙️ Use advanced options like seed control for reproducible outputs.
    - 🚀 Click Generate Audio to synthesize the voice output.
    - 🔊 Listen to or download the generated speech.

SpeakTwin supports one-shot voice cloning — you only need a single voice sample to create expressive, high-quality speech.
## Results & User Interface

![alt_text](https://github.com/krishnapriya-nynaru/ChefBot-AI/blob/main/ChefBot_AI/Results_and_UI/ChefBot-AI-UI.gif?raw=true)

## Contributing 
Contributions are welcome! To contribute to this project:
1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and ensure the code passes all tests.
4. Submit a pull request with a detailed description of your changes.

If you have any suggestions for improvements or features, feel free to open an issue!

## 🙏 Acknowledgments

🔊 **Powered by cutting-edge voice tech:**

- [**Resemble AI**](https://huggingface.co/ResembleAI) – One-shot voice cloning and speech synthesis engine  
- [**Chatterbox TTS**](https://github.com/resemble-ai/chatterbox) – Expressive text-to-speech generation framework  
- [**PyTorch**](https://pytorch.org/) – Deep learning framework powering the voice model  
- [**Gradio**](https://www.gradio.app/) – Fast and easy-to-use UI for interactive demos  


🎯 Shoutout to the open-source heroes bringing voices to life with AI.
