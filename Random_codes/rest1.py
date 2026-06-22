import streamlit as st  # pip install streamlit

st.header("Streamlit based Employee registration")
st.subheader("This is a subheader")

st.markdown("**Streamlit is nice**")
st.info("Hi, this is Streamlit")

age = st.text_input("Enter age", placeholder="0")
st.warning("Select the age!!!")
if age:  # check if input is not empty
    try:
        age = int(age)

        if age > 18:
            st.success("You can vote")
        else:
            st.error("You can't vote")

    except ValueError:
        st.error("Please enter a valid number")
else:
    st.info("Please enter your age first")

st.button("Submit")
st.title("Prove it :-")
st.file_uploader("uplode file",accept_multiple_files="directory",type=[".txt"])
st.button("Completed")
st.code(
    '''
    //java print
    System.out.printlb("hellow");
''',language="java"
)

# st.title("These are our products:")
# st.markdown(
#     """
#     - TV
#     - Phone
#     - Laptop
#     - PC
#     """
# )