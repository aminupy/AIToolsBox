"use client";
import Image from "next/image";
import { REGEXP_ONLY_DIGITS_AND_CHARS } from "input-otp";
import useUserStore from "@/lib/store/userStore";

import {
  InputOTP,
  InputOTPGroup,
  InputOTPSlot,
} from "@/components/ui/input-otp";

export default function EmailVerification() {
  const { email } = useUserStore();
  return (
    <div className="h-full w-full flex justify-center items-center">
      <div className="h-full w-[40rem] sm:h-[40rem] bg-white sm:rounded-3xl flex justify-center pt-16">
        <div className="flex flex-col gap-12 items-center">
          <Image src="/Logo.png" height={75} width={75} alt="Logo" />
          <div className="flex flex-col gap-5 items-center">
            <h2 className="text-4xl sm:text-5xl font-bold">Enter Code</h2>
            <p className="w-80 sm:w-96 text-center break-words">
              We’ve sent an email with an activation code to{" "}
              <span className="font-semibold">{email}</span>
            </p>
            <div className="flex flex-col items-center gap-6 mt-3">
              <p>Please enter the code</p>
              <InputOTP maxLength={6} pattern={REGEXP_ONLY_DIGITS_AND_CHARS}>
                <InputOTPGroup>
                  <InputOTPSlot index={0} />
                </InputOTPGroup>
                <InputOTPGroup>
                  <InputOTPSlot index={1} />
                </InputOTPGroup>
                <InputOTPGroup>
                  <InputOTPSlot index={2} />
                </InputOTPGroup>
                <InputOTPGroup>
                  <InputOTPSlot index={3} />
                </InputOTPGroup>
                <InputOTPGroup>
                  <InputOTPSlot index={4} />
                </InputOTPGroup>
                <InputOTPGroup>
                  <InputOTPSlot index={5} />
                </InputOTPGroup>
              </InputOTP>
            </div>
            <button className="text-sm text-blue mt-2">Resend email</button>
          </div>
        </div>
      </div>
    </div>
  );
}
