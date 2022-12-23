import streamlit as st

st.title('Projekti')



stringu=st.text_input('Jepni tekstin')


def convert_list(a):
    a=stringu.split()
    if st.button('Return list'):
        st.write(f"Result: {a}")
    return a    
print(convert_list(stringu))


# def convert_upper():
    
#     upper_words = []
#     n=convert_list
#     for word in n:
#         upper_words.append(word.upper())
#         return upper_words
#     st.button('Return list')
#     st.write(f"Result: {upper_words}")
# print(convert_upper())


def count():
    count=0
    m=convert_list
    for i in m:
        count=+1
    st.button('Return list')
    st.write(f"Result: {count}")
count()
        
