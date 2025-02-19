import streamlit as st
import sqlite3
from datetime import datetime, timedelta

# Function to initialize the database
def init_db():
    conn = sqlite3.connect('leetcode_streak.db')
    cursor = conn.cursor()
    return conn, cursor

# Function to update the streak
def update_streak():
    conn, cursor = init_db()
    today = datetime.now().strftime('%Y-%m-%d')

    # Fetch the last login date and current streak
    cursor.execute('SELECT last_login_date, current_streak FROM streak ORDER BY id DESC LIMIT 1')
    result = cursor.fetchone()

    if result:
        last_login_date, current_streak = result
        last_login_date = datetime.strptime(last_login_date, '%Y-%m-%d')
        today_date = datetime.strptime(today, '%Y-%m-%d')

        # Check if the user logged in yesterday
        if (today_date - last_login_date).days == 1:
            current_streak += 1
        elif (today_date - last_login_date).days > 1:
            current_streak = 1  # Reset streak if missed a day
        else:
            st.warning("You've already logged in today!")
            return
    else:
        # First login
        current_streak = 1

    # Update the database
    cursor.execute('INSERT INTO streak (last_login_date, current_streak) VALUES (?, ?)', (today, current_streak))
    conn.commit()
    st.success(f"Streak updated! Current streak: {current_streak} days")

# Streamlit app
def main():
    st.title("LeetCode Streak Tracker")
    st.write("Track your daily LeetCode streak and don't break it!")

    if st.button("Log Today's Progress"):
        update_streak()

    # Display current streak
    conn, cursor = init_db()
    cursor.execute('SELECT current_streak FROM streak ORDER BY id DESC LIMIT 1')
    result = cursor.fetchone()
    if result:
        st.write(f"Your current streak: {result[0]} days")
    else:
        st.write("No streak data found. Start your streak today!")

if __name__ == "__main__":
    main()