import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post


# Options for length and language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "French"]
title_options = ["Hi", "Hi All", "Dear"]


# Main app layout
def main():
    st.subheader("LinkedIn Post Generator: Hi there")

    # Create three columns for the dropdowns
    col1, col2 = st.columns(2)
    fs = FewShotPosts()
    tags = fs.get_tags()
    with col1:
        # Dropdown for Topic (Tags)
        selected_tag = st.selectbox("Topic", options=tags)

    with col2:
        # Dropdown for Length
        selected_length = st.selectbox("Length", options=length_options)

    col3, col4 = st.columns(2)
    with col3:
        # Dropdown for Language
        selected_language = st.selectbox("Language", options=language_options)

    with col3:
        # Dropdown for Language
        selected_title = st.selectbox("Title", options=title_options)


    # Generate Button
    if st.button("Generate"):
        post = generate_post(selected_length, selected_language, selected_tag, selected_title)
        st.write(post)


# Run the app
if __name__ == "__main__":
    main()