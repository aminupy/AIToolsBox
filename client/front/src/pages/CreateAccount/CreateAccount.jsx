import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import "./style.css";

export default function CreateAccount() {
  const navigate = useNavigate();
  const [phoneNumber, setPhoneNumber] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [password, setPassword] = useState("");
  const [phoneError, setPhoneError] = useState("");

  const handleFirstNameChange = (event) => {
    setFirstName(event.target.value);
  };

  const handleLastNameChange = (event) => {
    setLastName(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handlePhoneNumberChange = (event) => {
    setPhoneNumber(event.target.value);
    setPhoneError("");
  };

  const isValidPhoneNumber = (number) => {
    const regex = /^\+?[1-9]\d{1,14}$/;
    return regex.test(number);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (!firstName || !lastName || !phoneNumber || !password) {
      console.log("Please fill all required fields.");
      return;
    }
    if (!isValidPhoneNumber(phoneNumber)) {
      console.log("Invalid phone number.");
      return;
    }

    try {
      const response = await fetch(
        "http://iam.localhost/api/v1/users/Register",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            first_name: firstName,
            last_name: lastName,
            mobile_number: phoneNumber,
            password: password,
          }),
        }
      );

      if (!response.ok) {
        throw new Error("Registration failed");
      }

      const data = await response.json();
      console.log(data);

      localStorage.setItem("phoneNumber", phoneNumber);
      localStorage.setItem("password", password);

      navigate("./Otp");
    } catch (error) {
      console.error(error.message);
    }
  };

  return (
    <div className="h-full">
      <div className="bg-[#ede7e3] absolute rounded-[40px] w-full h-4/6 bottom-0 right-0 lg:w-4/6 lg:h-screen md:right-0 sm:bottom-0 sm:w-full sm:h-4/6">
        <div className=" bg-[#ede7e3] rounded-[40px]  overflow-hidden absolute lg:top-[100px] h-[735px] lg:h-[900px] 2xl:left-[100px] w-5/6 lg:left-10 sm:left-16">
          <div className="h-[17px] xl:left-[134px] lg:left-[76px] left-[0px] absolute lg:top-[712px] top-[550px] w-[720px]">
            <img
              className="h-px left-[0] object-cover absolute top-[11px] xl:w-[307px] lg:w-[250px] md:w-[307px] sm:w-[200px]"
              alt="Line"
              src="../img/line-1.svg"
            />
            <img
              className="h-px xl:left-[417px] lg:left-[357px] md:left-[417px] sm:left-[300px] object-cover absolute top-[11px] xl:w-[304px] lg:w-[250px] md:w-[304px] sm:w-[208px]"
              alt="Line"
              src="../img/line-2.svg"
            />
            <div className="text-[#6a6a6a] text-[24px] font-bold h-[17px] xl:left-[348px] lg:left-[290px] md:left-[348px] sm:left-[240px] tracking-[0] leading-[normal] absolute text-center -top-[10px] whitespace-nowrap">
              or
            </div>
          </div>
          <div className="h-[59px] xl:left-[134px] lg:left-[75px] left-[0px] absolute top-[600px] lg:top-[780px] w-[721px]">
            <div className="bg-[#ffffff] border-[1px] border-[solid] border-[#6a6a6a] rounded-[8px] h-[59px] left-[0] overflow-hidden absolute top-[0] xl:w-[352px] lg:w-[300px] md:w-[352px] sm:w-[250px]">
              <div className="text-[#6a6a6a] md:text-[16px] text-[14px] font-semibold h-[12px] left-[60px] tracking-[0] leading-[normal] absolute text-right top-[23px] w-[181px]">
                Sign Up With Facebook
              </div>
              <img
                className="h-[46px] left-[23px] object-cover absolute top-[7px] w-[46px]"
                alt="Facebook"
                src="../img/facebook-1.png"
              />
            </div>
            <div className="bg-[#ffffff] border-[1px] border-[solid] border-[#6a6a6a] rounded-[8px] h-[59px] xl:left-[369px] lg:left-[310px] md:left-[368px] left-[260px] overflow-hidden absolute top-[0] xl:w-[352px] lg:w-[300px] md:w-[352px] sm:w-[250px]">
              <div className="text-[#6a6a6a] md:text-[16px] text-[14px] font-semibold h-[12px] left-[100px] tracking-[0] leading-[normal] absolute text-center top-[23px] whitespace-nowrap">
                Sign Up With Google
              </div>
              <img
                className="h-[46px] left-[26px] object-cover absolute top-[7px] w-[46px]"
                alt="Google"
                src="../img/google-1.png"
              />
            </div>
          </div>
          <p className="text-transparent text-[16px] font-semibold h-[12px] 2xl:left-[133px] lg:left-[70px] absolute lg:top-[436px] tracking-[0] leading-[normal] absolute text-center lg:top-[640px] top-[475px] whitespace-nowrap">
            <span className="text-[#6a6a6a]">Already have an account</span>
            <span className="text-[#6a6a6a]">? </span>
            <Link to="/Login" className="text-[#489fb5]">
              login
            </Link>
          </p>
          <form
            className="h-[65px] 2xl:left-[133px] lg:left-[70px] absolute lg:top-[436px] top-[270px] w-[721px]"
            onSubmit={handleSubmit}
          >
            <div className="h-[65px] absolute -top-[75px] w-[352px]">
              <input
                className="bg-[#ede7e3] border-[1px] border-[solid] border-[#6a6a6a] rounded-[8px] h-[59px] left-[0] absolute top-[6px] xl:w-[352px] lg:w-[300px] md:w-[352px] sm:w-[250px]"
                type="text"
                value={firstName}
                onChange={handleFirstNameChange}
              />
              <div className="items-center bg-[#ede7e3] inline-flex gap-[10px] justify-center left-[19px] px-[8px] py-0 absolute top-[0]">
                <div className="font-inter text-[#6a6a6a] text-[16px] font-semibold tracking-[0] leading-[normal] -mt-px relative text-center whitespace-nowrap w-[fit-content]">
                  First Name
                </div>
              </div>
            </div>
            <div className="h-[65px] xl:left-[369px] lg:left-[310px] md:left-[368px] left-[260px] absolute -top-[75px] w-[352px]">
              <input
                className="bg-[#ede7e3] border-[1px] border-[solid] border-[#6a6a6a] rounded-[8px] h-[59px] left-[0] absolute top-[6px] xl:w-[352px] lg:w-[300px] md:w-[352px] sm:w-[250px]"
                type="text"
                value={lastName}
                onChange={handleLastNameChange}
              />
              <div className="items-center bg-[#ede7e3] inline-flex gap-[10px] justify-center left-[19px] px-[8px] py-0 absolute top-[0]">
                <div className="text-[#6a6a6a] text-[16px] font-semibold tracking-[0] leading-[normal] -mt-px relative text-center whitespace-nowrap w-[fit-content]">
                  Last Name
                </div>
              </div>
            </div>
            <div className="h-[65px] relative -top-[5px]">
              <input
                className="bg-[#ede7e3] border-[1px] border-[solid] border-[#6a6a6a] rounded-[8px] h-[59px] left-[0] absolute top-[6px] xl:w-[721px] lg:w-[609px] md:w-[721px] sm:w-[509px]"
                type="tel"
                value={phoneNumber}
                onChange={handlePhoneNumberChange}
              />
              <div className="items-center bg-[#ede7e3] inline-flex gap-[10px] justify-center left-[19px] px-[8px] py-0 absolute top-[0]">
                <div className="text-[#6a6a6a] text-[16px] font-semibold tracking-[0] leading-[normal] -mt-px relative text-center whitespace-nowrap w-[fit-content]">
                  Phone Number
                </div>
              </div>
            </div>
            <div className="h-[65px] relative">
              <input
                className="bg-[#ede7e3] border-[1px] border-[solid] border-[#6a6a6a] rounded-[8px] h-[59px] left-[0] absolute top-[6px] xl:w-[721px] lg:w-[609px] md:w-[721px] sm:w-[509px]"
                type="text-[#6a6a6a] text-[16px] font-semibold tracking-[0] leading-[normal] -mt-px relative text-center whitespace-nowrap w-[fit-content]"
                value={password}
                onChange={handlePasswordChange}
              />
              <div className="items-center bg-[#ede7e3] inline-flex gap-[10px] justify-center left-[19px] px-[8px] py-0 absolute top-[0]">
                <div className="text-[#6a6a6a] text-[16px] font-semibold tracking-[0] leading-[normal] -mt-px relative text-center whitespace-nowrap w-[fit-content]">
                  Password
                </div>
              </div>
            </div>
            <div className="h-[59px] left-[153px] absolute top-[576px]">
              <button
                className="items-center border-[none] bg-[#ffa62b] rounded-[8px] flex gap-[10px] h-[59px] justify-center p-[10px] relative xl:w-[721px] lg:w-[609px] md:w-[721px] sm:w-[509px] -top-[435px] -left-[153px]"
                type="submit"
                onClick={handleSubmit}
              >
                <div className="font-inter text-[#ffffff] text-[24px] font-bold tracking-[0] leading-[normal] relative text-center whitespace-nowrap w-[fit-content]">
                  Send Code
                </div>
              </button>
            </div>
          </form>
          <div className="font-inter text-[#4c4c4c] text-[40px] font-bold h-[29px] 2xl:left-[153px] xl:left-[80px] lg:left-[40px] tracking-[0] leading-[normal] absolute text-center top-[120px] whitespace-nowrap">
            Create Account
          </div>
          <div className="h-[11px] xl:left-[751px] lg:left-[500px] sm:left-[400px] left-[400px] absolute top-[42px] w-[105px]">
            <div className="text-[#6a6a6a] text-[14px] font-semibold h-[10px] left-[0] tracking-[0] leading-[normal] absolute text-center top-[90px] whitespace-nowrap">
              English (us)
            </div>
            <img
              className="h-[8px] left-[90px] absolute top-[95px] w-[12px]"
              alt="Polygon"
              src="../img/polygon-1.svg"
            />
          </div>
        </div>
      </div>
      <div className="items-start flex flex-col gap-[29px] h-[161px] left-[53px] absolute top-[180px] w-[427px] lg:top-[180px] lg:left-[40px] sm:top-16 sm:left-28">
        <p className=" absolute ">
          <span className="font-syncopate text-[#4c4c4c] font-normal text-[28px] xl:text-[40px] md:text-[34px] sm:text-[30px]">
            AI Tools Box <br />
            <br />
            All in one box
          </span>
        </p>
      </div>
      <img
        className="h-[42px] left-[23px] object-cover absolute top-[21px] w-[42px]"
        alt="Noun ai"
        src="../img/noun-ai-1552017-1.png"
      />
      <img
        className="absolute h-[309px] w-[387px] right-[0px] top-[200px] xl:h-[509px] xl:w-[587px] xl:left-[60px] xl:top-[450px] lg:h-[429px] lg:w-[507px] lg:left-[40px] lg:top-[450px] md:h-[329px] md:w-[407px] md:right-[20px] md:top-[150px] sm:h-[309px] sm:w-[387px] sm:right-[0px] sm:top-[200px]"
        alt="Kisspng big data"
        src="../img/kisspng-big-data-telecom-promotion-and-campaign-management-focus.png"
      />
    </div>
  );
}
