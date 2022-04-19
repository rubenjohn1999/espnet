import soundfile
from espnet2.bin.asr_inference import Speech2Text
import os
speech2text = Speech2Text.from_pretrained(
    "rmampill/malayalam-asr",
    # Decoding parameters are not included in the model file
    maxlenratio=0.0,
    minlenratio=0.0,
    beam_size=10,
    ctc_weight=0.5,
    lm_weight=0.3,
    penalty=0.0,
    nbest=1
)
# Confirm the sampling rate is equal to that of the training corpus.
# If not, you need to resample the audio data before inputting to speech2text


speech, rate = soundfile.read("speech.wav")
nbests = speech2text(speech)

text, *_ = nbests[0]
print(text)