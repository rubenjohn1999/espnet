import pickle
list_of_utterances = set()
male_utterances = open("male/test_ml/text", "r")
for line in male_utterances:
    list_of_utterances.add(line.split()[0].split("_")[1])

female_utterances = open("female/test_ml/text", "r")
for line in female_utterances:
    list_of_utterances.add(line.split()[0].split("_")[1])
list_of_utterances = list(list_of_utterances)
print(list_of_utterances)
f = open("test_speakers.pkl", "wb")
pickle.dump(list_of_utterances, f)
f.close()

open_file = open("test_speakers.pkl", "rb")
loaded_list = pickle.load(open_file)
open_file.close()