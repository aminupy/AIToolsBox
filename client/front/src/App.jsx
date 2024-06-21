import React from "react";
import { HashRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./pages/Login/Login";
import CreateAccount from "./pages/CreateAccount/CreateAccount";
import MainPage from "./pages/MainPage/MainPage";
import OCR from "./pages/OCRPage/OCR";
import Profile from "./pages/Profile/Profile";
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
      </Routes>
    </Router>
  );
}

export default App;
