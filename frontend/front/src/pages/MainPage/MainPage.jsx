import React, { useEffect, useState } from "react";
import { Link, Navigate, useNavigate } from "react-router-dom";
import "./style.css";

export default function MainPage() {
  const navigate = useNavigate();

  return (
    <div className="overflow-hidden flex flex-wrap justify-center w-full">
      <div className="overflow-hidden h-[4031px] relative w-full">
        <footer className=" h-[138px] xl:left-[550px] lg:left-[100px] absolute top-[3748px] w-[1150px]">
          <div className="h-[64px] left-[0] absolute top-[0] w-[1109px]">
            <div className="h-[64px] left-[0] absolute top-[20px] w-[1109px]">
              <img
                className="h-[3px] left-[44px] object-cover absolute top-[40px] lg:w-[1065px] md:w-[800px] w-[600px] "
                alt="Line"
                src="/img/line-3.svg"
              />
              <div className="text-[#16697a] font-inter text-[16px] font-normal h-[64px] left-[0] tracking-[0] leading-[normal] absolute text-center top-[0] w-[255px]">
                FAQ
              </div>
              <div className="text-[#16697a] font-inter text-[16px] font-normal h-[64px] left-[128px] tracking-[0] leading-[normal] absolute text-center top-[0] w-[255px]">
                Contact Us
              </div>
            </div>
            <img
              className="h-[34px] lg:left-[769px] md:left-[600px] left-[600px]  object-cover absolute top-[13px] w-[59px]"
              alt="Twitter"
              src="/img/twitter-1.png"
            />
            <img
              className="h-[40px] lg:left-[884px] md:left-[680px] left-[520px]  object-cover absolute top-[10px] w-[60px]"
              alt="Instagram"
              src="/img/instagram-1.png"
            />
            <img
              className="h-[53px] lg:left-[1000px] md:left-[770px] left-[450px]  object-cover absolute top-[3px] w-[46px]"
              alt="Facebook"
              src="/img/facebook-2.png"
            />
          </div>
          <div className="text-[#16697a] font-inter text-[22px] font-bold h-[64px] left-[97px] tracking-[0] leading-[normal] absolute text-center top-[74px] w-[148px]">
            AiToolsBox
          </div>
          <p className="text-[#16697a] font-inter text-[16px] font-normal h-[64px] lg:left-[452px] md:left-[300px] md:block hidden tracking-[0] leading-[normal] absolute text-center top-[74px] w-[255px]">
            2024 AIToolsBox. All rights reserved
          </p>
          <div className="h-[64px] left-[707px] absolute top-[74px] w-[431px]">
            <div className="text-[#16697a] font-inter text-[16px] font-normal h-[64px] lg:left-[176px] md:-left-[100px] md:block hidden tracking-[0] leading-[normal] absolute text-center top-[0] w-[255px]">
              Privacy Policy
            </div>
          </div>
        </footer>
        <div className="items-center content-center h-[226px] xl:left-[600px] lg:left-[150px] md:left-[50px] left-[50px] absolute top-[3461px] lg:w-[1065px] md:w-[800px] w-[600px] ">
          <div className="bg-[linear-gradient(180deg,_rgb(130,_192,_204)_0%,_rgba(130,_192,_204,_0)_100%)] h-[226px] relative">
            <button className="items-center bg-[#ffa62b] rounded-[5px] box-border flex gap-[32px] h-[57px] justify-center lg:left-[437px] md:left-[300px] left-[200px] px-[32px] py-[10px] absolute top-[140px] w-[189px]">
              <div className="text-[#ffffff] font-inter text-[16px] font-medium tracking-[0] leading-[normal] relative text-center whitespace-nowrap w-[fit-content]">
                Join Now
              </div>
            </button>
            <div className="h-[93px] lg:left-[252px] md:left-[130px] left-[30px] absolute top-[19px] w-[558px]">
              <p className="text-[#ffffff] font-inter text-[36px] font-medium left-[24px] tracking-[0] leading-[normal] absolute text-center top-[0] w-[511px]">
                Become A Premium Today !
              </p>
              <p className="text-[#ede7e3] font-inter text-[15px] font-medium left-[0] tracking-[0] leading-[normal] absolute text-center top-[47px] w-[558px]">
                Experience Unlimited Usage With Our Premium Account. Access All
                Tools Without Any Restrictions, Providing A Seamless And
                Limitless Experience.
              </p>
            </div>
          </div>
        </div>
        <div className="h-[518px] xl:left-[680px] lg:left-[200px] left-[50px] absolute top-[2754px] w-[963px]">
          <button className="items-center bg-[linear-gradient(180deg,_rgb(255,_166,_43)_0%,_rgba(255,_166,_43,_0)_100%)] rounded-[5px] box-border flex gap-[32px] h-[51px] justify-center left-[123px] px-[32px] py-[10px] absolute top-[393px] w-[223px]">
            <div className="text-[#ffffff] font-inter text-[16px] font-medium tracking-[0] leading-[normal] relative text-center whitespace-nowrap w-[fit-content]">
              Try It Out
            </div>
          </button>
          <div className="text-[#16697a] font-inter text-[60px] font-bold left-[0] tracking-[0] leading-[normal] absolute text-center top-[119px] whitespace-nowrap">
            SPEECH TO TEXT
          </div>
          <p className="text-[#489fb5] font-inter text-[18px] font-medium left-[31px] tracking-[0] leading-[normal] absolute text-justify top-[230px] w-[423px]">
            capture your thoughts, let the tool convert them into text. it&#39;s
            like a personal secretary, understanding your spoken words and
            translating them into written text.
          </p>
          <img
            className="h-[518px] lg:left-[561px] md:left-[400px] left-[300px] absolute lg:top-[0] md:top-[150px] top-[200px] w-[398px]"
            alt="Lovepik com"
            src="/img/lovepik-com-450072740-virtual-voice-assistant-flat-illustration.png"
          />
        </div>
        <div className="h-[469px] xl:left-[600px] lg:left-[100px] md:left-[50px] left-[40px] absolute top-[2028px] w-[1030px]">
          <button
            onClick={() => navigate("/OCR")}
            className=" items-center bg-[linear-gradient(180deg,_rgb(255,_166,_43)_0%,_rgba(255,_166,_43,_0)_100%)] rounded-[5px] box-border flex gap-[32px] h-[51px] justify-center xl:left-[665px] lg:left-[600px] left-[90px] px-[32px] py-[10px] absolute top-[385px] w-[223px]"
          >
            <div className="text-[#ffffff] font-inter text-[16px] font-medium tracking-[0] leading-[normal] relative text-center whitespace-nowrap w-[fit-content]">
              Try It Out
            </div>
          </button>
          <div className="text-[#16697a] font-inter text-[60px] font-bold xl:left-[542px] lg:left-[450px] tracking-[0] leading-[normal] absolute text-center top-[111px] whitespace-nowrap">
            IMAGE TO TEXT
          </div>
          <p className="text-[#489fb5] font-inter text-[18px] font-medium xl:left-[577px] lg:left-[500px] left-[30px] tracking-[0] leading-[normal] absolute text-justify top-[235px] w-[423px]">
            unleash the power of your images with this tool. it decodes text
            from images, making it easier for everyone to access and understand
            the information contained within them.
          </p>
          <img
            className="h-[469px] lg:left-[0] md:left-[350px] left-[300px] object-cover absolute lg:top-[0] md:top-[300px] top-[350px] w-[352px]"
            alt="Lovepik com"
            src="/img/lovepik-com-450083890-a-voice-recognition-isometric-illustration.png"
          />
        </div>
        <div className="h-[510px] xl:left-[700px] lg:left-[180px] left-[100px] absolute xl:top-[1400px] top-[1195px] w-[974px]">
          <button className=" items-center bg-[linear-gradient(180deg,_rgb(255,_166,_43)_0%,_rgba(255,_166,_43,_0)_100%)] rounded-[5px] box-border flex gap-[32px] h-[51px] justify-center left-[92px] px-[32px] py-[10px] absolute top-[371px] w-[223px]">
            <div className="text-[#ffffff] font-inter text-[16px] font-medium tracking-[0] leading-[normal] relative text-center whitespace-nowrap w-[fit-content]">
              Try It Out
            </div>
          </button>
          <div className="text-[#16697a] font-inter text-[60px] font-bold left-[0] tracking-[0] leading-[normal] absolute text-center top-[105px] whitespace-nowrap">
            TEXT TO SPEECH
          </div>
          <p className="text-[#489fb5] font-inter text-[18px] font-medium left-[5px] tracking-[0] leading-[normal] absolute text-justify top-[212px] w-[423px]">
            craft your ideas, let the tool give them life. it&#39;s like a
            digital storyteller, turning your text into spoken words, bringing
            your ideas to life.
          </p>
          <img
            className="h-[510px] lg:left-[524px] md:left-[320px] object-cover absolute lg:top-[0] top-[400px] w-[446px]"
            alt="Pngtreelaptop laptop"
            src="/img/pngtree-laptop-laptop-business-office-processing-3925220-1.png"
          />
        </div>
        <div className="bg-[#16697a] h-[107px] left-[0] absolute xl:top-[1250px] top-[1024px] w-full">
          <div className="h-[1223px]  relative -top-[442px] w-[2009px] content-center ">
            <div className="text-[#ffffff] font-inter text-[16px] font-bold xl:left-[620px] left-[80px] tracking-[0] leading-[normal] absolute text-center top-[489px] whitespace-nowrap">
              SPEECH TO TEXT
            </div>
            <div className="text-[#ffffff] font-inter text-[16px] font-bold xl:left-[1050px] lg:left-[500px] md:left-[400px] left-[260px] tracking-[0] leading-[normal] absolute text-center top-[489px] whitespace-nowrap">
              TEXT TO SPEECH
            </div>
            <div className="text-[#ffffff] font-inter text-[16px] font-bold xl:left-[1500px] lg:left-[900px] md:left-[700px] left-[450px] tracking-[0] leading-[normal] absolute text-center top-[489px] whitespace-nowrap">
              IMAGE TO TEXT
            </div>
          </div>
        </div>
        <div className="overflow-hidden h-[1024px] left-[0] absolute top-[0] w-full flex flex-wrap">
          <div className="overflow-hidden h-[1024px] left-[0] overflow-hidden absolute top-[0] w-full">
            <div className="h-[1000px] xl:left-[40px] md:-left-[500px] -left-[550px] relative -top-[114px] w-full">
              <div className="h-[385px] left-[590px] absolute top-[450px] w-[1050px]">
                <div className="h-[385px] relative w-[1046px]">
                  <Link
                    to="/OCR"
                    className="items-center bg-[#ffa62b] rounded-[5px] box-border flex gap-[32px] h-[51px] justify-center left-[3px] px-[32px] py-[10px] absolute top-[288px] w-[223px]"
                  >
                    <div className="text-[#ffffff] font-inter text-[16px] font-medium tracking-[0] leading-[normal] relative text-center whitespace-nowrap w-[fit-content]">
                      Let’s Start
                    </div>
                  </Link>
                  <button className="items-center bg-[#82c0cc] rounded-[5px] box-border flex gap-[32px] h-[51px] justify-center left-[241px] px-[32px] py-[10px] absolute top-[288px] w-[223px]r">
                    <div className="text-[#ffffff] font-inter text-[16px] font-medium tracking-[0] leading-[normal] relative text-center whitespace-nowrap w-[fit-content]">
                      Faq
                    </div>
                  </button>
                  <div className="h-[385px] left-[0] absolute top-[0] w-[1046px]">
                    <div className="text-[#ede7e3] font-inter text-[60px] font-bold left-[0] tracking-[0] leading-[normal] absolute text-center top-[34px] whitespace-nowrap">
                      Wide Range Of Tools
                    </div>
                    <img
                      className="h-[385px] lg:left-[523px] md:left-[300px] left-[130px] object-cover absolute lg:top-[0] md:top-[200px] top-[300px] w-[523px]"
                      alt="Kisspng information"
                      src="/img/kisspng-information-technology-technical-support-business-intern.png"
                    />
                  </div>
                  <p className="text-[#82c0cc] font-inter text-[18px] font-medium left-[0] tracking-[0] leading-[normal] absolute top-[142px] w-[423px]">
                    we give you access to a full range of tools. carefully
                    designed to be intuitive, engaging, and secure.
                  </p>
                </div>
              </div>
            </div>
          </div>
          <div className="flex flex-wrap h-[750px] xl:left-[600px] left-[150px] absolute top-[115px] w-[1033px]">
            <div className="h-[64px] left-[0] absolute top-[0] w-[1043px]">
              <Link
                to="/MainPage"
                className="text-[#ffffff] font-inter text-[22px] font-bold h-[64px] left-[0] tracking-[0] leading-[normal] absolute text-center top-[0] w-[148px]"
              >
                AiToolsBox
              </Link>
              <div className="h-[64px] left-[508px] absolute top-[0] w-[525px]">
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
    </div>
  );
}
