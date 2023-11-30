import streamlit as st
import langchainhelper

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("pick a Cuisine",("Indian","Italian","Arabic","Turkish","chinees"))

if cuisine:
    response = langchainhelper.generate_res_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("->",item)


