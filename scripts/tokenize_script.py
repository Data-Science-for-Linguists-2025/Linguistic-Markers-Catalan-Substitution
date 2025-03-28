# importing stanza tokenizer
import stanza
# importing pandas
import pandas as pd

# creating tokenization pipeline
tkzr = stanza.Pipeline(lang='ca', processors='tokenize')

# loading complete dataframe
complete_df = pd.read_pickle("/Users/janabruses/Documents/data_science/Linguistic-Markers-Catalan-Substitution/modified1_complete.pkl")

# creating a column for the return of the tkzr (a doc object)
complete_df["toks"] = complete_df["Text"].apply(tkzr)

# creating a column for text length in tokens
complete_df["Len_toks"] = complete_df["toks"].apply(lambda x : x.num_tokens)

# creating a function that only takes the tokens out of the Stanza's document
def tokenize(doc):
    tokens = [word.text for sentence in doc.sentences for word in sentence.tokens]
    return tokens

# keeping only the tokens of the documents as a list using custum function
complete_df["toks"] = complete_df["toks"].apply(tokenize)


# saving dataframe with new data/columns as a pickle
complete_df.to_pickle("tokcomplete_df.pkl")
