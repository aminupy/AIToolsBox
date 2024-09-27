"use client";
import Image from "next/image";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { SubmitHandler, useForm } from "react-hook-form";
import { MdVisibility, MdVisibilityOff } from "react-icons/md";
import { useState } from "react";
import useAdditionalInfo from "../hooks/useAdditionalInfo";
import useUserStore from "@/lib/store/userStore";
import { useRouter } from "next/navigation";

type Inputs = {
  password: string;
  confirmPassword: string;
};

export default function Password() {
  const { userId, email, firstName, lastName } = useUserStore();
  const [isPasswordValid, setIsPasswordValid] = useState(false);
  const [isPasswordVisible, setIsPasswordVisible] = useState(false);
  const [isConfirmPasswordVisible, setIsConfirmPasswordVisible] =
    useState(false);
  const handlePasswordVisibility = () =>
    setIsPasswordVisible(!isPasswordVisible);
  const handleConfirmPasswordVisibility = () =>
    setIsConfirmPasswordVisible(!isConfirmPasswordVisible);
  const {
    register,
    handleSubmit,
    setError,
    formState: { errors },
  } = useForm<Inputs>();

  const { mutate: setAdditionalInfo } = useAdditionalInfo();

  const router = useRouter();

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

  const onSubmit: SubmitHandler<Inputs> = (data) => {
    const { password, confirmPassword } = data;

    if (!password || !confirmPassword) {
      if (!password) {
        setError("password", {
          type: "manual",
          message: "Password is required",
        });
      }

      if (!confirmPassword) {
        setError("confirmPassword", {
          type: "manual",
          message: "Confirm password is required",
        });
      }

      return;
    }

    if (password !== confirmPassword) {
      setError("confirmPassword", {
        type: "manual",
        message: "Passwords do not match",
      });
      return;
    }

    if (!checkPassword(password)) {
      return;
    }

    setAdditionalInfo(
      { userId, email, fullName: firstName + " " + lastName, password },
      {
        onSuccess: () => {
          router.push("/");
        },
        onError: (err) => {
          console.log("verification failed", err);
        },
      }
    );
  };

  return (
    <main className="h-full w-full flex justify-center items-center">
      <div className="h-full w-[40rem] sm:h-[40rem] bg-white sm:rounded-3xl flex justify-center pt-16">
        <div className="flex flex-col gap-10 items-center">
          <Image src="/Logo.png" height={75} width={75} alt="Logo" />
          <div className="flex flex-col gap-5 items-center">
            <h2 className="text-3xl sm:text-4xl font-bold">
              Enter your password
            </h2>
            <form
              className="w-80 xs:w-[23rem] sm:w-96 flex flex-col gap-5 mt-8"
              onSubmit={handleSubmit(onSubmit)}
            >
              <div className="relative">
                <Input
                  type={isPasswordVisible ? "text" : "password"}
                  placeholder="Password"
                  className={`h-14 ${errors.password ? "border-red-600" : ""}`}
                  {...register("password", {
                    required: "Password is required",
                    minLength: {
                      value: 8,
                      message: "Password must be at least 8 characters long",
                    },
                  })}
                />
                <div
                  className="absolute top-1 right-0 mt-4 mr-5 cursor-pointer"
                  onClick={handlePasswordVisibility}
                >
                  {isPasswordVisible ? (
                    <MdVisibilityOff size={20} />
                  ) : (
                    <MdVisibility size={20} />
                  )}
                </div>
                {errors.password && (
                  <p className="font-semibold text-xs text-red-500 pl-1 pt-1">
                    {errors.password.message}
                  </p>
                )}
              </div>

              <div className="relative">
                <Input
                  type={isConfirmPasswordVisible ? "text" : "password"}
                  placeholder="Confirm Password"
                  className={`h-14 ${
                    errors.confirmPassword ? "border-red-600" : ""
                  }`}
                  {...register("confirmPassword", {
                    required: "Confirm password is required",
                  })}
                />
                <div
                  className="absolute top-1 right-0 mt-4 mr-5 cursor-pointer"
                  onClick={handleConfirmPasswordVisibility}
                >
                  {isConfirmPasswordVisible ? (
                    <MdVisibilityOff size={20} />
                  ) : (
                    <MdVisibility size={20} />
                  )}
                </div>
                {errors.confirmPassword && (
                  <p className="font-semibold text-xs text-red-500 pl-1 pt-1">
                    {errors.confirmPassword.message}
                  </p>
                )}
              </div>
              <Button className="h-14 bg-gradient-90 mt-6">Continue</Button>
            </form>
          </div>
        </div>
      </div>
    </main>
  );
}
