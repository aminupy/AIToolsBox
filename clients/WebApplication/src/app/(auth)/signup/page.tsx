"use client";
import SignUp from "./components/SignUp";
import EmailVerification from "./components/EmailVerification";
import { useState } from "react";

export default function SignUpPage() {
  const [signUpState, setSignUpState] = useState("initial");
  return (
    <main className="h-screen">
      {signUpState === "initial" && <SignUp setSignUpState={setSignUpState} />}
      {signUpState === "email-verification" && <EmailVerification />}
    </main>
  );
}
