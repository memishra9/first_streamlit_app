import streamlit
streamlit.title('My parent healthy diner')
streamlit.header('Breakfast menu')
streamlit.text('🥣 Omega3 & Blueberry Oatmeal')
streamlit.text('Kale spinach and Rocket Smoothie')
streamlit.text('🐔Hard Boiled Free-Range Egg')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

streamlit.multiselect("Pick some Fruits:" list(my_fruit_list.index) )

