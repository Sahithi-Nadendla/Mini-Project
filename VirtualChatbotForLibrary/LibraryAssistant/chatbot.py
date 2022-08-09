import spacy

nlp = spacy.load("C:\MiniProject\VirtualChatbotForLibrary\InputProcessing_Spacy\output\model-best")

doc = nlp("Silberschatz's Database System Concepts")
for ent in doc.ents:
    print(ent.text,ent.label_)
doc1=nlp("Gate books")
for ent in doc1.ents:
    print(ent.text,ent.label_)
doc2=nlp("Textbooks for Object oriented programming")
for ent in doc2.ents:
    print(ent.text,ent.label_)