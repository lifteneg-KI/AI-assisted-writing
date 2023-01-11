from .base import BasePage
import streamlit as st
from ..callbacks import submit_essay
from ..mysession import session

__inputtextpage__ = BasePage(name='input_text')

def input_text():
    global __inputtextpage__
    title_empty = st.empty()
    textarea_empty = st.empty()
    btn_empty = st.empty()

    __inputtextpage__.extend(li=[
        title_empty,
        textarea_empty,
        btn_empty
    ])

    title_empty.markdown("# Enter you essay here :)")
    prompt = session.get('prompt')

    if not prompt:
        essay = textarea_empty.text_area(
            label='',
            placeholder="Ich liebe Schokoladen...",
            height=500,
        )
    else:
        col1,col2 = textarea_empty.columns([1,1])
        col1.markdown(f'''**Original Essay:**''')
        col1.info(session.get('text'))
        essay = col2.text_area(
            label='',
            placeholder='change your essay here',
            height=500,
        )
        expander= col1.expander('show feedbacks')
        expander.success(session.get('feedback'))


    btn_empty.button("Submit", on_click=submit_essay,kwargs=dict(
        essay = essay
    ))

