import { useMutation } from "@tanstack/react-query";
import axiosInstance from "@/utils/axiosInstance";

export default function useRegisterUser() {
  return useMutation({
    mutationFn: (email: string) =>
      axiosInstance.post("users/register/", { email }),
  });
}
