from collections import defaultdict

labels = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']
label_dict = dict()
for i, l in enumerate(labels):
    label_dict[i] = l

preds_cnn = [2,0,0,0,0,0,0,0,2,0,0,0,7,0,5,5,2,1,5,1,2,2,0,5,0,2,1,2,2,2,5,0,0,0,0,0,7
,7,2,2,2,2,1,2,7,0,2,2,2,5,1,0,7,1,0,2,2,2,0,0,0,2,0,1,2,2,0,2,5,7,0,2,0,2
,0,0,1,0,5,0,0,2,0,0,0,0,0,2,2,0,5,2,7,0,1,0,0,1,0,2,2,2,5,0,2,5,2,1,5,2,5
,2,2,2,2,1,2,0]

preds_rnn = [9,7,9,9,2,2,2,7,9,2,9,2,9,2,2,2,9,1,2,9,9,9,1,2,2,1,9,2,2,2,2,2,2,9,2,0,9
,9,2,9,2,2,1,9,2,2,2,2,2,2,1,7,7,1,0,2,9,2,9,9,5,2,2,2,2,2,2,9,2,9,2,7,9,9
,0,9,1,9,2,2,9,2,2,9,0,2,9,2,7,2,2,2,1,2,1,7,2,1,2,9,2,2,2,2,2,0,2,1,9,2,2
,9,9,2,2,2,2,2]

preds_hybrid = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,1,2,2,4,2,2,1,1,2,9,2,2,2,2,2,2,4,9
,9,2,2,2,9,1,9,7,2,9,2,2,2,4,7,4,1,0,9,9,2,2,2,2,2,2,2,2,2,2,2,2,9,2,2,9,9
,0,2,1,2,2,2,2,2,2,9,2,2,2,2,9,2,9,2,1,9,1,2,2,4,2,2,2,2,2,2,2,9,2,1,2,2,2
,2,2,1,2,1,2,2]

counter = defaultdict(int)
counter_cnn = defaultdict(int)
counter_rnn = defaultdict(int)
counter_hybrid = defaultdict(int)

for p in preds_cnn:
    counter[label_dict[p]] += 1
    counter_cnn[label_dict[p]] += 1

for p in preds_rnn:
    counter[label_dict[p]] += 1
    counter_rnn[label_dict[p]] += 1

for p in preds_hybrid:
    counter[label_dict[p]] += 1
    counter_hybrid[label_dict[p]] += 1

print("Total Stats: ", counter)
print("CNN Stats: ", counter_cnn)
print("RNN Stats: ", counter_rnn)
print("Hybrid Stats: ", counter_hybrid)
