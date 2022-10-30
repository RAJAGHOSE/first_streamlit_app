import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
#
#
def fruit_list(fruit_choice) :
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
  #streamlit.text(fruityvice_response.json())
  # write your own comment -what does the next line do?
  return pandas.json_normalize(fruityvice_response.json())


streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
#
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
#
streamlit.dataframe(my_fruit_list.loc[fruits_selected])

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

streamlit.header('Smoothie Advice')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.text('Please select fruit')
  else:
    streamlit.write('The user entered ', fruit_choice)
    fruityvice_normalized = fruit_list(fruit_choice)
    streamlit.dataframe(fruityvice_normalized)
    
except URLerror as e:
  streamlit.error()
  
def get_fruit_list_from_db:
  my_cur = my_cnx.cursor()
  my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
  return my_cur.fetchall()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_data_row = get_fruit_list_from_db(my_cnx);
streamlit.text("Hello from Snowflake:")
streamlit.dataframe(my_data_row)

streamlit.stop()

fruit_choice1 = streamlit.text_input('What fruit would you like to add?','Kiwi')
streamlit.write('Thanks for adding ', fruit_choice1)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("INSERT INTO fruit_load_list values ('STREAMLIT')")
