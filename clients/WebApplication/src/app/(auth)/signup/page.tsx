"use client";
import SignUp from "./components/SignUp";
import EmailVerification from "./components/EmailVerification";
import { useState } from "react";

type SignUpState = "initial" | "email-verification";

export default function SignUpPage() {
  const [signUpState, setSignUpState] = useState<SignUpState>("initial");
  return (
    <main className="h-screen">
      {signUpState === "initial" && <SignUp setSignUpState={setSignUpState} />}
      {signUpState === "email-verification" && (
        <EmailVerification setSignUpState={setSignUpState} />
      )}
    </main>
  );
}
