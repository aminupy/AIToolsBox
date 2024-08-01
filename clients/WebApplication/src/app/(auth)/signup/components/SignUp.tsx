"use client";
import Image from "next/image";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { SubmitHandler, useForm } from "react-hook-form";
import { useState } from "react";
import { MdVisibility, MdVisibilityOff } from "react-icons/md";
import { useRouter } from "next/navigation";

type Inputs = {
  email: string;
  password: string;
};

interface SignUpProps {
  setSignUpState: React.Dispatch<React.SetStateAction<string>>;
}

export default function SignUp({ setSignUpState }: SignUpProps) {
  const router = useRouter();
  const [isEmailValid, setIsEmailValid] = useState(false);
  const [isPasswordValid, setIsPasswordValid] = useState(false);
  const [isVisible, setIsVisible] = useState(false);
  const handleVisibility = () => setIsVisible(!isVisible);
  const {
    register,
    handleSubmit,
    setError,
    reset,
    formState: { errors },
  } = useForm<Inputs>();

  const handleEmailChange = () => {
    setIsEmailValid(false);
    reset({ password: "" });
  };

  const checkEmail = (email: string) => {
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
      setError("email", {
        type: "manual",
        message: "Invalid email format",
      });
      setIsEmailValid(false);
      return;
    }
    setIsEmailValid(true);
  };

  const checkPassword = (password: string) => {
    console.log(password);
    const passwordPattern = /^(?=.*[A-Za-z])(?=.*\d).{8,}$/;
    console.log(passwordPattern.test(password));
    if (!passwordPattern.test(password)) {
      setError("password", {
        type: "manual",
        message:
          "Password must be at least 8 characters long and contain at least one letter and one number",
      });
      setIsPasswordValid(false);
      return false;
    }
    setIsPasswordValid(true);
    return true;
  };

  const onSubmit: SubmitHandler<Inputs> = (data: any) => {
    const { email, password } = data;

    if (!isEmailValid) {
      checkEmail(email);
      return;
    }

    if (!isPasswordValid) {
      if (!checkPassword(password)) return;
    }

    setSignUpState("email-verification");
  };

  return (
    <main className="flex mg:flex-row h-screen justify-center items-center mg:pb-16">
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
            <div className="flex flex-col items-center w-80 sm:w-[30rem] mg:w-80 lg:w-[23rem] 2xl:w-[28rem] h-full my-8">
              <h2 className="text-3xl sm:text-4xl mg:text-3xl 2xl:text-4xl font-bold">
                Create an account
              </h2>
              <form
                className="w-full flex flex-col gap-5"
                onSubmit={handleSubmit(onSubmit)}
              >
                <div className="flex flex-col gap-3 mt-9">
                  <div>
                    <div className="relative">
                      <Input
                        type="email"
                        placeholder="Email Address"
                        className={`h-14 ${
                          errors.email ? "border-red-600" : ""
                        }`}
                        readOnly={isEmailValid}
                        {...register("email")}
                      />
                      {errors.email && (
                        <p className="font-semibold text-xs text-red-500 pl-2 pt-1">
                          {errors.email.message}
                        </p>
                      )}
                      {isEmailValid && (
                        <div
                          onClick={handleEmailChange}
                          className="absolute top-0 right-0 text-blue mt-4 mr-5 cursor-pointer"
                        >
                          Edit
                        </div>
                      )}
                    </div>
                  </div>

                  {isEmailValid && (
                    <div>
                      <div className="relative">
                        <Input
                          type={isVisible ? "text" : "password"}
                          placeholder="Password"
                          className={`h-14 ${
                            errors.password ? "border-red-600" : ""
                          }`}
                          {...register("password")}
                        />
                        {errors.password && (
                          <p className="font-semibold text-xs text-red-500 pl-2 pt-1">
                            {errors.password.message}
                          </p>
                        )}
                        <div
                          className="absolute top-1 right-0 mt-4 mr-5 cursor-pointer"
                          onClick={handleVisibility}
                        >
                          {isVisible ? (
                            <MdVisibilityOff size={20} />
                          ) : (
                            <MdVisibility size={20} />
                          )}
                        </div>
                      </div>
                    </div>
                  )}
                </div>

                <Button className="h-14 w-full bg-gradient-90">Continue</Button>
                <p className="font-semibold text-sm mx-auto">
                  Already have an account?{" "}
                  <span
                    onClick={() => router.push("/login")}
                    className="text-blue cursor-pointer ml-1"
                  >
                    Login
                  </span>
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
              </form>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}
