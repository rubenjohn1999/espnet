import pickle
list_of_utterances = []
male_utterances = open("male/test_ml/text", "r")
for line in male_utterances:
    list_of_utterances.append(line.split()[0])

f = open("male_test_speakers.pkl", "wb")
pickle.dump(list_of_utterances, f)
f.close()

list_of_utterances = []
female_utterances = open("female/test_ml/text", "r")
for line in female_utterances:
    list_of_utterances.append(line.split()[0])

f = open("female_test_speakers.pkl", "wb")
pickle.dump(list_of_utterances, f)
f.close()

