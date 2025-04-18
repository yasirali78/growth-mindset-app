import streamlit as st

st.set_page_config(page_title="Growth Mindset Challenge", layout="centered")

st.title("Grow with a Growth Mindset!")

st.markdown("""

What is a Growth Mindset?

A growth mindset means believing that your abilities can improve through effort, learning, and persistence.


---

Tips to Develop a Growth Mindset:

Embrace Challenges instead of avoiding them.

Learn from Mistakes to improve yourself.

Stay Persistent even when it's tough.

Celebrate Effort, not just results.

Keep an Open Mind to new ideas.



---

Quick Quiz: Do You Have a Growth Mindset?

""")

q1 = st.radio("1. When I face difficulty, I:", ["Give up", "Look for help and try again"]) q2 = st.radio("2. Mistakes mean:", ["I'm not smart", "I can learn something"]) q3 = st.radio("3. Success comes from:", ["Talent", "Hard work and learning"])

if st.button("Check My Mindset"): score = 0 if q1 == "Look for help and try again": score += 1 if q2 == "I can learn something": score += 1 if q3 == "Hard work and learning": score += 1

st.subheader("Result:")
if score == 3:
    st.success("You have a strong growth mindset! Keep it up!")
elif score == 2:
    st.info("You're on the path! Just need a bit more confidence.")
else:
    st.warning("Try to focus on learning and persistence. You can grow!")

st.markdown("---") st.caption("Created with Streamlit for the Growth Mindset Challenge")

