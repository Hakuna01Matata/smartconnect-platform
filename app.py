%%writefile app.py

import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="SmartConnect Communication Platform",
    page_icon="📢",
    layout="wide"
)

# Header
st.title("📢 SmartConnect Communication Platform")
st.subheader("Challenge Enterprises of Ghana")

st.markdown("""
A centralized communication platform designed to improve information sharing,
coordination, and productivity across all branches and departments.
""")

# Sidebar
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Select Module",
    [
        "Home",
        "Announcements",
        "Department Channels",
        "Inventory Dashboard",
        "Knowledge Repository",
        "Feedback Center"
    ]
)

# HOME
if menu == "Home":

    st.header("🏠 Central Information Hub")

    col1, col2, col3 = st.columns(3)

    col1.metric("Branches", "6")
    col2.metric("Departments", "6")
    col3.metric("Active Users", "120")

    st.success("Latest Company Announcement")

    st.info("""
    Annual stock-taking exercise begins next Monday.
    All branches should submit inventory reports by Friday.
    """)

    st.warning("New operational update available.")

# ANNOUNCEMENTS
elif menu == "Announcements":

    st.header("📢 Company Announcements")

    announcements = pd.DataFrame({
        "Date": ["2026-06-10", "2026-06-11", "2026-06-12"],
        "Announcement": [
            "Inventory reports due Friday",
            "New leave policy uploaded",
            "Monthly sales meeting scheduled"
        ]
    })

    st.dataframe(announcements, use_container_width=True)

    st.subheader("Post New Announcement")

    title = st.text_input("Title")
    message = st.text_area("Message")

    if st.button("Publish Announcement"):
        st.success("Announcement Published Successfully!")

# DEPARTMENT CHANNELS
elif menu == "Department Channels":

    st.header("💬 Department Communication Channels")

    department = st.selectbox(
        "Select Department",
        [
            "Administration",
            "Accounts",
            "Marketing",
            "Supply Chain",
            "Warehouse & Inventory",
            "Bookshop Operations"
        ]
    )

    st.write(f"### {department} Channel")

    st.chat_message("user").write(
        "Inventory update required before close of business."
    )

    st.chat_message("assistant").write(
        "Inventory report has been submitted."
    )

    message = st.text_input("Enter Message")

    if st.button("Send Message"):
        st.success("Message Sent")

# INVENTORY DASHBOARD
elif menu == "Inventory Dashboard":

    st.header("📊 Inventory & Sales Dashboard")

    inventory = pd.DataFrame({
        "Item": ["Textbooks", "Exercise Books", "Pens", "Markers"],
        "Available Stock": [1200, 850, 1500, 600]
    })

    st.dataframe(inventory, use_container_width=True)

    st.bar_chart(inventory.set_index("Item"))

# KNOWLEDGE REPOSITORY
elif menu == "Knowledge Repository":

    st.header("📚 Knowledge Repository")

    search = st.text_input(
        "Search policies, manuals, procedures..."
    )

    documents = [
        "Employee Leave Policy",
        "Inventory Management Manual",
        "Customer Service Guidelines",
        "Procurement Procedures",
        "Health and Safety Policy"
    ]

    for doc in documents:
        st.write("📄", doc)

# FEEDBACK CENTER
elif menu == "Feedback Center":

    st.header("📝 Employee Feedback System")

    name = st.text_input("Employee Name")
    department = st.text_input("Department")

    feedback = st.text_area(
        "Suggestion / Question / Concern"
    )

    if st.button("Submit Feedback"):
        st.success(
            "Thank you. Your feedback has been submitted."
        )

# Footer
st.markdown("---")
st.caption("SmartConnect Communication Platform Prototype v1.0")