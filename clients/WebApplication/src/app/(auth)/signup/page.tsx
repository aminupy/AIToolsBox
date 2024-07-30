import Image from "next/image";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";

export default function SignUp() {
  return (
    <main className="flex  mg:flex-row h-screen justify-center items-center mg:pb-16">
      <div className="h-full mg:h-[80%] w-full mg:w-9/12 bg-gradient-180 mg:bg-gradient-360 shadow-md mg:rounded-5xl mg:rounded-r-6xl">
        <div className="h-full flex flex-col mg:flex-row justify-between">
          <div className="text-white flex flex-col items-center h-[60%] mg:w-[45%] pt-10 mg:pt-28">
            <div className="flex flex-col items-center gap-5 mg:gap-14">
              <div className="mg:hidden">
                <Image src="/Logo.png" width={150} height={150} alt="Logo" />
              </div>
              <h2 className="text-4xl mg:text-3xl xl:text-4xl 2xl:text-5xl font-bold">
                AI Tools Box
              </h2>
              <p>All You Need In a Box!</p>
            </div>
          </div>
          <div className="h-screen mg:h-full w-full mg:w-[55%] bg-white rounded-t-5xl mg:rounded-5xl flex flex-col items-center">
            <div className="pt-7 hidden mg:block">
              <Image src="/Logo.png" width={70} height={70} alt="Logo" />
            </div>
            <div className="flex flex-col items-center w-80 sm:w-[30rem] mg:w-80 lg:w-96 2xl:w-[28rem] h-full my-8">
              <h2 className="text-3xl sm:text-4xl mg:text-2xl xl:text-3xl 2xl:text-4xl font-bold">
                Create an account
              </h2>
              <div className="w-full flex flex-col gap-5">
                <div className="flex flex-col gap-3 mt-9">
                  <Input
                    type="email"
                    placeholder="Email Address"
                    className="h-14"
                  />
                  <Input
                    type="password"
                    placeholder="Password"
                    className="h-14 "
                  />
                </div>

                <Button className="h-14 w-full bg-gradient-90">Continue</Button>
                <p className="font-semibold text-sm mx-auto">
                  Already have an account?{" "}
                  <span className="text-blue ">Login</span>
                </p>
                <div className="relative flex items-center w-full my-4">
                  <div className="flex-grow border-t border-gray-400"></div>
                  <span className="flex-shrink mx-4 text-gray-800">Or</span>
                  <div className="flex-grow border-t border-gray-400"></div>
                </div>
                <div className="mx-auto w-full">
                  <Button className="h-14 w-full border-gray-200 border-[1px] bg-white text-black hover:bg-gray-100">
                    <Image
                      src="/Google.png"
                      width={70}
                      height={70}
                      alt="Google Logo"
                    />
                    Continue with Google
                  </Button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}
