import streamlit as st
from langchain_openai.chat_models import ChatOpenAI

st.title("Fit Fig")
st.write(
    "Get Personalized Ai Training Plans"
)
st.sidebar.image('fit_fig_logo.jpg', width=100)

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")


def generate_response(input_text):
    model = ChatOpenAI(temperature=0.7, api_key=openai_api_key)
    st.info(model.invoke(input_text))

with (((st.form("my_form")))):
    col1, col2 = st.columns(2)

    with col1:
        intent = st.selectbox("What is your MAIN fitness goal?",
                              ("lose weight", "gain muscle", "improve endurance", "just be healthier"),
                              index=None,
                              placeholder = 'select one'
        )
        experience = st.selectbox("What is experience with weight lifting, in general?",
                                  ("I don't know anything", "I know the basics", "I know a lot"),
                                  index=None,
                                  placeholder='select one'
        )

    with col2:
        time = st.selectbox("How many days per week can you like to devote to exercise?",
                            ("1", "2", "3", "4", "5", "6"),
                            index=None,
                            placeholder='select one'
        )
        equipment = st.selectbox("Do you have access to a gym or will you be primarly working out at home?",
                                 ("Yes, I have or will get a gym membership", "I work out at home, but I have a bench, dumbells, and basic equipment", "No, I will work out at home and have very little equipment"),
                                 index=None,
                                 placeholder='select one'
                                 )


    text = f"Using the principles of NASM, generate a 1 month training plan for a client looking to {intent}"
    submitted = st.form_submit_button("Submit")
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key!", icon="⚠")
    if submitted and openai_api_key.startswith("sk-"):
        generate_response(text)
