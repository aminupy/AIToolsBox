import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

const OtpInput = () => {
  const navigate = useNavigate();
  const [otp, setOtp] = useState("");
  const [loading, setLoading] = useState(false);
  const [countdown, setCountdown] = useState(60); // Initialize countdown

  const phoneNumber = localStorage.getItem("phoneNumber");
  const password = localStorage.getItem("password");

  useEffect(() => {
    if (countdown > 0) {
      setTimeout(() => setCountdown(countdown - 1), 1000);
    }
  }, [countdown]);

  const handleInputChange = (e) => {
    const target = e.target;
    const value = target.value;
    const name = target.name;

    if (name === "otp") {
      if (value.length <= 6) {
        setOtp(value);
      }
    }
  };

  const resendOtp = async () => {
    setLoading(true);
    try {
      const response = await fetch("http://iam.localhost/api/v1/users/ResendOTP", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ mobile_number: phoneNumber }),
      });

      if (!response.ok) {
        throw new Error("Resend failed");
      }

      const data = await response.json();
      console.log(data);
      setCountdown(60); // Reset the countdown
    } catch (error) {
      console.error("Failed to resend OTP:", error.message);
      alert("Failed to resend OTP. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  const verifyOtp = async () => {
    setLoading(true);
    try {
      console.log({
        mobile_number: phoneNumber,
        password: password,
      });

      const response = await fetch(
        "http://iam.localhost/api/v1/users/VerifyOTP",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            mobile_number: phoneNumber,
            OTP: otp,
          }),
        }
      );

      if (!response.ok) {
        throw new Error("Verification failed");
      }

      alert("OTP Verified Successfully!");

      await loginWithCredentials();

      navigate("/MainPage");
    } catch (error) {
      console.error("Failed to verify OTP:", error.message);
      alert("Failed to verify OTP. Please try again.");
      setLoading(false);
    } finally {
      setLoading(false);
    }
  };

  const loginWithCredentials = async () => {
    try {
      const encodedUsername = encodeURIComponent(phoneNumber);
      const encodedPassword = encodeURIComponent(password);

      const urlWithParams = `http://iam.localhost/api/v1/users/Token?username=${encodedUsername}&password=${encodedPassword}`;

      const response = await fetch(urlWithParams, {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: `username=${encodedUsername}&password=${encodedPassword}`,
      });

      if (!response.ok) {
        throw new Error("Login failed");
      }

      const data = await response.json();
      localStorage.setItem("accessToken", data.access_token);
      console.log("Logged in successfully!");
      navigate("/MainPage");
    } catch (error) {
      console.error("Failed to log in:", error.message);
      alert("Login failed. Please try again.");
      setLoading(false);
    }
  };

  return (
    <div style={{
      backgroundImage: `url('/img/Intro Desktop.png')`,
      backgroundSize: 'cover',
      height: '100vh'
    }}>
    <div className="flex justify-center items-center h-screen">
      <form className="space-y-4">
        <input
          type="text"
          placeholder="Enter OTP"
          value={otp}
          onChange={handleInputChange}
          maxLength={6}
          name="otp"
          className="w-full px-4 py-2 border rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm border-gray-300"
        />
        <p className="text-white">{countdown > 0 && `${countdown}s left`}</p> {/* Display countdown */}
        <button
          onClick={resendOtp}
          disabled={loading || countdown > 0} // Disable button while loading or countdown active
          className={`w-full px-4 py-2 text-white ${
            loading? "bg-gray-400" : "bg-[#ffa62b]"
          } rounded-md hover:bg-[#16697a] focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-opacity-50`}
        >
          Resend OTP
        </button>
        <button
          onClick={verifyOtp}
          disabled={loading} // Disable button while loading
          className={`w-full px-4 py-2 text-white ${
            loading? "bg-gray-400" : "bg-[#ffa62b]"
          } rounded-md hover:bg-[#16697a] focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-opacity-50`}
        >
          Verify OTP & Login
        </button>
      </form>
    </div>
    </div>
  );
};

export default OtpInput;