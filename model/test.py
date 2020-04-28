import spacy
output_dir="./"
test_text="Are indian locations like goa, pune, mumbai, delhi, jaipur, jammu and kashmir recognized as per 28 of arpril 2020?"
print("Loading from", output_dir)
nlp2 = spacy.load(output_dir)
doc2 = nlp2(test_text)
for ent in doc2.ents:
    print(ent.label_, ent.text)