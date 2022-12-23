import streamlit as st

st.title('Projekti')


def convert_list(texti):
    lista=texti.split()
    return lista

def convert_upper(text):

    uppercaselist=[]
    for i in text:
        i=i.upper()
        uppercaselist.append(i)
    return uppercaselist

def count(text_list):
    return len(text_list)

text=st.text_input('Sheno tekstin: ')
clist=convert_list(text)


if st.button('List'):
    st.write(convert_list(text))
if st.button('Upper-list'):
    st.write(convert_upper(clist))
if st.button('Count'):
    st.write(count(clist))