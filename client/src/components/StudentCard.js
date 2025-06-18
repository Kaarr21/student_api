import React, { useState } from "react";

function StudentCard({ student, onDelete, onUpdate }) {
  const [isEditing, setIsEditing] = useState(false);
  const [editData, setEditData] = useState({ ...student });

  const handleChange = (e) =>
    setEditData({ ...editData, [e.target.name]: e.target.value });

  const handleSave = () => {
    onUpdate(student.id, editData);
    setIsEditing(false);
  };

  return (
    <div style={{ border: "1px solid gray", padding: "10px", margin: "10px" }}>
      {isEditing ? (
        <>
          <input name="name" value={editData.name} onChange={handleChange} />
          <input name="email" value={editData.email} onChange={handleChange} />
          <input name="age" value={editData.age} onChange={handleChange} />
          <button onClick={handleSave}>Save</button>
        </>
      ) : (
        <>
          <p><strong>{student.name}</strong></p>
          <p>Email: {student.email}</p>
          <p>Age: {student.age}</p>
          <button onClick={() => setIsEditing(true)}>Edit</button>
        </>
      )}
      <button onClick={() => onDelete(student.id)}>Delete</button>
    </div>
  );
}

export default StudentCard;
