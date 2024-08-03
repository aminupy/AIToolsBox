"use client";
import SignUp from "./components/SignUp";
import EmailVerification from "./components/EmailVerification";
import AdditionalInfo from "./components/AdditionalInfo";
import Password from "./components/Password";
import { useState } from "react";
import { SignUpState } from "@/types";

export default function SignUpPage() {
  const [signUpState, setSignUpState] = useState<SignUpState>("initial");
  return (
    <main className="h-screen">
      {signUpState === "initial" && <SignUp setSignUpState={setSignUpState} />}
      {signUpState === "email-verification" && (
        <EmailVerification setSignUpState={setSignUpState} />
      )}
      {signUpState === "additional-info" && (
        <AdditionalInfo setSignUpState={setSignUpState} />
      )}
      {signUpState === "password" && (
        <Password />
      )}
    </main>
  );
}
