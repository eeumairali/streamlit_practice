import streamlit as st

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

