import pickle
list_of_utterances = set()
male_utterances = open("train_ml/text", "r")
for line in male_utterances:
    list_of_utterances.add(line.split()[0].split("_")[1])

female_utterances = open("dev_ml/text", "r")
for line in female_utterances:
    list_of_utterances.add(line.split()[0].split("_")[1])
list_of_utterances = list(list_of_utterances)



open_file = open("/home/ubuntu/espnet/egs2/ml_openslr63/asr1/local/test_speakers.pkl", "rb")
loaded_list = pickle.load(open_file)
open_file.close()

set_difference = set(list_of_utterances).intersection(set(loaded_list))
print(set_difference)
