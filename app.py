import streamlit as st
from gensim.models import Word2Vec

model = Word2Vec.load("reuters_word2vec.model")

st.title("🧠 Reuters Word Explorer")
st.markdown("Enter a word to discover its most similar terms using Word2Vec")

word = st.text_input("Type a word", "china")

if word:
    if word in model.wv:
        similar = model.wv.most_similar(word, topn=5)
        st.success(f"Top 5 similar words to **{word}**:")
        for w, score in similar:
            st.write(f"- {w} (score: {score:.2f})")
    else:
        st.warning("⚠️ Word not found in vocabulary.")
