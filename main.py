import streamlit as st


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