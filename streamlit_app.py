# Import python packages
import streamlit as st

# Write directly to the app
st.title(":cup_with_straw: Customized Your Smoothie !  :cup_with_straw:")
st.write(
  """Replace this example with your own code!
  **And if you're new to Streamlit,** check
  out our easy-to-follow guides at
  [docs.streamlit.io](https://docs.streamlit.io).
  """
)

# option = st.selectbox(
#     "What is your favorite fruits ?",
#     ("Banana", "Strawberries", "Peaches"),
# )

ingredients_string = ''
name_on_order = ''

name_on_order = st.text_input('Name on Smoothies')
st.write('The Name On The Smoothies Will Be :' ,name_on_order) 

# st.write("You favorite fruits is:", option)
from snowflake.snowpark.functions import col
session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)
ingredients_list=st.multiselect(
    'Chose up to 5 ingredents:'
    , my_dataframe
    ,max_selections =5
)

if ingredients_list:
    #st.write(ingredients_list) 
    #st.text(ingredients_list)   

    for fruit_chosen in ingredients_list:
     ingredients_string += fruit_chosen + ' '
#st.write(ingredients_string)

my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','""" + name_on_order + """')"""

#st.write(my_insert_stmt)
time_to_insert = st.button('Submit Order')

if time_to_insert:
    session.sql(my_insert_stmt).collect()
    cnx = st.connection("snowflake")
    session = cnx.session()
    st.success('Your Smoothie is ordered!', icon="✅")
#if ingredients_string:
    #session.sql(my_insert_stmt).collect()
    
