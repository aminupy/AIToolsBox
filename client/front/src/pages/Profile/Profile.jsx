import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import "./style.css";
import Edit from "./Edit";
import moment from "moment";

// Define fetchImageBlob and createDownloadLink here
const fetchImageBlob = async (url) => {
  const response = await fetch(url);
  const blob = await response.blob();
  return blob;
};

const createDownloadLink = (blob, filename) => {
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = filename;
  return link;
};

export default function Profile() {
  const [user, setUser] = useState(null);
  const [userHistory, setUserHistory] = useState([]);
  const [images, setImages] = useState([]);
  const [showModal, setShowModal] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem("accessToken");

    axios
    .get("http://iam.localhost/api/v1/users/Me", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })
    .then((response) => {
          setUser({
            firstName: response.data.first_name,
            lastName: response.data.last_name,
            phoneNumber: response.data.mobile_number,
          });
        })
    .catch((error) => {
          console.error(error);
        });

    // Fetch OCR history
    axios.get("http://ocr.localhost/api/v1/ocr/get_ocr_history", {
      headers: {
        accept: "application/json",
        Authorization: `Bearer ${token}`,
      },
    }).then(response => {
      setUserHistory(response.data);
    }).catch(error => {
      console.error(error);
    });
  }, []);

  return (
    <div className="bg-[#ede7e3] flex flex-row justify-center w-full">
      <div className="bg-[#ede7e3] h-[1406px] relative w-full">
        <div className="bg-[#16697a] h-[348px] left-[0] overflow-hidden absolute top-[0] w-full">
          <div className="h-[1919px] -left-[311px] relative -top-[260px] w-full">
            <div className="h-[1919px] left-[0] absolute top-[0] w-full">
              <div className="rounded-[257.5px/245px] filter blur-[124px] h-[490px] left-[1494px] absolute top-[769px] w-full" />
              <div className="h-[608px] left-[229px] absolute top-[0] w-[1522px]">
                <div className="rounded-[257.5px/245px] filter blur-[124px] h-[490px] left-[0] absolute top-[0] w-full" />
                <img
                  className="h-[348px] left-[70px] absolute top-[80px] w-full"
                  alt="Vector"
                  src="/img/vector.svg"
                />
              </div>
              <img
                className="h-[773px] left-[4911px] absolute top-[1510px] w-full"
                alt="Vector"
                src="/img/vector-1.png"
              />
            </div>
            <div className="h-[180px] xl:left-[840px] lg:left-[400px] md:left-[360px] left-[350px] absolute top-[400px] w-[1036px]">
              <div className="h-[180px] left-[0] absolute top-[0] w-[454px]">
                <div className="text-[#ffffff] font-inter text-[24px] font-semibold h-[53px] left-[164px] tracking-[0] leading-[normal] absolute text-center top-[37px] w-[265px]">
                  {user ? `${user.firstName} ${user.lastName}` : ""}
                </div>
                <div className="text-[#ffffff] font-inter text-[15px] font-light h-[53px] left-[149px] tracking-[0] leading-[normal] absolute text-center top-[74px] w-[265px]">
                  {user ? user.phoneNumber : ""}
                </div>
                <img
                  className="h-[20px] left-[430px] object-cover absolute top-[37px] w-[20px]"
                  alt="Transparent"
                  src="/img/transparent-interface-icon-assets-icon-edit-icon-interface-ico-5.png"
                />
                <img
                  className="h-[180px] left-[0] absolute top-[0] w-[189px]"
                  alt="Profile circle icon"
                  src="/img/profile-circle-icon-2048x2048-cqe5466q-2.png"
                  onClick={() => setShowModal(!showModal)}
                />
              </div>
              <div className="h-[80px] xl:left-[800px] lg:left-[770px] md:left-[600px] left-[500px] absolute top-[37px] w-[143px]">
                <div className="text-[#ffffff] font-inter text-[15px] font-light h-[80px] left-[px] absolute top-[2px] w-[143px]">
                  Premium Days Left
                </div>
                <div className="text-[#ffffff] font-inter text-[15px] font-light h-[53px] left-[57px] tracking-[0] leading-[normal] absolute text-center top-[40px] w-[38px]">
                  0
                </div>
              </div>
            </div>
            <div className="flex flex-wrap h-[750px] xl:left-[900px] lg:left-[500px] md:left-[400px] left-[350px] absolute top-[300px] w-[1033px]">
              <div className="h-[64px] left-[0] absolute top-[0] w-[1043px]">
                <Link
                  to="/MainPage"
                  className="text-[#ffffff] font-inter text-[22px] font-bold h-[64px] left-[0] tracking-[0] leading-[normal] absolute text-center top-[0] w-[148px]"
                >
                  AiToolsBox
                </Link>
                <div className="h-[64px] md:left-[370px] left-[500px] absolute top-[500] w-[525px]">
                  <div className="xl:block hidden text-[#ffffff] font-inter text-[16px] font-normal h-[64px] left-[123px] tracking-[0] leading-[normal] absolute text-center top-[0] w-[148px]">
                    about us
                  </div>
                  <Link
                    to="/Profile"
                    className="text-[#ffffff] font-inter text-[16px] font-normal h-[64px] xl:left-[369px] lg:left-[300px] md:left-[100px] -left-[110px] tracking-[0] leading-[normal] absolute text-center top-[0] w-[148px]"
                  >
                    profile
                  </Link>
                  <div className=" xl:block hidden text-[#ffffff] font-inter text-[16px] font-normal h-[64px] left-[0] tracking-[0] leading-[normal] absolute text-center top-[0] w-[148px]">
                    tools
                  </div>
                  <div className=" xl:block hidden text-[#ffffff] font-inter text-[16px] font-normal h-[64px] left-[246px] tracking-[0] leading-[normal] absolute text-center top-[0] w-[148px]">
                    contact
                  </div>
                  <img
                    className="h-[44px] xl:left-[482px] lg:left-[410px] md:left-[210px] object-cover absolute -top-[10px] w-[43px]"
                    alt="Profile circle icon"
                    src="/img/profile-circle-icon-2048x2048-cqe5466q-1.png"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
        <div className="text-[#16697a] font-inter text-[48px] font-semibold h-[53px] xl:left-[819px] lg:left-[315px] left-[290px] tracking-[0] leading-[normal] absolute text-center top-[890px] whitespace-nowrap w-[400px]">
          Premium Plans
        </div>
        <div className="h-auto xl:left-[300px] lg:-left-[205px] -left-[230px] absolute top-[415px] w-[1440px]">
          <div className="bg-[#ebe0e0] rounded-[7px] h-[406px] left-[257px] mix-blend-overlay opacity-40 overflow-hidden absolute top-[21px] w-[927px]">
            <img
              className="h-[2px] left-[0] absolute top-[44px] w-[927px]"
              alt="Line"
              src="/img/line-5-1.svg"
            />
            <img
              className="h-[360px] left-[147px] absolute top-[46px] w-[2px]"
              alt="Line"
              src="/img/line-7.svg"
            />
            <img
              className="h-[360px] left-[463px] absolute top-[46px] w-[2px]"
              alt="Line"
              src="/img/line-7.svg"
            />
            <img
              className="h-[360px] left-[779px] absolute top-[46px] w-[2px]"
              alt="Line"
              src="/img/line-7.svg"
            />
          </div>
          <table>
            <thead>
              <tr>
                <th className="text-[#82c0cc] font-inter text-[16px] font-bold left-[278px] tracking-[0] leading-[normal] absolute text-center top-[39px] w-[93px]">
                  Tool
                </th>
                <th className="text-[#82c0cc] font-inter text-[16px] font-bold left-[508px] tracking-[0] leading-[normal] absolute text-center top-[39px] w-[94px]">
                  Sent
                </th>
                <th className="text-[#82c0cc] font-inter text-[16px] font-bold left-[787px] tracking-[0] leading-[normal] absolute text-center top-[39px] w-[183px]">
                  Received
                </th>
                <th className="text-[#82c0cc] font-inter text-[16px] font-bold left-[1059px] tracking-[0] leading-[normal] absolute text-center top-[39px] w-[104px]">
                  Time
                </th>
              </tr>
            </thead>
            <tbody>
              {userHistory.map((item, index) => (
                <tr key={index}>
                  <td className="text-[#82c0cc] font-inter text-[16px] font-bold left-[278px] tracking-[0] leading-[normal] absolute text-center top-[89px] w-[93px]">OCR</td>
                  <td className="text-[#82c0cc] font-inter text-[16px] font-bold left-[508px] tracking-[0] leading-[normal] absolute text-center top-[89px] w-[94px]">
                    <a
                      href="#"
                      onClick={async (event) => {
                        event.preventDefault();
                        const blob = await fetchImageBlob(
                          `http://media.localhost/api/v1/media/GetMedia`,
                          item.image_id
                        );
                        const link = createDownloadLink(
                          blob,
                          `image-${item.ocr_id}.jpg`
                        );
                        link.click();
                      }}
                    >
                      Download Image
                    </a>
                  </td>
                  <td className="text-[#82c0cc] font-inter text-[16px] font-bold left-[787px] tracking-[0] leading-[normal] absolute text-center top-[89px] w-[183px]">
                    <a
                      href="#"
                      onClick={async (event) => {
                        event.preventDefault();
                        const blob = new Blob([item.text], {
                          type: "text/plain",
                        });
                        const link = createDownloadLink(
                          blob,
                          `text-${item.ocr_id}.txt`
                        );
                        link.click();
                      }}
                    >
                      Download Text
                    </a>
                  </td>
                  <td className="text-[#82c0cc] font-inter text-[16px] font-bold left-[1059px] tracking-[0] leading-[normal] absolute text-center top-[89px] w-[104px]">
                    {moment(item.created_at).format("YYYY-MM-DD HH:mm:ss")}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <div className="text-[#489fb5] font-inter text-[16px] font-bold xl:left-[555px] lg:left-[55px] left-[35px] tracking-[0] leading-[normal] absolute text-center top-[372px] whitespace-nowrap">
          SPEECH TO TEXT
        </div>
        <div className="text-[#489fb5] font-inter text-[16px] font-bold xl:left-[950px] lg:left-[455px] left-[435px] tracking-[0] leading-[normal] absolute text-center top-[372px] whitespace-nowrap">
          TEXT TO SPEECH
        </div>
        <div className="text-[#489fb5] font-inter text-[16px] font-bold xl:left-[1350px] lg:left-[855px] left-[835px] tracking-[0] leading-[normal] absolute text-center top-[372px] whitespace-nowrap">
          IMAGE TO TEXT
        </div>
        <img
          className="h-[2px] xl:left-[555px] lg:left-[55px] left-[30px] absolute top-[407px] w-[927px]"
          alt="Line"
          src="/img/line-5-1.svg"
        />
        <div className="bg-[#82c0cc] rounded-[3px] h-[285px] xl:left-[555px] lg:left-[55px] left-[25px] overflow-hidden absolute top-[993px] w-[253px]">
          <button className="items-center bg-[#ffa62b] rounded-[5px] box-border flex gap-[32px] h-[51px] justify-center left-[15px] px-[32px] py-[10px] absolute top-[203px] w-[223px]">
            <div className="text-[#ffffff] font-inter text-[16px] font-medium tracking-[0] leading-[normal] relative text-center whitespace-nowrap w-[fit-content]">
              Buy Now
            </div>
          </button>
          <div className="text-[#ede7e3] font-inter text-[32px] font-medium left-[82px] tracking-[0] leading-[normal] absolute text-center top-[82px] whitespace-nowrap">
            1.99 $
          </div>
          <div className="text-[#ede7e3] font-inter text-[20px] font-medium left-[73px] tracking-[0] leading-[normal] absolute text-center top-[39px] whitespace-nowrap">
            STANDARD
          </div>
          <p className="text-[#ede7e3] font-inter text-[12px] font-medium left-[61px] tracking-[0] leading-[normal] absolute text-center top-[134px] whitespace-nowrap">
            Up To 5 Uploads Daily
          </p>
        </div>
        <div className="bg-[#82c0cc] rounded-[3px] h-[285px] xl:left-[895px] lg:left-[390px] left-[355px] overflow-hidden absolute top-[993px] w-[253px]">
          <button className="items-center bg-[#ffa62b] rounded-[5px] box-border flex gap-[32px] h-[51px] justify-center left-[15px] px-[32px] py-[10px] absolute top-[202px] w-[223px]">
            <div className="text-[#ffffff] font-inter text-[16px] font-medium tracking-[0] leading-[normal] relative text-center whitespace-nowrap w-[fit-content]">
              Buy Now
            </div>
          </button>
          <div className="text-[#ede7e3] font-inter text-[32px] font-medium left-[72px] tracking-[0] leading-[normal] absolute text-center top-[78px] whitespace-nowrap">
            19.99 $
          </div>
          <div className="text-[#ede7e3] font-inter text-[20px] font-medium left-[80px] tracking-[0] leading-[normal] absolute text-center top-[37px] whitespace-nowrap">
            BUSINESS
          </div>
          <p className="text-[#ede7e3] font-inter text-[12px] font-medium left-[57px] tracking-[0] leading-[normal] absolute text-center top-[137px] whitespace-nowrap">
            Up To 20 Uploads Daily
          </p>
          <div className="text-[#ede7e3] font-inter text-[12px] font-medium left-[54px] tracking-[0] leading-[normal] absolute text-center top-[156px] whitespace-nowrap">
            Fast Er Download Speed
          </div>
        </div>
        <div className="bg-[#82c0cc] rounded-[3px] h-[285px] xl:left-[1235px] lg:left-[730px] left-[695px] overflow-hidden absolute top-[993px] w-[253px]">
          <button className="items-center bg-[#ffa62b] rounded-[5px] box-border flex gap-[32px] h-[51px] justify-center left-[15px] px-[32px] py-[10px] absolute top-[201px] w-[223px]">
            <div className="text-[#ffffff] font-inter text-[16px] font-medium tracking-[0] leading-[normal] relative text-center whitespace-nowrap w-[fit-content]">
              Buy Now
            </div>
          </button>
          <div className="text-[#ede7e3] font-inter text-[32px] font-medium left-[67px] tracking-[0] leading-[normal] absolute text-center top-[82px] whitespace-nowrap">
            49.99 $
          </div>
          <div className="text-[#ede7e3] font-inter text-[20px] font-medium left-[54px] tracking-[0] leading-[normal] absolute text-center top-[39px] whitespace-nowrap">
            PROFESSIONAL
          </div>
          <div className="text-[#ede7e3] font-inter text-[12px] font-medium left-[54px] tracking-[0] leading-[normal] absolute text-center top-[138px] whitespace-nowrap">
            Unlimited Daily Uploads
          </div>
          <div className="text-[#ede7e3] font-inter text-[12px] font-medium left-[44px] tracking-[0] leading-[normal] absolute text-center top-[157px] whitespace-nowrap">
            Unlimited Donwload Speed
          </div>
        </div>
        {showModal && <Edit />}
      </div>
    </div>
  );
}
