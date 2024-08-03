import Image from "next/image";
import InitalForm from "../components/InitialForm";

export default function Login() {
  return (
    <main className="h-screen flex justify-center items-center">
      <div className="h-full mg:h-[93%] w-full mg:w-[40rem] bg-white mg:rounded-5xl shadow-md">
        <div className="flex flex-col items-center">
          <div className="pt-10">
            <Image src="/Logo.png" width={70} height={70} alt="Logo" />
          </div>
          <h2 className="text-4xl font-bold mt-7">Welcome back</h2>
          <div className="w-80 sm:w-[30rem] mg:w-80 lg:w-[23rem] 2xl:w-[28rem]">
            <InitalForm formName="login" />
          </div>
        </div>
      </div>
    </main>
  );
}
