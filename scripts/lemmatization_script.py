import pandas as pd
import stanza

low_analysis_df = pd.read_pickle("LowAnalysisDF.pkl")
nlp = stanza.Pipeline(lang='ca', processors='tokenize,mwt,pos,lemma')
anar_doc = nlp("anar, vaig, has anat, anàvem, anàreu, aniran")
venir_doc = nlp("venir, vinc, has vingut, veníem, vinguéreu, vindran")
print("Lemmatization anar:")
print(*[f'word: {word.text+" "}\tlemma: {word.lemma}' for sent in anar_doc.sentences for word in sent.words], sep='\n')
print()
print("Lemmatization venir:")
print(*[f'word: {word.text+" "}\tlemma: {word.lemma}' for sent in venir_doc.sentences for word in sent.words], sep='\n')

low_analysis_df["Lemmas"] = low_analysis_df["Text"].apply(lambda doc:
                                                          [word.lemma for
                                                           sent in nlp(doc).sentences
                                                           for word in sent.words])


low_analysis_df.to_pickle("lemmaComplete.pkl")

