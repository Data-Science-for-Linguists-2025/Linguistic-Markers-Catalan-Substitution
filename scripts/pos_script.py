import pandas as pd
import stanza

low_analysis_df = pd.read_pickle("LowAnalysisDF.pkl")
nlp = stanza.Pipeline(lang='ca', processors='tokenize,mwt,pos,lemma')
pronoms_mini_doc = nlp("se les vol menjar totes perque li agraden molt")
print("word-POS tupples:")
print([(word.text, word.upos) for
        sent in nlp(pronoms_mini_doc).sentences
        for word in sent.words])
print()

low_analysis_df["POS"] = low_analysis_df["Text"].apply(lambda doc:
                                                        [(word.text, word.upos) for
                                                        sent in nlp(doc).sentences
                                                        for word in sent.words])
low_analysis_df.to_pickle("POS.pkl")
