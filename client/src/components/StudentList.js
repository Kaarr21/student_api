import React from "react";
import StudentCard from "./StudentCard";

function StudentList({ students, onDelete, onUpdate }) {
  return (
    <div>
      {students.map((student) => (
        <StudentCard
          key={student.id}
          student={student}
          onDelete={onDelete}
          onUpdate={onUpdate}
        />
      ))}
    </div>
  );
}

export default StudentList;
