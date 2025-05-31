import streamlit as st
import pandas as pd
df = pd.read_csv('df.csv')

# text display elements

# add title 
st.title("Streamlit App with Sidebar")

# header 
st.header("This is a header")

# subheader
st.subheader("This is a subheader")

# more control with markdown
st.markdown("## This is a markdown header")
# equation F_{a^2 + b^2 = c^2} = F_{a^2 + b^2 = c^2}
st.markdown('$$F_{a^2 + b^2} == F_{(a + b)^2}$$')


st.code("""
def hello_world():
    print("Hello, World!")
""", language='python')


# caption
st.caption("This is a caption")

# latex
st.latex(r"""
    F_{a^2 + b^2} = F_{(a + b)^2}""")

st.divider()
# sidebar
st.sidebar.title("Sidebar Title")

# sidebar header
st.sidebar.header("Sidebar Header")

# sidebar subheader
st.sidebar.subheader("Sidebar Subheader")

# sidebar markdown
st.sidebar.markdown("## Sidebar Markdown Header")
# sidebar code

### all above was text input elements
# ________________________________________________--

## now starting data input elements

st.dataframe(
    data={
        'Column 1': [1, 2, 3],
        'Column 2': [4, 5, 6],
        'Column 3': [7, 8, 9]
    }
) # it will also show pandas dataframe in sidebar


st.metric(label="Temperature", value="20 °C", delta="1 °C", delta_color="inverse")

# ### data input elements done

# ________________________________________________--

# ### now starting plotting elements
import numpy as np
x = np.linspace(0, 10, 100)
y = np.sin(x)
st.line_chart(y)
st.bar_chart(y)
st.area_chart(y)
# ### plotting elements done



# buttons and widgets


primary_button = st.button("Click Me",type="primary", help="This is a primary button")
seoncd_button = st.button("Click Me Too", type="secondary", help="This is a secondary button")
# checkbox divider
st.divider()
checkbox = st.checkbox("Check Me", value=True, help="This is a checkbox")

if checkbox:
    st.write("Checkbox is checked")
else:
    st.write("Checkbox is unchecked")

# radio button
radio = st.radio("Select Year", options=df.columns[1:], horizontal=True, index=0, help="This is a radio button")

st.divider()
# selectbox

select = st.selectbox("Select Year", options=df.columns[1:], index=0, help="This is a selectbox")

# multiselect
multiselect = st.multiselect("Select Years", options=df.columns[1:], default=[df.columns[1]], help="This is a multiselect")

