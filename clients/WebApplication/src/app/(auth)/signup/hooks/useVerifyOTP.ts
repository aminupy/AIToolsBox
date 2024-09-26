import { useMutation } from "@tanstack/react-query";
import axiosInstance from "@/utils/axiosInstance";

export default function useVerifyOTP() {
  return useMutation({
    mutationFn: ({ email, otp }: { email: string; otp: string }) =>
      axiosInstance.post("auth/otp/verify", { email, otp }),
  });
}
