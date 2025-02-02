import cv2
import mss
import numpy as np
import os
import time
import sounddevice as sd
import soundfile as sf

def capture_screen(duration=10, resolution=None, framerate=20.0, record_audio=False):
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        width = monitor["width"]
        height = monitor["height"]

        if resolution:
            width, height = resolution

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    output_file = os.path.join(os.getenv("TEMP"), "screen_record.mp4")
    out = cv2.VideoWriter(output_file, fourcc, framerate, (width, height))

    audio_file = None
    if record_audio:
        audio_file = os.path.join(os.getenv("TEMP"), "screen_record_audio.wav")
        samplerate = 44100
        channels = 2    
        audio_stream = sd.InputStream(samplerate=samplerate, channels=channels)
        audio_frames = []

    start_time = time.time()
    with mss.mss() as sct:
        if record_audio:
            audio_stream.start()

        while time.time() - start_time < duration:
            frame = np.array(sct.grab(monitor))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
            frame = cv2.resize(frame, (width, height))
            out.write(frame)

            if record_audio:
                audio_data, _ = audio_stream.read(int(samplerate * (1 / framerate)))
                audio_frames.append(audio_data)

    out.release()
    if record_audio:
        audio_stream.stop()
        audio_stream.close()
        sf.write(audio_file, np.concatenate(audio_frames), samplerate)

        final_output_file = os.path.join(os.getenv("TEMP"), "screen_record_final.mp4")
        merge_video_audio(output_file, audio_file, final_output_file)
        output_file = final_output_file

    print(f"[INFO] Screen recording saved as {output_file}")
    return output_file

def merge_video_audio(video_file, audio_file, output_file):
    import subprocess
    command = [
        "ffmpeg", "-i", video_file, "-i", audio_file,
        "-c:v", "copy", "-c:a", "aac", "-strict", "experimental", output_file
    ]
    subprocess.run(command, check=True)