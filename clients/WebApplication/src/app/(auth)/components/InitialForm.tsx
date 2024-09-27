"use client";
import Image from "next/image";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { SubmitHandler, useForm } from "react-hook-form";
import { useState } from "react";
import { MdVisibility, MdVisibilityOff } from "react-icons/md";
import { useRouter } from "next/navigation";
import useUserStore from "@/lib/store/userStore";
import { Dispatch, SetStateAction } from "react";
import Link from "next/link";
import { SignUpState } from "@/types";
import useRegisterUser from "./hooks/useRegisterUser";
import useOTPRequest from "./hooks/useOTPRequest";
import useLogin from "./hooks/useLogin";
import axios from "axios";
import { log } from "console";

type Inputs = {
  email: string;
  password?: string;
};

interface FormProps {
  formName: string;
  setSignUpState?: Dispatch<SetStateAction<SignUpState>>;
}

export default function InitialForm({ setSignUpState, formName }: FormProps) {
  const { setEmail, setUserId } = useUserStore();
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

  const { mutate: registerUser, isPending: isLoading } = useRegisterUser();

  const { mutate: otpRequest } = useOTPRequest();

  const { mutate: login } = useLogin();

  const handleEmailChange = () => {
    setIsEmailValid(false);
    reset({ password: "" });
  };

  const checkEmail = (email: string) => {
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
      setError("email", {
        type: "manual",
        message: "Please enter a valid email address.",
      });
      setIsEmailValid(false);
      return;
    }
    setEmail(email);
    setIsEmailValid(true);
  };

  const checkPassword = (password: string) => {
    const passwordPattern = /^(?=.*[A-Za-z])(?=.*\d).{8,}$/;
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

  const onSubmit: SubmitHandler<Inputs> = async (data: any) => {
    const { email: email_input, password: password_input } = data;

    if (!isEmailValid) {
      checkEmail(email_input);
      if (formName == "login") return;
    }

    if (formName === "login") {
      if (password_input) {
        login(
          { email: email_input, password: password_input },
          {
            onSuccess: () => router.push("/"),
          }
        );
      } else {
        setError("password", {
          type: "manual",
          message: "Password is required",
        });
      }
      //TODO check if password has provided
    } else if (formName === "signup") {
      registerUser(email_input, {
        onSuccess: async (response) => {
          console.log(response.data.user_id);
          setSignUpState!("email-verification");
          otpRequest(email_input);
          setUserId(response.data.user_id);
        },
        onError: (error) => {
          setIsEmailValid(false);
          if (axios.isAxiosError(error)) {
            setError("email", {
              type: "manual",
              message: error.response?.data.detail,
            });
          }
        },
      });
    }
  };

  return (
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
              className={`h-14 ${errors.email ? "border-red-600" : ""}`}
              readOnly={isEmailValid && formName === "login"}
              {...register("email")}
            />
            {errors.email && (
              <p className="font-semibold text-xs text-red-500 pl-2 pt-1">
                {errors.email.message}
              </p>
            )}
            {isEmailValid && formName === "login" ? (
              <div
                onClick={handleEmailChange}
                className="absolute top-0 right-0 text-purple mt-4 mr-5 cursor-pointer"
              >
                Edit
              </div>
            ) : (
              ""
            )}
          </div>
        </div>

        {formName === "login" && isEmailValid && (
          <div>
            <div className="relative">
              <Input
                type={isVisible ? "text" : "password"}
                placeholder="Password"
                className={`h-14 ${errors.password ? "border-red-600" : ""}`}
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
            <div className="mt-3 ml-1 mb-1">
              <Link href="/" className="text-sm text-purple font-semibold">
                Forget Password?
              </Link>
            </div>
          </div>
        )}
      </div>
      <Button
        className="h-14 w-full bg-gradient-90"
        type="submit"
        disabled={isLoading}
      >
        {isLoading ? "Registering..." : "Continue"}
      </Button>

      <p className="font-semibold text-sm mx-auto">
        {formName === "signup"
          ? "Already have an account?"
          : "Don't have an account?"}
        <Link
          href={formName === "signup" ? "/login" : "/signup"}
          className="text-blue cursor-pointer ml-1"
        >
          {formName === "signup" ? "Login" : "Sign Up"}
        </Link>
      </p>
      <div className="relative flex items-center w-full my-4">
        <div className="flex-grow border-t border-gray-400"></div>
        <span className="flex-shrink mx-4 text-gray-800">Or</span>
        <div className="flex-grow border-t border-gray-400"></div>
      </div>
      <div className="mx-auto w-full">
        <Button className="h-14 w-full border-gray-200 border-[1px] bg-white text-black hover:bg-gray-100">
          <Image src="/Google.png" width={70} height={70} alt="Google Logo" />
          Continue with Google
        </Button>
      </div>
    </form>
  );
}
