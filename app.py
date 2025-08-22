import streamlit as st
import matplotlib.pyplot as plt

# --- App title ---
st.title("💰 Personal Finance Chatbot")

# --- User input ---
question = st.text_input("Ask me something like: 'How can I save ₹5000 from my ₹15000 salary?'")

# --- Rule-based simple response ---
if question:
    st.subheader("Answer:")
    
    # Example calculation
    total_salary = 15000
    savings_goal = 5000
    needs = 7000      # Rent, food, bills
    wants = total_salary - needs - savings_goal
    
    # Rule-based text advice
    advice = (
        f"From your ₹{total_salary} salary:\n"
        f"✅ Needs: ₹{needs}\n"
        f"✅ Wants: ₹{wants}\n"
        f"✅ Savings: ₹{savings_goal}\n\n"
        "Tip: Try to reduce Wants to increase Savings!"
    )
    st.text(advice)
    
    # --- Pie chart ---
    labels = ['Needs', 'Wants', 'Savings']
    sizes = [needs, wants, savings_goal]
    colors = ['#ff9999', '#66b3ff', '#99ff99']  # Pastel colors
    explode = (0.05, 0.05, 0.05)  # Slightly separate slices
    
    fig, ax = plt.subplots()
    ax.pie(
        sizes, labels=labels, autopct='%1.1f%%', startangle=90,
        colors=colors, explode=explode, shadow=True
    )
    ax.axis('equal')  # Circle shape
    st.pyplot(fig)
