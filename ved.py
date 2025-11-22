import uuid
import requests
import cv2
from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration

device = "cuda" if torch.cuda.is_available() else "cpu"

print("Loading model (BLIP)...")
model_id = "Salesforce/blip-image-captioning-base"
processor = BlipProcessor.from_pretrained(model_id)
model = BlipForConditionalGeneration.from_pretrained(model_id).to(device)

# -------------------------------------------
# Safe & Reliable Video Download + Frame Extraction
# -------------------------------------------
def sample_frames(url, num_frames=6):
    print("\n🔽 Downloading video...")
    try:
        response = requests.get(url, timeout=60)
    except Exception as e:
        print("ERROR while downloading:", e)
        return []

    content_type = response.headers.get("Content-Type", "")
    print("Content-Type:", content_type)

    # Validate the content type
    if "video" not in content_type:
        print("ERROR: The URL did NOT return a video file.")
        print("Here is preview of response:\n", response.text[:200])
        return []

    # Save video
    file_id = str(uuid.uuid4())
    video_path = f"./{file_id}.mp4"
    with open(video_path, "wb") as f:
        f.write(response.content)
    print(f"✅ Saved video as: {video_path}")

    print("🎞 Extracting frames...")

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("❌ ERROR: OpenCV cannot read this video.")
        return []

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    interval = max(1, total_frames // num_frames)

    frames = []
    count = 0

    for i in range(total_frames):
        ret, frame = cap.read()
        if not ret:
            break

        if i % interval == 0:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frames.append(Image.fromarray(frame_rgb))
            count += 1

    cap.release()
    print(f"✅ Extracted {count} frames.")
    return frames

# -------------------------------------------
# Describe Video Frames Using BLIP
# -------------------------------------------
def describe_video(frames):
    captions = []
    print("📝 Generating captions...")

    for idx, img in enumerate(frames):
        inputs = processor(images=img, return_tensors="pt").to(device)
        output = model.generate(**inputs, max_new_tokens=50)
        caption = processor.decode(output[0], skip_special_tokens=True)
        captions.append(caption)
        print(f"Frame {idx+1}: {caption}")

    return captions


# -------------------------------------------
# 100% WORKING DIRECT MP4 URL
# -------------------------------------------

video_url = "https://filesamples.com/samples/video/mp4/sample_640x360.mp4"

# -------------------------------------------
# RUN PIPELINE
# -------------------------------------------
frames = sample_frames(video_url)
if frames:
    captions = describe_video(frames)

print("\n----- FINAL VIDEO DESCRIPTION -----")
for i, c in enumerate(captions, 1):
    print(f"{i}. {c}")
