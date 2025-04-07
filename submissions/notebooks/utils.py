import os
import librosa
# functions for extract the audios and extract the labels

def load_audio_files(path, duration=None):
  root = path
  files = os.listdir(path)
  audio_signals = []
  for file in files:
    file_path = os.path.join(root,file)
    audio_signal, sample_rate = librosa.load(file_path, duration=duration)
    audio_signals.append(audio_signal)
  return audio_signals, sample_rate

def extract_labels(path):
  labels = []
  root = path
  files = os.listdir(path)
  for file in files:
    parts = str.split(file,'.')
    labels.append(parts[0])
  return labels


