import streamlit as st
import pandas as pd
import altair as alt

if 'scores' not in st.session_state:
    st.session_state['scores'] = {
        'Jess': 0,
        'Courtland': 0,
        'Ksenia': 0
    }

def update_score(player, wager, correct):
    if correct:
        st.session_state['scores'][player] += wager
    else:
        st.session_state['scores'][player] -= wager

def display_standings():
    st.subheader('Current standings:')
    for player, score in st.session_state['scores'].items():
        st.write(f'{player}: {score}')

if __name__=='__main__':
    st.set_page_config(
        page_title="Jeopardy App",
        page_icon="🎲",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://www.extremelycoolapp.com/help',
            'Report a bug': "https://www.extremelycoolapp.com/bug",
            'About': "# This is a header. This is an *extremely* cool app!"
        }
    )
    st.title(':red[Streamlit Jeopardy] :tada:')

    player = st.selectbox('Select player', ['Jess', 'Courtland', 'Ksenia'])
    wager = st.number_input('Enter wager:')
    correct = st.checkbox('Correct answer?')

    if st.button('Update Score'):
        update_score(player, wager, correct)


    display_standings()