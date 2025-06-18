import React, { useState, useEffect } from "react";
import axios from "axios";
import StudentForm from "./components/StudentForm";
import StudentList from "./components/StudentList";

const baseURL = "http://127.0.0.1:5000/students/";

function App() {
  const [students, setStudents] = useState([]);

  const fetchStudents = () => {
    axios.get(baseURL)
      .then((res) => setStudents(res.data))
      .catch((err) => console.error(err));
  };

  useEffect(() => {
    fetchStudents();
  }, []);

  const addStudent = (newStudent) => {
    axios.post(baseURL, newStudent)
      .then(() => fetchStudents())
      .catch((err) => console.error(err));
  };

  const updateStudent = (id, updatedStudent) => {
    axios.patch(`${baseURL}${id}`, updatedStudent)
      .then(() => fetchStudents())
      .catch((err) => console.error(err));
  };

  const deleteStudent = (id) => {
    axios.delete(`${baseURL}${id}`)
      .then(() => fetchStudents())
      .catch((err) => console.error(err));
  };

  return (
    <div className="App">
      <h1>Student Management</h1>
      <StudentForm onSubmit={addStudent} />
      <StudentList
        students={students}
        onDelete={deleteStudent}
        onUpdate={updateStudent}
      />
    </div>
  );
}

export default App;
