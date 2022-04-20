import os
import time
# Download the files

while "kaggle_male.zip" not in os.listdir('~/espnet/egs2/ml_openslr63/asr1/downloads/'):
    os.system("gdown --id 14V24RX041vCyjd6LJ8bGD6YOOJAr05gk")
    time.sleep(30)

os.system("unzip kaggle_male.zip")
os.system("rm -rf kaggle_male.zip")

time.sleep(30)

while "kaggle_female.zip" not in os.listdir('~/espnet/egs2/ml_openslr63/asr1/downloads/'):
    os.system("gdown --id 1NeH8U2sGAx37k0J2nA4F0YR4Qtsox31M")
    time.sleep(30)

os.system("unzip kaggle_female.zip")
os.system("rm -rf kaggle_female.zip")

# male
male_tsv = open("kaggle_male/label_male.tsv", "r", encoding="utf-8")
male_tsv_lines = male_tsv.readlines()
male_tsv.close()
os.system("mkdir -p monolingual_data")

male_tsv = open("monolingual_data/label_male.tsv", "w", encoding="utf-8")

for line in male_tsv_lines:
    values = line.split("\t")
    file_name = values[0]
    audio_text = values[1]
    file_name = "mlm_mono_" + file_name
    male_tsv.write(file_name + "\t" + audio_text)

male_tsv.close()


# female
female_tsv = open("kaggle_female/label_female.tsv", "r", encoding="utf-8")
female_tsv_lines = female_tsv.readlines()
female_tsv.close()
os.system("mkdir -p monolingual_data")

female_tsv = open("monolingual_data/label_female.tsv", "w", encoding="utf-8")

for line in female_tsv_lines:
    values = line.split("\t")
    file_name = values[0]
    audio_text = values[1]
    file_name = "mlm_mono_" + file_name
    female_tsv.write(file_name + "\t" + audio_text)

female_tsv.close()

# move audio files from kaggle_male and kaggle_female to monolingual_data
os.system("mv kaggle_male/wav/*.wav monolingual_data")
os.system("mv kaggle_female/wav/*.wav monolingual_data")