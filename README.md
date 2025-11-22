📌 Video-to-Text Caption Generator

An AI-powered Video-to-Text Captioning system that extracts frames from a video and generates meaningful captions using BLIP (Bootstrapped Language-Image Pretraining) vision-language model. The project processes online video URLs, samples frames, and produces human-like descriptions for each frame.

🚀 Features

🎞 Extracts frames from video using OpenCV

🤖 Generates descriptions using BLIP Transformer model

📥 Accepts direct MP4 video URLs for processing

🔍 Handles non-video URLs safely with validation

⚡ Supports GPU acceleration (CUDA) when available

🧠 Tech Stack
Component	Technology
Programming Language	Python
Video Processing	OpenCV, MoviePy
Captioning Model	BLIP (Salesforce/blip-image-captioning-base)
Transformers	Hugging Face
Image Handling	Pillow
Utilities	Requests, UUID4


🛠 How It Works

Download video from provided URL

Validate content type to ensure it's a video

Extract frames at intervals using OpenCV

Convert frames to RGB format and process via BLIP model

Generate natural language captions

Output final summarized caption list

📦 Installation

git clone https://github.com/your-repo/video-to-text-captioning.git
cd video-to-text-captioning
pip install -r requirements.txt

▶️ Usage

python ved.py

Example Output

Frame 1: a man speaking in a studio environment
Frame 2: a laptop on a table with a screen visible
Frame 3: presenter gesturing with hands
...

📷 Model

BLIP Image Captioning Model
🔗 https://huggingface.co/Salesforce/blip-image-captioning-base

📈 Future Enhancements

Full video summarization text

Speech-to-text integration (Whisper API)

GUI / Web-based interface

Support for YouTube video URLs

🙌 Contributions

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to modify.

📮 Contact

Himanshu Aggarwal
📧 himanshuaggarwal.0011@gmail.com
