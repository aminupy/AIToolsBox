import React, { useState } from "react";
import { useDropzone } from "react-dropzone";
import { Link } from "react-router-dom";
import axios from "axios";
import "./style.css";

export default function OCR() {
  const [files, setFiles] = useState([]);
  const [warning, setWarning] = useState("");

  const [receivedText, setReceivedText] = useState("");

  const { getRootProps, getInputProps } = useDropzone({
    accept: "image/*",
    onDrop: async (acceptedFiles, rejectedFiles) => {
      setFiles(acceptedFiles);
      if (rejectedFiles.length > 0) {
        setWarning("Only image files are allowed.");
      } else if (acceptedFiles.length > 0) {

        const token = localStorage.getItem("accessToken");
        console.log("Token:", token);

        const formData = new FormData();
        formData.append("file", acceptedFiles[0]);
        console.log("FormData:", formData);

        try {
          const response = await axios.post(
            "http://localhost:80/api/ocr/",
            formData,
            {
              headers: {
                "Content-Type": "multipart/form-data",
                Authorization: `Bearer ${token}`,
              },
            }
          );

          console.log("Response:", response);

          setReceivedText(response.data.text);
        } catch (error) {
          console.error(error);
          setWarning("An error occurred while processing the image.");
        }
      } else {
        setWarning("No files selected.");
      }
    },
  });

  const downloadTextFile = (text) => {
    const blob = new Blob([text], { type: "text/plain;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.setAttribute("href", url);
    link.setAttribute("download", "output.txt");
    link.click();
  };

  return (
    <div className="flex flex-row justify-center w-full">
      <div className=" h-[1024px] overflow-hidden w-[1440px]">
        <div className="h-[1919px] -left-[266px] relative -top-[81px] w-[2009px]">
          <div className="h-[750px] xl:left-[470px] left-[350px] absolute top-[115px] w-[1033px]">
            <div className="h-[64px] left-[0] absolute top-[0] w-[1043px]">
              <Link to="/MainPage" className="text-[#ffffff] font-inter text-[22px] font-bold h-[64px] left-[0] tracking-[0] leading-[normal] absolute text-center top-[0] w-[148px]">
                AiToolsBox
              </Link>
              <div className="h-[64px] left-[508px] absolute top-[0] w-[525px]">
                <div className="xl:block hidden text-[#ffffff] font-inter text-[16px] font-normal h-[64px] left-[123px] tracking-[0] leading-[normal] absolute text-center top-[0] w-[148px]">about us</div>
                <Link to="/Profile" className="text-[#ffffff] font-inter text-[16px] font-normal h-[64px] xl:left-[369px] lg:left-[300px] md:left-[100px] -left-[110px] tracking-[0] leading-[normal] absolute text-center top-[0] w-[148px]">
                  profile
                </Link>
                <div className=" xl:block hidden text-[#ffffff] font-inter text-[16px] font-normal h-[64px] left-[0] tracking-[0] leading-[normal] absolute text-center top-[0] w-[148px]">tools</div>
                <div className=" xl:block hidden text-[#ffffff] font-inter text-[16px] font-normal h-[64px] left-[246px] tracking-[0] leading-[normal] absolute text-center top-[0] w-[148px]">contact</div>
                <img
                  className="h-[44px] xl:left-[482px] lg:left-[410px] md:left-[210px] object-cover absolute -top-[10px] w-[43px]"
                  alt="Profile circle icon"
                  src="/img/profile-circle-icon-2048x2048-cqe5466q-1.png"
                />
              </div>
            </div>
          </div>
          <button
            className=" items-center bg-[#ffa62b] rounded-[5px] box-border flex gap-[32px] h-[51px] justify-center xl:left-[1084px] lg:left-[951px] md:left-[545px] left-[450px] px-[32px] py-[10px] absolute lg:top-[814px] top-[1000px] w-[345px]"
            onClick={() => downloadTextFile(receivedText)}
          >
            <div className="text-[#ffffff] font-inter text-[16px] font-medium tracking-[0] leading-[normal] relative text-center whitespace-nowrap w-[fit-content]">Download Txt File</div>
          </button>
          <div className="bg-[#ffffff] h-[312px] md:left-[544px] left-[450px] absolute lg:top-[473px] top-[330px] rounded-[8px] w-[345px]">
            <div className="bg-[#ede7e3] top-[10px] left-[12px] rounded-[8px] h-[290px] absolute w-[321px]" {...getRootProps()}>
              <input {...getInputProps()} />
              <p className="text-[#ffffff] font-inter text-[16px] font-medium left-[10px] tracking-[0] leading-[normal] absolute text-center top-[192px] whitespace-nowrap w-[299px]">
                Drag &amp; Drop, select Or Paste Image
              </p>
              <div className="h-[58px] left-[130px] absolute top-[115px] w-[62px]">
                <div className="bg-[#489fb5] rounded-[30px/29px] h-[58px] relative w-[60px]">
                  <div className="text-[#ede7e3] font-inter text-[32px] font-medium left-[11px] tracking-[0] leading-[normal] absolute text-center top-[10px] whitespace-nowrap w-[36px]">+</div>
                </div>
              </div>
            </div>
            {warning && <div className="warning">{warning}</div>}
          </div>
          <div className="bg-[#ffffff] rounded-[8px] h-[312px] xl:left-[1084px] lg:left-[950px] md:left-[545px] left-[450px] absolute lg:top-[473px] top-[680px] w-[345px]" />
          <div className="bg-[#ede7e3] rounded-[8px] h-[290px] xl:left-[1096px] lg:left-[962px] md:left-[557px] left-[462px] absolute lg:top-[484px] top-[691px] w-[321px]">{receivedText}</div>
          <div className="text-[#ede7e3] font-inter md:text-[60px] text-[50px] font-bold xl:left-[608px] lg:left-[500px] md:left-[400px] left-[330px] tracking-[0] leading-[normal] absolute text-center lg:top-[291px] top-[200px] whitespace-nowrap">Image To Text Converter</div>
        </div>
      </div>
    </div>
  );
}
