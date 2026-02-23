from collections import defaultdict

corpus = [
    ["<s>","I","love","NLP","</s>"],
    ["<s>","I","love","deep","learning","</s>"],
    ["<s>","deep","learning","is","fun","</s>"]
]

unigram = defaultdict(int)
bigram = defaultdict(int)

for sent in corpus:
    for i in range(len(sent)):
        unigram[sent[i]] += 1
        if i > 0:
            bigram[(sent[i-1],sent[i])] += 1

def bigram_prob(w1,w2):
    return bigram[(w1,w2)] / unigram[w1]

def sentence_prob(sentence):
    prob = 1
    for i in range(1,len(sentence)):
        prob *= bigram_prob(sentence[i-1],sentence[i])
    return prob

s1 = ["<s>","I","love","NLP","</s>"]
s2 = ["<s>","I","love","deep","learning","</s>"]

print("S1 probability:", sentence_prob(s1))
print("S2 probability:", sentence_prob(s2))

# Q8.9: Decide which sentence is preferred by the model
if s1 > s2:
    print("The model prefers Sentence 1: '<s> I love NLP </s>' because it has a higher probability.")
elif s2 > s1:
    print("The model prefers Sentence 2: '<s> I love deep learning </s>' because it has a higher probability.")
else:
    print("Both sentences have equal probability.")
