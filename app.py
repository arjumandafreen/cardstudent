import streamlit as st

def CalculateGrade(percentage):
    if percentage >= 80:
        return 'A+ 🎉'
    elif percentage >= 70:
        return 'A 😊'
    elif percentage >= 60:
        return 'B 🙂'
    elif percentage >= 50:
        return 'C 😐'
    elif percentage >= 40:
        return 'D 😕'
    else:
        return 'E 😢'

# Set Streamlit page config
st.set_page_config(page_title="Student Grades", page_icon="📚", layout="centered")

# Custom CSS for background color and styling
st.markdown(
    """
    <style>
    body {
        background-color: lightgreen; /* Light green background */
    }
    .stNumberInput > div > div > input {
        background-color: #800000; /* Light maroon for input boxes */
        color: white;
    }
    .stButton > button {
        background-color: #FF6347; /* Tomato color for button */
        color: white;
        font-weight: bold;
    }
    .stTitle {
        color: #4B0082; /* Indigo color for title */
    }
    .stSubheader {
        color: #8B0000; /* Dark red for subheader */
    }
    .stMarkdown {
        background-color: lightgreen; /* Light green for report card numbers */
        color: black; /* Black text for better visibility */
        padding: 10px;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main heading with emoji
st.title("📚 Student Report Card Generator")
st.markdown("### Created by **Arjumand Afreen Tabinda** 🍓🌟", unsafe_allow_html=True)

# List of subjects
subjects = ["MATH", "PHYSICS", "URDU", "ENGLISH", "COMPUTER"]

# Initialize session state to store student data
if 'students' not in st.session_state:
    st.session_state.students = []

# Function to add a student
def add_student(name, roll_number, marks_dict):
    total_marks = sum(marks_dict.values())
    percentage = (total_marks / (len(subjects) * 100)) * 100
    grade = CalculateGrade(percentage)
    st.session_state.students.append({
        "Name": name,
        "Roll Number": roll_number,
        "Marks": marks_dict,
        "Total Marks": total_marks,
        "Percentage": percentage,
        "Grade": grade
    })

# Input fields for student details
st.subheader("Enter Student Details")
StudentName = st.text_input("Enter your name:")
StudentRollNo = st.text_input("Enter your roll number:")

# Input fields for marks with light maroon background
marks_dict = {}
for subject in subjects:
    marks = st.number_input(
        f"Enter marks for {subject} (out of 100):",
        min_value=0,
        max_value=100,
        step=1,
        key=subject
    )
    marks_dict[subject] = marks

# Button to add student
if st.button("Add Student"):
    if not StudentName or not StudentRollNo:
        st.error("Please enter both the student's name and roll number.")
    else:
        add_student(StudentName, StudentRollNo, marks_dict)
        st.success(f"Record of {StudentName} added successfully!")

# Button to generate report cards for all students
if st.button("Generate Report Cards"):
    if not st.session_state.students:
        st.warning("No student records found. Please add students first.")
    else:
        st.subheader("📝 Report Cards for Students")
        for student in st.session_state.students:
            st.markdown(f"**Name:** {student['Name']}", unsafe_allow_html=True)
            st.markdown(f"**Roll Number:** {student['Roll Number']}", unsafe_allow_html=True)
            st.markdown(f"**Total Marks Obtained:** <div style='background-color: lightgreen; color: black; padding: 5px; border-radius: 5px;'>{student['Total Marks']} out of {len(subjects) * 100}</div>", unsafe_allow_html=True)
            st.markdown(f"**Percentage:** <div style='background-color: lightgreen; color: black; padding: 5px; border-radius: 5px;'>{student['Percentage']:.2f}%</div>", unsafe_allow_html=True)
            st.markdown(f"**Grade:** <div style='background-color: lightgreen; color: black; padding: 5px; border-radius: 5px;'>{student['Grade']}</div>", unsafe_allow_html=True)
            st.markdown("---")