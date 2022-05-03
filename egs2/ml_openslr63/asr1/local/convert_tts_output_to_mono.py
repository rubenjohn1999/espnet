import os
import time
# Download the files

while "leipzig_male.zip" not in os.listdir('../downloads'):
    os.system("gdown --id 1I17gbcbRI_Fi6oO1DJpKVe4ZLa0Tcv2p")
    time.sleep(2)

os.system("unzip leipzig_male.zip")
os.system("rm -rf leipzig_male.zip")

while "leipzig_female.zip" not in os.listdir('../downloads'):
    os.system("gdown --id 1Rcje1qeo_Y9QJ5RbmObrYYlFRcDp-UGU")
    time.sleep(2)

os.system("unzip leipzig_female.zip")
os.system("rm -rf leipzig_female.zip")

# male
male_tsv = open("leipzig_male/label_male.tsv", "r", encoding="utf-8")
male_tsv_lines = male_tsv.readlines()
male_tsv.close()
os.system("mkdir -p monolingual_data")

male_tsv = open("monolingual_data/label_male.tsv", "w", encoding="utf-8")

for line in male_tsv_lines:
    values = line.split("\t")
    file_name = values[0].split('.wav')[0]
    audio_text = values[1]
    file_name = "mlm_mono_" + file_name
    male_tsv.write(file_name + "\t" + audio_text)

male_tsv.close()


# female
female_tsv = open("leipzig_female/label_female.tsv", "r", encoding="utf-8")
female_tsv_lines = female_tsv.readlines()
female_tsv.close()
os.system("mkdir -p monolingual_data")

female_tsv = open("monolingual_data/label_female.tsv", "w", encoding="utf-8")

for line in female_tsv_lines:
    values = line.split("\t")
    file_name = values[0].split('.wav')[0]
    audio_text = values[1]
    file_name = "mlm_mono_" + file_name
    female_tsv.write(file_name + "\t" + audio_text)

female_tsv.close()

# move audio files from kaggle_male and kaggle_female to monolingual_data

for file in os.listdir("../downloads/leipzig_male/wav"):
    os.system("mv leipzig_male/wav/" + file + " leipzig_male/wav/mlm_mono_" + file)
for file in os.listdir("../downloads/leipzig_female/wav"):
    os.system("mv leipzig_female/wav/" + file + " leipzig_female/wav/mlm_mono_" + file)

os.system("mv leipzig_male/wav/*.wav monolingual_data")
os.system("mv leipzig_female/wav/*.wav monolingual_data")

# ----------------------------Adding Kaggle data-----------------------------

while "kaggle_male.zip" not in os.listdir('../downloads'):
    os.system("gdown --id 1v7ZGJi7mBNL0ED46dZB2NHmVz1m_HiYu")
    time.sleep(2)

os.system("unzip kaggle_male.zip")
os.system("rm -rf kaggle_male.zip")

while "kaggle_female.zip" not in os.listdir('../downloads'):
    os.system("gdown --id 1y_hfgGnrM_hc5uBwy-fiL52B1T8M37JZ")
    time.sleep(2)

os.system("unzip kaggle_female.zip")
os.system("rm -rf kaggle_female.zip")

# male
male_tsv = open("kaggle_male/label_male.tsv", "r", encoding="utf-8")
male_tsv_lines = male_tsv.readlines()
male_tsv.close()
os.system("mkdir -p monolingual_data")

male_tsv = open("monolingual_data/label_male.tsv", "a", encoding="utf-8")

for line in male_tsv_lines:
    values = line.split("\t")
    file_name = values[0].split('.wav')[0]
    audio_text = values[1]
    file_name = "mlm_mono_" + file_name
    male_tsv.write(file_name + "\t" + audio_text)

male_tsv.close()


# female
female_tsv = open("kaggle_female/label_female.tsv", "r", encoding="utf-8")
female_tsv_lines = female_tsv.readlines()
female_tsv.close()
os.system("mkdir -p monolingual_data")

female_tsv = open("monolingual_data/label_female.tsv", "a", encoding="utf-8")

for line in female_tsv_lines:
    values = line.split("\t")
    file_name = values[0].split('.wav')[0]
    audio_text = values[1]
    file_name = "mlm_mono_" + file_name
    female_tsv.write(file_name + "\t" + audio_text)

female_tsv.close()

# move audio files from kaggle_male and kaggle_female to monolingual_data

for file in os.listdir("../downloads/kaggle_male/wav"):
    os.system("mv kaggle_male/wav/" + file + " kaggle_male/wav/mlm_mono_" + file)
for file in os.listdir("../downloads/kaggle_female/wav"):
    os.system("mv kaggle_female/wav/" + file + " kaggle_female/wav/mlm_mono_" + file)

os.system("mv kaggle_male/wav/*.wav monolingual_data")
os.system("mv kaggle_female/wav/*.wav monolingual_data")