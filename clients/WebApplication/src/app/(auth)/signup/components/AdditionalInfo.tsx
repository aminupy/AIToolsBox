import Image from "next/image";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Dispatch, SetStateAction } from "react";
import { SubmitHandler, useForm } from "react-hook-form";
import { SignUpState } from "@/types";
import useUserStore from "@/lib/store/userStore";

interface AdditionalInfoProps {
  setSignUpState: Dispatch<SetStateAction<SignUpState>>;
}

type Inputs = {
  firstName: string;
  lastName: string;
};

export default function AdditionalInfo({
  setSignUpState,
}: AdditionalInfoProps) {
  const { setFirstName, setLastName } = useUserStore();

  const {
    register,
    handleSubmit,
    setError,
    formState: { errors },
  } = useForm<Inputs>();

  const onSubmit: SubmitHandler<Inputs> = (data: any) => {
    const { firstName, lastName } = data;

    if (!firstName || !lastName) {
      if (!firstName) {
        setError("firstName", {
          type: "manual",
          message: "First name is required",
        });
      }

      if (!lastName) {
        setError("lastName", {
          type: "manual",
          message: "Last name is required",
        });
      }

      return;
    }

    setFirstName(firstName);
    setLastName(lastName);

    setSignUpState("password");
  };

  return (
    <main className="h-full w-full flex justify-center items-center">
      <div className="h-full w-[40rem] sm:h-[40rem] bg-white sm:rounded-3xl flex justify-center pt-16">
        <div className="flex flex-col gap-10 items-center">
          <Image src="/Logo.png" height={75} width={75} alt="Logo" />
          <div className="flex flex-col gap-5 items-center">
            <h2 className="text-3xl sm:text-4xl font-bold">
              Tell us about you
            </h2>
            <form
              className="w-80 xs:w-[23rem] sm:w-96 flex flex-col gap-5 mt-8"
              onSubmit={handleSubmit(onSubmit)}
            >
              <Input
                type="text"
                placeholder="First Name"
                className={`h-14 ${errors.firstName ? "border-red-600" : ""}`}
                {...register("firstName")}
              />
              {errors.firstName && (
                <p className="font-semibold text-xs text-red-500 pl-1">
                  {errors.firstName.message}
                </p>
              )}
              <Input
                type="text"
                placeholder="Last Name"
                className={`h-14 ${errors.lastName ? "border-red-600" : ""}`}
                {...register("lastName")}
              />
              {errors.lastName && (
                <p className="font-semibold text-xs text-red-500 pl-1">
                  {errors.lastName.message}
                </p>
              )}
              <Button className="h-14 bg-gradient-90 mt-6">Continue</Button>
            </form>
          </div>
        </div>
      </div>
    </main>
  );
}
