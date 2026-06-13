import streamlit as st
import pandas as pd

# ---------------------------
# PAGE CONFIGURATION
# ---------------------------
st.set_page_config(
    page_title="SmartConnect",
    page_icon="🚀",
    layout="wide"
)

# ---------------------------
# CUSTOM CSS
# ---------------------------
st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.header-box {
    background: linear-gradient(90deg,#0f4c81,#1b6ca8);
    padding:20px;
    border-radius:15px;
    color:white;
    margin-bottom:20px;
}

.notification-box {
    background:#fff8e1;
    padding:15px;
    border-left:6px solid orange;
    border-radius:10px;
}

.footer {
    text-align:center;
    color:gray;
    padding:20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# SIDEBAR
# ---------------------------
st.sidebar.title("🚀 SmartConnect")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Announcements",
        "Department Channels",
        "Inventory Dashboard",
        "Knowledge Repository",
        "Feedback Centre"
    ]
)

# ---------------------------
# HEADER
# ---------------------------
st.markdown("""
<div class='header-box'>
<h1>🚀 SmartConnect Communication Platform</h1>
<h4>Challenge Enterprises of Ghana</h4>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# DASHBOARD
# ---------------------------
if page == "Dashboard":

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Employees", "120")

    with col2:
        st.metric("Branches", "6")

    with col3:
        st.metric("Departments", "6")

    with col4:
        st.metric("Notifications", "14")

    st.markdown("### 📢 Latest Updates")

    st.markdown("""
    <div class='notification-box'>
    Annual Stock Taking Exercise begins Monday.<br>
    Inventory reports due by Friday.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📊 Branch Activity")

    branch_data = pd.DataFrame({
        "Branch": [
            "Legon",
            "Kokomlemle",
            "Tema",
            "Takoradi",
            "Kumasi",
            "Baastona"
        ],
        "Activity": [85, 72, 65, 51, 45, 40]
    })

    st.bar_chart(branch_data.set_index("Branch"))

# ---------------------------
# ANNOUNCEMENTS
# ---------------------------
elif page == "Announcements":

    st.subheader("📢 Company Announcements")

    announcements = pd.DataFrame({
        "Date": [
            "2026-06-10",
            "2026-06-11",
            "2026-06-12"
        ],
        "Announcement": [
            "Inventory reports due Friday",
            "Leave policy updated",
            "Monthly sales meeting scheduled"
        ]
    })

    st.dataframe(
        announcements,
        use_container_width=True
    )

    st.divider()

    st.subheader("Create Announcement")

    title = st.text_input("Title")
    message = st.text_area("Message")

    if st.button("Publish"):
        st.success("Announcement Published Successfully")

# ---------------------------
# DEPARTMENT CHANNELS
# ---------------------------
elif page == "Department Channels":

    st.subheader("💬 Department Communication")

    dept = st.selectbox(
        "Department",
        [
            "Administration",
            "Accounts",
            "Marketing",
            "Supply Chain",
            "Warehouse & Inventory",
            "Bookshop Operations"
        ]
    )

    st.info(f"Current Channel: {dept}")

    st.chat_message("user").write(
        "Inventory report needed urgently."
    )

    st.chat_message("assistant").write(
        "Report uploaded successfully."
    )

    msg = st.text_input("Type Message")

    if st.button("Send"):
        st.success("Message Sent")

# ---------------------------
# INVENTORY DASHBOARD
# ---------------------------
elif page == "Inventory Dashboard":

    st.subheader("📦 Inventory Dashboard")

    inventory = pd.DataFrame({
        "Item": [
            "Textbooks",
            "Pens",
            "Exercise Books",
            "Markers"
        ],
        "Stock": [
            1200,
            1400,
            950,
            600
        ]
    })

    st.dataframe(
        inventory,
        use_container_width=True
    )

    st.line_chart(
        inventory.set_index("Item")
    )

# ---------------------------
# KNOWLEDGE REPOSITORY
# ---------------------------
elif page == "Knowledge Repository":

    st.subheader("📚 Knowledge Repository")

    search = st.text_input(
        "Search Policies, Manuals and Procedures"
    )

    docs = [
        "Employee Leave Policy",
        "Inventory Management Manual",
        "Customer Service Guide",
        "Procurement Procedures",
        "Health & Safety Policy"
    ]

    for doc in docs:
        st.write("📄", doc)

# ---------------------------
# FEEDBACK CENTRE
# ---------------------------
elif page == "Feedback Centre":

    st.subheader("📝 Employee Feedback")

    name = st.text_input("Name")

    dept = st.text_input("Department")

    feedback = st.text_area(
        "Suggestion / Concern"
    )

    if st.button("Submit Feedback"):
        st.success(
            "Feedback submitted successfully."
        )

# ---------------------------
# FOOTER
# ---------------------------
st.markdown("---")

st.markdown(
    "<div class='footer'>SmartConnect v2.0 | Challenge Enterprises of Ghana</div>",
    unsafe_allow_html=True
)
