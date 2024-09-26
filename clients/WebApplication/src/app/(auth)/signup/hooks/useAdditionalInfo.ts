import { useMutation } from "@tanstack/react-query";
import axiosInstance from "@/utils/axiosInstance";

export default function useAdditionalInfo() {
  return useMutation({
    mutationFn: ({
      userId,
      email,
      fullName,
      password,
    }: {
      userId: string;
      email: string;
      fullName: string;
      password: string;
    }) =>
      axiosInstance.put(`/users/register/${userId}/`, {
        email,
        fullname: fullName,
        password,
      }),
  });
}
