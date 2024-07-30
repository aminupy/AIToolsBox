import Image from "next/image";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";

export default function SignUp() {
  return (
    <main className="flex h-screen justify-center items-center pb-16">
      <div className="h-[80%] w-9/12 bg-gradient-360 shadow-md rounded-5xl rounded-r-6xl">
        <div className="h-full flex justify-between">
          <div className="text-white flex gap-14 flex-col items-center w-[45%] pt-28">
            <h2 className="text-3xl xl:text-4xl 2xl:text-5xl font-bold">
              AI Tools Box
            </h2>
            <p className="font-semibold">All You Need In a Box!</p>
          </div>
          <div className="h-full w-[55%] bg-white rounded-5xl flex flex-col items-center">
            <div className="pt-7">
              <Image src="/Logo.png" width={70} height={70} alt="Logo" />
            </div>
            <div className="flex flex-col items-center w-80 lg:w-96 2xl:w-[28rem] h-full my-10">
              <h2 className="text-2xl xl:text-3xl 2xl:text-4xl font-bold">
                Create an account
              </h2>
              <div className="w-full flex flex-col gap-5">
                <Input
                  type="email"
                  placeholder="Email Address"
                  className="h-14  mt-16"
                />
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
