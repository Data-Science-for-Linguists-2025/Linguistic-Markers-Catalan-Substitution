import pandas as pd
import stanza

data_df = pd.read_pickle("lemmaComplete.pkl")
nlp = stanza.Pipeline(lang='ca', processors='tokenize')
mini_doc = nlp("Hola, com estas? Jo genial. I tu? Anem a fer una volta?")
print("sentences list:")
print([sent.text  for
        sent in nlp(mini_doc).sentences])
print()

data_df["Sent_toks"] = data_df["Text"].apply(lambda doc:
                                                        [sent.text  for
                                                        sent in nlp(doc).sentences])
data_df.to_pickle("sent_tok.pkl")
