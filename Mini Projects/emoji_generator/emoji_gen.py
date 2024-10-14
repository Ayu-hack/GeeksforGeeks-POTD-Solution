import streamlit as st
import random
import emoji

# Get a list of all emojis
all_emojis = list(emoji.EMOJI_DATA.keys())

# Function to generate a random emoji combination
def generate_random_emoji_combo(n):
    return ''.join(random.choices(all_emojis, k=n))

# Streamlit app
st.title("Random Emoji Generator")

st.write("This app generates a unique and funky combination of emojis.")

# Slider to select the number of emojis
num_emojis = st.slider("Select number of emojis:", 1, 10, 5)

# Button to generate emoji combination
if st.button("Generate"):
    random_emojis = generate_random_emoji_combo(num_emojis)
    st.write(f"The Random Emoji U many want: {random_emojis}")
    st.markdown(f"<div style='font-size: 50px;'>{random_emojis}</div>", unsafe_allow_html=True)

print("Hello")
