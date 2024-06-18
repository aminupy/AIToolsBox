import React, { useState } from "react";
import axios from "axios";
import "./style.css";
import Edit from "./Edit";

export default function AdminzPage() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");

  const handleTitleChange = (event) => setTitle(event.target.value);
  const handleDescriptionChange = (event) => setDescription(event.target.value);
  const [showModal, setShowModal] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const adminToken = localStorage.getItem("AdminToken");

      await axios.put(
        "http://localhost:80/api/config/",
        { title, description },
        {
          headers: {
            Authorization: `Bearer ${adminToken}`,
          },
        }
      );

      alert("Content updated successfully");
    } catch (error) {
      console.error("Failed to update content:", error);
    }
  };

  return (
    <div>
      <div className="h-[64px] lg:left-[400px] md:left-[400px] left-[300px] absolute top-[115px] w-[148px]">
        <div
          onClick={() => setShowModal(true)}
          className="text-[#ffffff] font-inter text-[22px] font-bold h-[64px] -left-[150%] tracking-[0] leading-[normal] absolute text-center -top-full w-[148px]"
        >
          Profile
        </div>
      </div>
      <form onSubmit={handleSubmit}>
        <label>
          <input
            className="bg-[#ffffff] rounded-[8px] h-[79px] xl:left-[440px] lg:left-[200px] md:left-[100px] left-[50px] absolute top-[500px] xl:w-[915px] lg:w-[700px] md:w-[600px] w-[500px] "
            type="text"
            value={title}
            onChange={handleTitleChange}
          />
        </label>
        <label>
          <input
            className="bg-[#ffffff] rounded-[8px] h-[79px] xl:left-[440px] lg:left-[200px] md:left-[100px] left-[50px] absolute top-[700px] xl:w-[915px] lg:w-[700px] md:w-[600px] w-[500px]"
            type="text"
            value={description}
            onChange={handleDescriptionChange}
          />
        </label>
        <button className="items-center bg-[#ffa62b] rounded-[5px] box-border flex gap-[32px] h-[51px] justify-center xl:left-[735px] lg:left-[370px] md:left-[230px] left-[130px] px-[32px] py-[10px] absolute top-[830px] w-[345px]">
          <div className="text-[#ffffff] font-inter text-[16px] font-medium tracking-[0] leading-[normal] relative text-center whitespace-nowrap w-[fit-content]">
            Submit
          </div>
        </button>
      </form>
      <div className="text-[#ede7e3] font-inter text-[60px] font-bold xl:left-[735px] lg:left-[370px] md:left-[230px] left-[130px] tracking-[0] leading-[normal] absolute text-center top-[291px] whitespace-nowrap">
        Admin Panel
        <p className="text-[#ffffff] font-inter text-[24px] font-semibold xl:-left-[290px] lg:-left-[190px] md:-left-[160px] -left-[100px] tracking-[0] leading-[normal] absolute text-center top-[170px] w-[392px]">
          Change the title of the intro
        </p>
        <p className="text-[#ffffff] font-inter text-[24px] font-semibold xl:-left-[290px] lg:-left-[190px] md:-left-[160px] -left-[100px] tracking-[0] leading-[normal] absolute text-center top-[360px] w-[471px]">
          Change the description of the intro
        </p>
        {showModal && <Edit />}
      </div>
    </div>
  );
}