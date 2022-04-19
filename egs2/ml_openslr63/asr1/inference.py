import soundfile
from espnet2.bin.asr_inference import Speech2Text
import os

# Download monolingual data
# os.system("gdown --id 1xJX4--ahGgItJAoMnT99wrLAHDiUpaY6")
os.system("gdown --id 1gEbggPorufsJTrXz7CGoQT3Jw6zBbZ4x")
os.system("unzip -o monolingual_audio.zip")
os.system("rm -f monolingual_audio.zip")

parent_dir = "monolingual_audio/"
for file in os.listdir(parent_dir):
    os.system("ffmpeg -i " + parent_dir + file + " -y -f wav -ar 16000 -ab 16 -ac 1 " + parent_dir + "formatted_" +file)

speech2text = Speech2Text.from_pretrained(
    "rmampill/malayalam-asr",
    # Decoding parameters are not included in the model file
    asr_train_config='conf/tuning/train_asr_conformer_s3prlfrontend_hubert_fused.yaml',
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
with open("monolingual_index.tsv", "w", encoding="utf-8") as output_file:
    for file in os.listdir(parent_dir):

        speech, rate = soundfile.read(parent_dir + file)
        nbests = speech2text(speech)
        text, _ = nbests[0]
        # output_file.write(file + "\t" + text + "\n")
        # Write to tsv file
        print(text)