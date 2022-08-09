import json
import spacy
from spacy.tokens import Span,DocBin

nlp=spacy.blank("en")

with open("Train_data.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

docs=[]

for data in TEXTS:
    doc=nlp(data["text"])
    spans=[]
    for ent in data["entities"]:
        spans.append(Span(doc, ent[0], ent[1], label=ent[2]))
    doc.ents=spans
    docs.append(doc)

doc_bin = DocBin(docs=docs)
doc_bin.to_disk("./train.spacy")


with open("Development_data.json", encoding="utf8") as f:
    texts = json.loads(f.read())

DOCS=[]

for data in texts:
    doc=nlp(data["text"])
    spans=[]
    for ent in data["entities"]:
        spans.append(Span(doc, ent[0], ent[1], label=ent[2]))
    doc.ents=spans
    DOCS.append(doc)

doc_bin = DocBin(docs=DOCS)
doc_bin.to_disk("./dev.spacy")