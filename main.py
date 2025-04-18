
import streamlit as st

st.title("Growth Mindset Quiz")
st.write("Answer the following questions to see your mindset score.")

score = 0

q1 = st.radio("1. What do you do when faced with a difficult problem?", 
              ("Give up", "Look for help and try again", "Ignore it"))
if q1 == "Look for help and try again":
    score += 1

q2 = st.radio("2. How do you feel about learning new things?", 
              ("It's boring", "I can learn something new", "I avoid it"))
if q2 == "I can learn something new":
    score += 1

q3 = st.radio("3. What do you think about failure?", 
              ("It's the end", "It's a chance to learn", "Avoid at all costs"))
if q3 == "It's a chance to learn":
    score += 1

q4 = st.radio("4. How do you react to feedback?", 
              ("Ignore it", "Take it personally", "Use it to improve"))
if q4 == "Use it to improve":
    score += 1

q5 = st.radio("5. Do you believe intelligence is fixed?", 
              ("Yes", "No", "Not sure"))
if q5 == "No":
    score += 1

if st.button("Check My Mindset"):
    if score >= 4:
        st.success("You have a growth mindset! Keep it up!")
    elif 2 <= score < 4:
        st.info("You're on the way to developing a growth mindset.")
    else:
        st.warning("You might have a fixed mindset. Reflect on how you can grow.")

st.markdown("---")
st.caption("Created with Streamlit for the Growth Mindset Challenge")
