import React from "react";
import { HashRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./pages/Login/Login";
import CreateAccount from "./pages/CreateAccount/CreateAccount";
import MainPage from "./pages/MainPage/MainPage";
import OCR from "./pages/OCRPage/OCR";
import Profile from "./pages/Profile/Profile";
import AdminPage from "./pages/AdminPage/AdminPage";
import AdminLogin from "./pages/AdminLogin/AdminLogin";
import AdminCreateAccount from "./pages/AdminCreateAccount/AdminCreateAccount";
import Otp from "./pages/CreateAccount/otp";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<CreateAccount />} />
        <Route path="/Otp" element={<Otp />} />
        <Route path="/Login" element={<Login />} />
        <Route path="/MainPage" element={<MainPage />} />
        <Route path="/OCR" element={<OCR />} />
        <Route path="/Profile" element={<Profile />} />
        <Route path="/AdminPage" element={<AdminPage />} />
        <Route path="/AdminLogin" element={<AdminLogin />} />
        <Route path="/AdminCreateAccount" element={<AdminCreateAccount />} />
      </Routes>
    </Router>
  );
}

export default App;
