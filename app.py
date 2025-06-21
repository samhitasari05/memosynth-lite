import streamlit as st
from memosynth.vector_store import query_memory

# Streamlit app UI
st.set_page_config(page_title="MemoSynth", page_icon="🧠")
st.title("🧠 MemoSynth - Memory Assistant")
st.markdown("Ask me a question and I’ll retrieve related memory entries from Qdrant!")

# Input from user
query = st.text_input("What would you like to know?", "")

# When user hits Enter
if query:
    with st.spinner("🔍 Searching..."):
        results = query_memory(query)

    # Display results
    if results:
        st.success(f"Found {len(results)} matching memory entries:")
        for idx, r in enumerate(results, 1):
            st.markdown(f"### 📌 Result {idx}")
            st.markdown(f"**Summary:** {r.get('summary', 'N/A')}")
            st.markdown(f"**Project:** {r.get('project', 'N/A')}")
            st.markdown(f"**Source:** {r.get('source', 'N/A')}")
            st.markdown(f"**Date:** {r.get('created_at', 'N/A')}")
            st.markdown("---")
    else:
        st.warning("No relevant memory entries found.")



