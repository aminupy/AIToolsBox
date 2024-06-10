import React, { useState, useEffect } from "react";
import axios from 'axios';
import { useNavigate } from "react-router-dom";
import "./edit.css"

export default function EditProfile () {
 const [firstName, setFirstName] = useState("");
 const [lastName, setLastName] = useState("");
 const [email, setEmail] = useState("");
 const [password, setPassword] = useState("");
 const [isEditOpen, setIsEditOpen] = useState(true);
 const navigate = useNavigate();
 const [userId, setUserId] = useState("");


 useEffect(() => {
    const token = localStorage.getItem('accessToken');

    axios.get('http://localhost:80/api/users', {
      headers: {
       'Authorization': `Bearer ${token}`
      }
    }).then(response => {
      setFirstName(response.data.User.first_name);
      setLastName(response.data.User.last_name);
      setEmail(response.data.User.email);
      setPassword(response.data.User.password);
      setUserId(response.data.User.id);
    }).catch(error => {
      console.error(error);
    });
 }, []);

 const handleBlur = (event, setter) => {
    setter(event.target.innerText);
 };

 const handleSave = () => {
  const token = localStorage.getItem('accessToken');
  
  if (!firstName || !lastName || !email) {
      alert('Please fill out all fields');
      return;
  }
  
  const userInfo = {
      first_name: firstName,
      last_name: lastName,
      email: email,
  };
  
  const params = new URLSearchParams(userInfo).toString();
  console.log(`http://localhost:80/api/users/?${params}`)
  axios.put(`http://localhost:80/api/users/?${params}`, {}, {
     headers: {
       'Authorization': `Bearer ${token}`
     }
  }).then(response => {
      console.log('Response:', response);
      alert('User information updated successfully');
  }).catch(error => {
      console.error('Error:', error);
      if (error.response) {
        console.log('Response data:', error.response.data);
        console.log('Response status:', error.response.status);
        console.log('Response headers:', error.response.headers);
      } else if (error.request) {
        console.log('Request:', error.request);
      } else {
        console.log('Error message:', error.message);
      }
      console.log('Config:', error.config);
  });
 };
 
 
 const handleDelete = () => {
  const token = localStorage.getItem('accessToken');
    
  axios.delete(`http://localhost:80/api/users/`, {
      headers: {
        'Authorization': `Bearer ${token}`
      }
  }).then(response => {
      console.log('Response:', response);
      alert('Account deleted successfully');
      navigate('/Login');
  }).catch(error => {
      console.error('Error:', error);
      if (error.response) {
        switch (error.response.status) {
          case 404:
            alert('Resource not found');
            break;
          case 500:
            alert('Server error');
            break;
          default:
            alert('Failed to delete account');
        }
      } else {
        alert('Network error');
      }
  });
 };
 
 

 const handleCancel = () => {
    setIsEditOpen(false);
 };

 const handleLogout = () => {
    navigate('/Login');
 };

 if (!isEditOpen) {
    return null;
 }

 return (
    <div className="edit-profile">
        <div className="div">
        <img className="profile-circle-icon" src="img\profile-circle-icon-2048x2048-cqe5466q-2.png"/>
        <div className="text-wrapper">
            <span>First Name:</span>
            <span contentEditable={true} suppressContentEditableWarning={true} onBlur={(e) => handleBlur(e, setFirstName)}>{firstName}</span>
        </div>
        <div className="text-wrapper-2">
            <span>Last Name:</span>
            <span contentEditable={true} suppressContentEditableWarning={true} onBlur={(e) => handleBlur(e, setLastName)}>{lastName}</span>
        </div>
        <p className="email">
            <span className="span">Email:</span>
            <span contentEditable={true} suppressContentEditableWarning={true} onBlur={(e) => handleBlur(e, setEmail)}>{email}</span>
        </p>
        <button className="button" onClick={handleLogout}>
        <div className="delete-account">Log Out</div>
        </button>
        <button className="delete-account-wrapper" onClick={handleDelete}>
        <div className="delete-account">Delete Account</div>
        </button>
        <button className="cancel-wrapper" onClick={handleCancel}>
        <div className="delete-account">cancel</div>
        </button>
        <button className="save-wrapper" onClick={handleSave}>
            <div className="delete-account">save</div>
        </button>
        </div>        
    </div>
 );
};
