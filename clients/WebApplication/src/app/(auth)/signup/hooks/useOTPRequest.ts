import { useMutation } from "@tanstack/react-query";
import axiosInstance from "@/utils/axiosInstance";

export default function useOTPRequest() {
  return useMutation({
    mutationFn: (email: string) =>
      axiosInstance.post("auth/otp/request", { email }),
  });
}
