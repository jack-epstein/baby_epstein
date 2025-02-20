import streamlit as st

GENDER = "girl"  # change to "boy" if needed 

if "gender" not in st.session_state:
    st.session_state.gender = "None"

# if st.session_state.gender == "girl":
#     st.markdown("# :violet[Baby Epstein is a ...]")
# elif st.session_state.gender == "boy":
#     st.markdown("# :blue[Baby Epstein is a ...]")
# else:
#     st.markdown("# :black[Baby Epstein is a ...]")
st.markdown("# :grey[Baby Epstein is a ...]")
st.markdown("# 🤰🏻")

gender_button = st.button("Click here to see")

if gender_button:
    st.session_state.gender = GENDER
    if st.session_state.gender == "girl":
        st.markdown("""# :heartpulse: :violet[GIRL!!!!!] :heartpulse:""")
        st.markdown("""# :heartpulse: GIRL!!!!! :heartpulse:""")
    elif st.session_state.gender == "boy":
        st.markdown("""# :blue_heart: :blue[BOY!!!!!] :blue_heart:""")
    st.balloons()
