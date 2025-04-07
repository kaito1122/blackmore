from pydub import AudioSegment
import os


def split_wav_to_chunks(input_file, chunk_length_ms=30_000, output_folder="song/split"):
    # Load the song
    audio = AudioSegment.from_wav(input_file)

    # Make output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    total_chunks = len(audio) // chunk_length_ms
    chunk_files = []

    for i in range(total_chunks + 1):
        start = i * chunk_length_ms
        end = min((i + 1) * chunk_length_ms, len(audio))
        chunk = audio[start:end]

        # Skip very short final chunk (optional)
        if len(chunk) < 10_000:  # <10s
            continue

        chunk_filename = os.path.join(output_folder, f"chunk_{i}.wav")
        chunk.export(chunk_filename, format="wav")
        chunk_files.append(chunk_filename)
        print(f"Saved: {chunk_filename}")

    return chunk_files

chunk_files = split_wav_to_chunks("song/Blackmore's Night - Under a Violet Moon [Full Album].wav")
