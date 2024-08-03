import Image from "next/image";
import { Dispatch, SetStateAction } from "react";
import InitalForm from "../../components/InitialForm";
import { SignUpState } from "@/types";

interface SignUpProps {
  setSignUpState: Dispatch<SetStateAction<SignUpState>>;
}

export default function SignUp({ setSignUpState }: SignUpProps) {
  return (
    <main className="flex mg:flex-row h-screen justify-center items-center">
      <div className="h-full mg:h-[90%] w-full mg:w-9/12 mg:bg-gradient-360 shadow-xl mg:rounded-5xl mg:rounded-r-6xl">
        <div className="h-full flex flex-col mg:flex-row justify-between">
          <div className="text-white bg-custom-gradient mg:bg-none flex flex-col items-center h-[60%] mg:w-[45%] pt-10 mg:pt-28">
            <div className="flex flex-col items-center gap-5 mg:gap-14">
              <div className="mg:hidden">
                <Image
                  src="/Logo.png"
                  width={150}
                  height={150}
                  alt="Logo"
                  className="w-24 h-24 mg:w-36 mg:h-36"
                />
              </div>
              <h2 className="text-5xl mg:text-3xl xl:text-4xl 2xl:text-5xl font-bold mt-5">
                AI Tools Box
              </h2>
              <p>All You Need In a Box!</p>
            </div>
          </div>
          <div className="bg-[#4B5094] mg:bg-white overflow-y-hidden mg:rounded-5xl w-full mg:w-[55%]">
            <div className="h-screen mg:h-full w-full bg-white rounded-t-5xl mg:rounded-5xl flex flex-col items-center">
              <div className="pt-7 hidden mg:block">
                <Image src="/Logo.png" width={70} height={70} alt="Logo" />
              </div>
              <div className="flex flex-col items-center w-80 sm:w-[30rem] mg:w-80 lg:w-[23rem] 2xl:w-[28rem] h-full my-8">
                <h2 className="text-3xl sm:text-4xl mg:text-3xl 2xl:text-4xl font-bold">
                  Create an account
                </h2>
                <InitalForm setSignUpState={setSignUpState} formName="signup" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}
