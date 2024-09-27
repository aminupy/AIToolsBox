import { useMutation } from "@tanstack/react-query";
import axiosInstance from "@/utils/axiosInstance";

export default function useLogin() {
  return useMutation({
    mutationFn: ({ email, password }: { email: string; password: string }) =>
      axiosInstance.post(
        "auth/login/",
        {
          grant_type: "password",
          username: email,
          password,
        },
        {
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
        }
      ),
  });
}
