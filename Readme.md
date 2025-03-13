
 **Student Report Card Generator** project. This README provides an overview of the project, its features, how to use it, and other relevant details.

---

# 📚 Student Report Card Generator

## 🚀 Overview
The **Student Report Card Generator** is a Streamlit-based web application designed to help teachers or administrators generate report cards for students. It allows users to input student details, marks for various subjects, and automatically calculates the total marks, percentage, and grade for each student. The application supports batch processing, enabling users to add multiple students and generate their report cards in one go.

---

## ✨ Features
1. **Interactive User Interface**:
   - Simple and intuitive interface for entering student details and marks.
   - Real-time feedback for successful data entry or errors.

2. **Grade Calculation**:
   - Automatically calculates the total marks, percentage, and grade based on the provided marks.
   - Uses a predefined grading scale:
     - A+ 🎉 (80% and above)
     - A 😊 (70% to 79%)
     - B 🙂 (60% to 69%)
     - C 😐 (50% to 59%)
     - D 😕 (40% to 49%)
     - E 😢 (Below 40%)

3. **Batch Processing**:
   - Add multiple students in one session.
   - Generate report cards for all students at once.

4. **Error Handling**:
   - Validates input fields to ensure no empty values for student names or roll numbers.
   - Ensures marks are within the valid range (0 to 100).

5. **Styling**:
   - Light green background for the page.
   - Light maroon input boxes for marks.
   - Visually appealing report cards with emojis and colored backgrounds.

---

## 🛠️ How to Use
1. **Enter Student Details**:
   - Input the student's name and roll number.
   - Enter marks for each subject (Math, Physics, Urdu, English, Computer).

2. **Add Students**:
   - Click the **"Add Student"** button to save the student's data.
   - Repeat the process to add more students.

3. **Generate Report Cards**:
   - Click the **"Generate Report Cards"** button to view report cards for all added students.

4. **View Report Cards**:
   - The application displays each student's name, roll number, total marks, percentage, and grade in a formatted report card.

---

## 🖥️ Running the Application
1. **Install Streamlit**:
   If you don't have Streamlit installed, run the following command:
   ```bash
   pip install streamlit
   ```

2. **Run the Application**:
   Save the code in a file (e.g., `student_report_card.py`) and run it using Streamlit:
   ```bash
   streamlit run student_report_card.py
   ```

3. **Access the Application**:
   Open the provided URL in your web browser to use the application.

---

## 🎨 Customization
- **Change Subjects**:
  Modify the `subjects` list in the code to include or remove subjects.
  ```python
  subjects = ["MATH", "PHYSICS", "URDU", "ENGLISH", "COMPUTER"]
  ```

- **Update Grading Scale**:
  Adjust the grading logic in the `CalculateGrade` function to match your institution's grading system.

- **Styling**:
  Customize the CSS in the `st.markdown` section to change colors, fonts, or other visual elements.

---

## 📝 Example Output
### Input:
- **Name**: Ali
- **Roll Number**: 101
- **Marks**:
  - Math: 85
  - Physics: 90
  - Urdu: 75
  - English: 80
  - Computer: 95

### Output:
```
📝 Report Card
--------------------------------------
Name: Ali
Roll Number: 101
--------------------------------------
Total Marks Obtained: 425 out of 500
Percentage: 85.00%
Grade: A+ 🎉
--------------------------------------
```

---

## 🛑 Error Handling
- If the user leaves the **name** or **roll number** fields empty, an error message is displayed.
- If no students are added before generating report cards, a warning message is shown.

---

## 📂 Project Structure
- **Streamlit App**:
  - Built using Python and Streamlit.
  - Uses session state to store student data.
  - Custom CSS for styling.

- **Dependencies**:
  - Streamlit (`pip install streamlit`)

---

## 👩‍💻 Created By
This project was created by **Arjumand Afreen Tabinda** 🍓🌟.

---

## 📜 License
This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it as needed.

---

## 🙏 Acknowledgments
- Thanks to **Streamlit** for providing an excellent framework for building interactive web applications.
- Special thanks to all contributors and users for their feedback and support.

---

## 📧 Contact
For questions or feedback, please contact:
- **Email**: [Your Email]
- **GitHub**: [Your GitHub Profile]

---

Enjoy using the **Student Report Card Generator**! 🚀



