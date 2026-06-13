import streamlit as st
import pandas as pd
import os

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

    import pandas as pd
    import os

    st.subheader("📢 Company Announcements")

    file_path = "announcements.csv"

    # ---------------------------
    # LOAD EXISTING ANNOUNCEMENTS
    # ---------------------------
    if os.path.exists(file_path):
        announcements = pd.read_csv(file_path)
    else:
        announcements = pd.DataFrame(columns=["Date", "Announcement"])

    st.dataframe(announcements, use_container_width=True)

    st.divider()

    # ---------------------------
    # CREATE NEW ANNOUNCEMENT
    # ---------------------------
    st.subheader("Create Announcement")

    date = st.date_input("Date")
    message = st.text_area("Message")

    if st.button("Publish"):

        if message:

            new_data = pd.DataFrame([{
                "Date": str(date),
                "Announcement": message
            }])

            if os.path.exists(file_path):
                old_data = pd.read_csv(file_path)
                updated = pd.concat([old_data, new_data], ignore_index=True)
            else:
                updated = new_data

            updated.to_csv(file_path, index=False)

            st.success("Announcement Published Successfully!")

        else:
            st.error("Please enter a message.")

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

    st.bar_chart(
        inventory.set_index("Item")
    )

# ---------------------------
# KNOWLEDGE REPOSITORY
# ---------------------------
elif page == "Knowledge Repository":

    st.subheader("📚 Knowledge Repository")

    docs_folder = "documents"

    search = st.text_input("🔍 Search Documents")

    if not os.path.exists(docs_folder):
        st.error("Documents folder not found. Please create a 'documents/' folder in your repo.")
        st.stop()

    files = os.listdir(docs_folder)

    # Keep only PDFs
    files = [f for f in files if f.endswith(".pdf")]

    # Search filter
    if search:
        files = [f for f in files if search.lower() in f.lower()]

    if len(files) == 0:
        st.info("No documents found.")
    else:
        for file in files:

            path = os.path.join(docs_folder, file)

            # ✅ FIX: read file properly in binary mode
            with open(path, "rb") as f:
                file_bytes = f.read()

            st.download_button(
                label=f"📄 {file}",
                data=file_bytes,
                file_name=file,
                mime="application/pdf"
            )
# ---------------------------
# ---------------------------
# FEEDBACK CENTRE
# ---------------------------
elif page == "Feedback Centre":

    import pandas as pd
    import os

    st.subheader("📝 Employee Feedback")

    file_path = "feedback.csv"

    name = st.text_input("Name")
    dept = st.text_input("Department")
    feedback = st.text_area("Suggestion / Concern")

    if st.button("Submit Feedback"):

        if name and dept and feedback:

            new_data = pd.DataFrame([{
                "Name": name,
                "Department": dept,
                "Feedback": feedback
            }])

            # If file exists, append; else create new
            if os.path.exists(file_path):
                old_data = pd.read_csv(file_path)
                updated_data = pd.concat([old_data, new_data], ignore_index=True)
            else:
                updated_data = new_data

            updated_data.to_csv(file_path, index=False)

            st.success("Feedback submitted successfully!")

        else:
            st.error("Please fill all fields before submitting.")

    st.divider()

    st.subheader("📂 All Submitted Feedbacks")

    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No feedback submitted yet.")
